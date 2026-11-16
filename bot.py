
import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

TOKEN = os.getenv("BOT_TOKEN")

BOOKING_URL = "https://www.goethe.de/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "مرحبا بك في Goethe B2 Monitor 🇩🇪\n\n"
        "البوت يساعدك في متابعة حجز امتحان Goethe.\n\n"
        "الأقسام التي تريد متابعتها:\n"
        "✍️ Schreiben\n"
        "🗣 Sprechen\n\n"
        "الأوامر:\n"
        "/booking - رابط الحجز\n"
        "/help - المساعدة"
    )
    await update.message.reply_text(message)

async def booking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"رابط Goethe الرسمي للحجز:\n{BOOKING_URL}"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Goethe B2 Monitor\n"
        "هذا إصدار تجريبي.\n"
        "سيتم إضافة تنبيهات المواعيد بعد ربط مصدر رسمي للتوفر."
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("booking", booking))
    app.add_handler(CommandHandler("help", help_command))

    print("Goethe Bot is running!")
    app.run_polling()

if __name__ == "__main__":
    main()
