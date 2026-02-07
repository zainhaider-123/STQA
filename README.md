# STQA - Software Testing and Quality Assurance

This project contains examples of software testing with Python unittest for a simple calculator.

## Prerequisites

- Python >= 3.12
- uv (fast Python package installer and resolver)

## Installing uv

### Windows
Use the PowerShell installer:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Or via WinGet:
```powershell
winget install --id=astral-sh.uv -e
```

Or via Scoop:
```powershell
scoop install main/uv
```

### macOS
Using Homebrew:
```bash
brew install uv
```

Or standalone installer:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Linux
Standalone installer:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or via package manager (if available).

For other installation methods, see the [official documentation](https://docs.astral.sh/uv/getting-started/installation/).

## Running the Code

To run the calculator tests, use uv to execute the script:

```bash
uv run python lecture_one.py
```

This will run the unit tests for the calculator functions (add, subtract, multiply, divide) and display results with execution times.