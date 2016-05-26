import os, sys, subprocess
import numpy as np

#	usage: python spew.py <amount> <number of random chunks> <to address>
#	eg. python spew.py 100 5 <address> sends 100 split into 5 random chunks to <address>

def spew():

	amount = int(sys.argv[1])
	chunks = int(sys.argv[2])
	address = str(sys.argv[3])

	#send <chunks> of <amount - 1, to avoid running out> 
	a = np.random.random(chunks)
	a /= (a.sum() / (amount)
	total = 0
	for item in a:
		b = round(item, 8) #truncate to 8dp
		total = total + b
		print 'Sending ' + str(b) + ' to  ' + address
		r = subprocess.check_output('./darkcoind sendtoaddress ' + address + ' ' + str(b), shell=True)
		print './darkcoind sendtoaddress ' + address + ' ' + str(b)
		print 'Total sent: ' + str(total)


#now wait for incoming from paired wallet
#time.sleep(120)
#mainloop
#while 1:
	#s = 0
	#get current blockheigt
	#h = subprocess.check_output('./darkcoind getbalance', shell=True)
	#hint = int(h)
	#if hint > s:
		#spew()
		#s += hint

		
	#print '/n/n/n/nspew1/n/n/n/n'
	#spew()
	#time.sleep(120)
	#get new? blockheight
	
spew()
