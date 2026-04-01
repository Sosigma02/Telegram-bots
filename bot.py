from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os

TOKEN = os.getenv("BOT_TOKEN")

# Buttons
def get_buttons():
    keyboard = [
        [InlineKeyboardButton("Register", url="https://bydi.real-james.bond/register?ref=MJ4BRJ")],
        [InlineKeyboardButton("Channel", url="https://t.me/+MPbzn0DeBHM5ODc1")],
        [InlineKeyboardButton("Customer Service", url="https://t.me/byd_servicio1")]
    ]
    return InlineKeyboardMarkup(keyboard)

# /start command (private chat)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to BYD.\n\n"
        "Remember we have no bonuses.\n"
        "Do not do any private transaction to avoid getting scammed.\n\n"
        "Choose an option below:",
        reply_markup=get_buttons()
    )

# Auto welcome in group
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(
            f"Welcome {member.first_name}.\n\n"
            "Remember we have no bonuses.\n"
            "Do not do any private transaction to avoid getting scammed.\n\n"
            "Choose an option below:",
            reply_markup=get_buttons()
        )

# Run bot
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

print("Bot is running...")
app.run_polling()