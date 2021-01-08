from telegram import *
from telegram.ext import *


bot = Bot("1531640639:AAFiO04LlneQmePP51TXeEYz75izug_WTJI")
print(bot.get_me())
updater=Updater("1531640639:AAFiO04LlneQmePP51TXeEYz75izug_WTJI",use_context=True)

dispatcher=updater.dispatcher
def test_function(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="tutorial link : https://www.youtube.com/watch?v=XSCg6qdi18M",
    )

start_value=CommandHandler('motion_detection',test_function)

dispatcher.add_handler(start_value)

updater.start_polling()

