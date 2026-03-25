@echo off
setlocal EnableExtensions

set "VENV_DIR=%USERPROFILE%\power-data-analysis-kernel\.venv"

if not exist "%VENV_DIR%\Scripts\jupyter-lab.exe" (
    echo JupyterLab was not found in "%VENV_DIR%".
    echo Run install_power_data_kernel.bat first.
    exit /b 1
)

call "%VENV_DIR%\Scripts\activate.bat"
jupyter lab
