import discord
from discord.ext import commands
from model import model 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def control(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            filename= attachment.filename
            fileurl = attachment.url
            await attachment.save (f"./{attachment.filename}")
            await ctx.send(f"Resim başarıyla kaydedildi ./{attachment.filename}")
            await ctx.send(model(model_path="./keras_model.h5",labels_path="./labels.txt",image_path="./{attachment.filename}"))
    else:
        await ctx.send(f"Resim yükle ./{attachment.filename}")

bot.run("TOKEN")