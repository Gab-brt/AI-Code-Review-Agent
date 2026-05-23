import ast


class SyntaxCheckerTool:
    """
    Tool responsible for checking Python syntax using the ast module.
    """

    def execute(self, source_code: str):
        try:
            tree = ast.parse(source_code)

            return {
                "valid": True,
                "message": "Syntax is valid.",
                "line": None,
                "tree": tree
            }

        except SyntaxError as error:
            return {
                "valid": False,
                "message": error.msg,
                "line": error.lineno,
                "tree": None
            }

        except Exception as error:
            return {
                "valid": False,
                "message": f"Unexpected syntax checking error: {error}",
                "line": None,
                "tree": None
            }
