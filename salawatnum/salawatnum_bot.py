from telegram import *
from telegram.ext import *

# this is bot token
tokena = ""
upder = Updater(tokena, use_context=True)
desp = upder.dispatcher
salwatnum = 0


def main():
    """this is the brain of the bot"""
    desp.add_handler(CommandHandler("start", start))
    desp.add_handler(CallbackQueryHandler(button))
    upder.start_polling()
    upder.idle()


def start(update, context):
    """sends a message with two
    inline buttons for count Salawat"""
    cht_id = update.effective_message.chat_id
    if cht_id == 1643421234:
        global salwatnum
        salwatnum = 0
        # buttons
        keybutton = [
            [
                InlineKeyboardButton("+", callback_data="1"),
                InlineKeyboardButton("reset", callback_data="2"),
            ]
        ]
        reply_mar = InlineKeyboardMarkup(keybutton)

        welcome = "Welcome to Salawat number bot\n" +\
            "number of counts 0"
        update.message.reply_text(welcome, reply_markup=reply_mar)
    else:
        update.message.reply_text("you do not have the access to use this bot")


def button(update, context):
    """analysis of responses and reactions"""
    global salwatnum
    keybutton = [
        [
            InlineKeyboardButton("+", callback_data='1'),
            InlineKeyboardButton("reset", callback_data='2'),
        ]
    ]
    reply_mar = InlineKeyboardMarkup(keybutton)
    query = update.callback_query
    query.answer()
    # check call back data
    if query.data == "1":
        salwatnum += 1
        welcome = "Welcome to Salawat number bot\n" +\
            "number of counts " + str(salwatnum)
        query.edit_message_text(text=welcome, reply_markup=reply_mar)
    else:
        salwatnum = 0
        welcome = "Welcome to Salawat number bot\n" +\
            "number of counts " + str(salwatnum)
        query.edit_message_text(text=welcome, reply_markup=reply_mar)


# the server turns on
if __name__ == '__main__':
    print("Server started")
    main()
