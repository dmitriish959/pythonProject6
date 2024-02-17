import logging

#from telegram import Update, ForceReply
#Старая версия
#from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

# ForceReply ?


#вкл логирование

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(engine: Update, context: CallbackContext) -> None:
    # Получаю имя пользователя указанное при регистрации
    user = engine.effective_user
    # Приветствие
    engine.message.reply_markdown_v2(
        fr'Привет,{user.mention_markdown_v2()}!\',reply_markup=ForceReply(selective=True),')

def help_command(engine: Update, context: CallbackContext) -> None:
    engine.message.reply_text('Я сам себе помочь не могу, а ты еще тут клацаешь!')

def echo(engine: Update, context: CallbackContext) -> None:
    # Зеркалим запрос
    engine.message.reply_text(engine.message.text)

def main() -> None:
    from dotenv import load_dotenv
    import os
    load_dotenv()
    token = os.getenv('TOKEN')
    print(TOKEN)
# тут нужна команда для вставки токена из setting.py




    car = updater(token)
    dispatcher = car.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo ))
    updater.start_polling()
    updater.idle()

if __name__ == '__name__':
    main()