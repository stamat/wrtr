#! /usr/bin/python

import sys
import os.path
import json

_conf = {}

_confpath = '~/.wrtr.conf'

del sys.argv[0]

if not os.path.isfile(_confpath):
	_conf['filename'] = raw_input("Enter a path to a new book:")
	storeConfig()
else:
	loadConfig()

print json.dumps(_conf)

def loadConfig():
	global _confpath, _conf
	file = open(_confpath, 'r')
	_conf = json.loads(file.read())
	file.close()

def storeConfig():
	global _confpath, _conf
	file = open(_conf, 'w+')
	file.write(json.dumps(_conf))
	file.close()
	
