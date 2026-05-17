# AI Code Review Agent — Step 1 Planning Documentation

**Project:** AI Code Review Agent  
**Student:** Gabriel Bartoux  
**Submission stage:** Step 1 — System Planning and Documentation  
**Deadline:** 17.05  
**Repository name:** `ai-code-review-agent`

---

## 1. Project Concept / Vision

### 1.1 Short System Description

The **AI Code Review Agent** is a Python-based command-line software system designed to help programming students review Python source files before submission or publication on GitHub.

The system receives a file path from the user, reads the selected Python file, analyzes its content through several specialized tools, and returns a structured review. The review includes syntax validation, basic code metrics, possible quality issues, and improvement suggestions.

The purpose of the project is not to replace a teacher, professional code reviewer, or advanced static analysis platform. Instead, it provides an educational and understandable first-level review that helps students identify common programming problems early in the development process.

### 1.2 Project Goal

The main goal is to build a functional agent-based Python application that can:

- accept user input from the command line;
- read and analyze a local Python source file;
- use multiple tools during execution;
- detect basic syntax and code quality issues;
- generate a clear and structured feedback report;
- be tested, documented, versioned with Git, and prepared for controlled local deployment.

### 1.3 Target Users

The target users are mainly:

- programming students learning Python;
- beginner developers who want quick feedback before submitting code;
- teachers or assistants who need a simple demonstration of agent-based software design;
- developers who want a lightweight local pre-review tool.

### 1.4 Expected Value

The system provides value by helping users:

- detect syntax errors before running or submitting code;
- understand basic code metrics such as number of lines, functions, classes, and imports;
- identify simple maintainability issues;
- receive structured feedback in a readable format;
- improve their code before committing it to a GitHub repository.

---

## 2. AI / Agent-Based Approach

### 2.1 General Agent Logic

The project follows an **agent-based workflow**. The system is organized around a central agent that coordinates several tools. The agent receives the user request, decides which tools must be used, executes them, combines their outputs, and returns a final structured answer.

The workflow is designed to avoid treating the AI or agent component as a black box. Each action is separated into clear steps.

### 2.2 Planned Agent Workflow

The expected workflow is:

1. The user launches the program from the command line.
2. The user provides the path of a Python file to analyze.
3. The agent validates the input path.
4. The agent calls the file reader tool to load the source code.
5. The agent calls the syntax checker tool to verify Python syntax.
6. If the syntax is valid, the agent calls the metrics tool.
7. The agent calls the code quality tool to detect basic maintainability issues.
8. The agent combines all tool outputs.
9. The agent generates a structured review.
10. The system optionally saves the review as a Markdown or text report.

### 2.3 Decision-Making Logic

The agent will use simple rule-based decision logic:

- If the file path is missing, the system asks for a valid path.
- If the file does not exist, the system returns a clear error message.
- If the file is not a `.py` file, the system warns the user.
- If the file contains syntax errors, the system reports them and stops deeper analysis.
- If the syntax is valid, the system continues with metrics and quality analysis.
- If report generation is enabled, the system writes the final output to a file.

This makes the system predictable, testable, and easier to debug.

### 2.4 Fallback Strategy

The system will include fallback behavior:

- If a file cannot be read, the user receives an explanation instead of a crash.
- If the syntax checker fails, the error is captured and returned in the review.
- If one non-critical tool fails, the system still tries to return partial results.
- If the report cannot be saved, the final review is still displayed in the terminal.

---

## 3. Planned Tools

The system will use several internal tools. Each tool has one clear responsibility and can be tested independently.

| Tool | Purpose | Input | Output |
|---|---|---|---|
| `FileReaderTool` | Reads a local Python file | File path | Source code as text |
| `SyntaxCheckerTool` | Checks if the code has valid Python syntax | Source code | Syntax status and error details |
| `CodeMetricsTool` | Extracts basic code metrics | Source code | Number of lines, functions, classes, imports, comments |
| `CodeQualityTool` | Detects simple code quality issues | Source code / AST | List of warnings and suggestions |
| `ReportGeneratorTool` | Builds a structured report | Analysis results | Markdown or text report |

### 3.1 FileReaderTool

The `FileReaderTool` will open and read a local `.py` file using UTF-8 encoding. It will handle common errors such as missing files, permission problems, or invalid paths.

### 3.2 SyntaxCheckerTool

The `SyntaxCheckerTool` will use Python's built-in `ast` module to parse the source code. If parsing succeeds, the file is considered syntactically valid. If parsing fails, the system returns the error line and message.

### 3.3 CodeMetricsTool

