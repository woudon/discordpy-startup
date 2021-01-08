from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

def get_problems(): # word.txtからリストを返す
    with open("word.txt", "r") as f:
        problems = f.readlines()

        problems = [x.strip() for x in problems]
        
    return problems

def start_english_word_test(problems): # 英語と日本語を表示
    for index, p in enumerate(problems):
        x = p.split(",")
        print(x)

        english = x[0]
        japanese = x[1]

        await message.channel.send("===Q{}===".format(index+1))

        await message.channel.send(english)
        time.sleep(2)
        await message.channel.send(japanese)
        time.sleep(2)

def main():
    p = get_problems()
    random.shuffle(p)
    start_english_word_test(problems=p)

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.event
async def on_message(message):
    # 送信者がbotである場合は弾く
    if message.author.bot:
        return 
    # メッセージの本文が /tango だった場合
    if message.content == "/tango":
        
        # メッセージが送られてきたチャンネルに送る
        await message.channel.send("Please enter an integer.")
            if isinstance(message.content, int):
                main()
    elif message.content == "おはよう":
        await message.channel.send("おはよう！！")


bot.run(token)
