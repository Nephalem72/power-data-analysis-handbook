@echo off
setlocal EnableExtensions

set "SCRIPT_DIR=%~dp0"
set "INSTALL_ROOT=%USERPROFILE%\power-data-analysis-kernel"
set "VENV_DIR=%INSTALL_ROOT%\.venv"
set "REQ_FILE=%SCRIPT_DIR%power_data_kernel_requirements.txt"
set "KERNEL_NAME=power-data-analysis"
set "DISPLAY_NAME=Power Data Analysis"

echo.
echo [1/5] Preparing installation directory...
if not exist "%INSTALL_ROOT%" mkdir "%INSTALL_ROOT%"

echo [2/5] Selecting Python launcher...
py -3.11 -V >nul 2>&1
if %errorlevel%==0 (
    set "PY_CMD=py -3.11"
) else (
    py -3 -V >nul 2>&1
    if %errorlevel%==0 (
        set "PY_CMD=py -3"
    ) else (
        echo Python launcher "py" was not found.
        echo Install Python 3.11+ and rerun this installer.
        exit /b 1
    )
)

echo [3/5] Creating virtual environment...
if not exist "%VENV_DIR%\Scripts\python.exe" (
    %PY_CMD% -m venv "%VENV_DIR%"
)

echo [4/5] Installing учебное ядро...
"%VENV_DIR%\Scripts\python.exe" -m pip install --upgrade pip
if errorlevel 1 exit /b 1

"%VENV_DIR%\Scripts\python.exe" -m pip install -r "%REQ_FILE%"
if errorlevel 1 exit /b 1

echo [5/5] Registering Jupyter kernel...
"%VENV_DIR%\Scripts\python.exe" -m ipykernel install --user --name "%KERNEL_NAME%" --display-name "%DISPLAY_NAME%"
if errorlevel 1 exit /b 1

echo.
echo Installation completed.
echo Kernel name: %KERNEL_NAME%
echo Display name: %DISPLAY_NAME%
echo Virtual environment: %VENV_DIR%
echo.
echo To start JupyterLab with this environment, run:
echo "%SCRIPT_DIR%launch_jupyter_lab.bat"
echo.
pause
