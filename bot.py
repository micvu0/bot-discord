import discord
from discord.ext import commands
from generator_hasel import gen_pass
from os import listdir
from random import choice

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command()
async def haslo(ctx, pass_lenght=10):
    await ctx.send(gen_pass(pass_lenght))

@bot.command()
async def mem(ctx):
    file_list = listdir("img")
    with open("img\\"+choice(file_list), 'rb') as file:
        discord_file = discord.File(file)
        await ctx.send(file=discord_file)


@bot.command()
async def smietniki(ctx):
    file_list = listdir("img")
    with open("img/" + choice(file_list), 'rb') as file:  
        discord_file = discord.File(file)
        await ctx.send(file=discord_file)
    

@bot.command()
async def kosze(ctx, count_pojemnik=0):
    await ctx.send("pojemnik" * count_pojemnik)

# Zmienna mapująca przedmioty do pojemników
pojemniki = {
    "papier": {"obrazek": "link_do_obrazka_pojemnika_papierowego.png", "opis": ["gazety", "zeszyty", "tektura", "kartony", "ulotek"]},
    "plastik": {"obrazek": "link_do_obrazka_pojemnika_plastikowego.png", "opis": ["butelki plastikowe", "opakowania po jogurtach", "worki", "puszki"]},
    "szkło": {"obrazek": "link_do_obrazka_pojemnika_szklany.png", "opis": ["butelki szklane", "słoiki bez pokrywek", "szkło opakowaniowe"]},
    "zmieszane": {"obrazek": "link_do_obrazka_pojemnika_zmieszane.png", "opis": ["ubrania", "ceramika", "popiół", "kości"]},
}

@bot.command(name="recycling")
async def recycling(ctx, *, przedmiot: str):
    # Znajdź odpowiedni pojemnik za pomocą list comprehension
    pojemnik = next((k for k, v in pojemniki.items() if przedmiot.lower() in v["opis"]), None)

    if pojemnik:
        info = pojemniki[pojemnik]
        embed = discord.Embed(
            title=f"Pojemnik na {pojemnik}",
            description=f"Do tego pojemnika wrzucamy: {', '.join(info['opis'])}",
            color=0x00ff00
        )
        embed.set_image(url=info["obrazek"])
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"Niestety, nie wiem, gdzie wyrzucić '{przedmiot}'.")


bot.run("")  
