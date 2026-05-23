# AI Code Review Agent — Step 2 Software Code Development

**Project:** AI Code Review Agent  
**Student:** Gabriel Bartoux  
**Submission stage:** Step 2 — Software Code Development  
**Repository:** AI-Code-Review-Agent  
**Project ID:** PRJ-MP9VPLZR-81C5  

---

## 1. Purpose of Step 2

The purpose of Step 2 is to transform the Step 1 planning work into executable Python software. In Step 1, the system was defined as a local rule-based agent that reviews Python source files. In Step 2, this planned system has been converted into a modular command-line application with working Python modules.

This step is different from Step 1 because it focuses on implementation instead of planning. The goal is no longer only to describe the system, but to show that the software architecture can be translated into executable code.

---

## 2. Software Composition

The software to be built is a local Python command-line tool called **AI Code Review Agent**.

The system receives a local Python file path from the user, analyzes the selected `.py` file without executing it, and generates a structured review report. The review includes syntax status, code metrics, quality warnings, and improvement suggestions.

The system does not use a web server, database, external paid API, or external LLM in this version. It uses a local rule-based workflow and Python libraries such as `argparse`, `pathlib`, and `ast`.

---

## 3. Runtime Components

The application is composed of seven executable modules.

| Module | Runtime Role |
|---|---|
| `main.py` | Command-line entry point |
| `code_review_agent.py` | Central rule-based workflow coordinator |
| `file_reader_tool.py` | Reads local Python source files |
| `syntax_checker_tool.py` | Validates Python syntax using AST parsing |
| `code_metrics_tool.py` | Extracts measurable information from the code |
| `code_quality_tool.py` | Applies rule-based quality checks |
| `report_generator_tool.py` | Generates the final Markdown-style review |

---

## 4. Processing Flow

The software follows this execution flow:

1. The user runs the program from the command line.
2. The user provides the path to a Python file.
3. `main.py` parses the command-line argument.
4. `main.py` creates an instance of `CodeReviewAgent`.
5. `CodeReviewAgent` validates the file path and extension.
6. `FileReaderTool` reads the selected Python file.
7. `SyntaxCheckerTool` parses the code using the `ast` module.
8. If the syntax is invalid, the agent stops deeper analysis and generates a syntax-focused report.
9. If the syntax is valid, `CodeMetricsTool` extracts code metrics.
10. `CodeQualityTool` applies predefined quality rules.
11. `ReportGeneratorTool` builds the final structured report.
12. The report is displayed in the terminal.
13. If the `--save` option is used, the report can also be saved as a Markdown file.

---

## 5. Module Implementation Details

### 5.1 Module 1 — `main.py`

`main.py` is the command-line entry point of the system.

Its responsibilities are:

- parse command-line arguments with `argparse`;
- receive the path of the Python file to analyze;
- optionally receive the `--save` flag;
- instantiate the `CodeReviewAgent`;
- run the review process;
- display the generated report in the terminal;
- catch unexpected runtime errors.

Example execution command:

```bash
python main.py ../examples/bad_code_example.py
```

---

### 5.2 Module 2 — `code_review_agent.py`

`code_review_agent.py` contains the main `CodeReviewAgent` class.

This module is the central coordinator of the system. It does not directly perform all analysis tasks. Instead, it controls the execution order of the specialized tools.

Its responsibilities are:

- validate the file path;
- verify that the file exists;
- verify that the selected file has a `.py` extension;
- call `FileReaderTool`;
- call `SyntaxCheckerTool`;
- stop deeper analysis if syntax is invalid;
- call `CodeMetricsTool` if syntax is valid;
- call `CodeQualityTool` if syntax is valid;
- send all collected results to `ReportGeneratorTool`;
- optionally save the generated report.

The decision-making is rule-based and implemented with explicit Python conditions such as `if`, `elif`, and `else`.

---

### 5.3 Module 3 — `file_reader_tool.py`

`file_reader_tool.py` contains the `FileReaderTool` class.

This tool reads the content of a local Python file using UTF-8 encoding.

Input:

- file path.

Output:

- success status;
- file content if reading succeeds;
- error message if reading fails.

Handled errors include:

- missing file;
- permission error;
- UTF-8 decoding error;
- empty file;
- unexpected reading error.

---

### 5.4 Module 4 — `syntax_checker_tool.py`

`syntax_checker_tool.py` contains the `SyntaxCheckerTool` class.

This tool validates Python syntax using the built-in `ast` module. The code is parsed but not executed, which makes the analysis safer.

Input:

- source code text.

Output:

- `valid = True` if syntax is valid;
- `valid = False` if syntax is invalid;
- syntax error message;
- error line number;
- AST tree when parsing succeeds.

This module is important because later tools depend on valid Python syntax.

---

### 5.5 Module 5 — `code_metrics_tool.py`

`code_metrics_tool.py` contains the `CodeMetricsTool` class.

This tool extracts quantitative information from the source code and AST structure.

It calculates:

- total number of lines;
- number of empty lines;
- number of comment lines;
- number of non-empty lines;
- comment ratio;
- empty line ratio;
- number of functions;
- number of classes;
- number of import statements.

The result is returned as a dictionary so that the agent and quality tool can reuse it.

---

### 5.6 Module 6 — `code_quality_tool.py`

