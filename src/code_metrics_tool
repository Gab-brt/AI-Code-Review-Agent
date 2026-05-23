import ast


class CodeMetricsTool:
    """
    Tool responsible for extracting basic code metrics.
    """

    def execute(self, source_code: str, tree):
        lines = source_code.splitlines()

        total_lines = len(lines)
        empty_lines = sum(1 for line in lines if not line.strip())
        comment_lines = sum(1 for line in lines if line.strip().startswith("#"))

        functions = 0
        classes = 0
        imports = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions += 1
            elif isinstance(node, ast.ClassDef):
                classes += 1
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                imports += 1

        non_empty_lines = total_lines - empty_lines

        comment_ratio = 0
        if non_empty_lines > 0:
            comment_ratio = comment_lines / non_empty_lines

        empty_line_ratio = 0
        if total_lines > 0:
            empty_line_ratio = empty_lines / total_lines

        return {
            "total_lines": total_lines,
            "empty_lines": empty_lines,
            "comment_lines": comment_lines,
            "non_empty_lines": non_empty_lines,
            "comment_ratio": round(comment_ratio, 2),
            "empty_line_ratio": round(empty_line_ratio, 2),
            "functions": functions,
            "classes": classes,
            "imports": imports
        }
