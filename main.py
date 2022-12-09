import asyncio
import json
import sys

import discord
from discord.ext import commands
from pychatgpt import Chat, Options

from config_reader import email, password, token

discord_intents = discord.Intents.all()
bot = commands.Bot(
    command_prefix='?',
    intents=discord_intents
)

chat_history = {}
options = Options()

# Track conversation
options.track = True

# Use a proxy
# options.proxies = 'http://localhost:8080'

# Optionally, you can pass a file path to save the conversation
# They're created if they don't exist
# options.chat_log = "chat_log.txt"
# options.id_log = "id_log.txt"

chat: Chat = Chat(email=email, password=password, options=options)


@bot.event
async def on_ready():
    print("Login now....")


@bot.command()
async def ask(ctx, *args):
    global chat
    message = ' '.join(args)
    uid = ctx.author.id
    try:
        await ctx.typing()
        # Load thread id
        if uid in chat_history:
            previous_convo = chat_history[uid]["previous_convo_id"]
            convo_id = chat_history[uid]["conversation_id"]
        else:
            previous_convo = None
            convo_id = None

        print("You: " + message)
        # TODO 今はprevious_convo, convo_idを取得出来ないため、N:1会話となる。
        # 将来的には N:Nにするつもり
        # answer = chat.ask(message)
        answer, previous_convo_id, conversation_id = chat.ask(message, previous_convo_id=previous_convo,
                                                              conversation_id=convo_id)
        print("Chat GPT: " + answer)

        if answer == "Error":
            raise "[Error] We're working to restore all services as soon as possible. Please check back soon."

        chat_history[uid] = {
            "answer": answer,
            "previous_convo_id": previous_convo_id,
            "conversation_id": conversation_id
        }
        await bot.wait_until_ready()
    except asyncio.TimeoutError:
        await ctx.send("[Error] TimeOut Error")
    except Exception as ex:
        print(type(ex), str(ex), file=sys.stderr)
        trace = []
        tb = ex.__traceback__
        while tb is not None:
            trace.append({
                "filename": tb.tb_frame.f_code.co_filename,
                "name": tb.tb_frame.f_code.co_name,
                "lineno": tb.tb_lineno
            })
            tb = tb.tb_next

        embed = discord.Embed(title=f"{type(ex)}", description=f"'message': {str(ex)},", color=discord.Colour.red())
        embed.add_field(name="type", value=str(ex), inline=False)
        embed.add_field(name="trace", value=trace, inline=False)
        await ctx.reply(embed=embed)
    else:
        await ctx.reply(answer, mention_author=True)
        chat.save_data()


@bot.command()
async def history(ctx, args=None):
    global chat_history
    uid = ctx.author.id
    if args == "all":
        chat_str = json.dumps(chat_history, ensure_ascii=False)
        await ctx.send(f"{chat_str}")
    elif uid in chat_history:
        chat_str = json.dumps(chat_history[uid], ensure_ascii=False)
        await ctx.send(f"{chat_str}")
    else:
        await ctx.send(f"Not fond")


@bot.command()
async def reset(ctx, args=None):
    global chat_history
    uid = ctx.author.id
    if args == "all":
        chat_history = {}
        if len(chat_history) == 0:
            await ctx.send("Reset Thread for all。")
        else:
            await ctx.send("oops reset Thread")
    else:
        del chat_history[uid]
        if uid in chat_history:
            await ctx.send(f"<@{uid}> Reset Thread")
        else:
            await ctx.send("Not fond Thread")


@bot.command()
async def kill(ctx):
    await ctx.send("Good bye")
    exit(0)


bot.run(token)
