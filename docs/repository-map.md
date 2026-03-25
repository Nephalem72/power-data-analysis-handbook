# Карта репозитория

Корень репозитория:
[https://github.com/Nephalem72/power-data-analysis-handbook](https://github.com/Nephalem72/power-data-analysis-handbook)

## Основные каталоги

- [README.md](https://github.com/Nephalem72/power-data-analysis-handbook/blob/main/README.md) — входная точка проекта.
- [docs/](https://github.com/Nephalem72/power-data-analysis-handbook/tree/main/docs) — методические и организационные документы.
- [notebooks/](https://github.com/Nephalem72/power-data-analysis-handbook/tree/main/notebooks) — учебные блокноты и шаблоны.
- [data/](https://github.com/Nephalem72/power-data-analysis-handbook/tree/main/data) — данные и правила их размещения.
- [src/](https://github.com/Nephalem72/power-data-analysis-handbook/tree/main/src) — вспомогательный код.
- [kernel/](https://github.com/Nephalem72/power-data-analysis-handbook/tree/main/kernel) — состав учебного ядра и bat-установщики.
- [handbook/](https://github.com/Nephalem72/power-data-analysis-handbook/tree/main/handbook) — LaTeX-макет пособия и собранный PDF.
- [release-assets/](https://github.com/Nephalem72/power-data-analysis-handbook/tree/main/release-assets) — архивы для GitHub Releases.
- [tasks/](https://github.com/Nephalem72/power-data-analysis-handbook/tree/main/tasks) — задания и упражнения.
- [figures/](https://github.com/Nephalem72/power-data-analysis-handbook/tree/main/figures) — графические материалы.

## Репозиторная логика

- `docs/` хранит организационный каркас курса и пособия.
- `notebooks/` хранит исполняемые артефакты по темам и кейсам.
- `data/sample/` хранит небольшие учебные фрагменты, пригодные для публикации.
- `data/raw/` и `data/processed/` используются для локальной работы и не должны захламлять git-историю.
- `src/` нужен для функций, которые слишком громоздки для ноутбуков.
- `kernel/` фиксирует единый состав библиотек и способ регистрации отдельного Jupyter kernel.
- `handbook/latex/` хранит исходники пособия в LaTeX, план рисунков и собранный PDF.
- `release-assets/` хранит собранные архивы, публикуемые как releases.
