import discord
import responses
import creds




async def send_message(message, user_message, is_private):
    try:


        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as error:
        print("error", error)


articles = responses.get_all_articles()

def run_discord_bot():
    TOKEN ='' #bot token here

    print(TOKEN)
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now online!")
        channel =''#channel ID here
        for article in articles:
            await channel.send(article)

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        # username = str(message.author)
        user_msg = str(message.content)
        # current_channel = str(message.channel)
        #
        # print(f"{username} said: '{user_msg}' {current_channel}")

        if user_msg[0] == '!':
            await  send_message(message, user_msg, is_private=False)

    client.run(TOKEN)


