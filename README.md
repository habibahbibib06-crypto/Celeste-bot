import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("8878736209:AAHeuosXPllFWeVuKzwIINHiZ3SWwSrez-4")
ADMIN_ID = int(os.getenv("ADMIN_ID", "8654958132"))

PRODUK = {
    "netflix": {"nama": "Netflix Premium", "harga": 35000},
    "canva": {"nama": "Canva Pro", "harga": 15000},
    "capcut": {"nama": "CapCut Pro", "harga": 20000},
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(f"{v['nama']} - Rp{v['harga']}", callback_data=k)] for k,v in PRODUK.items()
    ]
    await update.message.reply_text("🌟 Selamat datang di CELESTE STORE 🌟\nPilih produk:", reply_markup=InlineKeyboardMarkup(keyboard))

async def tombol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    produk = PRODUK.get(query.data)
    if produk:
        text = f"Kamu pilih {produk['nama']}\nHarga: Rp{produk['harga']}\n\nSilahkan bayar via DANA:\n`0831-xxxx-xxxx`\n\nSetelah bayar, kirim bukti ke admin @username_kamu"
        await query.message.reply_text(text, parse_mode='Markdown')
        if ADMIN_ID != 0:
            await context.bot.send_message(chat_id=ADMIN_ID, text=f"ORDER BARU!\nUser: @{query.from_user.username}\nProduk: {produk['nama']}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(tombol))
print("Bot Celeste jalan 24 jam...")
app.run_polling()# Celeste-bot
