import discord
import discord.ext
from discord.ext import commands

import openai

DISCORD_TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
openai.api_key = 'YOUR_OPEN_AI_API_KEY'

bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

#COMMANDS TREE
@bot.tree.command(name="generate")
async def imagine(interaction: discord.Interaction, text: str):
        await interaction.response.defer(ephemeral=False)
        url = generate_image(text)        
        await interaction.followup.send(url)
#-------------

def generate_image(text):
    response = openai.Image.create(
    prompt=text,
    n=1,
    size="1024x1024",
    )
    image_url = response['data'][0]['url']
    return image_url

bot.run(DISCORD_TOKEN)