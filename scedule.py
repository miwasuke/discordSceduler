# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NTY5MDg1MTMzOTcwMjEwODI2.XLrf1Q.rs9tvcAz6IJp5Id6-XpQ1b_6H-4'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('login')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # /test に対してunkoを返答
    if message.content == '/test':
        await message.channel.send('unko')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
