from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = 'f9LHodD0cOLLYcDM1MFUkXj63iuccZc-pcCslxJZup3CwOOKDHNW6aBb0haNpMicnAGp-QZK5LT89sqYVtz0'

# Главная страница
MAIN_MENU_KEYBOARD = [
    [KeyboardButton('Выбрать бассейн')],
    [KeyboardButton('Стоимость занятий')],
    [KeyboardButton('Тренерский состав')],
    [KeyboardButton('Администратор')],
    [KeyboardButton('Личный кабинет')]
]

def start(update: Update, context: CallbackContext) -> None:
    """Приветственное сообщение"""
    update.message.reply_text(
        "Вас приветствует бот школы плавания Proswimming.ru.\n\n"
        "Я помогу вам ознакомиться с основной информацией, записаться на бесплатное занятие.",
        reply_markup=ReplyKeyboardMarkup(MAIN_MENU_KEYBOARD, resize_keyboard=True)
    )

def handle_menu_choice(update: Update, context: CallbackContext) -> None:
    """Обработка выбора пункта меню"""
    choice = update.message.text
    
    if choice == 'Выбрать бассейн':
        update.message.reply_text("Здесь будет информация о выборе бассейна.")
        
    elif choice == 'Стоимость занятий':
        update.message.reply_text("Здесь будет информация о стоимости занятий.")
        
    elif choice == 'Тренерский состав':
        update.message.reply_text("Здесь будет информация о тренерском составе.")
        
    elif choice == 'Администратор':
        update.message.reply_text("Связаться с администратором можно по телефону +7 (XXX) XXX-XX-XX")
        
    elif choice == 'Личный кабинет':
        update.message.reply_text("Авторизация в личном кабинете доступна по ссылке: http://proswimming.ru/login")

def main() -> None:
    updater = Updater(TOKEN)
    
    dispatcher = updater.dispatcher
    
    # Обработчик команды /start
    dispatcher.add_handler(CommandHandler("start", start))
    
    # Обработчик сообщений с выбором пунктов меню
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_menu_choice))
    
    # Запуск бота
    updater.start_polling()
    print("Bot started...")
    updater.idle()

if __name__ == '__main__':
    main()
