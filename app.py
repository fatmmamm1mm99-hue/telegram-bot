"""
Telegram Bot - Text to Speech with Multiple Voices
يحول النص إلى صوت بأصوات مختلفة
"""

import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)
from dotenv import load_dotenv
import tempfile

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Get tokens from environment
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Voice categories with their voice IDs
VOICE_CATEGORIES = {
    "🇬🇧 English": [
        ("English_expressive_narrator", "Expressive Narrator"),
        ("English_radiant_girl", "Radiant Girl"),
        ("English_magnetic_voiced_man", "Magnetic-voiced Man"),
        ("English_Aussie_Bloke", "Aussie Bloke"),
        ("English_ManWithDeepVoice", "Man With Deep Voice"),
        ("English_Comedian", "Comedian"),
        ("English_WiseScholar", "Wise Scholar"),
    ],
    "🇪🇸 Spanish": [
        ("Spanish_Narrator", "Narrator"),
        ("Spanish_Comedian", "Comedian"),
        ("Spanish_BossyLeader", "Bossy Leader"),
    ],
    "🇨🇳 Chinese": [
        ("Chinese (Mandarin)_News_Anchor", "News Anchor"),
        ("Chinese (Mandarin)_Male_Announcer", "Male Announcer"),
    ],
    "🇯🇵 Japanese": [
        ("Japanese_LoyalKnight", "Loyal Knight"),
        ("Japanese_DecisivePrincess", "Decisive Princess"),
    ],
    "🇰🇷 Korean": [
        ("Korean_CalmGentleman", "Calm Gentleman"),
        ("Korean_BraveAdventurer", "Brave Adventurer"),
    ],
    "🇧🇷 Portuguese": [
        ("Portuguese_Narrator", "Narrator"),
    ],
    "🇸🇦 العربية": [
        ("Arabic_CalmWoman", "أنثى هادئة"),
        ("Arabic_FriendlyGuy", "ذكر ودود"),
    ],
}

user_voices = {}


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = """
🎙️ مرحباً! أنا بوت تحويل النص إلى صوت

اختر اللغة والصوت، ثم أرسل النص وسأحوله لك!
    """
    await_
