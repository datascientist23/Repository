# Импортируем библиотеки
import os
import logging
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import UNSET_PARSE_MODE
from transliterate import translit 


# Устанавливаем уровень логгирования
logging.basicConfig(level=logging.INFO)

# Указываем параметры бота
#from config import TOKEN
#API_TOKEN = 'TOKEN'
API_TOKEN = os.getenv('TOKEN')
LOG_FILE = 'bot.log'


# Создаем объект бота
bot = Bot(token=API_TOKEN)

# Создаем объект диспетчера
# Все хэндлеры(обработчики) должны быть подключены к диспетчеру
dp = Dispatcher()

# Задание
# - Включить запись log в файл
# - Бот принимает кириллицу отдаёт латиницу в соответствии с Приказом МИД по транслитерации
# - Бот работает из-под docker контейнера


#Включаем запись логов в файл
logging.basicConfig(filename=LOG_FILE, level=logging.INFO)


# Словарь для транслитерации в соответствии с Приказом МИД по транслитерации
dict = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
    'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
    'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '',
    'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
 
# Хэндлер на команду /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f"Hello, {user_name}! Я бот транслитерации. Отправьте мне текст на кириллице, а я верну его в латинской транслитерации."
    logging.info(f"{user_name=} {user_id=} sent message: {message.text}")
    await message.reply(text)


# Хэндлер на текстовые сообщения
@dp.message (lambda message: message.text and not message.text.startswith('/'))
async def transliterate(message: types.Message):
    user_text = message.text
    transliterated_text = ''.join(dict.get(char, char) for char in user_text)
    await message.reply(f"Транслитерированный текст: {transliterated_text}")

#def transliterated_text(text):
    #result = ''
    #for char in text:
        #if char.lower() in dict:
            #if char.isupper():
                #result += dict[char.lower()].capitalize()
            #else:
                #result += dict[char]
        #else:
            #result += char
    #return result

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())




