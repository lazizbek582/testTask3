# Документация для Google Sheets API Script

[Google sheet]([URL](https://docs.google.com/spreadsheets/d/19AtK-XAQSvLOpwNhvGxqYtrKGxrZCoch4mnBFm5Aqv4/edit#gid=1477734741))

Данная документация описывает код и его использование для работы с Google Sheets API. Код представляет собой скрипт на языке Python для выполнения простой операции сложения и вычитания чисел, а также записи результатов в Google Sheets.

## Установка и настройка

1. Создайте проект в Google Cloud Console:
   - Перейдите на страницу Google Cloud Console: https://console.cloud.google.com/
   - Создайте новый проект или выберите существующий, с которым хотите работать.
   - Включите Google Sheets API для своего проекта:
     - Перейдите в раздел "API и сервисы" -> "Библиотека".
     - В поисковой строке найдите "Google Sheets API" и нажмите "Включить".
   - Создайте учетные данные OAuth 2.0:
     - Перейдите в раздел "API и сервисы" -> "Учетные данные".
     - Нажмите "Создать учетные данные" -> "Идентификатор клиента OAuth".
     - Выберите тип приложения "Десктоповое приложение".
     - Введите имя приложения и нажмите "Создать".
     - Нажмите на скачанный JSON-файл с учетными данными и переименуйте его в "credentials.json".
     - Переместите файл "credentials.json" в ту же папку, где находится скрипт.

2. Установите необходимые библиотеки:
   - Откройте командную строку (терминал) и перейдите в папку с проектом.
   - Установите библиотеки Google API с помощью команды:

     ```bash
     pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
     ```

3. Настройте Google Sheets:
   - Создайте новую Google таблицу (Google Sheets).
   - В URL-адресе таблицы найдите и скопируйте идентификатор таблицы (SPREADSHEET_ID). Идентификатор находится между "/d/" и "/edit" в URL-адресе таблицы.

## Использование

1. Запустите скрипт:
   - Откройте командную строку (терминал) и перейдите в папку с проектом.
   - Запустите скрипт с помощью команды:

     ```bash
     python main.py
     ```

   - При первом запуске скрипта он откроет окно браузера для авторизации вашего приложения. Авторизуйтесь через свой аккаунт Google и предоставьте разрешение на доступ к вашим таблицам Google Sheets.

2. Результаты выполнения:
   - Скрипт выполнит сложение чисел из столбцов "A" и "B" на листе "Adding" в таблице Google Sheets.
   - Результаты сложения будут записаны в столбец "C" на том же листе.
   - Кроме того, в столбец "D" будет записано значение "Done", чтобы отметить, что вычисления были выполнены.
   - Если в столбце "A" или "B" не будет числа, то строка будет пропущена, а скрипт продолжит проверку для следующей строки.
   - Скрипт также выполнит вычитание чисел из столбцов "A" и "B" на листе "Minus" в таблице Google Sheets.
   - Результаты вычитания будут записаны в столбец "C" на том же листе.
   - Кроме того, в столбец "D" будет записано значение "Done", чтобы отметить, что вычисления были выполнены.
   - Если в столбце "A" или "B" не будет числа, то строка будет пропущена, а скрипт продолжит проверку для следующей строки.
