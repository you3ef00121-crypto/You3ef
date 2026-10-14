import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! 🤖\n"
        "به ربات LarCarHunterBot خوش اومدی.\n\n"
        "برای جست‌وجوی فرصت‌های خرید، یکی از گزینه‌ها رو انتخاب کن:\n"
        "/motor - موتور دست‌دوم\n"
        "/car - ماشین\n"
        "/gold - طلا\n"
        "/phone - گوشی"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
