heroku run

import discord
import random
import io
import requests

client = discord.Client()

@client.event

async def on_ready():
    print('---------------')
    print(' Logged in as')
    print('---------------')
    print(" Join : " + client.user.name)
    print('---------------')
    print('  Created by ')
    print('   Aiden ©  ')
    print('---------------')

@client.event

async def on_message(message):
    await client.change_presence(game=discord.Game(name='xhelp'))

    prefix = 'x'

    if message.content.startswith(prefix + 'help'):
        await client.send_message(message.channel, "```css\nComandos Xmass\n```\n*xinvite* -> Link para invitarme a tu server.\n*xplatano* -> Invitación al server del plátano.\n*xplay* -> Lista de comandos chorra.")

    if message.content.startswith(prefix + 'invite'):
        await client.send_message(message.channel,"Aquí va un link para invitarme chavales: " + "https://discordapp.com/oauth2/authorize?client_id=437954268004352010&scope=bot&permissions=66186303")

    if message.content.startswith(prefix + 'platano'):
        await client.send_message(message.channel, "Una invitacion infinita para el server del platano: " + "https://discord.gg/7Z37tFu")

    if message.content.startswith('<@437954268004352010>'):
        await client.send_message(message.channel, "Mi prefijo es _***x***_")

    if message.content.startswith("salchicha rica"):
        response = requests.get("https://media.discordapp.net/attachments/435099020378243083/442380382051237888/GUMEHHH.jpg", stream=True)
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="salchicha.png", content= "Salchichita rica.")

    if message.content.lower().startswith('ola tio'):
        await client.add_reaction(message, '🇴')
        await client.add_reaction(message, '🇱')
        await client.add_reaction(message, '🇦')

    if message.content.lower().startswith(prefix + 'flip'):
        choice = random.randint(1, 2)
        if choice == 1:
            await client.add_reaction(message, '🌑')
        if choice == 2:
            await client.add_reaction(message, '🌕')

    if message.content.startswith(prefix + 'user'):
        try:
            user = message.mentions[0]
            userjoinedat = str(user.joined_at).split('.', 1)[0]
            usercreatedat = str(user.created_at).split('.', 1)[0]
            useravatar = str(user.default_avatar_url).split('.', )[0]

            userembed = discord.Embed(
                title='Nombre de usuario:',
                description=user.name,
                color=000000
            )
            userembed.set_author(
                name="Información del usuario"
            )
            userembed.add_field(
                name='Entró al server el:',
                value=userjoinedat
            )
            userembed.add_field(
                name='Usuario creado el:',
                value=usercreatedat
            )
            userembed.add_field(
                name='Discriminator:',
                value=user.discriminator
            )
            userembed.add_field(
                name='ID del usuario:',
                value=user.id
            )

            await client.send_message(message.channel, embed=userembed)
        except IndexError:
            await client.send_message(message.channel, 'Ese usuario no está en el server')
        except:
            await client.send_message(message.channel, 'Sorry Error :C')
        finally:
            pass

    if message.content.startswith(prefix + 'user'):
        try:
           
            userembed = discord.Embed(
                title='Comandos:',
                description=user.name,
                color=000000
            )
            userembed.set_author(
                name="Comandos Xmass"
            )

client.run(TOKEN)




