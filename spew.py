import os, sys, subprocess
import numpy as np

#       usage: python spew.py <amount> <number of random chunks> <to address>
#       eg. python spew.py 100 5 <address> sends 100 split into 5 random chunks to <address>

def spew():

    amount = int(sys.argv[1])
    chunks = int(sys.argv[2])
    address = str(sys.argv[3])

    #send <chunks> of <amount - 1, to avoid running out> 
    a = np.random.random(chunks)
    a /= (a.sum() / amount)
    total = 0
    for item in a:
        b = round(item, 8) #truncate to 8dp
        total = total + b
        print 'Sending ' + str(b) + ' to  ' + address
        r = subprocess.check_output('./bitcredit-cli sendtoaddress ' + address + ' ' + str(b)$
        print './bitcredit-cli sendtoaddress ' + address + ' ' + str(b)
        print 'Total sent: ' + str(total)

spew()
