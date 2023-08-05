package middleware

import (
	"errors"
	"fmt"
	"net/http"
	"reflect"
	"strings"

	"github.com/dgrijalva/jwt-go"
	"github.com/gin-gonic/gin"
)

type (
	// JWTConfig defines the config for JWT middleware.
	JWTConfig struct {
		// Skipper defines a function to skip middleware.
		Skipper Skipper

		// Signing key to validate token.
		// This is one of the three options to provide a token validation key.
		// The order of precedence is a user-defined KeyFunc, SigningKeys and SigningKey.
		// Required if neither user-defined KeyFunc nor SigningKeys is provided.
		SigningKey interface{}

		// Map of signing keys to validate token with kid field usage.
		// This is one of the three options to provide a token validation key.
		// The order of precedence is a user-defined KeyFunc, SigningKeys and SigningKey.
		// Required if neither user-defined KeyFunc nor SigningKey is provided.
		SigningKeys map[string]interface{}

		// Signing method used to check the token's signing algorithm.
		// Optional. Default value HS256.
		SigningMethod string

		// Context key to store user information from the token into context.
		// Optional. Default value "user".
		ContextKey string

		// Claims are extendable claims data defining token content. Used by default ParseTokenFunc implementation.
		// Not used if custom ParseTokenFunc is set.
		// Optional. Default value jwt.MapClaims
		Claims jwt.Claims

		// TokenLookup is a string in the form of "<source>:<name>" or "<source>:<name>,<source>:<name>" that is used
		// to extract token from the request.
		// Optional. Default value "header:Authorization".
		// Possible values:
		// - "header:<name>"
		// - "query:<name>"
		// - "param:<name>"
		// - "cookie:<name>"
		// - "form:<name>"
		// Multiply sources example:
		// - "header: Authorization,cookie: myowncookie"
		TokenLookup string

		// TokenLookupFuncs defines a list of user-defined functions that extract JWT token from the given context.
		// This is one of the two options to provide a token extractor.
		// The order of precedence is user-defined TokenLookupFuncs, and TokenLookup.
		// You can also provide both if you want.
		TokenLookupFuncs []TokenLookupFunc

		// AuthScheme to be used in the Authorization header.
		// Optional. Default value "Bearer".
		AuthScheme string

		// KeyFunc defines a user-defined function that supplies the public key for a token validation.
		// The function shall take care of verifying the signing algorithm and selecting the proper key.
		// A user-defined KeyFunc can be useful if tokens are issued by an external party.
		// Used by default ParseTokenFunc implementation.
		//
		// When a user-defined KeyFunc is provided, SigningKey, SigningKeys, and SigningMethod are ignored.
		// This is one of the three options to provide a token validation key.
		// The order of precedence is a user-defined KeyFunc, SigningKeys and SigningKey.
		// Required if neither SigningKeys nor SigningKey is provided.
		// Not used if custom ParseTokenFunc is set.
		// Default to an internal implementation verifying the signing algorithm and selecting the proper key.
		KeyFunc jwt.Keyfunc

		// ParseTokenFunc defines a user-defined function that parses token from given auth. Returns an error when token
		// parsing fails or parsed token is invalid.
		// Defaults to implementation using `github.com/golang-jwt/jwt` as JWT implementation library
		ParseTokenFunc func(auth string, c *gin.Context) (interface{}, error)
	}

	// Skipper defines a function to skip middleware. Returning true skips processing
	// the middleware.
	Skipper func(*gin.Context) bool

	// TokenLookupFunc defines a function for extracting JWT token from the given context.
	TokenLookupFunc func(*gin.Context) (string, error)
)

// Algorithms
const (
	AlgorithmHS256      = "HS256"
	HeaderAuthorization = "Authorization"
)

var (
	// DefaultJWTConfig is the default JWT auth middleware config.
	DefaultJWTConfig = JWTConfig{
		Skipper:          DefaultSkipper,
		SigningMethod:    AlgorithmHS256,
		ContextKey:       "user",
		TokenLookup:      "header:" + HeaderAuthorization,
		TokenLookupFuncs: nil,
		AuthScheme:       "Bearer",
		Claims:           jwt.MapClaims{},
		KeyFunc:          nil,
	}
)

var ErrJWTMissing = errors.New("missing or malformed jwt")

// JWT returns a JSON Web Token (JWT) auth middleware.
//
// For valid token, it sets the user in context and calls next handler.
// For invalid token, it returns "401 - Unauthorized" error.
// For missing token, it returns "400 - Bad Request" error.
//
// See: https://jwt.io/introduction
// See `JWTConfig.TokenLookup`
func JWT(key interface{}) gin.HandlerFunc {
	c := DefaultJWTConfig
	c.SigningKey = key
	return JWTWithConfig(c)
}

