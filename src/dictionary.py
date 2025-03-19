from typing import TypedDict


class Greetings(TypedDict):
    start: str


class Errors(TypedDict):
    file_not_found: str
    invalid_format: str


class Instructions(TypedDict):
    send_excel: str
    waiting_for_file: str
    canceling_file_sending: str


class Keyboards(TypedDict):
    send_excel: str
    cancel: str


class Messages(TypedDict):
    greetings: Greetings
    errors: Errors
    instructions: Instructions
    keyboards: Keyboards


messages: Messages = {
    "greetings": {"start": "Привет! Отправь мне Excel-файл с данными для парсинга"},
    "errors": {
        "file_not_found": "Файл не найден. Пожалуйста, загрузите его снова.",
        "invalid_format": "Неверный формат файла. Пожалуйста, используйте Excel.",
    },
    "instructions": {
        "send_excel": "Пожалуйста, отправьте Excel-файл для обработки.",
        "waiting_for_file": "Отправьте файл или нажмите кнопку отмены",
        "canceling_file_sending": "Действие отменено",
    },
    "keyboards": {"send_excel": "Загрузить файл", "cancel": "Отменить действие"},
}
