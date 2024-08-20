import os
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user} y fui creado para dar consejos de la contaminacion!')

@bot.command()
async def heh(ctx, count_heh = 10):
    await ctx.send("he" * count_heh)\

@bot.command()
async def test(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def mem(ctx):
    lista_de_imagenes = os.listdir('images')
    image_aleatoria = random.choice(lista_de_imagenes)
    with open(f'images/{image_aleatoria}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mempet(ctx):
    lista_de_imagenes = os.listdir('imagenespt')
    image_aleatoria = random.choice(lista_de_imagenes)
    with open(f'imagenespt/{image_aleatoria}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def consejodeldia(ctx):
    consejos = [
        'Usa bolsas reutilizables para tus compras',
        'Evita los productos de un solo uso como sorbetes y cubiertos de plastico',
        'Separa correctamente tus residuos: los envases de plástico, vidrio, papel y cartón deben ir a los contenedores de reciclaje correspondientes. Esto ayuda a reducir la contaminación y permite que los materiales sean reutilizados eficientemente.'
    ]

    consejo = random.choice(consejos)
    await ctx.send(consejo)

@bot.command()
async def manualidades(ctx):
    manualidad = [
        'Maceta con latas',
        'Estuche con botellas de plástico',
        'Portavasos con corchos'
    ]

    consejo = random.choice(manualidad)
    await ctx.send(consejo)



@bot.command()
async def contaminacion(ctx):
    lista_de_imagenes = os.listdir('contaminacion')
    image_aleatoria = random.choice(lista_de_imagenes)
    with open(f'contaminacion/{image_aleatoria}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run("token")