The `CodeMetricsTool` will extract basic measurable information:

- total number of lines;
- number of empty lines;
- number of comment lines;
- number of functions;
- number of classes;
- number of import statements.

These metrics help the user understand the structure and size of the code.

### 3.4 CodeQualityTool

The `CodeQualityTool` will detect simple issues, for example:

- functions that are too long;
- missing function docstrings;
- missing class docstrings;
- too many nested conditions;
- unused-looking imports if detectable with simple rules;
- files with very low comment or documentation presence.

The goal is not to perform advanced static analysis, but to provide educational feedback.

### 3.5 ReportGeneratorTool

The `ReportGeneratorTool` will format the result into a clear report containing:

- file analyzed;
- syntax status;
- code metrics;
- detected issues;
- improvement suggestions;
- final conclusion.

---

## 4. Preliminary Programming Concepts

The project will require the following programming concepts.

### 4.1 Python Modules and Packages

The system will be divided into multiple files and folders to keep the structure clean. For example, the agent logic, tools, tests, and documentation will be separated.

### 4.2 Object-Oriented Programming

Each tool will be represented as a class. A common tool interface may be used so that all tools follow the same structure. This makes the system easier to extend later.

### 4.3 Abstract Base Classes

An abstract base class can define the expected behavior of all tools, such as a `name` property and an `execute()` method. This improves consistency across the project.

### 4.4 File Handling

The system must read local files and may write output reports. This requires safe file opening, reading, writing, and error handling.

### 4.5 Exception Handling

The system must not crash when the user provides invalid input. Exceptions such as `FileNotFoundError`, `SyntaxError`, and permission errors will be handled properly.

### 4.6 AST Parsing

Python's `ast` module will be used to analyze the structure of source code. This allows the system to count functions, classes, imports, and detect syntax errors without executing the analyzed code.

### 4.7 Data Structures

The system will use dictionaries and lists to store intermediate analysis results. For example, tool outputs can be collected into a single dictionary before generating the final report.

### 4.8 Command-Line Interface

The first version will run as a command-line tool. The user will provide a file path, and the system will print the review in the terminal.

### 4.9 Unit Testing

The main tools and agent workflow will be tested using `pytest` or Python's standard testing tools. Tests will check valid input, invalid input, syntax errors, and expected analysis results.

### 4.10 Git and GitHub Version Control

The project will be stored in a GitHub repository. Regular commits will be used to show progressive development from planning to implementation, testing, documentation, and final deployment preparation.

---

## 5. Initial System Architecture

The planned architecture is modular.

```text
User
 |
 | provides file path
 v
Command-Line Interface
 |
 v
AI Code Review Agent
 |
 |-- FileReaderTool
 |-- SyntaxCheckerTool
 |-- CodeMetricsTool
 |-- CodeQualityTool
 |-- ReportGeneratorTool
 |
 v
Structured Review Output
```

### 5.1 Planned Folder Structure

