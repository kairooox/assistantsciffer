import discord
from discord.ext import commands
from discord import app_commands
import os
from flask import Flask
from threading import Thread
from dotenv import load_dotenv

# Bot setup
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    try:
        # Set the bot's status to "Playing .gg/sciffershop"
        game = discord.Game(".gg/sciffershop")
        await bot.change_presence(activity=game)

        # Sync application commands (slash commands)
        await bot.tree.sync()
        print(f"Synced {len(bot.tree.get_commands())} command(s).")
        print(f"Logged in as {bot.user}")
    except Exception as e:
        print(f"Error syncing commands: {e}")

# Slash command: /gcash
@bot.tree.command(name="gcash", description="Send the GCash QR code or image")
async def gcash(interaction: discord.Interaction):
    # Path to the GCash image
    image_path = "gcashqr.jpg"

    try:
        # Send the image
        await interaction.response.send_message(file=discord.File(image_path))
    except Exception as e:
        await interaction.response.send_message(
            "Failed to send the GCash image. Please check the file path or URL.",
            ephemeral=True
        )
        print(f"Error: {e}")

def run_flask():
    # Run the Flask app in a separate thread to avoid blocking the bot
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

if __name__ == "__main__":
    # Run Flask in a separate thread so it doesn't block the bot
    t = Thread(target=run_flask)
    t.start()

    # Fetch the bot token from environment variables
    bot_token = os.getenv("DISCORD_BOT_TOKEN")  # Make sure your .env file has the DISCORD_BOT_TOKEN key

    if not bot_token:
        raise ValueError("DISCORD_BOT_TOKEN environment variable is not set.")
    
    bot.run(bot_token)
# MTMyNjg0OTM1MTgwODQ1NDcwOA.GK-nAB.tgcTF51FBx7uDUNBtPcg5hmKljr7m5b5FgApP0
