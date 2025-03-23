# Windows Development Environment Setup Guide

This guide documents the development environment setup for Windows 10, including installed tools, configuration steps, and instructions for additional installations.

## Currently Installed Development Tools

### Core Tools
| Tool | Version | Status | Purpose |
|------|---------|--------|---------|
| Winget | v1.10.340 | ✅ Installed | Windows package manager for installing software |
| Git | 2.47.0.windows.1 | ✅ Installed | Version control system |
| Node.js | v23.1.0 | ✅ Installed | JavaScript runtime environment |
| npm | 10.9.0 | ✅ Installed | Node.js package manager |
| Python | 3.12.9 | ✅ Installed | Programming language |
| pip | 25.0 | ✅ Installed | Python package manager |
| Visual Studio Code | - | ✅ Installed | Code editor |
| Notepad++ | - | ✅ Installed | Text editor |

### Additional Tools
| Tool | Version | Status | Purpose |
|------|---------|--------|---------|
| Windows Terminal | 1.22.10352.0 | ✅ Installed | Modern terminal application |
| PowerToys | 0.89.0 | ✅ Installed | Set of utilities for power users |

## Installing Additional Tools

Some tools couldn't be installed automatically through Winget. Here are manual installation instructions for these tools:

### Postman (API Testing)
1. Visit: https://www.postman.com/downloads/
2. Download the Windows installer
3. Run the installer with administrative privileges

### GitHub Desktop (Git GUI)
1. Visit: https://desktop.github.com/
2. Download the Windows installer
3. Run the installer with administrative privileges

### Docker Desktop (Container Platform)
1. Visit: https://www.docker.com/products/docker-desktop
2. Download Docker Desktop for Windows
3. Run the installer with administrative privileges
4. Note: Requires Hyper-V or WSL 2

## Using Package Managers

### Winget (Windows Package Manager)
Winget is Microsoft's official package manager for Windows, similar to Homebrew on macOS.

#### Basic Winget Commands
```powershell
# Search for packages
winget search [package-name]

# Install a package
winget install [package-id]

# List installed packages
winget list

# Upgrade packages
winget upgrade
winget upgrade --all
```

### npm (Node.js Package Manager)
Already installed with Node.js.

#### Basic npm Commands
```powershell
# Install a package globally
npm install -g [package-name]

# Create a new Node.js project
npm init

# Install dependencies for a project
npm install

# Run scripts defined in package.json
npm run [script-name]
```

### pip (Python Package Manager)
Already installed with Python.

#### Basic pip Commands
```powershell
# Install a package
pip install [package-name]

# List installed packages
pip list

# Upgrade a package
pip install --upgrade [package-name]

# Install packages from requirements.txt
pip install -r requirements.txt
```

## Configuring Git

Git is already installed, but you may want to set up your identity:

```powershell
# Set your name
git config --global user.name "Your Name"

# Set your email
git config --global user.email "your.email@example.com"

# Set default branch to main
git config --global init.defaultBranch main

# Configure line endings (recommended on Windows)
git config --global core.autocrlf true
```

## Using Windows Terminal

Windows Terminal provides a modern terminal experience with tabs, panes, and customization options.

### Key Features
- Multiple tabs and panes
- Custom themes and color schemes
- Unicode and UTF-8 character support
- GPU accelerated text rendering

### Customization
Open settings by pressing `Ctrl+,` or clicking the dropdown menu → Settings. You can customize:
- Default profile
- Color schemes
- Key bindings
- Font settings
- Background (including opacity)

## Using PowerToys

PowerToys includes several useful utilities for developers:

### Key Utilities
- **FancyZones**: Advanced window manager
- **PowerRename**: Bulk file renaming
- **Image Resizer**: Resize images directly from File Explorer
- **PowerToys Run**: Quick launcher (Alt+Space)
- **Color Picker**: System-wide color picker (Win+Shift+C)
- **File Explorer Add-ons**: Preview panes for additional file types

Access PowerToys from the system tray icon to configure each utility.

## Creating New Projects

### Node.js Project
```powershell
# Create a new directory
mkdir my-project
cd my-project

# Initialize a new Node.js project
npm init -y

# Install dependencies
npm install [dependency-name]

# Create an index.js file
notepad index.js
```

### Python Project
```powershell
# Create a new directory
mkdir my-python-project
cd my-python-project

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install [package-name]

# Create a main.py file
notepad main.py
```

## Maintaining Your Development Environment

### Keeping Tools Updated
```powershell
# Update Winget packages
winget upgrade --all

# Update npm
npm install -g npm@latest

# Update npm packages globally
npm update -g

# Update pip
python -m pip install --upgrade pip

# Update Git
winget upgrade Git.Git
```

## Troubleshooting

### PATH Variables
If a command isn't recognized, check if it's in your PATH:
```powershell
# Display PATH environment variable
echo $env:PATH

# Add a directory to PATH (current session only)
$env:PATH += ";C:\path\to\directory"

# Add a directory to PATH permanently (requires admin)
[Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";C:\path\to\directory", "User")
```

### Administrative Privileges
Some installers require administrative privileges. Right-click and select "Run as administrator" or use:
```powershell
# Run PowerShell as administrator
Start-Process powershell -Verb RunAs
```
