from itertools import product
import time
loops = 3
guessNumber = 0

userPW = raw_input('Please enter your password')
start_time = time.time()
while loops <=8:
    for solution in product('ABCDEFGHIJKLMNOPQRSTUVWXYXZabcdefghijklmnopqrstuvwxyz!@#$%&* ~+=',repeat=loops):
        if (guessNumber % 10000) == 0:
            print "".join(solution)
            print guessNumber
        guessNumber = guessNumber + 1
        if userPW == "".join(solution):
            print 'your password was' + "".join(solution)
            print "This took %s seconds" % (time.time() - start_time)
            exit()
    loops = loops + 1
        
        