// JWTWithConfig returns a JWT auth middleware with config.
// See: `JWT()`.
func JWTWithConfig(config JWTConfig) gin.HandlerFunc {
	// Defaults
	if config.Skipper == nil {
		config.Skipper = DefaultJWTConfig.Skipper
	}
	if config.SigningKey == nil && len(config.SigningKeys) == 0 && config.KeyFunc == nil && config.ParseTokenFunc == nil {
		panic("echo: jwt middleware requires signing key")
	}
	if config.SigningMethod == "" {
		config.SigningMethod = DefaultJWTConfig.SigningMethod
	}
	if config.ContextKey == "" {
		config.ContextKey = DefaultJWTConfig.ContextKey
	}
	if config.Claims == nil {
		config.Claims = DefaultJWTConfig.Claims
	}
	if config.TokenLookup == "" && len(config.TokenLookupFuncs) == 0 {
		config.TokenLookup = DefaultJWTConfig.TokenLookup
	}
	if config.AuthScheme == "" {
		config.AuthScheme = DefaultJWTConfig.AuthScheme
	}
	if config.KeyFunc == nil {
		config.KeyFunc = config.defaultKeyFunc
	}
	if config.ParseTokenFunc == nil {
		config.ParseTokenFunc = config.defaultParseToken
	}

	// Initialize
	// Split sources
	sources := strings.Split(config.TokenLookup, ",")
	var extractors = config.TokenLookupFuncs
	for _, source := range sources {
		parts := strings.Split(source, ":")

		switch parts[0] {
		case "query":
			extractors = append(extractors, jwtFromQuery(parts[1]))
		case "param":
			extractors = append(extractors, jwtFromParam(parts[1]))
		case "cookie":
			extractors = append(extractors, jwtFromCookie(parts[1]))
		case "form":
			extractors = append(extractors, jwtFromForm(parts[1]))
		case "header":
			extractors = append(extractors, jwtFromHeader(parts[1], config.AuthScheme))
		}
	}

	return func(c *gin.Context) {
		if config.Skipper(c) {
			c.Next()
			return
		}

		var auth string
		var err error

		for _, extractor := range extractors {
			// Extract token from extractor, if it's not fail break the loop and
			// set auth
			auth, err = extractor(c)
			if err == nil {
				break
			}
		}

		if err != nil {
			c.AbortWithStatusJSON(http.StatusUnauthorized, gin.H{
				"code":    40102,
				"message": "missing or malformed jwt",
			})
			return
		}

		token, err := config.ParseTokenFunc(auth, c)

		if err == nil {
			// Store user information from token into context.
			c.Set(config.ContextKey, token)
			c.Next()
			return
		}

		c.Error(err)

		c.AbortWithStatusJSON(http.StatusUnauthorized, gin.H{
			"code":    40103,
			"message": "invalid or expired jwt",
		})
	}
}

func (config *JWTConfig) defaultParseToken(auth string, c *gin.Context) (interface{}, error) {
	token := new(jwt.Token)
	var err error
	// Issue #647, #656
	if _, ok := config.Claims.(jwt.MapClaims); ok {
		token, err = jwt.Parse(auth, config.KeyFunc)
	} else {
		t := reflect.ValueOf(config.Claims).Type().Elem()
		claims := reflect.New(t).Interface().(jwt.Claims)
		// https://github.com/dgrijalva/jwt-go/issues/460
		token, err = jwt.ParseWithClaims(auth, claims, config.KeyFunc)
	}
	if err != nil {
		return nil, err
	}
	if !token.Valid {
		return nil, errors.New("invalid token")
	}
	return token, nil
}

// defaultKeyFunc returns a signing key of the given token.
func (config *JWTConfig) defaultKeyFunc(t *jwt.Token) (interface{}, error) {
	// Check the signing method
	if t.Method.Alg() != config.SigningMethod {
		return nil, fmt.Errorf("unexpected jwt signing method=%v", t.Header["alg"])
	}
	if len(config.SigningKeys) > 0 {
		if kid, ok := t.Header["kid"].(string); ok {
			if key, ok := config.SigningKeys[kid]; ok {
				return key, nil
			}
		}
		return nil, fmt.Errorf("unexpected jwt key id=%v", t.Header["kid"])
	}

	return config.SigningKey, nil
}

// jwtFromHeader returns a `TokenLookupFunc` that extracts token from the request header.
func jwtFromHeader(header string, authScheme string) TokenLookupFunc {
	return func(c *gin.Context) (string, error) {
		auth := c.Request.Header.Get(header)
		l := len(authScheme)
		if len(auth) > l+1 && strings.EqualFold(auth[:l], authScheme) {
			return auth[l+1:], nil
		}
		return "", ErrJWTMissing
	}
}

// jwtFromQuery returns a `TokenLookupFunc` that extracts token from the query string.
func jwtFromQuery(param string) TokenLookupFunc {
	return func(c *gin.Context) (string, error) {
		token := c.Query(param)
		if token == "" {
			return "", ErrJWTMissing
		}
		return token, nil
	}
}

// jwtFromParam returns a `TokenLookupFunc` that extracts token from the url param string.
func jwtFromParam(param string) TokenLookupFunc {
	return func(c *gin.Context) (string, error) {
		token := c.Param(param)
		if token == "" {
			return "", ErrJWTMissing
		}
		return token, nil
	}
}

// jwtFromCookie returns a `TokenLookupFunc` that extracts token from the named cookie.
func jwtFromCookie(name string) TokenLookupFunc {
	return func(c *gin.Context) (string, error) {
		cookie, err := c.Cookie(name)
		if err != nil {
			return "", ErrJWTMissing
		}
		return cookie, nil
	}
}

// jwtFromForm returns a `TokenLookupFunc` that extracts token from the form field.
func jwtFromForm(name string) TokenLookupFunc {
	return func(c *gin.Context) (string, error) {
		field := c.PostForm(name)
		if field == "" {
			return "", ErrJWTMissing
		}
		return field, nil
	}
}

// DefaultSkipper returns false which processes the middleware.
func DefaultSkipper(*gin.Context) bool {
	return false
}
