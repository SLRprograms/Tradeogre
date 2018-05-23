from tradeogre import Commands
import time
#import pygame
from threading import Thread
#pygame.init()
'''
size = [800, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bid/Ask View")
clock = pygame.time.Clock()
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
'''
API_KEY = '008861e80c0bf5e2500bc78394c7722a'
API_SECRET = 'df623b099e0a9f2c83bf7593a9048438'
TO_ = Commands(API_KEY,API_SECRET)

def convertScale(_min, _max, pos, newMin, newMax):
    POSITION = float(abs(_min-pos))
    RANGE = float(abs(_max - _min))
    RATIO = float(POSITION / RANGE)
    NEWRANGE = float(abs(newMax - newMin))
    NEWPOSITION = newMin + float(NEWRANGE * RATIO)
    return NEWPOSITION

def shiftInPlace(l, n):
    n = n % len(l)
    head = l[:n]
    l[:n] = []
    l.extend(head)
    return l

def openProcess(i):#processes
    tick = TO_.ticker('GRFT')['price']
    end = time.time()-start
    print 'time: '+str(end)
start = time.time()
for i in range(0,4):
    t = Thread(target=openProcess,args=(start,))
    t.start()
time.sleep(10000)

#init bid and ask lists
bidPrice = []
askPrice = []
for i in range(0,800):
    bidPrice.insert(len(bidPrice),0.05)
    askPrice.insert(len(askPrice),0.1)
bidPrice[500] = 0.04
bidPrice[200] = 0.06
#recalculate min and max prices    
minPrice = 10000000.0
maxPrice = 0.00000001
for i in range(0,800):
    if bidPrice[i] < minPrice:
        minPrice = bidPrice[i]
    if askPrice[i] > maxPrice:
        maxPrice = askPrice[i]
while True:
    start = time.time()
    tick = TO_.ticker('GRFT')['bid']
    end = time.time()
    took = (end - start)
    print took
    #recalculate min and max prices    
    #minPrice = 10000000.0
    #maxPrice = 0.0
    #for i in range(0,800):
        #if bidPrice[i] < minPrice:
            #minPrice = bidPrice[i]
        #if askPrice[i] > maxPrice:
            #maxPrice = askPrice[i]
    #maxPrice = maxPrice + (maxPrice * 0.002)
    #minPrice = minPrice - (minPrice * 0.002)

    #wait(gonnaWait)
    
    #bidPrice.pop(0)
    #bidPrice.insert(len(bidPrice),float(tick['bid']))
    #askPrice.pop(0)
    #askPrice.insert(len(askPrice),float(tick['ask']))

    #render display
    #pygame.init()
    #size = [800, 300]
    #screen = pygame.display.set_mode(size)
    #pygame.display.set_caption("Bid/Ask View")
    #screen.fill(BLACK)
    #for i in range(0,799):
        #bid coords
        #x1Bid = i
        #y1Bid = convertScale(maxPrice,minPrice,bidPrice[i],0.0,300.0)
        #x2Bid = i+1
        #y2Bid = convertScale(maxPrice,minPrice,bidPrice[i+1],0.0,300.0)
        #ask coords
        #x1Ask = i
        #y1Ask = convertScale(maxPrice,minPrice,askPrice[i],0.0,300.0)
        #x2Ask = i+1
        #y2Ask = convertScale(maxPrice,minPrice,askPrice[i+1],0.0,300.0)
        #draw a ask and bid line
        #pygame.draw.line(screen, RED,   [x1Ask, y1Ask], [x2Ask, y2Ask], 1)
        #pygame.draw.line(screen, GREEN, [x1Bid, y1Bid], [x2Bid, y2Bid], 1)
    #smooth brute forcing
    #pygame.display.flip()
    #clock.tick(60)
    #if took < targetTime:
        #extra = targetTime - took
    #gonnaWait = (gonnaWait + extra)/2.0