```text
ai-code-review-agent/
│
├── src/
│   ├── main.py
│   ├── agent.py
│   └── tools/
│       ├── file_reader_tool.py
│       ├── syntax_checker_tool.py
│       ├── code_metrics_tool.py
│       ├── code_quality_tool.py
│       └── report_generator_tool.py
│
├── tests/
│   ├── test_file_reader_tool.py
│   ├── test_syntax_checker_tool.py
│   ├── test_code_metrics_tool.py
│   └── test_agent.py
│
├── docs/
│   ├── step1_planning.md
│   ├── step2_progress.md
│   ├── step3_testing_deployment.md
│   └── final_report.md
│
├── examples/
│   ├── good_code_example.py
│   └── bad_code_example.py
│
├── reports/
│   └── generated_report.md
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 6. Initial Functional and Non-Functional Requirements

### 6.1 Functional Requirements

| ID | Requirement |
|---|---|
| FR1 | The system shall accept a Python file path as user input. |
| FR2 | The system shall read the content of the selected file. |
| FR3 | The system shall check whether the file contains valid Python syntax. |
| FR4 | The system shall extract basic code metrics from the file. |
| FR5 | The system shall detect basic code quality issues. |
| FR6 | The system shall generate structured feedback for the user. |
| FR7 | The system shall optionally save the feedback into a report file. |

### 6.2 Non-Functional Requirements

| ID | Requirement |
|---|---|
| NFR1 | The system should run locally using Python 3.11 or higher. |
| NFR2 | The system should return feedback within a few seconds for small or medium files. |
| NFR3 | The system should be understandable for beginner and intermediate Python students. |
| NFR4 | The system should be modular and easy to extend with new tools. |
| NFR5 | The system should handle common errors without crashing. |

### 6.3 Constraints

| ID | Constraint |
|---|---|
| C1 | The system must be implemented in Python. |
| C2 | The system must use at least one tool during execution. |
| C3 | The system must include tests for the main functionality. |
| C4 | The system must include deployment instructions. |
| C5 | The system must be stored in a GitHub repository. |

---

## 7. Initial Risk Assessment

| Risk | Description | Mitigation |
|---|---|---|
| Invalid file input | The user may provide a wrong path or unsupported file type. | Validate input and return clear error messages. |
| Syntax parsing failure | The analyzed file may contain syntax errors. | Catch parsing errors and include them in the report. |
| Overly simple analysis | The tool may not detect advanced issues. | Clearly document the system as an educational first-level review tool. |
| False positives | The quality tool may report issues that are not critical. | Present warnings as suggestions, not absolute errors. |
| Poor project structure | The project may become hard to maintain. | Use modular folders and clear documentation. |
| Testing gaps | Some edge cases may not be covered. | Add test scenarios for valid, invalid, and incomplete files. |

---

## 8. Initial Testing Strategy

Testing will be developed progressively with the implementation.

### 8.1 Planned Unit Tests

| Component | Planned Tests |
|---|---|
| FileReaderTool | valid file, missing file, empty file |
| SyntaxCheckerTool | valid syntax, invalid syntax |
| CodeMetricsTool | functions count, classes count, imports count |
| CodeQualityTool | long function detection, missing docstring detection |
| Agent workflow | normal execution, invalid input, syntax error case |

### 8.2 Planned Integration Tests

The integration tests will verify that:

- the agent can call several tools in sequence;
- each tool output is correctly passed to the next component;
- the final report includes all required sections;
- errors from tools are handled without stopping the entire program unexpectedly.

---

## 9. Development Roadmap

The project will be developed progressively.

| Milestone | Target Content |
|---|---|
| Step 1 | Planning documentation, project idea, tools, concepts, initial architecture |
| Step 2 | First implementation of the CLI, agent workflow, and main tools |
| Step 3 | Test scenarios, error handling, deployment preparation, data conversion explanation |
| Final Submission | Final code, tests, documentation, README, GitHub link, final report |

### 9.1 Planned Commit Strategy

The GitHub repository will include regular commits such as:

```text
Initial repository setup
Add step 1 planning documentation
Create basic project structure
Implement file reader tool
Implement syntax checker tool
Implement code metrics tool
Add agent workflow
Add unit tests for tools
Add report generator
Update README with setup instructions
Add final report documentation
```

---

## 10. Data Porting and Conversion Plan

The system will transform data through several stages:

1. **User input:** file path entered in the terminal.
2. **Raw file content:** the file reader converts the path into source code text.
3. **Parsed structure:** the syntax checker and metrics tools use the source code and AST representation.
4. **Analysis results:** each tool returns structured dictionaries or lists.
5. **Final report:** the report generator converts structured results into readable Markdown or plain text.

This ensures that data is not handled randomly. Each component receives a clear input format and returns a clear output format.

---

## 11. Deployment Preparation Plan

The system will be prepared as a local command-line application.

The expected launch process will be:

```bash
git clone <repository-url>
cd ai-code-review-agent
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python src/main.py examples/bad_code_example.py
```

The final README will explain:

- how to install Python dependencies;
- how to run the program;
- how to analyze an example file;
- how to run tests;
- how to generate a report;
- what limitations the system has.

---

## 12. Proposed Deployment Strategy

The most suitable deployment strategy for this project is a **local command-line deployment**.

This strategy is appropriate because:

- the system analyzes local Python files;
- it does not require a web server;
- it is simple to install and test;
- it is suitable for students and controlled academic use;
- it avoids unnecessary infrastructure complexity.

A future version could be deployed as:

- a GitHub Action that reviews code automatically after each push;
- a VS Code extension;
- a small web service with an upload interface.

For the current academic version, local deployment is the safest and most realistic approach.

---

## 13. Step 1 Conclusion

At this stage, the project is clearly defined but not fully implemented yet. The Step 1 work focuses on planning, feasibility, architecture, tools, risks, and the development direction.

The planned system is a domain-specific agent, not a generic chatbot. It focuses on Python code review and uses specialized tools to analyze source files. This makes the project suitable for the assignment because it demonstrates agent-based logic, tool usage, modular implementation, testability, documentation, and preparation for controlled deployment.

The next step will be to implement the first working version of the project with a command-line interface, the agent workflow, and the first analysis tools.
