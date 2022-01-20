import json
import telegram
from urllib.request import urlopen
from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler, CallbackQueryHandler
from telegram.utils import helpers

USING_ENTITIES = "using-entities-here"

def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'Xatolik: {e}'
            print(error_message)
            raise e

    return inner


@log_errors
def do_text(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text

    reply_text = "Sizning ID = {}\n\n{}".format(chat_id, text)
    update.message.reply_text(
        text=reply_text,
    )


@log_errors
def return_company_list(update: Update, context: CallbackContext):
    if context.args:
        keyboards = []
        response = urlopen("https://ticker-2e1ica8b9.now.sh/keyword/{}".format(context.args[0]))
        data_json = json.loads(response.read())

        if data_json:
            for item in data_json:
                keyboards.append([InlineKeyboardButton(item['name'], callback_data=f"{item['name']} -- {item['symbol']}")])

            menu_choices = InlineKeyboardMarkup(keyboards)
            update.message.reply_text("Kompaniyalar ro'yxati", reply_markup=menu_choices)
        else:
            update.message.reply_text("Kompaniya topilmadi!")
    else:
        update.message.reply_text("Kamida 2 ta belgi kiriting!")

@log_errors
def return_company_selected(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    # query.answer()

    text_arr = query.data.split(' -- ')
    return_text = f"Tanlangan Kompaniya \n <b>{text_arr[0]} ({text_arr[1]})</b>"

    keyboards = []
    # keyboards.append([InlineKeyboardButton(item['name'], callback_data=f"{item['name']} -- {item['symbol']}")])

    tanlashlar = InlineKeyboardMarkup(keyboards)
    query.edit_message_text(text=return_text,
                            parse_mode=telegram.ParseMode.HTML,
                            reply_markup=tanlashlar)



@log_errors
def test2(update: Update, context: CallbackContext) -> None:
    pass


class Command(BaseCommand):
    help = "Telegram Bot"

    def handle(self, *args, **options):
        updater = Updater(settings.TOKEN)
        dispatcher = updater.dispatcher


        updater.dispatcher.add_handler(CallbackQueryHandler(return_company_selected))

        dispatcher.add_handler(CommandHandler("list", return_company_list))

        dispatcher.add_handler(MessageHandler(Filters.text, do_text))

        updater.start_polling()
        updater.idle()
