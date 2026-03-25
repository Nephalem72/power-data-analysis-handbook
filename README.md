# Системный анализ данных для электроэнергетиков в Jupyter-блокнотах

Учебно-методический комплект предназначен для освоения прикладного анализа данных в задачах электроэнергетики.
Основными компонентами комплекта являются учебное пособие, Jupyter-блокноты по разделам, демонстрационные данные, задания и единое учебное ядро Python.

## Назначение

Материалы ориентированы на:

- студентов и магистрантов электроэнергетических направлений подготовки;
- инженеров, осваивающих методы анализа данных на табличных и временных рядах;
- преподавателей, которым необходим воспроизводимый комплект учебных материалов.

## Состав

- главы учебного пособия;
- LaTeX-макет пособия и собранный PDF;
- блокноты по темам курса;
- три сквозных кейса:
  классификация, регрессия, временные ряды;
- демонстрационные датасеты и инструкции их получения;
- задания для самостоятельной работы;
- инструкции по установке учебного ядра и запуску блокнотов.

## Структура

```text
.
├─ docs/                # пособие, outline, методические документы
├─ notebooks/           # учебные блокноты
├─ data/                # raw, sample, processed
├─ src/                 # вспомогательные функции
├─ kernel/              # учебное ядро и bat-установщики
├─ release-assets/      # артефакты для GitHub Releases
└─ tasks/               # задания и упражнения
```

Подробная карта:
[docs/repository-map.md](docs/repository-map.md)

## Установка учебного ядра

Основной способ запуска материалов — через подготовленное учебное ядро Python, зарегистрированное в Jupyter как отдельный kernel.

Инструкция:
[docs/kernel-installation.md](docs/kernel-installation.md)

Прямая ссылка на текущий установочный архив:
[power-data-kernel-bootstrap-v0.1.0.zip](https://github.com/Nephalem72/power-data-analysis-handbook/releases/download/v0.1.0/power-data-kernel-bootstrap-v0.1.0.zip)

Краткая схема:

1. Скачать последний release с установочным архивом ядра.
2. Распаковать архив.
3. Запустить `install_power_data_kernel.bat`.
4. Дождаться регистрации kernel `power-data-analysis`.
5. Открыть `JupyterLab` или `Jupyter Notebook` и выбрать установленное ядро.

## Порядок изучения

Основная последовательность разделов зафиксирована в:

- [docs/handbook-outline.md](docs/handbook-outline.md)
- [docs/case-studies.md](docs/case-studies.md)

## Основные документы

- [docs/handbook-outline.md](docs/handbook-outline.md)
- [docs/chapter-template.md](docs/chapter-template.md)
- [docs/datasets.md](docs/datasets.md)
- [docs/case-studies.md](docs/case-studies.md)
- [docs/notebook-style-guide.md](docs/notebook-style-guide.md)
- [docs/jupyter-environment.md](docs/jupyter-environment.md)
- [docs/kernel-installation.md](docs/kernel-installation.md)
- [handbook/latex/main.tex](handbook/latex/main.tex)
- [handbook/latex/main.pdf](handbook/latex/main.pdf)
- [handbook/latex/FIGURE_PLAN.md](handbook/latex/FIGURE_PLAN.md)

## Воспроизводимость

Воспроизводимость обеспечивается:

- единым составом библиотек в учебном ядре;
- разделением исходных и подготовленных данных;
- привязкой каждой главы к соответствующему блокноту;
- выделением повторно используемых функций в `src/`.
