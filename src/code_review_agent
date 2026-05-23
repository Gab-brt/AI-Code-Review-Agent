from pathlib import Path

from file_reader_tool import FileReaderTool
from syntax_checker_tool import SyntaxCheckerTool
from code_metrics_tool import CodeMetricsTool
from code_quality_tool import CodeQualityTool
from report_generator_tool import ReportGeneratorTool


class CodeReviewAgent:
    """
    Central rule-based agent that coordinates all code review tools.
    """

    def __init__(self):
        self.file_reader = FileReaderTool()
        self.syntax_checker = SyntaxCheckerTool()
        self.metrics_tool = CodeMetricsTool()
        self.quality_tool = CodeQualityTool()
        self.report_generator = ReportGeneratorTool()

    def review_file(self, file_path: str, save_report: bool = False) -> str:
        """
        Review a Python file using a predefined rule-based workflow.
        """

        path = Path(file_path)

        analysis_results = {
            "file_path": str(path),
            "file_name": path.name,
            "errors": [],
            "syntax": {},
            "metrics": {},
            "issues": []
        }

        if not file_path:
            analysis_results["errors"].append("No file path was provided.")
            return self.report_generator.generate_report(analysis_results)

        if not path.exists():
            analysis_results["errors"].append("The provided file does not exist.")
            return self.report_generator.generate_report(analysis_results)

        if not path.is_file():
            analysis_results["errors"].append("The provided path is not a file.")
            return self.report_generator.generate_report(analysis_results)

        if path.suffix != ".py":
            analysis_results["errors"].append("Unsupported file type. Please provide a .py file.")
            return self.report_generator.generate_report(analysis_results)

        file_result = self.file_reader.execute(path)

        if not file_result["success"]:
            analysis_results["errors"].append(file_result["error"])
            return self.report_generator.generate_report(analysis_results)

        source_code = file_result["content"]

        syntax_result = self.syntax_checker.execute(source_code)
        analysis_results["syntax"] = syntax_result

        if not syntax_result["valid"]:
            return self.report_generator.generate_report(analysis_results)

        metrics_result = self.metrics_tool.execute(source_code, syntax_result["tree"])
        analysis_results["metrics"] = metrics_result

        quality_result = self.quality_tool.execute(
            source_code=source_code,
            tree=syntax_result["tree"],
            metrics=metrics_result
        )
        analysis_results["issues"] = quality_result

        report = self.report_generator.generate_report(analysis_results)

        if save_report:
            self.report_generator.save_report(report, "reports/generated_report.md")

        return report
