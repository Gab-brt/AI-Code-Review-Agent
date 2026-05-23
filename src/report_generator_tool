from pathlib import Path


class ReportGeneratorTool:
    """
    Tool responsible for generating a structured Markdown report.
    """

    def generate_report(self, analysis_results: dict) -> str:
        report = []

        report.append("# AI Code Review Report")
        report.append("")
        report.append(f"**File:** {analysis_results.get('file_name', 'Unknown')}")
        report.append(f"**Path:** {analysis_results.get('file_path', 'Unknown')}")
        report.append("")

        errors = analysis_results.get("errors", [])

        if errors:
            report.append("## Errors")
            for error in errors:
                report.append(f"- {error}")
            report.append("")
            report.append("## Final Conclusion")
            report.append("The analysis could not be completed because an input or file error occurred.")
            return "\n".join(report)

        syntax = analysis_results.get("syntax", {})

        report.append("## Syntax Status")
        if syntax.get("valid"):
            report.append("- The Python syntax is valid.")
        else:
            report.append("- The Python syntax is invalid.")
            report.append(f"- Error line: {syntax.get('line')}")
            report.append(f"- Error message: {syntax.get('message')}")
            report.append("")
            report.append("## Final Conclusion")
            report.append("The file should be corrected before deeper quality analysis can be performed.")
            return "\n".join(report)

        metrics = analysis_results.get("metrics", {})

        report.append("")
        report.append("## Code Metrics")
        report.append(f"- Total lines: {metrics.get('total_lines', 0)}")
        report.append(f"- Empty lines: {metrics.get('empty_lines', 0)}")
        report.append(f"- Comment lines: {metrics.get('comment_lines', 0)}")
        report.append(f"- Functions: {metrics.get('functions', 0)}")
        report.append(f"- Classes: {metrics.get('classes', 0)}")
        report.append(f"- Import statements: {metrics.get('imports', 0)}")

        issues = analysis_results.get("issues", [])

        report.append("")
        report.append("## Quality Warnings and Suggestions")

        if issues:
            for issue in issues:
                report.append(f"- {issue}")
        else:
            report.append("- No quality issue was detected.")

        report.append("")
        report.append("## Final Conclusion")
        report.append(
            "The file was analyzed successfully. The suggestions above can help improve readability, "
            "structure, and maintainability."
        )

        return "\n".join(report)

    def save_report(self, report: str, output_path: str):
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w", encoding="utf-8") as file:
            file.write(report)
