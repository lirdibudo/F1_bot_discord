import http.client
from bs4 import BeautifulSoup
import discord
import requests
import json

TOKEN = ''

DRIVERSTANDINGSAPI = 'https://ergast.com/api/f1/current/driverStandings.json'
LASTRACEAPI = 'https://ergast.com/api/f1/current/last/results.json'

def fetchData( api, parameters):
        response = requests.get(f"{api}", params=parameters)
        if response.status_code == 200:
            return response.json()
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")

driverStandings = fetchData( DRIVERSTANDINGSAPI, {})




driverStandings = driverStandings['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
driverStandingsFinal = []
longestName = 0
for driver in (driverStandings):
    name = driver['Driver']['givenName'] + ' ' +  driver['Driver']['familyName']
    if(len(name)>longestName): 
        longestName=len(name)
    driverStandingsFinal.append({
        'position': driver['position'],
        'points': driver['points'],
        'wins': driver['wins'],
        'name': driver['Driver']['givenName'] + ' ' +  driver['Driver']['familyName']
    })


positionSpace = 12
nameSpace = longestName + 4
pointsSpace = 10


firstMessage = 'Position'+' '*6,'Name'+' '*(longestName)+'Points'+' '*(pointsSpace)+'Wins'
#print()
for driver in (driverStandingsFinal):
    ranking = driver['position']+' '*(pointsSpace-len(driver['position']))+driver['name']+' '*(longestName-len(driver['name']))+driver['points']+' '*(pointsSpace-len(driver['points'])+2)+driver['wins']
    #print(ranking)



#discord
client = discord.Client(intents=discord.Intents.default())


#Current driver standing
"""
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channel = client.get_channel(1018252166286286948)
    #test 1018252166286286948
    help1 = 'Position'+' '*(positionSpace-8)+'Name'+' '*(longestName+8)+'Points'+' '*(pointsSpace-6)+'Wins'
    print(help1)
    await channel.send(help1)
    for driver in (driverStandingsFinal):
        ranking = driver['position']+' '*(pointsSpace-len(driver['position']))+driver['name']+' '*(longestName-len(driver['name']))+driver['points']+' '*(pointsSpace-len(driver['points'])+2)+driver['wins']
        await channel.send(ranking)
    
client.run(TOKEN)
"""
