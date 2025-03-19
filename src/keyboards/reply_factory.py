from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class ReplyKeyboardFactory:
    @staticmethod
    def create(
        texts: list[str],
        buttons_per_row: int = 1,
        resize_keyboard: bool = True,
        one_time_keyboard: bool = False,
    ) -> ReplyKeyboardMarkup | None:
        """
        Фабрика для создания reply-клавиатур

        :param texts: Список текстов для кнопок
        :param buttons_per_row: Количество кнопок в одном ряду
        :param resize_keyboard: Автоматическое изменение размера клавиатуры
        :param one_time_keyboard: Скрывать клавиатуру после использования

        :return: ReplyKeyboardMarkup или None при ошибке
        """
        try:
            if not texts or buttons_per_row < 1:
                return None

            # Разбиваем список текстов на ряды
            rows = [
                texts[i : i + buttons_per_row]
                for i in range(0, len(texts), buttons_per_row)
            ]

            # Создаем клавиатуру
            return ReplyKeyboardMarkup(
                keyboard=[[KeyboardButton(text=text) for text in row] for row in rows],
                resize_keyboard=resize_keyboard,
                one_time_keyboard=one_time_keyboard,
            )

        except (TypeError, ValueError):
            return None
