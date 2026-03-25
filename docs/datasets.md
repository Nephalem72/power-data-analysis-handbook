# Подбор и паспорт датасетов

Для учебных кейсов выбраны открытые наборы данных, пригодные для воспроизводимого использования в учебной среде.
При отборе учитывались доступность, устойчивость источника, понятность признаков и пригодность для демонстрации типовых этапов анализа.

| Тип задачи | Набор данных | Источник | Формат | Масштаб | Целевая переменная | Ключевые признаки | Основные проблемы предобработки | Связанный блокнот | Способ получения |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Классификация | Electrical Grid Stability Simulated Data | https://archive.ics.uci.edu/dataset/471/electrical+grid+stability+simulated+data | CSV | 10 000 строк, 12 столбцов | `stabf` | `tau1`-`tau4`, `p2`-`p4`, `g1`-`g4` | контроль баланса классов, масштабирование признаков, явное указание на моделируемый характер данных | `notebooks/05_case_study_classification.ipynb` | загрузка с UCI или через `ucimlrepo`, `id=471` |
| Регрессия | Combined Cycle Power Plant | https://archive.ics.uci.edu/dataset/294/combined+cycle+power+plant | XLSX, ODS | 9 568 строк, 5 столбцов | `PE` | `AT`, `V`, `AP`, `RH` | приведение шкал признаков, корректное разбиение без искусственной временной интерпретации | `notebooks/06_case_study_regression.ipynb` | загрузка с UCI или через `ucimlrepo`, `id=294` |
| Временные ряды | Individual Household Electric Power Consumption | https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption | TXT с разделителем `;` | 2 075 259 строк, 9 столбцов | `Global_active_power` или агрегированная нагрузка | `Date`, `Time`, `Voltage`, `Global_reactive_power`, `Global_intensity`, `Sub_metering_1`-`3` | объединение даты и времени, обработка пропусков, ресемплинг, ограничение окна наблюдений для учебных расчетов | `notebooks/07_case_study_time_series.ipynb` | загрузка с UCI или через `ucimlrepo`, `id=235` |

## Методические замечания

- датасеты по классификации и регрессии подходят для первого цикла обучения работе с табличными данными;
- датасет по временным рядам намеренно более объемный, поскольку на нем удобно показывать агрегацию, лаги и временное разбиение;
- при изложении необходимо отдельно указывать, какие данные являются реальными наблюдениями, а какие — результатом моделирования;
- все выбранные источники пригодны для цитирования и повторного использования в учебных целях.

## Локальные учебные файлы

Для бесшовного локального запуска в репозиторий включены следующие файлы:

- `data/sample/classification/electrical_grid_stability.csv`
- `data/sample/regression/combined_cycle_power_plant.csv`
- `data/sample/time_series/household_power_hourly_january_2007.csv`
- `data/sample/formats/grid_stability_fragment.csv`
- `data/sample/formats/combined_cycle_power_plant_fragment.xlsx`
- `data/sample/formats/household_power_fragment.txt`
- `data/sample/formats/dataset_catalog.json`

Эти файлы должны использоваться в блокнотах через относительные пути.

Каталог `data/sample/formats/` предназначен для главы о форматах и источниках данных. Он позволяет на реальных тематических примерах показать чтение `CSV`, `XLSX`, `TXT` и `JSON` без внешней подгрузки файлов.

## Восстановление полных исходных данных

Полные версии открытых наборов данных можно повторно получить командой:

```bash
python scripts/fetch_open_datasets.py
```

После выполнения скрипта:

- полные версии сохраняются в `data/raw/external/`;
- локальные учебные выборки обновляются в `data/sample/`.
