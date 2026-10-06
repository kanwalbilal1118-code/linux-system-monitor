# Linux System Monitor

A Linux system monitoring and log analysis tool built with **Python, Bash, pytest, Git, GitHub Actions, and Streamlit**.

The project collects system information, executes controlled Linux commands, analyzes log files, generates reports, and provides an interactive Streamlit dashboard for viewing monitoring results.

---

## Overview

**Linux System Monitor** was developed as a practical Linux and Python automation project.

The project combines:

* Python-based system monitoring
* Linux command execution
* Log analysis and error classification
* Bash automation
* Linux pipelines and command-line processing
* Automated testing with pytest
* Git and GitHub version control
* GitHub Actions continuous integration
* Streamlit dashboard visualization

The goal is to demonstrate how Linux tools, Python automation, testing, and Git-based development can be combined into a single working system.

---

## Features

### System Information

Collects information about the Linux environment, including:

* Hostname
* Operating system
* OS version
* CPU model
* Total memory
* Available memory
* Disk capacity
* Disk usage

### Log Analysis

Analyzes log files and classifies detected errors into categories such as:

* Connection Error
* Permission Error
* File Error
* Other Error

The analyzer processes a specified log file and produces structured error statistics that can be used by the monitoring workflow and dashboard.

### Linux Command Execution

Uses Python's `subprocess` functionality to execute controlled Linux commands and capture their output.

Command execution handles:

* Standard output
* Standard error
* Exit codes
* Command failures

### Bash Automation

The project includes Bash scripts for automating monitoring and execution workflows.

### Resource Monitoring

The system collects and presents resource information such as:

* Memory utilization
* Available memory
* Disk utilization
* Disk usage

### Report Generation

The monitoring workflow generates a structured system report containing:

* System information
* Memory information
* Disk information
* Linux command output
* Pipeline information
* Log analysis results
* Total detected errors

### Automated Testing

The project includes a pytest-based test suite covering the project's major components.

The complete test suite currently contains **29 tests**, which pass successfully.

### Streamlit Dashboard

The project includes an interactive Streamlit dashboard for viewing monitoring results.

The dashboard provides:

* System overview
* Memory and disk utilization
* System health information
* Error distribution
* System information
* Log analysis
* Linux command information
* Manual data refresh

---

## Project Architecture

```text
linux-system-monitor/
│
├── dashboard/
│   └── app.py
│
├── logs/
│   └── system.log
│
├── reports/
│   └── generated reports
│
├── scripts/
│   ├── monitor.sh
│   └── run_monitor.sh
│
├── src/
│   ├── config.py
│   ├── log_analyzer.py
│   ├── main.py
│   ├── monitor.py
│   ├── pipeline_commands.py
│   ├── system_commands.py
│   ├── system_info.py
│   └── system_report.py
│
├── tests/
│   └── pytest test files
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── .gitignore
└── README.md
```

---

## How It Works

The project follows a monitoring and analysis pipeline:

```text
Linux Environment
       │
       ▼
System Information
       │
       ├── CPU
       ├── Memory
       └── Disk
       │
       ▼
Linux Commands
       │
       ▼
Python Processing
       │
       ├── Log Analysis
       ├── Error Classification
       ├── Pipeline Processing
       └── Report Generation
       │
       ▼
Streamlit Dashboard
```

The dashboard retrieves monitoring information from the project's Python modules rather than relying on hard-coded monitoring values.

---

## Technologies Used

| Technology         | Purpose                                                            |
| ------------------ | ------------------------------------------------------------------ |
| **Python**         | System monitoring, automation, log analysis, and report generation |
| **Linux / WSL**    | Operating environment and command-line tools                       |
| **Bash**           | Automation scripts                                                 |
| **subprocess**     | Controlled Linux command execution                                 |
| **pytest**         | Automated testing                                                  |
| **Git**            | Version control                                                    |
| **GitHub**         | Repository hosting and collaboration                               |
| **GitHub Actions** | Continuous integration                                             |
| **Streamlit**      | Interactive monitoring dashboard                                   |

---

## Requirements

The project requires:

* Linux or WSL
* Python 3
* Git
* Bash
* pytest
* Streamlit

