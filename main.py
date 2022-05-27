import discord
import os
import requests
import json
import random
from keep_alive import keep_alive
import time


client = discord.Client()

keyword = ["prison", "jail","prison food","prison mike"]

starter_mike = [
    "Eh, fifty-fifty, both. Look, prison stinks, is what I'm saying. It's not like you can go home, and, recharge your batteries, and come back in the morning and, be with your friends, having fun in the office .",
    "I stole. ... And I robbed. And I kidnapped... the... president's son. And held him for ransom",
    "The worst thing about prison was the... was the Dementors. They... were flying all over the place, and they were scary. And they'd come down, and they'd suck the soul out of your body, and it hurt!",
    "Gruel. Sandwiches. Gruel omelettes. Nothing but gruel. Plus, you can eat your own hair."
]


def get_quote():
    response = requests.get(
        "https://michael-scott-quotes-api.herokuapp.com/randomQuote")
    json_data = json.loads(response.text)
    quote = json_data["quote"]
    return (quote)

@client.event
async def on_ready():
    print('{0.user} Locked and loaded'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.lower().startswith('?micheal'):
        quote = get_quote()
        await message.channel.send(quote)

    elif msg.lower().startswith('?mike'):
        quote = get_quote()
        await message.channel.send(quote)

    elif any(word in msg for word in keyword):
        await message.channel.send(random.choice(starter_mike))
        await message.channel.send(random.choice(["https://tenor.com/view/michael-scott-prison-mike-kissy-prison-mike-kissy-gif-13582037","https://media.giphy.com/media/niC0LL8nmXnWp0d7Sn/giphy.gif"]))

  
    elif msg.lower().startswith('?she'):
       await message.channel.purge(limit=1)
       await message.channel.send("That's what she said ")

    elif msg.lower().startswith('?help'):
     await message.channel.send("```?micheal or ?mike -> Random quotes\n?why -> When   someone pisses you off\n?she -> For a big surprise\nGifs -> [cringe, kms, kill you, noo, vance, huh, white, broke]\n\"prison\", \"jail\",\"prison food\",\"prison mike\" -> Keywords for prison  mike quotes\n``` ```md\n#Nothing is case sensitive , keywords & Gifs dont need \"?\" ```")
    elif msg.lower().startswith('cringe'):
      await message.channel.purge(limit=1)
      await message.channel.send("https://tenor.com/view/shit-cringe-gif-9261764")
    elif msg.lower().startswith('kms'):
      await message.channel.purge(limit=1)
      await message.channel.send("https://tenor.com/view/wanna-kill-myself-the-office-michael-scott-steve-carell-frustrated-gif-13414030")
    elif msg.lower().startswith('kill you'):
      await message.channel.purge(limit=1)
      await message.channel.send("https://tenor.com/view/embarrassed-michaelscott-theoffice-gif-5120730")
    elif msg.lower().startswith('noo'):
      await message.channel.purge(limit=1)
      await message.channel.send("https://tenor.com/view/no-do-not-want-the-office-michael-scott-steve-carrell-gif-5644457")
    elif msg.lower().startswith('vance'):
      await message.channel.purge(limit=1)
      await message.channel.send("https://tenor.com/view/bob-vance-vance-refrigeration-the-office-shake-hands-introduce-gif-17948038")
    elif msg.lower().startswith('huh'):
      await message.channel.purge(limit=1)
      await message.channel.send(random.choice(["https://media.giphy.com/media/5wWf7H89PisM6An8UAU/giphy.gif","https://media.giphy.com/media/SAAMcPRfQpgyI/giphy.gif"]))
    elif msg.lower().startswith('white'):
      await message.channel.purge(limit=1)
      await message.channel.send("https://media.giphy.com/media/RLHP0SjHQQjIc/giphy.gif")
    elif msg.lower().startswith('broke'):
     await message.channel.purge(limit=1)
     await message.channel.send("https://media.giphy.com/media/NbsN8ERSfcCys/giphy.gif")

keep_alive()
client.run(os.getenv('KeY'))
