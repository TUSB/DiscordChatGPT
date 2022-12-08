# import asyncio
# import time
#
# import discord
# from discord.ext import commands
#
# TOKEN = ''
# discord_intents = discord.Intents.all()
# bot = commands.Bot(
#     command_prefix='!',
#     intents=discord_intents
# )
#
# def check(author):
#     time.sleep(10)
#     return True
#
# @bot.command()
# async def good(ctx):
#     try:
#         await ctx.typing()
#         await asyncio.sleep(10)
#         await bot.wait_until_ready()
#     except asyncio.TimeoutError:
#         await ctx.send('👎')
#     else:
#         await ctx.send('👍')
#
#
# bot.run(TOKEN)

def test(message):
    return message, 1, None

if __name__ == "__main__":
    answer, previous_convo_id, conversation_id = test("Test")
    print(answer)
    print(previous_convo_id)
    print(conversation_id)
