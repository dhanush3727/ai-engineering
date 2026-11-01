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
