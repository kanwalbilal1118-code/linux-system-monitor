
# Linux System Monitor

A Linux system monitoring and log analysis tool built with Python, Bash, pytest, Git, and Streamlit.

The project collects system information, analyzes log files, executes controlled Linux system commands, generates reports, and provides an interactive Streamlit dashboard for viewing system health and monitoring results.

---

## Overview

Linux System Monitor was developed as a practical Linux and Python automation project.

The project combines:

- Python system monitoring
- Linux subprocess execution
- Log analysis and error classification
- Bash automation
- Pipelines and command-line processing
- Automated testing with pytest
- Git and GitHub version control
- Streamlit dashboard visualization

The project is designed to demonstrate how Linux command-line tools, Python automation, testing, and Git-based development can be combined into one working system.

---

## Features

### System Information

Collects information about the Linux environment, including:

- Hostname
- Operating system
- OS version
- CPU model
- Total memory
- Available memory
- Disk capacity
- Disk usage

### Log Analysis

The project analyzes log files and classifies detected errors into categories such as:

- Connection Error
- Permission Error
- File Error
- Other Error

The analyzer can process a log file and generate a structured report.

### Linux Command Execution

The project uses Python's `subprocess` functionality to execute controlled Linux commands and capture their output.

Command execution handles:

- Standard output
- Standard error
- Exit codes
- Command failures

### Bash Automation

Shell scripts are included for automating monitoring and execution workflows.

### Resource Monitoring

The system calculates and presents:

- Memory utilization
- Available memory
- Disk utilization
- Disk usage

### Automated Testing

The project includes a pytest-based test suite for validating system information, log analysis, command execution, monitoring functionality, and related components.

### Streamlit Dashboard

The project includes an interactive dashboard for presenting monitoring results.

The dashboard provides:

- System overview
- Memory and disk utilization
- System health status
- Error distribution
- System information
- Log analysis
- Linux command information
- Manual data refresh

---

## Project Architecture

The project follows a modular structure:

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
├── .gitignore
└── README.md
````

---

## How It Works

The project follows a simple monitoring pipeline:

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
       └── Report Generation
       │
       ▼
Streamlit Dashboard
```

The dashboard retrieves data from the project's Python backend rather than using hard-coded monitoring values. The Streamlit application imports the system information, log analysis, and system command modules directly. 

---

## Technologies Used

| Technology | Purpose                                      |
| ---------- | -------------------------------------------- |
| Python     | System monitoring, automation, analysis      |
| Linux      | Operating environment and command-line tools |
| Bash       | Automation scripts                           |
| subprocess | Linux command execution                      |
| pytest     | Automated testing                            |
| Git        | Version control                              |
| GitHub     | Repository and collaboration                 |
| Streamlit  | Interactive monitoring dashboard             |

---

## Requirements

The project requires:

* Linux or WSL
* Python 3
* Git
* Bash
* pytest
* Streamlit

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/linux-system-monitor.git
cd linux-system-monitor
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

```bash
source .venv/bin/activate
```

### 4. Install the required packages

```bash
pip install pytest streamlit
```

---

## Running the Project

### Run the monitoring application

The main Python entry point can be used to run the monitoring workflow.

```bash
python -m src.main logs/system.log
```

### Run the Bash monitoring script

```bash
bash scripts/run_monitor.sh
```

or:

```bash
bash scripts/monitor.sh
```

Use the script appropriate to the workflow configured in the project.

---

## Running the Dashboard

Start the Streamlit dashboard with:

```bash
streamlit run dashboard/app.py
```

The dashboard provides several sections:

### Overview

Displays a current snapshot of:

* Memory usage
* Available memory
* Disk usage
* Log errors
* Resource utilization
* System health
* Error distribution

### System Information

Displays information collected from the Linux environment, including the hostname, operating system, OS version, CPU model, memory, and disk information. 

### Log Analysis

Displays the results generated by the project's log analyzer, including total errors, error categories, and the error breakdown. 

### Linux Commands

Displays information collected through the project's subprocess command layer. 

---

## Testing

The project uses pytest for automated testing.

Run the complete test suite with:

```bash
pytest
```

For more detailed output:

```bash
pytest -v
```

Tests are organized under the `tests/` directory and cover different parts of the project.

---

## Log Analysis

The log analyzer reads the specified log file and categorizes errors.

Example:

```bash
python -m src.log_analyzer logs/system.log
```

The resulting information can be used by the monitoring workflow and dashboard.

The dashboard loads the project's log file and passes it to the backend analyzer before displaying the resulting error categories. 

---

## Git and GitHub Workflow

Git was used throughout development to manage the project history and development branches.

The project workflow includes:

```text
main
 │
 ├── feature branches
 │
 ├── commits
 │
 ├── pull requests
 │
 ├── code review
 │
 └── merge
```

GitHub collaboration features are used to practice:

* Branching
* Pull requests
* Code reviews
* Issue tracking
* Continuous integration
* Project management

---

## Continuous Integration

GitHub Actions can be used to automatically run the project's test suite whenever changes are pushed or a pull request is opened.

The intended workflow is:

```text
Push / Pull Request
        │
        ▼
 GitHub Actions
        │
        ▼
 Install dependencies
        │
        ▼
     Run pytest
        │
        ▼
   Pass / Fail
```

This helps detect problems before changes are merged into the main branch.

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

This project was developed as a practical application of Linux and Git/GitHub concepts.

It demonstrates experience with:

* Linux command-line tools
* Python automation
* subprocess management
* environment variables
* standard output and standard error
* exit codes
* Bash scripting
* pipelines and redirection
* log processing
* automated testing
* Git branching and history management
* GitHub collaboration
* Continuous Integration
* Streamlit dashboard development

---

## Future Improvements

Potential future improvements include:

* More system resource metrics
* CPU utilization monitoring
* Historical monitoring data
* Automated scheduled reports
* Additional log categories
* More advanced dashboard visualizations
* Expanded automated test coverage
* Additional CI checks

---

## Project Status

The core Linux monitoring, log analysis, testing, Git workflow, and Streamlit dashboard functionality has been implemented.

The project is being maintained as a learning and portfolio project focused on practical Linux automation and software development workflows.

---

## Author

**Kanwal Bilal**

Software Engineering Student
Pakistan

---

## License

This project currently does not specify an open-source license.

If the repository is later intended for reuse, modification, and redistribution by others, an appropriate open-source license can be added.

````
