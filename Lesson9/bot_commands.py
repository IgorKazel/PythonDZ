from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import calc

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hello\n/help\n/time\n/sum\n/calc\n/new_year')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{datetime.datetime.now().strftime("%H:%M:%S")}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    numbers = msg.split()
    a = int(numbers[1])
    b = int(numbers[2])
    await update.message.reply_text(a+b)

async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    example = msg.split()
    example.pop(0)
    await update.message.reply_text(calc.calc(example))

async def new_year_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    now = datetime.date.today()
    new_year = datetime.date(2024, 1, 1)
    days_before_new_year = (new_year - now).days
    await update.message.reply_text(f'До нового года осталось {days_before_new_year} дней')