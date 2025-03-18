from typing import TypedDict


class Greetings(TypedDict):
    start: str


class Errors(TypedDict):
    file_not_found: str
    invalid_format: str


class Instructions(TypedDict):
    send_excel: str


class Messages(TypedDict):
    greetings: Greetings
    errors: Errors
    instructions: Instructions


messages: Messages = {
    "greetings": {"start": "Привет! Отправь мне Excel-файл с данными для парсинга"},
    "errors": {
        "file_not_found": "Файл не найден. Пожалуйста, загрузите его снова.",
        "invalid_format": "Неверный формат файла. Пожалуйста, используйте Excel.",
    },
    "instructions": {"send_excel": "Пожалуйста, отправьте Excel-файл для обработки."},
}
