# GigaChat_Professions_Analyzer

Проект предназначен для анализа профессий на предприятии с использованием модели GigaChat. Данные о профессиях берутся 
из Excel-файла, отправляются в GigaChat для получения описания, а результат сохраняется в Markdown-файлы.

## 📁 Структура проекта

```makefile
    project/ 
    ├── main.py            # Основной модуль для запуска проекта 
    ├── settings/ 
    │ └── config.env       # Файл конфигурации с токенами и настройками 
    ├── utils/ │ 
    ├── file_operations.py # Работа с файлами (создание папок, запись данных) 
    │ ├── data_reader.py   # Работа с чтением данных из Excel 
    │ └── chat_gigachat.py # Работа с API GigaChat 
    ├── file.xlsx          # Excel-файл с данными 
    └── logs/              # Лог-файлы (создается автоматически)
```

---

## 🚀 Функционал

1. Чтение данных из Excel-файла (участок и профессия).
2. Формирование запроса к GigaChat для получения описания профессии.
3. Создание папок для каждого участка.
4. Сохранение результата в файлы `.md` в соответствующих папках.
5. Логирование работы приложения.

---

## 🛠 Установка и настройка

### Шаг 1: Клонирование репозитория

```bash
git clone https://github.com/your-repo/gigachat-professions-analyzer.git
cd gigachat-professions-analyzer
```

### Шаг 2: Установка зависимостей
Создайте виртуальное окружение и установите зависимости:

```bash
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Шаг 3: Настройка окружения
Создайте файл settings/config.env и добавьте токен GigaChat:

```makefile
GIGA_CHAT=your_gigachat_token
```

## 📊 Формат данных
**Excel-файл** (`file.xlsx`) должен содержать две колонки:

* **Колонка A**: Участок (например, "Отдел производства").
* **Колонка B**: Профессия (например, "Начальник участка").

Пример таблицы:

| Участок            | Профессия         |
|--------------------|-------------------|
| Руководство        | Директор          |
| Отдел производства | Начальник участка |
| Бухгалтерия        | Бухгалтер         |

## ⚙️ Использование
Запустите скрипт:

```bash
python main.py
```

Программа:

Прочитает данные из `file.xlsx`.
Отправит запросы в GigaChat для получения описаний профессий.
Сохранит результаты в файлы `.md` в папке `test/`.
📁 Пример результата
После выполнения скрипта структура папок будет выглядеть так:

```makefile
test/
├── Руководство/
│   └── Директор.md
├── Отдел производства/
│   └── Начальник участка.md
└── Бухгалтерия/
    └── Бухгалтер.md
```

Файл `Директор.md` может содержать, например:

```makefile
Участок: Руководство
Профессия: Директор
Описание: Директор отвечает за общее управление предприятием, планирование стратегии развития и контроль исполнения задач.
```

## 📝 Логирование
Логи работы приложения сохраняются в папке `logs/` с ротацией (максимальный размер файла — 1 MB). Например:

```bash
logs/app.log
```

## 🛡️ Обработка ошибок
Если возникнут ошибки:

Проверьте формат Excel-файла.
Убедитесь, что токен GigaChat указан верно в `settings/config.env`.
Посмотрите лог-файлы в папке `logs/` для диагностики.

## 📄 Лицензия
Проект распространяется под лицензией GNU GENERAL PUBLIC LICENSE. Подробнее в LICENSE.

## 📬 Обратная связь
Если у вас есть вопросы или предложения, создайте Issue или свяжитесь со мной напрямую.

