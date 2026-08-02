import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

# prerequisites
load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Logged in as {bot.user}")
        print(f"Synced {len(synced)} slash commands.")
    except Exception as e:
        print(e)
      
# /announce command
@bot.tree.command(name="announce", description="Create an announcement")
@app_commands.describe(
    channel="Channel to send the announcement",
    title="Announcement title",
    message="Announcement body",
    logo="Thumbnail image URL (optional)",
    image="Large image URL (optional)"
)

async def announce(
    interaction: discord.Interaction,
    channel: discord.TextChannel,
    title: str,
    message: str,
    logo: str = "",
    image: str = ""
):
    allowed_role = "ROLE HERE"

    if not any(role.name == allowed_role for role in interaction.user.roles):
        await interaction.response.send_message(
            "❌ You do not have permission to use this command.",
            ephemeral=True
        )
        return
    
    message = message.replace("\\n", "\n")
    embed = discord.Embed(
        title=title,
        description=message,
        color=discord.Color.green()
    )
    if logo:
        embed.set_thumbnail(url=logo)
    if image:
        embed.set_image(url=image)

    await channel.send(embed=embed)
    await interaction.response.send_message(
        "✅ Announcement posted.",
        ephemeral=True
    )

bot.run(TOKEN)
