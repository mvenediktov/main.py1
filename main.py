import discord
from discord.ext import commands 
from model import get_class
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents = discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as{bot.user}')


@bot.event
async def check1(ctx):
    if ctx.massage.attachments:
        for attachments in ctx.massage.attachments:
            file_name = attachments.filenamepip
            fille_url = attachments.fille_url
            await attachments.save(f"/{attachments.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachments.filename}"))
    else:
        await ctx.send('Вы забыли загрузить картинку')

        
bot.run('MTEyNzUzNzEyNDgwODMzOTQ3OQ.GkNgxP.rIlSK6qJ4Yspx9NaxGsC3hSlip5G-EYgcR1Yt0')