import discord
client = discord.Client()
@client.event
async def on_ready():
    print('로그인되었습니다!')
    print(client.user.name)
    print(client.user.id)
    print('====================================')

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("채편님 팬이에요"))

@client.event
async def on_message(message):
    if message.content == '심채편':
        await message.channel.send('잘생김!')
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