The project has been developed and tested in a WSL Ubuntu environment.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/kanwalbilal1118-code/linux-system-monitor.git
cd linux-system-monitor
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

### 3. Activate the Virtual Environment

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install pytest streamlit
```

---

## Running the Project

### Run the Monitoring Application

The main Python entry point runs the monitoring workflow.

```bash
python -m src.main logs/system.log
```

The workflow collects system information, executes Linux commands, analyzes the specified log file, and generates a system report.

### Run the Bash Monitoring Script

```bash
bash scripts/run_monitor.sh
```

The additional monitoring script can also be executed with:

```bash
bash scripts/monitor.sh
```

---

## Running the Dashboard

Start the Streamlit dashboard with:

```bash
streamlit run dashboard/app.py
```

The dashboard provides several sections for viewing monitoring information.

### Overview

Displays information such as:

* Memory usage
* Available memory
* Disk usage
* Log errors
* Resource utilization
* System health
* Error distribution

### System Information

Displays information collected from the Linux environment, including:

* Hostname
* Operating system
* OS version
* CPU model
* Memory information
* Disk information

### Log Analysis

Displays results produced by the project's log analyzer, including:

* Total errors
* Error categories
* Error breakdown

### Linux Commands

Displays information collected through the project's Linux command execution layer.

---

## Testing

The project uses **pytest** for automated testing.

Run the complete test suite with:

```bash
pytest
```

For detailed test output:

```bash
pytest -v
```

The current test suite contains **29 tests**, covering system information, log analysis, Linux commands, monitoring functionality, report generation, and related components.

---

## Continuous Integration

The project uses **GitHub Actions** to automatically run the test suite.

The CI workflow runs when changes are pushed to the repository or when a pull request is opened against the `main` branch.

The workflow:

```text
Push / Pull Request
        │
        ▼
GitHub Actions
        │
        ▼
Set up Python
        │
        ▼
Install Dependencies
        │
        ▼
Run pytest
        │
        ▼
Pass / Fail
```

The CI workflow helps detect test failures before changes are merged into the `main` branch.

---

## Git and GitHub Workflow

Git was used throughout development to manage project history and development branches.

The project follows a feature-based workflow:

```text
main
 │
 ├── feature branch
 │
 ├── development commits
 │
 ├── automated tests
 │
 ├── pull request
 │
 ├── GitHub Actions CI
 │
 └── merge into main
```

The project demonstrates practical use of:

* Branching
* Commits
* Pull requests
* Pull request reviews
* Continuous integration
* Merging
* Remote repository management

---

## Log Analysis

The log analyzer reads a specified log file and categorizes detected errors.

Example:

```bash
python -m src.log_analyzer logs/system.log
```

The resulting information can be used by the monitoring workflow and Streamlit dashboard.

---

## Development Workflow

A typical development workflow for the project is:

```bash
# Create a feature branch
git checkout -b feature/example

# Make changes

# Check the working tree
git status

# Stage changes
git add .

# Commit changes
git commit -m "Add example feature"

# Push the branch
git push -u origin feature/example
```

A pull request can then be opened on GitHub for review and integration into `main`.

---

## Learning Outcomes

This project provided practical experience with:

* Linux command-line tools
* Python automation
* Python `subprocess`
* Environment variables
* Standard output and standard error
* Exit codes
* Bash scripting
* Linux pipelines and redirection
* Log processing
* Error classification
* Automated testing
* Git branching and commits
* GitHub pull requests
* GitHub Actions
* Continuous integration
* Streamlit dashboard development

---

## Future Improvements

Possible future improvements include:

* CPU utilization monitoring
* Additional system resource metrics
* Historical monitoring data
* Automated scheduled reports
* Additional log categories
* More advanced dashboard visualizations
* Expanded automated test coverage
* Additional CI checks

---

## Project Status

The core Linux monitoring, log analysis, report generation, testing, Git workflow, continuous integration, and Streamlit dashboard functionality has been implemented.

The project is currently maintained as a learning and portfolio project focused on practical Linux automation, Python development, testing, and software development workflows.

---

## Author

**Kanwal Bilal**

Software Engineering Student
Pakistan

---

## License

This project currently does not specify an open-source license.

If the repository is later intended for public reuse, modification, and redistribution, an appropriate open-source license can be added.
