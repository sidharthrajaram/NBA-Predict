import random

noShotResponses = [" doesn't have a great jumper.", 
" needs to work on his scoring ability.", 
" risks lowering his chances at stardom with his suspect shot."]

starResponses = [" has a high ceiling.", 
" is going to be great.", 
" is going to be an all star."]

scorerResponses = [" looks like he is gonna blossom into a high caliber scorer", 
" shows signs of all star scoring ability.", 
" can develop into a reliable scorer."]

defenseResponses = [" has solid defensive habits.", 
" can become a contributing member on both ends of the floor."]

efficientResponses = [" exhibits solid habits on both sides of the floor.", 
" is an efficient basketball player."]

inefficientResponses = [" needs to get rid of some bad habits on court.", 
" is relatively inefficient."]

durableResponses = [" can be a potential franchise cornerstone.", 
" is physically ready to take the next step to stardom."]


def sumUpSent(name, result):
	if(result):
		index = random.randint(0, len(starResponses)-1)
		sentence = name + starResponses[index]
		return sentence

def scoringSent(name, result):
	if(result):
		index = random.randint(0, len(scorerResponses)-1)
		sentence = name + scorerResponses[index]
	else:
		index = random.randint(0, len(noShotResponses)-1)
		sentence = name + noShotResponses[index]
	return sentence

def defenseSent(name, result):
	if(result):
		index = random.randint(0, len(defenseResponses)-1)
		sentence = name + defenseResponses[index]
		return sentence

def efficiencySent(name, result):
	if(result):
		index = random.randint(0, len(efficientResponses)-1)
		sentence = name + efficientResponses[index]
	else:
		index = random.randint(0, len(inefficientResponses)-1)
		sentence = name + inefficientResponses[index]
	return sentence

def durableSent(name, result):
	if(result):
		index = random.randint(0, len(durableResponses)-1)
		sentence = name + durableResponses[index]
		return sentence



