# -*- coding: utf-8 -*-

import copy
import json
import os
from Constants import *
import urllib.request as urllib2
import time

UUID = {}


def name_to_uuid_fromAPI(name):
	url = 'http://tools.glowingmines.eu/convertor/nick/' + name
	response = urllib2.urlopen(url)
	data = response.read()
	js = json.loads(str(data))
	return js['offlinesplitteduuid']


def name_to_uuid(server, info, name):
	global UUID
	if UUID.has_key(name):
		return UUID[name]
	printMessage(server, info, 'name not found, use API')
	UUID[name] = name_to_uuid_fromAPI(name)
	return UUID[name]


def refreshUUIDList(server, info, name,showTip=False):
	global UUID
	UUID_file = {}
	UUID_cache = {}
	if not os.path.isdir(os.path.dirname(UUIDFile)):
		os.makedirs(os.path.dirname(UUIDFile))
	if os.path.isfile(UUIDFile):
		UUID_file = json.load(open(UUIDFile, 'r'))
	fileName = ServerPath + 'usercache.json'
	if os.path.isfile(fileName):
		with open(fileName, 'r') as f:
			try:
				js = json.load(f)
			except ValueError:
				printMessage(server, info, 'cann\'t open json file ' + fileName)
				return name_to_uuid_fromAPI(name)
			for i in js:
				UUID_cache[i['name']] = i['uuid']
	UUID = dict(UUID, **dict(UUID_cache, **UUID_file))
	json.dump(UUID, open(UUIDFile, 'w'))
	if server is not None and showTip:
		server.say('La lista UUID se actualiza y su longitud es: ' + str(len(UUID)))


def isBot(name):
	blacklist = 'A_Pi#nw#sw#SE#ne#nf#SandWall#storage#zi_ming#Steve#Alex###########'
	blackkey = ['farm', 'bot_', 'cam', '_b_', 'bot-']
	if blacklist.find(name) >= 0: return True
	if len(name) < 4 or len(name) > 16: return True
	for i in blackkey:
		if name.find(i) >= 0:
			return True
	return False


def printMessage(server, info, msg, isTell=True):
	if server is None:
		print(msg)
		return
	for line in msg.splitlines():
		if info.isPlayer:
			if isTell:
				server.tell(info.player, line)
			else:
				server.say(line)
		else:
			print(line)


def getStatsData(server, info, uuid, classification, target):
	jsonfile = WorldPath + 'stats/' + uuid + '.json'
	if not os.path.isfile(jsonfile):
		return (0, False)

	with open(jsonfile, 'r') as f:
		try:
			js = json.load(f)
		except ValueError:
			return (0, False)
		try:
			data = js['stats']['stat.' + classification]['minecraft:' + target]
		except KeyError:
			return (0, False)
		return (data, True)


def getPlayerList(server, info, listBot):
	global UUID
	ret = []
	for i in UUID.items():
		if listBot or not isBot(i[0]):
			ret.append(i)
	return ret


def triggerSaveAll(server):
	server.execute('save-all')
	time.sleep(0.2)


def getString(classification, target):
	return '§6' + classification + '§r.§e' + target + '§r'


def showStats(server, info, name, classification, target, isUUID, isTell):
	uuid = name
	if not isUUID:
		uuid = name_to_uuid(server, info, uuid)

	data = getStatsData(server, info, uuid, classification, target)

	msg = 'Player§b' + name + '§rInformacion stat de[' + getString(classification, target) + ']el valor de§a' + str(data) + '§r'
	printMessage(server, info, msg, isTell)


