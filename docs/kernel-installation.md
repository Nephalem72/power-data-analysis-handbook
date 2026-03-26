# Установка учебного ядра

Учебные материалы следует запускать через отдельное ядро Python, чтобы состав библиотек и регистрация в Jupyter были одинаковыми для всех разделов курса.

## Рекомендуемый способ

Использовать готовый release-архив ядра.

Страница release:
[https://github.com/Nephalem72/power-data-analysis-handbook/releases](https://github.com/Nephalem72/power-data-analysis-handbook/releases)

Текущий установочный архив:
[power-data-kernel-bootstrap-v0.1.0.zip](https://github.com/Nephalem72/power-data-analysis-handbook/releases/download/v0.1.0/power-data-kernel-bootstrap-v0.1.0.zip)

## Состав установочного архива

Архив содержит:

- `install_power_data_kernel.bat` — создание виртуального окружения и регистрация kernel;
- `launch_jupyter_lab.bat` — запуск `JupyterLab` из установленного окружения;
- `power_data_kernel_requirements.txt` — список библиотек учебного ядра.

## Порядок установки

1. Скачать последний release-архив ядра.
2. Распаковать архив в удобную локальную папку.
3. Запустить `install_power_data_kernel.bat`.
4. Дождаться завершения установки.
5. Открыть `JupyterLab` через `launch_jupyter_lab.bat` или через свою установку Jupyter.
6. При открытии блокнота выбрать kernel `Power Data Analysis`.

## Что делает установщик

Установщик:

- создает виртуальное окружение в `%USERPROFILE%\power-data-analysis-kernel\.venv`;
- устанавливает требуемые библиотеки;
- регистрирует ядро в Jupyter командой `ipykernel install --user`;
- делает ядро доступным в системе под именем `power-data-analysis`.

## Требования

- Windows;
- установленный Python 3.11 или новее;
- доступ к сети для загрузки библиотек;
- права обычного пользователя достаточны.

## Проверка результата

После установки нужно убедиться, что:

- команда запуска `launch_jupyter_lab.bat` открывает JupyterLab;
- в списке kernels доступно ядро `Power Data Analysis`;
- блокнот [notebooks/01_course_setup.ipynb](https://gitverse.ru/Nephalem/power-data-analysis-handbook/blob/main/notebooks/01_course_setup.ipynb) выполняется без ошибок.
