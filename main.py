from bot import Bot
import pyrogram.utils

# Set minimum valid channel ID (if needed for forward checks etc.)
pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

if __name__ == "__main__":
    Bot().run()
