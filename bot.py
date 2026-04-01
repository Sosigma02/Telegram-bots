import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Get token from environment (Render)
TOKEN = os.getenv("BOT_TOKEN")

# Stop if token missing (prevents crash confusion)
if not TOKEN:
    print("ERROR: BOT_TOKEN is missing")
    exit()

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
    if update.message:
        await update.message.reply_text(
            "Welcome to BYD.\n\n"
            "Remember we have no bonuses.\n"
            "Do not do any private transaction to avoid getting scammed.\n\n"
            "Choose an option below:",
            reply_markup=get_buttons()
        )

# Welcome new members in group
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.new_chat_members:
        for user in update.message.new_chat_members:
            await update.message.reply_text(
                f"Welcome {user.first_name}.\n\n"
                "Remember we have no bonuses.\n"
                "Do not do any private transaction to avoid getting scammed.\n\n"
                "Choose an option below:",
                reply_markup=get_buttons()
            )

# Build app
app = ApplicationBuilder().token(TOKEN).build()

# Handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

print("Bot started successfully")

# Run bot
app.run_polling()
