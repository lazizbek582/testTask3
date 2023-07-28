
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "19AtK-XAQSvLOpwNhvGxqYtrKGxrZCoch4mnBFm5Aqv4"


def main():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()

        # Обрабатываем лист "Adding"
        process_sheet(sheets, "Adding", SPREADSHEET_ID)

        # Обрабатываем лист "Minus"
        process_sheet(sheets, "Minus", SPREADSHEET_ID)

    except HttpError as error:
        print(error)


def process_sheet(sheets, sheet_name, spreadsheet_id):
    try:
        range_name = f"{sheet_name}!A:C"  # Используем столбцы "A", "B" и "C" на указанном листе
        response = sheets.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        values = response.get("values", [])

        if not values:
            print(f"No data found on sheet '{sheet_name}'.")
            return

        for i, row in enumerate(values):
            if len(row) < 2:
                # Пропускаем строки с неполными данными
                continue

            try:
                num1 = int(row[0])
                num2 = int(row[1])
                

                if sheet_name == "Adding":
                    calculation_result = num1 + num2
                    print(f"Processing {num1} + {num2} in row {i+1}")
                elif sheet_name == "Minus":
                    calculation_result = num1 - num2
                    print(f"Processing {num1} - {num2} in row {i+1}")
                else:
                    print(f"Invalid operation '{sheet_name}' in row {i+1}. Skipping.")
                    continue

                # Записываем результат в столбец "C" и помечаем выполнение в столбце "D"
                sheets.values().update(
                    spreadsheetId=spreadsheet_id,
                    range=f"{sheet_name}!C{i+1}",
                    valueInputOption="USER_ENTERED",
                    body={"values": [[f"{calculation_result}"]]}
                ).execute()

                sheets.values().update(
                    spreadsheetId=spreadsheet_id,
                    range=f"{sheet_name}!D{i+1}",
                    valueInputOption="USER_ENTERED",
                    body={"values": [["Done"]]}
                ).execute()

            except ValueError:
                print(f"Invalid data in row {i+1}. Skipping.")

    except HttpError as error:
        print(error)


if __name__ == "__main__":
    main()