`code_quality_tool.py` contains the `CodeQualityTool` class.

This tool applies simple rule-based checks for beginner-level code quality and readability.

Implemented checks include:

- detecting functions longer than 30 lines;
- detecting missing function docstrings;
- detecting missing class docstrings;
- detecting more than 10 import statements;
- detecting less than 5% comment lines;
- detecting more than 25% empty lines;
- detecting large files with no functions or classes.

The tool returns a list of warnings and improvement suggestions.

These checks are intentionally simple and educational. They are not meant to replace professional static analysis tools, but they make the agent's behavior understandable and testable.

---

### 5.7 Module 7 — `report_generator_tool.py`

`report_generator_tool.py` contains the `ReportGeneratorTool` class.

This tool generates the final Markdown-style report.

The report includes:

- file name;
- file path;
- input or file errors if present;
- syntax status;
- syntax error line and message if needed;
- code metrics;
- quality warnings;
- final conclusion.

The module can also save the report into a Markdown file when requested.

---

## 6. Architecture Summary Generated for Step 2

The Step 2 architecture is based on a local Python command-line tool that analyzes Python source files using a rule-based agent. The agent orchestrates several internal tools to check syntax, extract code metrics, identify quality issues, and generate a structured review report without executing the analyzed code.

The implemented architecture follows the original Step 1 idea but turns it into concrete runtime modules.

---

## 7. Expected Behavior

The expected behavior of the software is:

- the program runs from the terminal;
- the user gives a `.py` file path;
- the system validates the file;
- the system reads and analyzes the file;
- the system never executes the analyzed file;
- the system handles common errors without crashing;
- the system returns a structured report;
- the report is understandable for beginner Python students.

If a file has syntax errors, the agent must stop deeper analysis and report the syntax problem. If the syntax is valid, the agent continues with metrics extraction and quality analysis.

---

## 8. Example Runtime Tests Performed

### 8.1 Test with `bad_code_example.py`

Command used:

```bash
python main.py ../examples/bad_code_example.py
```

Observed result:

- the file was read successfully;
- the syntax was valid;
- the system detected 70 total lines;
- the system detected 11 import statements;
- the system detected one function;
- the system generated several warnings.

Detected warnings included:

- the function `process_student_data` is longer than 30 lines;
- the function has no docstring;
- the file contains more than 10 import statements;
- less than 5% of non-empty lines are comments.

This result is expected because `bad_code_example.py` was intentionally written with several beginner-level quality issues.

---

### 8.2 Test with `good_code_example.py`

Command used:

```bash
python main.py ../examples/good_code_example.py
```

Observed result:

- the file was read successfully;
- the syntax was valid;
- the system detected 52 total lines;
- the system detected 5 functions;
- the system detected no imports;
- the system generated minor formatting/documentation warnings.

Detected warnings included:

- less than 5% of non-empty lines are comments;
- more than 25% of the file lines are empty.

This result is acceptable because the file is structurally cleaner, but the rule-based thresholds are strict. This also demonstrates one limitation of the system: docstrings are not currently counted as comment lines.

---

## 9. Gemini Simulation Result

After the module code was completed on the project development platform, the Gemini simulation was executed.

The simulation result showed:

- the implementation is modular;
- the command-line workflow is present;
- the rule-based agent coordinates multiple tools;
- syntax checking is implemented using the AST module;
- code metrics extraction is implemented;
- code quality checks are implemented;
- the report generator produces structured output;
- the original Step 1 requirements were fully covered.

The simulation reported **100% requirements coverage** for Step 2.

---

## 10. Difference Between Step 1 and Step 2

Step 1 was mainly a planning and documentation stage. It described the project idea, the system goal, the expected tools, the agent approach, the risks, and the initial architecture.

Step 2 is an implementation stage. It focuses on executable software code, concrete modules, runtime behavior, and simulation validation.

The main progress from Step 1 to Step 2 is:

| Step 1 | Step 2 |
|---|---|
| Planned system concept | Implemented executable modules |
| Planned tools | Working Python tool classes |
| Planned agent workflow | Implemented `CodeReviewAgent` workflow |
| Planned architecture | Actual module-based structure |
| Planned testing approach | First runtime tests executed |
| Planned report generation | Working Markdown-style output |

---

## 11. Current Repository Structure

The current implementation uses the following structure:

```text
AI-Code-Review-Agent/
│
├── src/
│   ├── main.py
│   ├── code_review_agent.py
│   ├── file_reader_tool.py
│   ├── syntax_checker_tool.py
│   ├── code_metrics_tool.py
│   ├── code_quality_tool.py
│   └── report_generator_tool.py
│
├── examples/
│   ├── bad_code_example.py
│   └── good_code_example.py
│
├── docs/
│   └── step1_planning_ai_code_review_agent.md
│
├── reports/
│
├── README.md
└── .gitignore
```

---

## 12. Step 2 Conclusion

The Step 2 objective has been reached. The planned AI Code Review Agent has been transformed into executable Python software.

The system now includes a command-line entry point, a rule-based coordinating agent, several internal analysis tools, and a report generator. It can analyze local Python files, detect syntax status, extract metrics, identify basic quality issues, and generate readable feedback.

The project is ready to continue toward Step 3, where the focus will be stronger testing, error handling validation, deployment preparation, and data conversion explanation.
