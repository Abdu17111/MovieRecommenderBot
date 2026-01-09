import os
import telebot
from telebot import types
from dotenv import load_dotenv

from movies import get_random_movie
from ai import get_ai_recommendation

# ====== ЗАГРУЗКА ТОКЕНА ======
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError('❌ BOT_TOKEN не найден в .env')

bot = telebot.TeleBot(BOT_TOKEN)

# ====== КНОПКИ ======
RANDOM_BTN = '🎲 Случайный фильм'
AI_BTN = '🪄 Подобрать фильм по вкусу'


def main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(RANDOM_BTN),
        types.KeyboardButton(AI_BTN)
    )
    return keyboard


# ====== /start ======
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        '<b>Привет! Я помогу тебе выбрать фильм на вечер 🍿</b>\n'
        'Выбирай кнопку ниже 👇',
        parse_mode='HTML',
        reply_markup=main_keyboard()
    )


# ====== СЛУЧАЙНЫЙ ФИЛЬМ ======
@bot.message_handler(func=lambda message: message.text == RANDOM_BTN)
def random_movie(message):
    try:
        movie = get_random_movie()
        inline_keyboard = types.InlineKeyboardMarkup()
        for name, url in movie['links'].items():
            inline_keyboard.add(types.InlineKeyboardButton(text=name, url=url))
        text = f"""
<b>{movie['title']}</b>
{movie['description']}
<i>Посмотреть фильм можно тут 👇</i>
"""
        bot.send_photo(
            chat_id=message.chat.id,
            photo=movie['image'],
            caption=text,
            reply_markup=inline_keyboard,
            parse_mode='HTML',

        )

    except Exception as e:
        bot.send_message(message.chat.id, '😔 Не смог подобрать фильм.')
        print(f'Ошибка: {e}')

# ====== ПОДБОР ПО ВКУСУ ======
@bot.message_handler(func=lambda message: message.text == AI_BTN)
def ai_movie(message):
    msg = bot.send_message(
        message.chat.id,
        '🎥 Напиши, какой фильм ты хочешь:\n'
        'жанр, настроение, примеры 👇'
    )
    bot.register_next_step_handler(msg, process_ai_request)


def process_ai_request(message):
    try:
        recommendation = get_ai_recommendation(message.text)
        bot.send_message(
            message.chat.id,
            f'✨ <b>Вот что я подобрал:</b>\n\n{recommendation}',
            parse_mode='HTML',
            reply_markup=main_keyboard()
        )
    except Exception as e:
        bot.send_message(message.chat.id, '😔 Ошибка. Попробуй ещё раз.')
        print(f'Ошибка: {e}')


# ====== ЗАПУСК ======
if __name__ == '__main__':
    print('🤖 Бот запущен...')
    bot.infinity_polling(skip_pending=True)
