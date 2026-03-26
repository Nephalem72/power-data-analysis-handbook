# Карта репозитория

Корень репозитория:
[GitVerse](https://gitverse.ru/Nephalem/power-data-analysis-handbook) или [GitHub](https://github.com/Nephalem72/power-data-analysis-handbook)

## Основные каталоги

- [README.md](https://gitverse.ru/Nephalem/power-data-analysis-handbook/blob/main/README.md) или [GitHub](https://github.com/Nephalem72/power-data-analysis-handbook/blob/main/README.md) — входная точка проекта.
- [docs/](https://gitverse.ru/Nephalem/power-data-analysis-handbook/tree/main/docs) или [GitHub](https://github.com/Nephalem72/power-data-analysis-handbook/tree/main/docs) — методические и организационные документы.
- [notebooks/](https://gitverse.ru/Nephalem/power-data-analysis-handbook/tree/main/notebooks) или [GitHub](https://github.com/Nephalem72/power-data-analysis-handbook/tree/main/notebooks) — учебные блокноты и шаблоны.
- [data/](https://gitverse.ru/Nephalem/power-data-analysis-handbook/tree/main/data) или [GitHub](https://github.com/Nephalem72/power-data-analysis-handbook/tree/main/data) — данные и правила их размещения.
- [scripts/](https://gitverse.ru/Nephalem/power-data-analysis-handbook/tree/main/scripts) или [GitHub](https://github.com/Nephalem72/power-data-analysis-handbook/tree/main/scripts) — сценарии загрузки и подготовки открытых наборов данных.
- [src/](https://gitverse.ru/Nephalem/power-data-analysis-handbook/tree/main/src) или [GitHub](https://github.com/Nephalem72/power-data-analysis-handbook/tree/main/src) — вспомогательный код.
- [kernel/](https://gitverse.ru/Nephalem/power-data-analysis-handbook/tree/main/kernel) или [GitHub](https://github.com/Nephalem72/power-data-analysis-handbook/tree/main/kernel) — состав учебного ядра и bat-установщики.
- [handbook/](https://gitverse.ru/Nephalem/power-data-analysis-handbook/tree/main/handbook) или [GitHub](https://github.com/Nephalem72/power-data-analysis-handbook/tree/main/handbook) — LaTeX-макет пособия и собранный PDF.
- [release-assets/](https://gitverse.ru/Nephalem/power-data-analysis-handbook/tree/main/release-assets) или [GitHub](https://github.com/Nephalem72/power-data-analysis-handbook/tree/main/release-assets) — архивы для GitHub Releases.
- [tasks/](https://gitverse.ru/Nephalem/power-data-analysis-handbook/tree/main/tasks) или [GitHub](https://github.com/Nephalem72/power-data-analysis-handbook/tree/main/tasks) — задания и упражнения.
- [figures/](https://gitverse.ru/Nephalem/power-data-analysis-handbook/tree/main/figures) или [GitHub](https://github.com/Nephalem72/power-data-analysis-handbook/tree/main/figures) — графические материалы.

## Репозиторная логика

- `docs/` хранит организационный каркас курса и пособия.
- `notebooks/` хранит исполняемые артефакты по темам и кейсам.
- `data/sample/` хранит небольшие учебные фрагменты, пригодные для публикации.
- `data/sample/formats/` хранит демонстрационные тематические файлы в форматах `CSV`, `XLSX`, `TXT` и `JSON`.
- `data/raw/` и `data/processed/` используются для локальной работы и не должны захламлять git-историю.
- `scripts/` содержит сценарии восстановления открытых датасетов и подготовки учебных подвыборок.
- `src/` нужен для функций, которые слишком громоздки для ноутбуков.
- `kernel/` фиксирует единый состав библиотек и способ регистрации отдельного Jupyter kernel.
- `handbook/latex/` хранит исходники пособия в LaTeX, план рисунков и собранный PDF.
- `release-assets/` хранит собранные архивы, публикуемые как releases.

Зеркало GitHub для тех же путей:
[https://github.com/Nephalem72/power-data-analysis-handbook](https://github.com/Nephalem72/power-data-analysis-handbook)
