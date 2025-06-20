import discord
from discord.ext import commands
import requests
import pyttsx3
import random

Engine = pyttsx3.init()
Engine.setProperty('rate', 150)  # Velocidad de habla
voices = Engine.getProperty('voices')
Engine.setProperty('volume', 1)  # Volumen (0.0 a 1.0)
Engine.setProperty('voice', voices[0].id)  # Cambia a la voz en español


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')


def Hablar(text: str):
    Engine.say(text)
    Engine.runAndWait()


@bot.command()
async def SobreMi(ctx):
    await ctx.send("Hola, soy un bot relacionado con el cambio climático.")
    Hablar(f'Hola, soy un bot relacionado con el cambio climático.')
    await ctx.send("Yo busco traer las últimas estadísticas sobre el tema.")
    Hablar(f'Yo busco traer las últimas estadísticas sobre el tema.')
    await ctx.send("Traigo actualizaciones sobre los GEI, calentamiento global, etcétera.")
    Hablar(f'Traigo actualizaciones sobre los GEI, calentamiento global, etcétera.')
    await ctx.send("Si deseas saber los comandos, utiliza .Comandos.")
    Hablar(f'Si deseas saber los comandos, utiliza el comando .Comandos.')


@bot.command()
async def Comandos(ctx):
    comandos = (
        "SobreMi: Información sobre el bot.\n"
        "Comandos: Lista de comandos disponibles.\n"
        "Temperatura_Anom: Muestra una anomalía de temperatura aleatoria.\n"
        "CO2: Muestra un registro aleatorio de CO2.\n"
        "Metano: Muestra un registro aleatorio de metano.\n"
        "Oxido_Nitroso: Muestra un registro aleatorio de óxido nitroso.\n"
    )
    await ctx.send(comandos)
    Hablar("Estos son los comandos disponibles.")
    Hablar("Todos utilizan el mismo prefijo, punto.")


@bot.command()
async def Temperatura_Anom(ctx):
    url = "https://global-warming.org/api/temperature-api"
    try:
        r = requests.get(url)
        r.raise_for_status()                       # lanza excepción.
        datos = r.json()["result"]                # lista de dicts
        registro = random.choice(datos)           # escoger año aleatorio
        año = registro["time"]
        oceano = registro["station"]
        tierra = registro["land"]
        mensaje = (
            f"Año:{año}. \n"
            f"Anomalía océano = {oceano} °C. \n"
            f"Anomalí tierra = {tierra} °C. \n"
        )
        await ctx.send(mensaje)
        Hablar(mensaje)
    except (requests.RequestException, KeyError, ValueError) as e:
        await ctx.send("Lo siento, no pude obtener la estadística.")
        Hablar("Lo siento, no pude obtener la estadística.")
        print("Error al consumir la API:", e)


@bot.command()
async def CO2(ctx):
    url = "https://global-warming.org/api/co2-api"
    try:
        r = requests.get(url)
        r.raise_for_status()                      # lanza excepción.
        datos = r.json()["co2"]                   # lista de dicts
        registro = random.choice(datos)           # escoger año aleatorio
        año = registro["year"]
        mes = registro["month"]
        día = registro["day"]
        ciclo = registro["cycle"]
        tendencia = registro["trend"]
        mensaje = (
            f"Año: {año}. \n"
            f"Mes: {mes}. \n"
            f"Día: {día}. \n"
            f"Ciclo: {ciclo} ppm. \n"
            f"Tendencia: {tendencia} ppm. \n"
            "ppm =  Partes por millón, la unidad utilizada."
        )
        await ctx.send(mensaje)
        Hablar(mensaje)
    except (requests.RequestException, KeyError, ValueError) as e:
        await ctx.send("Lo siento, no pude obtener la estadística.")
        Hablar("Lo siento, no pude obtener la estadística.")
        print("Error al consumir la API:", e)


@bot.command()
async def Metano(ctx):
    url = "https://global-warming.org/api/methane-api"
    try:
        r = requests.get(url)
        r.raise_for_status()                       # lanza excepción.
        datos = r.json()["methane"]                # lista de dicts
        registro = random.choice(datos)           # escoger año aleatorio
        Año = registro["date"]
        Promedio = registro["average"]
        Tendencia = registro["trend"]
        mensaje = (
            f"Año: {Año}. \n"
            f"Promedio: {Promedio} ppb. \n"
            f"Tendencia: {Tendencia} ppb. \n"
            "ppb = Partes por billón, la unidad utilizada. \n"
        )
        await ctx.send(mensaje)
        Hablar(mensaje)
    except (requests.RequestException, KeyError, ValueError) as e:
        await ctx.send("Lo siento, no pude obtener la estadística.")
        Hablar("Lo siento, no pude obtener la estadística.")
        print("Error al consumir la API:", e)


@bot.command()
async def Oxido_Nitroso(ctx):
    url = "https://global-warming.org/api/nitrous-oxide-api"
    try:
        r = requests.get(url)
        r.raise_for_status()                       # lanza excepción.
        datos = r.json()["nitrous"]                # lista de dicts
        registro = random.choice(datos)           # escoger año aleatorio
        Año = registro["date"]
        Promedio = registro["average"]
        Tendencia = registro["trend"]
        mensaje = (
            f"Año: {Año}. \n"
            f"Promedio: {Promedio} ppb. \n"
            f"Tendencia: {Tendencia} ppb. \n"
            "ppb = Partes por billón, la unidad utilizada. "
        )
        await ctx.send(mensaje)
        Hablar(mensaje)
    except (requests.RequestException, KeyError, ValueError) as e:
        await ctx.send("Lo siento, no pude obtener la estadística.")
        Hablar("Lo siento, no pude obtener la estadística.")
        print("Error al consumir la API:", e)

bot.run("Tu token.")
