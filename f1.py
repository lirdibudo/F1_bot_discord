import http.client
from bs4 import BeautifulSoup
import discord


TOKEN = ''

#Connection to the api
conn = http.client.HTTPSConnection("ergast.com")
payload = ''
headers = {}
conn.request("GET", "/api/f1/current/last/results", payload, headers)
res = conn.getresponse()
data = res.read()
#print(data.decode("utf-8"))


soup = BeautifulSoup(data, 'html.parser')

#Results of a race
circuit = soup.find("circuitname")
circuit=str(circuit).replace('<circuitname>','')
circuit=str(circuit).replace('</circuitname>','')

familynames = soup.find_all("familyname")
count=1


for i,name in enumerate(familynames):
   familynames[i] = str(name).replace('</familyname>','')
   
   
for i,name in enumerate(familynames):
    familynames[i] = str(name).replace('<familyname>','')
    
print(circuit)
for i in familynames:
    print(count ,'.', i)
    count = count+1


#Standing after a race

conn1 = http.client.HTTPSConnection("ergast.com")
conn1.request("GET", "/api/f1/current/driverStandings", payload, headers)
res1 = conn1.getresponse()
data1 = res1.read()
#print(data1.decode("utf-8"))
soup1 = BeautifulSoup(data1, 'html.parser')
#print(soup1)
familynamesstanding = soup1.find_all("familyname")
#print(familynamesstanding)


for i,name in enumerate(familynamesstanding):
   familynamesstanding[i] = str(name).replace('</familyname>','')
   
   
for i,name in enumerate(familynamesstanding):
    familynamesstanding[i] = str(name).replace('<familyname>','')
count=1
for i in familynamesstanding:
    print(count ,'.', i)
    count = count+1

#print(soup.get_text(soup.Driver.max_verstappen))

#print(soup)


#discord
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channel = client.get_channel(1016760789421531188)
    count = 1
    help1 = "Results of " + circuit + "          Standing"
    await channel.send(help1)
    for i,j in zip(familynames,familynamesstanding):
        help = str(count)+'.'+str(i) +"          " + str(count) + "." + str(j)
        await channel.send(help)
        #await channel.send(count)
        count = count+1
    
client.run(TOKEN)
