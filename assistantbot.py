import discord
from discord.ext import commands
from discord import app_commands

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
    image_path = "C:/Users/migs/Desktop/ScifferBot/Assistant/gcashqr.jpg"

    try:
        # Send the image
        await interaction.response.send_message(file=discord.File(image_path))
    except Exception as e:
        await interaction.response.send_message(
            "Failed to send the GCash image. Please check the file path or URL.",
            ephemeral=True
        )
        print(f"Error: {e}")

# Run the bot
TOKEN = "MTMyNjg0OTM1MTgwODQ1NDcwOA.GK-nAB.tgcTF51FBx7uDUNBtPcg5hmKljr7m5b5FgApP0"  # Replace with your bot token
bot.run(TOKEN)



# MTMyNjg0OTM1MTgwODQ1NDcwOA.GK-nAB.tgcTF51FBx7uDUNBtPcg5hmKljr7m5b5FgApP0