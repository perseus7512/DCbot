import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# 取得環境設定
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
# intents
intents = discord.Intents.default()
intents.message_content = True
# client
client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_message(message):
	if message.author == client.user:  # 排除機器人本身的訊息
		return
	await client.process_commands(message)

@client.command()
async def hello(ctx, message: str=""):
	await ctx.send(f"您好w {'您說了' + message if message else ''}")

@commands.command()
async def test(ctx):
	await ctx.send('test')

client.add_command(test)
				
client.run(DISCORD_TOKEN)