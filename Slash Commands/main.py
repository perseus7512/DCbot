# 導入 套件
import re
import discord
import os
from dotenv import load_dotenv
import datetime as dt

# 取得環境設定
load_dotenv()
DISCORD_TOKEN=os.getenv("DISCORD_TOKEN")
# intents
intents=discord.Intents.default()
intents.message_content=True
# client
client = discord.Client(intents=intents)
#channel_id=1208243111990530110

# event 事件處理
@client.event
async def on_ready():
    print(f"「{client.user}」已登入")

@client.event
async def on_message(message):
    print(message)
    if message.author==client.user:# 排除機器人本身的訊息
        return
    # 純文字偵測「ping」
    if message.content=='ping':
        await message.channel.send('pong')# 發送訊息到目標伺服器的文字頻道
        await message.reply('ha')# 使用「回覆」目標訊息
        await message.author.send("私訊給你~ pong")
    # 偵測機器人被Tag
    elif re.findall(f"<@{client.application_id}>",message.content):
        await message.reply("安安 找我嗎~")# 使用「回覆」目標訊息
    # 文字判斷
    elif re.findall("呼叫幫手",message.content):
        newStr=message.content.split('呼叫幫手')
        await message.author.send("私訊給你~ 你剛剛說:"+newStr[1])# 發送訊息到目標成員私訊

#偵測編輯
@client.event
async def on_message_edit(before, after):
    # channel = client.get_channel(before.channel.id)
    # await channel.send(f'{ before.author.mention }修改了訊息!!!')
    embed=discord.Embed(color=0x34495E,timestamp=dt.datetime.utcnow())
    embed.description=f"{before.author.mention}在{before.channel.mention}編輯了訊息"
    embed.add_field(name="編輯前",value=f"``{before.clean_content}``",inline=False)
    embed.add_field(name="編輯後",value=f"``{after.clean_content}``")
    embed.set_author(name="訊息編輯紀錄")
    guild=client.get_guild(before.guild.id)
    await guild.system_channel.send(embed=embed,silent=True)
    return

#偵測刪除
@client.event
async def on_message_delete(message):
    #channel = client.get_channel(message.channel.id)
    #await channel.send(f'{ message.author.mention }刪除了訊息:{message.content}')
    embed=discord.Embed(color=0xDE353E,timestamp=dt.datetime.utcnow())
    embed.description=f"{message.author.mention}在{message.channel.mention}刪除了訊息"
    embed.add_field(name="刪除的內容",value=f"``{message.content}``")
    embed.set_author(name="訊息刪除紀錄")
    guild=client.get_guild(message.guild.id)
    await guild.system_channel.send(embed=embed,silent=True)
    return

if __name__=="__main__":
    client.run(DISCORD_TOKEN)