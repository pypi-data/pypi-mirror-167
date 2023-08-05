from toolkit.template.code_style import CamelCaseStyle, get_camel_case_styles


def test_get_camel_case_styles():
    pairs = (
        (
            (
                "camel case",
                "camel-case",
                "Camel Case",
                "camel_case",
                "camel case ",
                "camel-case-",
                "camel_case_",
                "Camel-case",
            ),
            CamelCaseStyle(
                "camel case",
                "camel-case",
                "Camel Case",
                "camel_case",
                "CamelCase",
            ),
        ),
    )

    for pair in pairs:
        for i in range(len(pair[0])):
            assert get_camel_case_styles(pair[0][i]) == pair[1]
