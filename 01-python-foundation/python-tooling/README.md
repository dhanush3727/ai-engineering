# Python Tooling
## Virtual Environments (`venv`)
### Overview:
A virtual environment is an isolated python environment for a specific project. It allows each project to have its own installed packages and package versions. So if we have differnt Projects like Project A and Project B then we can easily manage separate dependencies based on the project requirements

### How does it work?
Step 1: Open your project directory
Step 2: Create a virtual environment
```bash
python -m venv .venv
```
- It creates a `.venv` file. Don't commit this to the github
Step 3: Activate it
```bash
.venv\Scripts\Activate.ps1
```
Step 4: Install packages inside the environment
Step 5: Check installed packages
Step 6: Deactivate the environment

## `pip`:
`pip` is Python's package installer. It allows you to install, update, uninstall and inspect external Python libraries.

### How does pip work?
Make sure your `.venv` is activated before running these commands.
- Install a package: `python -m pip install httpx`. It installs `httpx` into the currently selected python environment.
- Install a specific version: `python -m pip install httpx==0.28.1`. Useful when your application requires a particular package version.
- Upgrade a package: `python -m pip install --upgrade httpx`. Installs the latest compatible release available from the configured package index.
- Uninstall a package: `python -m pip uninstall rich`. Removes the package from the active environment.
- List installed packages: `python -m pip list`. Displays installed packages and their versions.
- Inspect package information: `python -m pip show httpx`. Displays details such as, Installed version, package location, dependencies, package information.
- Check dependency issues: `python -m pip check`. Checks whether installed packages have incompatible or missing dependencies.

### Share the packages:
What happens when you share your python project with another developer? They won't automatically have the same packages installed on their computer. That's where `requirements.txt` comes in. 

This is a text file that lists the Python packages and their versions required by your project. Example,
```text
httpx==0.28.1
requests==2.34.2
python-dotenv==1.2.4
```
It tells another developer which dependencies to install.

### How does it work?
- Step 1: Activate your virtual environment. `.venv\Scripts\Activate.ps1`.
- Step 2: Generate `requirements.txt`. `python -m pip freeze > requirements.txt`.
- Step 3: Open `requirements.txt`.
- Step 4: Install needed dependencies. If another developer wants to install the dependencies the run this command `python -m pip install -r requirements.txt`.

## `pyproject.toml`:
`pyproject.toml` is a configuration file used by modern Python projects. It can define:
- Project name and version.
- Python version requirements.
- Project dependencies.
- Build system configuration.
- Tool configurations such as Ruff and pytest.
Think of it as a central configuration file for your python project.

### How does it work?
Let's create a `pyproject.toml` file in your project directory. Add configuration
```toml
[project]
name = "python-tooling"
version = "0.1.0"
description = "Python engineering learning project"
requires-python = ">=3.14"
dependencies = [
    "httpx>=0.28.1",
    "requests>=2.34.2",
    "python-dotenv>=1.2.4"
]
```
Here,
`[project]`
Defines your project's metadata.
- `name`: Project name.
- `version`: Current project version.
- `description`: What the project does.
- `requires-python`: Minimum supported Python version.
- `dependencies`: External packages required by the project.
Why `>=` instead of `==`?
- `httpx==0.28.1` means exactly version 0.28.1.
- `httpx>=0.28.1` means version 0.28.1 or newer.
For a project using this configuration, pip can install its  dependencies directly. `python -m pip install .`. The `.` means install the current project, including its declared dependencies.

## Ruff:
Ruff is a fast python development tool that provides two main features:
- `Linting`: Detects potential bugs, unused imports, code-quality issues and common mistakes.
- `Formatting`: Automatically formats code into a consistent style.
Think of it like ESLint + Prettier in the JS ecosystem.

### How does it work?
Step 1 - Install Ruff: Activate your `.venv` first. `python -m pip install ruff`.
Step 2 - Check the installed version: `ruff --version`.
Step 3 - Unserstand linting: If we have any unused import then we run `ruff check .` ruff identifies these issues. To fix run `ruff check . --fix`.
Step 4 - Understand formatting: run `ruff format .`.

## pytest:
`pytest` is a python testing framework used to test your functions and application logic automatically.

### How does pytest work?
Step 1 - Install pytest: Activate your `.venv` and run: `python -m pip install pytest`
Step 2 - Create a file: `test_equipment.py`.
Step 3 - Write application code
Step 4 - Write test cases
Step 5 - Run your tests: `python -m pytest`