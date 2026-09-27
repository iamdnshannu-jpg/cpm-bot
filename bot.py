import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8905610308:AAHXmjUX3pw2314w_WQ14iYtUn98CHTAOz4"

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = (
        f"<b>👤 Name:</b> {user.first_name}\n"
        f"<b>💰 Money:</b> 50,000,000\n"
        f"<b>💎 Coins:</b> 30,000\n"
        "------------------------------------\n"
        "☠️☠️☠️ <b>TRADER CPM1| DM ME FOR SUBSCRIPTION @TRADERRSS321</b> ☠️☠️☠️\n"
        "------------------------------------\n"
        "🎛️ <b>Activation Menu</b>"
    )

    keyboard = [
        [
            InlineKeyboardButton("🔵 Change Email", callback_data='sub_info'),
            InlineKeyboardButton("🟡 Change Password", callback_data='sub_info')
        ],
        [
            InlineKeyboardButton("📋 Clone Account", callback_data='sub_info'),
            InlineKeyboardButton("🚗 Unlock Cars", callback_data='sub_info')
        ],
        [
            InlineKeyboardButton("⚡ W16 Engine", callback_data='sub_info'),
            InlineKeyboardButton("📢 Horns", callback_data='sub_info')
        ],
        [
            InlineKeyboardButton("🥤 Unlimited Fuel", callback_data='sub_info'),
            InlineKeyboardButton("🛡️ Disable Damage", callback_data='sub_info')
        ],
        [
            InlineKeyboardButton("💨 Smoke", callback_data='sub_info'),
            InlineKeyboardButton("👑 King Rank", callback_data='sub_info')
        ],
        [
            InlineKeyboardButton("🔧 Fix Account", callback_data='sub_info'),
            InlineKeyboardButton("🆔 Change ID", callback_data='sub_info')
        ],
        [
            InlineKeyboardButton("💰 Add Money", callback_data='sub_info'),
            InlineKeyboardButton("💎 Add Coins", callback_data='sub_info')
        ],
        [
            InlineKeyboardButton("💀 Ultimate Unlock", callback_data='sub_info')
        ],
        [
            InlineKeyboardButton("🔄 Refresh Info", callback_data='refresh')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, reply_markup=reply_markup, parse_mode='HTML')

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'sub_info':
        await query.message.reply_text("📩 <b>DM ME FOR SUBSCRIPTION @TRADERRSS321</b>", parse_mode='HTML')
    elif query.data == 'refresh':
        await query.message.reply_text("🔄 <b>Refreshed successfully!</b>", parse_mode='HTML')

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
