#! /usr/bin/python

import sys
import os
import json
import re

##############################
#
# 	Functinality plan:
# 	------------------
#
# 	wrtr I am entering some text | 	wrtr -w | --write I am entering some text						~ this text after wrtr appends in the last paragraph, or the current paragraph set in the config
#	wrtr -i  | --insert 	1 | 1.5 	Some text											~ this text is inserted as a fift paragraph of chapter one if there is the 4th one ofcourse
#	wrtr -p  | --prepend 			Some text											~ this text is prepended to the curent chapter
#	wrtr -r  | --read   	empty | 1 | 1-3 | 1.2 | 1.2-1.4 | 1n (with note) | 1.2n		~ empty reads all the notebook
#	wrtr -c  | --chapter	empty | number of a chapter									~ emty shows the current chapter, also shows the stats number of words and chars
#	wrtr -rm | --remove		notebookname | 1 | 1-3 | 1.2 | 1.2-1.4| 1a (delets the chapter contents)
#	wrtr -lc | --list-chapters
#	wrtr -ln | --list-notebooks
#	wrtr -nc | --new-chapter	empty | name of the chapter
#	wrtr -t  | --title			empty | new name for the title
#	wrtr -e  | --edit			1 | 1.2													~ edits a paragraph or a chapter
#   wrtr -n  | --note			1 | 1.2 | empty + note ofc
# 	wrtr -a	 | --author			Name Surname | empty									~ stores the author in conf file too, empty shows the author
#	wrtr --export				/dir/													~ exports to html
#	wrtr -cp | --copy			0 1 | 1.2 2 | 1.2 2.3
#	wrtr -mv | --move			0 1 | 1.2 2 | 1.2 2.3

#	Format:
#
#	First three lines describe the document and they are mandatory.
#	[title] Untitled \n
#	[author] Name Surname \n
#	[date;last-modified="timestamp"] timestamp crated\n
#	\n
#
#	There is a zero chapter, by default, used to add the 
#	[zero-chapter] \n
#	\n
#
#	[chapter;note="chapter note"] \n
#	\n
#	[p;note="paragraph note"] Paragraph text\n


#	Ideas:
#		- Document stats in the title line
#		- Notes, list all notes in a chapter, read all chapter with notes, eddit a note etc... note is bound to chapter or a paragraph
#		- --edit 1.2 (edit second paragraph from the first chapter)
#		- export to html

_conf = {}
_confname = '.wrtr.conf'
_HOME = os.path.expanduser('~');
_confpath = os.path.join(_HOME, _confname)
FILE = ''

fns = {
	'-t': '_setTitle',
	'--title': '_setTitle',
	'-e': '_edit',
	'--edit': '_edit',
	'-w': '_write',
	'--write': '_write',
	'-i': '_write',
	'--insert': '_write',
	'-r': '_read',
	'--read': '_read'
}

del sys.argv[0]

def fn(fname, *argv):
	globals()[fname](*params)

def _setTitle(args):
	print 'setTitle'

def _edit(args):
	print 'edit'

def _write(args):
	print 'write'

def _read(args):
	print 'read'

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
	#TODO: validate file, a file is walid by validating a title first line
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

def appendParagaph(chapter):
	return True;

def newChapter(chapter_title, after_chapter):
	return True;

def setChapter(chapter, chapter_title):
	return True;

def readChapter(chapter):
	return True;

def readParagraph(chapter, paragraph):
	global _conf
	return True;

#TODO: with readline
def editParagraph(chapter, paragraph):
	return True;

def getNotebookStats():
	#num of chapters, num of paragraphs, num of words
	return True;

def _init():
	
	promptForPath()

	newNotebook()

	storeConfig()

if not os.path.isfile(_confpath):
	_init()
else:
	loadConfig()
	
