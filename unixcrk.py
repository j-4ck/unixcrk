# long live deletehumanity
import crypt
import sys
import commands
import time
import datetime

def checkfile(file):
	try:
		f = open(file, 'r')
	except:
		print 'Unable to open: ' + file
		sys.exit()

def gethash(user):
	try:
		cmd = commands.getstatusoutput('cat /etc/shadow | grep ' + user)
		un, hash = cmd[1].split(user)
		a,b,c,d,e,f,g,h = hash[1:].split(':')
		return a
	except Exception as e:
		print '[!] ' + e
		hash = raw_input('[!] Unable to get hash for user "' + user + '".\n[?] Manually enter: ')
		return hash
def main():
	print '''
 _   _ _   _ _______   _______ ______ _   __
| | | | \ | |_   _\ \ / /  __ \| ___ \ | / /
| | | |  \| | | |  \ V /| /  \/| |_/ / |/ / 
| | | | . ` | | |  /   \| |    |    /|    \ 
| |_| | |\  |_| |_/ /^\ \ \__/\| |\ \| |\  \ 
 \___/\_| \_/\___/\/   \/\____/\_| \_\_| \_/

	  -- Author: @0xjack --
	'''

	if len(sys.argv) < 3:
		print 'Usage:\n\tpython unixcrk.py root wlist.txt [-v/--verbose]\n'
		sys.exit()
	uname = sys.argv[1]
	wlist = sys.argv[2]
	if '-v' in sys.argv or '--verbose' in sys.argv:
		start = raw_input('[!] Warning: Verbose mode can greatly decrease cracking speed. Would you like to proceed? [y/n] ')
		if start.lower().strip() != 'y':
			sys.exit()
	print '[' + str(datetime.datetime.now()) + '] Attack started!'
	checkfile(wlist)
	words = open(wlist, 'r')
	hash = gethash(uname)
	start = time.time()
	wordnum = 1
	for line in words:
		try:
			enc = crypt.crypt(line.strip(),hash[:2])
			if '-v' in sys.argv or '--verbose' in sys.argv:
				print '[' + str(datetime.datetime.now()) + '] ' + uname + ':' + line,
			if enc.strip() == hash.strip():
				print '[' + str(datetime.datetime.now()) + '] "' + hash + '" == "' + line.strip() + '"'
				print '[+] Tried: ' + str(wordnum) + ' words'
				if time.time() - start < 60:
					endstr = str((time.time() - start)) + ' seconds'
				elif time.time() - start > 60 and time.time() - start < 3600:
					endstr = str(time.time() - start/60) + ' minutes'
				else:
					endstr = str((time.time() - start)/60/60) + ' hours'
				print '[+] Attack lasted: ' + endstr
				print '[+] Attack rate: ' + str(wordnum / (time.time() - start)) + ' words per-second!\n'
				sys.exit()
			wordnum += 1
		except KeyboardInterrupt:
			print '\n[!] Shutting down...'
			sys.exit()
if __name__ == '__main__':
	main()
