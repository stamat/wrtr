#! /usr/bin/python

import sys
import os
import json
import re

_conf = {}
_confname = '.wrtr.conf'
_HOME = os.path.expanduser('~');
_confpath = os.path.join(_HOME, _confname)
FILE = ''

del sys.argv[0]

def loadConfig():
	global _confpath, _conf, FILE
	f = open(_confpath, 'r')
	_conf = json.loads(f.read())
	f.close()
	FILE = os.path.join(_conf['path'], _conf['filename']);

def storeConfig():
	global _confpath, _conf, FILE
	f = open(_confpath, 'w')
	f.write(json.dumps(_conf))
	f.close()
	FILE = os.path.join(_conf['path'], _conf['filename']);

def countDefaultNotebooks(path):
	count = []
	reg = re.compile(r'^notebook([0-9]+)\.txt$')
	for f in os.listdir(path):
		fpath = os.path.join(path,f)
		match = re.match( reg, f)
		if fpath and match:
			m = match.group(1);
			if match.group(1) == '':
				m = 0;
			else:
				m = int(m)
			count.append(m)

	if len(count) == 0:
		return '';
	else: 
		count = max(count)
		return str(count+1);

def changeNotebook():
	notebook_name = raw_input("Enter a name or a full path of your notebook file: ")
	#TODO: validate file
	pts = os.path.split(notebook_name)
	if not pts[0] == '':
		_conf['path'] = os.path.expanduser(pts[0])
	
	
	return True

def newNotebook():
	global _conf, FILE
	count = countDefaultNotebooks(_conf['path'])
	nname = "notebook"+count+".txt"
	notebook_name = raw_input("Enter a name of your new notebook file ( "+nname+" ): ")
	if notebook_name == '':
		notebook_name = nname
	
	_conf['filename'] = notebook_name
	_conf['chapter'] = 0

	FILE = os.path.join(_conf['path'],_conf['filename'])
	f = open(FILE, 'w')
	f.write('') #TODO: Add empty title and chapter 1
	f.close()
	
	return True

def promptForPath():
	global _conf, _HOME
	_conf['path'] = os.path.expanduser(raw_input("Enter a path where you will store your notebooks ("+_HOME+"): "))
	if _conf['path'] == '':
			_conf['path'] = _HOME
		else:
			if not os.path.exists(_conf['path']):
				os.makedirs(_conf['path'])
	
	return True

def changePath():
	promptForPath()
	storeConfig()
	return True;

def setTitle():
	return True;

def appendParagaph(chapter):
	return True;

def newChapter(chapter_title, after_chapter):
	return True;

def setChapter(chapter, chapter_title):
	return True;

def readChapter(chapter):
	return True;

def read():
	return True;

def readParagraph(chapter, paragraph):
	global _conf
	return True;

#TODO: with readline
def editParagraph(chapter, paragraph):
	return True;

def _init():
	
	promptForPath()

	newNotebook()

	storeConfig()

if not os.path.isfile(_confpath):
	_init()
else:
	loadConfig()
	
