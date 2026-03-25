@echo off
setlocal EnableExtensions

set "SCRIPT_DIR=%~dp0"
set "ROOT_DIR=%SCRIPT_DIR%.."
set "RELEASE_DIR=%ROOT_DIR%\release-assets"
set "BUNDLE_DIR=%RELEASE_DIR%\power-data-kernel-bootstrap"
set "ZIP_FILE=%RELEASE_DIR%\power-data-kernel-bootstrap-v0.1.0.zip"

if not exist "%RELEASE_DIR%" mkdir "%RELEASE_DIR%"
if exist "%BUNDLE_DIR%" rmdir /s /q "%BUNDLE_DIR%"
mkdir "%BUNDLE_DIR%"

copy "%SCRIPT_DIR%install_power_data_kernel.bat" "%BUNDLE_DIR%\" >nul
copy "%SCRIPT_DIR%launch_jupyter_lab.bat" "%BUNDLE_DIR%\" >nul
copy "%SCRIPT_DIR%power_data_kernel_requirements.txt" "%BUNDLE_DIR%\" >nul
copy "%SCRIPT_DIR%README_RELEASE.txt" "%BUNDLE_DIR%\" >nul

if exist "%ZIP_FILE%" del "%ZIP_FILE%"

powershell -NoProfile -ExecutionPolicy Bypass -Command "Compress-Archive -Path '%BUNDLE_DIR%\*' -DestinationPath '%ZIP_FILE%'"

echo Release bundle created:
echo %ZIP_FILE%
