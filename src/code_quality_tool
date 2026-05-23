import ast


class CodeQualityTool:
    """
    Tool responsible for detecting simple rule-based quality issues.
    """

    def execute(self, source_code: str, tree, metrics: dict):
        issues = []

        self._check_long_functions(tree, issues)
        self._check_missing_docstrings(tree, issues)
        self._check_import_count(metrics, issues)
        self._check_comment_ratio(metrics, issues)
        self._check_empty_line_ratio(metrics, issues)
        self._check_unstructured_code(metrics, issues)

        if not issues:
            issues.append("No major beginner-level code quality issue was detected.")

        return issues

    def _check_long_functions(self, tree, issues):
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if hasattr(node, "end_lineno") and node.end_lineno is not None:
                    function_length = node.end_lineno - node.lineno + 1

                    if function_length > 30:
                        issues.append(
                            f"Function '{node.name}' is longer than 30 lines. "
                            "Consider splitting it into smaller functions."
                        )

    def _check_missing_docstrings(self, tree, issues):
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if ast.get_docstring(node) is None:
                    issues.append(
                        f"Function '{node.name}' has no docstring. "
                        "Consider adding a short explanation of its purpose."
                    )

            elif isinstance(node, ast.ClassDef):
                if ast.get_docstring(node) is None:
                    issues.append(
                        f"Class '{node.name}' has no docstring. "
                        "Consider documenting what this class represents."
                    )

    def _check_import_count(self, metrics, issues):
        if metrics.get("imports", 0) > 10:
            issues.append(
                "The file contains more than 10 import statements. "
                "Consider checking whether all imports are necessary."
            )

    def _check_comment_ratio(self, metrics, issues):
        if metrics.get("non_empty_lines", 0) > 10 and metrics.get("comment_ratio", 0) < 0.05:
            issues.append(
                "Less than 5% of the non-empty lines are comments. "
                "Consider adding comments for complex parts of the code."
            )

    def _check_empty_line_ratio(self, metrics, issues):
        if metrics.get("empty_line_ratio", 0) > 0.25:
            issues.append(
                "More than 25% of the file lines are empty. "
                "Consider reducing excessive blank lines."
            )

    def _check_unstructured_code(self, metrics, issues):
        if (
            metrics.get("total_lines", 0) > 40
            and metrics.get("functions", 0) == 0
            and metrics.get("classes", 0) == 0
        ):
            issues.append(
                "The file contains many lines but no functions or classes. "
                "Consider organizing the code into reusable functions or classes."
            )
