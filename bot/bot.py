import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} está online!')

    # Comando simples de exemplo
    @bot.command()
    async def ping(ctx):
        await ctx.send('Pong!')

        bot.run('MTMxMDIyMTYyMDczMTcxMTU1OA.GgIYV7.3VamA4o7D7NvW5Iyzi14hQCS5f3K5YopZ1RnGo')
