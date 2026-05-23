import argparse
from code_review_agent import CodeReviewAgent


def main():
    parser = argparse.ArgumentParser(
        description="AI Code Review Agent - Analyze a Python source file."
    )

    parser.add_argument(
        "file_path",
        help="Path to the Python file to analyze."
    )

    parser.add_argument(
        "--save",
        action="store_true",
        help="Save the generated report into the reports folder."
    )

    args = parser.parse_args()

    try:
        agent = CodeReviewAgent()
        report = agent.review_file(args.file_path, save_report=args.save)
        print(report)

    except Exception as error:
        print("An unexpected error occurred during execution.")
        print(f"Error details: {error}")


if __name__ == "__main__":
    main()
