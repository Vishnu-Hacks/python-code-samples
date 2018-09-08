import random

""" all random module operations are based on the seed, which is current time by default"""

""" creating 4 random numbers """

rand= [random.random() for _ in range(4)]
print rand

""" creating 4 random numbers b/w 2 & 10 """
rand = [random.randrange(2,10) for _ in range (4)]
print rand

"""random generator with a custom seed, default is current time """
random.seed(100)
rand1 = [random.random() for _ in range(4)]
random.seed(100)
rand2 = [random.random() for _ in range(4)]

print rand1 == rand2 # returns True

random.seed(10)
rand3 = [random.random() for _ in range(4)]
print rand2==rand3 #return False

""" shuffling elements """
list1 = [x  for x in range(10)]

shuffledList = random.shuffle(list1)
print list1

""" making a random choice """
luckyWinner = random.choice(list1)
print luckyWinner

winners = random.sample(list1,3) # 3 distinct samples
print winners

duplicateWinners = [random.choice(list1) for _ in range(4)]
print duplicateWinners