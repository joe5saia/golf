#!/usr/bin/python
import json, urllib
from pprint import pprint



x = dict([('Joe',['34046', '24502', '20848', '06522', '20396']),
          ('Blake',['32102','32839','33448','26331','29221']),
          ('Alex',['21209','21528','25364','27408','25804']),
          ('Stephen',['28089','46970','29974','29478','36689']),
          ('Eric',['24024','06527','25686','33293','24361']),
          ('Justin',['28237','22405','26329','27649','23108'])
          ])


y = dict([('Joe',dict([('Last' , ['First', 'Score', 'Position'])])),
          ('Blake',dict([('Last' , ['First', 'Score', 'Position'])])),
          ('Alex',dict([('Last' , ['First', 'Score', 'Position'])])),
          ('Stephen',dict([('Last' , ['First', 'Score', 'Position'])])),
          ('Eric',dict([('Last' , ['First', 'Score', 'Position'])])),
          ('Justin',dict([('Last' , ['First', 'Score', 'Position'])]))
          ])

purse = 36.3
shares = [18.0, 10.8, 6.8, 4.8, 4, 3.6, 3.35, 3.1, 2.9, 2.7, \
          2.5, 2.3, 2.1, 1.9, 1.8, 1.7, 1.6, 1.5, 1.4, 1.3,\
          1.2, 1.12, 1.04, 0.96, 0.88, 0.8, 0.77, 0.74, 0.71,\
          0.68,0.65,0.62,0.59,\
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0,len(shares)-1):
  shares[i]=shares[i]/100


lboardf = urllib.urlopen('http://gripapi-static-pd.usopen.com/gripapi/leaderboard.json')

lboard = json.loads(lboardf.read())
pos = map (lambda x:lboard['standings'][x]['position']['displayValue'], 
  range(0,len(lboard['standings'])-1))

for keya in x:
  for keyb in x[keya]:
    url = "http://gripapi-static-pd.usopen.com/gripapi/player/"+keyb+".json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    first = data['player']['firstName']
    last  = data['player']['lastName']
    score = data['toPar']['value']
    position = data['position']['displayValue']
    if position == '':
      position = 'T120'
    posshort = int(position.replace("T",""))
    earnshare = sum(shares[(posshort-1):(posshort+pos.count(position)-1)])/max(pos.count(position),1)
    earn = purse*earnshare
    player = dict([(last, [first,score,position, earn])])
    y[keya].update(player)
  del y[keya]['Last']



for keya in y:
  keys = y[keya].keys()
  scores = map (lambda k:y[keya][k][1],y[keya].keys())
  index = sorted(range(len(scores)), key=lambda k: scores[k])
  tmp = keys[:]
  for i in range(0,len(index)):
    keys[i] = tmp[index[i]]
  print '\n\n' + keya + '\'s players and scores are:'
  for keyb in keys:
    print y[keya][keyb][0] + " " + keyb + " at " + \
    y[keya][keyb][2] +  " with " + str(y[keya][keyb][1]) \
    + ". Earnings is " + str(y[keya][keyb][3])
  totearn = sum(map(lambda x:y[keya][x][3], y[keya].keys()))
  print "His total earnings is " + str(totearn)

print "\n"

