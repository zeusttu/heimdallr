import os
from discord.ext import commands
prefix = '!'
bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
    print("I'm in your area")


@bot.listen()
async def on_member_join(member):
    channel = member.guild.system_channel
    msg = (
        ":postal_horn: "
        f"Greetings, {member.mention}. I am Heimdallr, he who stands "
        "guard over this Server. State your level of Danish so that I may "
        "grant you your right tag. Fear not if you have questions, our "
        "moderators and mentors shall answer them."
    )
    msg_dk = (
        ":postal_horn: "
        f"Vær hilset, {member.mention}. Jeg er Heimdallr, han som vogter "
        "over denne Server. Fortæl mig dit niveau af dansk så jeg kan give "
        "dig din rette tag. Frygt ej hvis du har spørgsmål, for vore "
        "moderatorer og mentorer skal nok svare på dem."
    )
    await channel.send(f"{msg}\n\n{msg_dk}")


@bot.listen()
async def on_member_remove(member):
    channel = member.guild.system_channel
    msg = (
        ":rainbow: "
        f"Farewell, {member.display_name}. As brave as you may feel it is dangerous "
        "beyond these halls!"
    )
    msg_dk = (
        ":rainbow: "
        f"Farvel, {member.display_name}. Så tapper som du end føler du er, "
        "så er det farligt hinsides disse sale!"
    )
    await channel.send(f"{msg}\n\n{msg_dk}")


@bot.command()
async def ping(ctx):
    '''
    Check if bot is online
    '''
    latency = bot.latency
    await ctx.send(f"Latency: {latency}")

bot.run(os.environ.get('TOKEN'))
