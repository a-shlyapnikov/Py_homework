from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from isOdd import isOdd

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def isOdd_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    item = msg.split()
    number = int(item[1])
    if isOdd(number):
        await update.message.reply_text(f'Число {number} нечетное')
    else:
        await update.message.reply_text(f'Число {number} четное')
app = ApplicationBuilder().token("5868534886:AAGeWvqtbi6LbPtYBWnx8Ks20cOF9Qy3Z1w").build()
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("isOdd", isOdd_comand))

print('server start')
app.run_polling()