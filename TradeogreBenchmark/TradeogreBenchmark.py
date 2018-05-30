from tradeogre import Commands
import time
key = ''
secret = ''
TO_ = Commands(key,secret)
print 'Benching, please wait..'
print '3 sets of 10,','3 sets of 100'
print '_______________________'
for i in range(0,3):
    print str(i+1)+': 10 tradeogre calls..'
    start = time.time()
    for i in range(0,10):
        tick = TO_.ticker('LTC')
    bench = time.time()-start
    bench = bench/10.0
    print 'Averaged: '+str(round(bench,3)) + ' seconds/call'

for i in range(0,3):
    print str(i+1)+': 100 tradeogre calls..'
    start = time.time()
    for i in range(0,100):
        tick = TO_.ticker('LTC')
    bench = time.time()-start
    bench = bench/100.0
    print 'Averaged: '+str(round(bench,3)) + ' seconds/call'

print 'Done Benching!'
while True:
    time.sleep(1)
    