def showRank(server, info, classification, target, listBot, isTell, isAll, isCalled=False):
	getPlayerListResult = getPlayerList(server, info, listBot)
	arr = []
	sum = 0
	for player in getPlayerListResult:
		ret = getStatsData(server, info, player[1], classification, target)
		if ret[1] and ret[0] > 0:
			data = ret[0]
			arr.append((player[0], data))
			sum += data

	if len(arr) == 0:
		if not isCalled:
			printMessage(server, info, 'No se encontro stat o no existe！')
		return 'Cannot find stats file'
	arr.sort(key=lambda x: x[0])
	arr.reverse()
	arr.sort(key=lambda x: x[1])
	arr.reverse()

	showRange = min(RankAmount + isAll * len(arr), len(arr))
	if not isCalled:
		printMessage(server, info,'Stat [{}] numero total de §c{}§r, ex {} llamado'.format(getString(classification, target), str(sum), str(showRange)),isTell)
	ret = ['{}.{}'.format(classification, target)]

	maxNameLength = 0
	for i in range(0, showRange):
		maxNameLength = max(maxNameLength, len(str(arr[i][1])))
	for i in range(0, showRange):
		s = '#' + str(i + 1) + ' ' * (1 if isCalled else 4 - len(str(i + 1))) + \
			    str(arr[i][1]) + ' ' * (1 if isCalled else maxNameLength - len(str(arr[i][1])) + 2) + \
				str(arr[i][0])
		ret.append(s)
		if not isCalled:
			printMessage(server, info, rankColor[min(i, len(rankColor) - 1)] + s, isTell)

	ret.append('Total: ' + str(sum))
	return '\n'.join(ret)


def showScoreboard(server, info):
	server.execute('scoreboard objectives setdisplay sidebar ' + ScoreboardName)


def hideScoreboard(server, info):
	server.execute('scoreboard objectives setdisplay sidebar')


def buildScoreboard(server, info, classification, target, listBot):
	playerList = getPlayerList(server, info, listBot)
	server.execute('scoreboard objectives remove ' + ScoreboardName)
	server.execute('scoreboard objectives add ' + ScoreboardName + ' ' + 'stat.' + classification + '.minecraft.' + target +' §6' + classification + '§r.§e' + target)
	for player in playerList:
		ret = getStatsData(server, info, player[1], classification, target)
		if ret[1]:
			server.execute('scoreboard players set ' + player[0] + ' ' + ScoreboardName + ' ' + str(ret[0]))
	showScoreboard(server, info)


def onServerInfo(server, info, arg=None):
	isCalled = arg != None
	content = arg if isCalled else info.content
	isUUID = content.find('-uuid') >= 0
	content = content.replace('-uuid', '')
	listBot = content.find('-bot') >= 0
	content = content.replace('-bot', '')
	isTell = content.find('-tell') >= 0
	content = content.replace('-tell', '')
	isAll = content.find('-all') >= 0
	content = content.replace('-all', '')
	if not isCalled and not info.isPlayer and content.endswith('<--[HERE]'):
		content = content.replace('<--[HERE]', '')

	command = content.split()
	if len(command) == 0 or command[0] != Prefix:
		return
	del command[0]

	if len(command) == 0:
		if not isCalled:
			printMessage(server, info, HelpMessage)
		return

	cmdlen = len(command)
	if cmdlen == 4 and command[0] == 'query':
		showStats(server, info, command[1], command[2], command[3], isUUID, isTell)
	elif cmdlen == 3 and command[0] == 'rank':
		return showRank(server, info, command[1], command[2], listBot, isTell, isAll, isCalled)
	elif cmdlen == 3 and command[0] == 'scoreboard':
		buildScoreboard(server, info, command[1], command[2], listBot)
	elif cmdlen == 2 and command[0] == 'scoreboard' and command[1] == 'show':
		showScoreboard(server, info)
	elif cmdlen == 2 and command[0] == 'scoreboard' and command[1] == 'hide':
		hideScoreboard(server, info)
	elif cmdlen == 1 and command[0] == 'refreshUUID':
		refreshUUIDList(server, True)
	else:
		printMessage(server, info, 'Error, introduzca ' + Prefix + ' para obtener ayuda.')

# MCDReforged

def on_info(server, info):
	i = copy.deepcopy(info)
	i.isPlayer = i.is_player
	onServerInfo(server, i)
