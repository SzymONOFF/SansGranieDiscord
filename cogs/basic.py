import discord
from discord import app_commands
from discord.ext import commands

class Basic(commands.Cog):
    """Podstawowe komendy bota"""

    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="ping", description="Sprawdza, czy bot działa")
    async def ping(self, interaction: discord.Interaction):
        """Zwraca 'Pong!' w odpowiedzi na /ping"""
        await interaction.response.send_message("Pong!", ephemeral=True)  # ephemeral=True = widoczne tylko dla użytkownika

async def setup(bot):
    """Ładowanie cogu"""
    await bot.add_cog(Basic(bot))
