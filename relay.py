import discord
import os
from dotenv import load_dotenv
import json
import boto3

load_dotenv('.env')

TOKEN = os.getenv('DISCBOT_TOKEN')
BUS_ARN = os.getenv('BUS_ARN')

eventbridge = boto3.client('events')


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        json_message = {
            "content": message.content,
            "id": message.id,
            "author": {
                "id": message.author.id,
                "name": message.author.name
            },
            "channel": {
                "id": message.channel.id,
                "name": message.channel.name,
            },
            "guild": {
                "id": message.guild.id,
                "name": message.guild.name
            }
        }
        json_message_dump = json.dumps(json_message)
        response = eventbridge.put_events(
            Entries=[
                {
                    'Source': f'discord.bot.{self.user.name}',
                    'DetailType': 'discord.message',
                    'Detail': json_message_dump,
                    'EventBusName': BUS_ARN
                },
            ]
        )
        eventid = response['Entries'][0]['EventId']
        print(f'Relayed message to {BUS_ARN}. Eventid {eventid}')


def main():
    client = MyClient()
    client.run(TOKEN)


if __name__ == '__main__':
    main()
