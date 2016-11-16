import random
from random import randint
print "Random Speech Generator"

#Random number generator for selecting random file number
def randomizer (n):
	return randint(0,n)
	
#Random line selector for returning random line from given file
def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
      if random.randrange(num + 2): continue
      line = aline
    return line
global speech	
#open all speech files for reading
def openall():
	speech = [open("speech{}.txt".format(x),'r') for x in range(6)]
	
def closeall():
	for filename in speech:
		filename.close()

speech = [open("speech{}.txt".format(x),'r') for x in range(6)]

#Take number of sentences required
num = input ("Enter number of sentences (for approximation, consider 10 words on average per sentence):")	
print num
#read from speech and write to output sentence by sentence
for i in range (0,num):	
	# read a line of file
	r = randomizer(5)
	lines = speech[r].read().splitlines()
	speech[r].seek(0)
	str = random.choice(lines)
	

	#str = random.choice(speech[randomizer(5)].readlines())
	#str = random_line(speech[randomizer(5)])
	
	#write into output file	
	output = open("output.txt","a")
	output.write (str)
	
	
output.close()	
closeall()