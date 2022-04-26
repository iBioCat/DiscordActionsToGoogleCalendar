#импорт дискор
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from itertools import cycle
import datetime
#импорт гугл
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
#константы дискорда
client = discord.ext.commands.Bot(command_prefix = '>')
TOKEN = 'NDE4MDcwMDE4NDA5MTAzMzcw.DpuzOw.q6pq6HEy0MwMY7PeK9Q4_R0KPPE'
now = datetime.datetime.utcnow().isoformat() + '+03:00'
change = []
event_body = {}
fl_df = datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=10, hours=0, weeks=0)
#константы гугла
SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))
#манипуляции дискордбота
@client.event
async def on_ready():
    print("Bot is on the server")
    print("Voice ready:",discord.opus.is_loaded())
    print("Name:",client.user.name)
    print("ID:",client.user.id)

@client.event
async def on_message(message):
    if message.content == 'ch_id':
        await client.send_message(message.channel,str(message.channel.id))

@client.event
async def on_member_update(before,after):
    if str(before.status) != str(after.status):
        current_member = {  'name' : str(after.name),
                            'before_status' : str(before.status),
                            'after_status' : str(after.status),
                            'change_time' : str(datetime.datetime.utcnow().isoformat() + '+00:00'),
                            'fl_time' : datetime.datetime.now(tz=None)
                          }

        if len(change) == 0:
            change.append(current_member)
        else:
            for i in range(0,len(change)):
                changed_member = change[i]
                if str(changed_member['name']) == str(current_member['name']):
                    member_name = str(current_member['name'])
                    clevent = str(current_member['before_status'])
                    start_time = str(changed_member['change_time'])
                    end_time = str(current_member['change_time'])
                    fl_st = changed_member['fl_time']
                    fl_en = current_member['fl_time']
                    fl_dl = fl_en - fl_st
                    
                    if clevent == 'online':
                        color = '2'
                    elif clevent == 'dnd':
                        color = '11'
                    elif clevent == 'idle':
                        color = '5'
                    elif clevent == 'offline':
                         color = '8'   
                    event_body = {
                      'summary': member_name,
                      'colorId':color,
                      'start': {
                        'dateTime': start_time,
                        'timeZone': 'Europe/Moscow',
                      },
                      'end': {
                        'dateTime': end_time,
                        'timeZone': 'Europe/Moscow',
                      }
                    }
                else:
                    change.append(current_member)
        if fl_dl > fl_df :
            event = service.events().insert(calendarId='omf4r9khmb7jqj4tc4d1cfvi3c@group.calendar.google.com',
                                                    body=event_body).execute()
            #await client.send_message(discord.Object(id='531178257903517712'),str("\n{}\n{}\n{}\n{}\n{}".format(current_member['name'],current_member['before_status'],fl_st,fl_en,fl_dl)))


client.run(TOKEN)
