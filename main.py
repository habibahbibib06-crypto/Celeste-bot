import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("8878736209:AAHeuosXPllFWeVuKzwIINHiZ3SWwSrez-4")
ADMIN_ID = os.getenv("8654958132")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎬 NETFLIX 35K", callback_data="netflix")],
        [InlineKeyboardButton("🎧 SPOTIFY 25K", callback_data="spotify")],
        [InlineKeyboardButton("💬 CHAT ADMIN", url="https://t.me/celestestore")]
    ]
    text = "✨ *CELESTE STORE - AUTO ORDER 24 JAM* ✨\n\nPilih produk di bawah:"
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

async def tombol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    if q.data == "netflix":
        await q.message.reply_text("NETFLIX 35K\n\nSilahkan bayar ke DANA 0831xxxx dan kirim bukti ke @celestestore")
    elif q.data == "spotify":
        await q.message.reply_text("SPOTIFY 25K\n\nSilahkan bayar ke DANA 0831xxxx")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(tombol))
print("BOT JALAN...")
app.run_polling()
