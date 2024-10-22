import speech_recognition as sr
import pyttsx3
import pyjokes  
import time
import math
import os
import webbrowser		# WILL GO DEEPER LATER (WIKIPEDIA,PHUE,WOLFARM)
import linecache

robot_ear = sr.Recognizer()
engine = pyttsx3.init() 
robot_brain = ""
name = ""
memory = ""

if os.path.exists("ai_memory.txt"):
	file = open("ai_memory.txt", "r")
	if file.read != "":
		name = file.read()
	else:
		name = ""
	file.close()
else:
	name = ""

if os.path.exists("filetest.txt") and os.path.exists("line.txt"):
	ft = open("filetest.txt","r")
	fi = open("line.txt","r")
	if ft.read() != "" and fi.read() != "0":
		note = "activate"
	else:
		note = "not activate"
	ft.close()
	fi.close()
else:
	note = "not activate"


def check_line(line):
	if os.path.exists("line.txt") == False:
		f1 = open("line.txt","x")
		with open("line.txt","w") as f1:
			f1.write("0")

	f1 = open("line.txt","r")
	line_r = int(f1.read()) + line
	print(line_r)

	with open("line.txt","w") as f1:
			f1.write(str(line_r))
# chrome_p = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
	
print("say anything: ")

while True:
	with sr.Microphone() as mic:
	    robot_ear.adjust_for_ambient_noise(mic)
	    print("--------------------------------")
	    audio = robot_ear.listen(mic)
	    try:
	    	you = robot_ear.recognize_google(audio)
	    except:
	    	you = ""

	print("You: " + str(you))

	if you == "":
		robot_brain = "i can't hear you"

	elif "what" and "you say" in you:
		if robot_brain == "":
			robot_brain = "Bruh, i haven't say anything for the whole time"
		else:
			robot_brain = "Hm, I remember I said: " + robot_brain

	elif "shut up" in you:
		robot_brain = ""

	elif you == "good job":
		if name != "":
			robot_brain = "Thank you, " + name
		else:
			robot_brain = "Thanks"

	elif "haha" in you:
		robot_brain = "hahahahahahahahaaahaahaahaaaaaaaaaahaaaahaaaaaaaaahahahha"

	elif "hehe" in you:
		robot_brain = "hehe"

	# elif "where" and "you" in you:
	# 	robot_brain = "Im next to you"

	elif "what is" in you and "root of" in you:
		if "what is the root of" in you:
			result = float(you.replace("what is the root of ",""))
			print(result)
			result1 = math.sqrt(result)
		elif "what is root of" in you:
			result = float(you.replace("what is root of ",""))
			print(result)
			result1 = math.sqrt(result)
		else:
			result = "error"

		robot_brain = "It's " + str(result1)

	elif you == "ping":
		robot_brain = "pong"

	elif "boohoo" in you:
		robot_brain = "I'm a robot, i cannot cry."

	elif "you" in you and "idiot" in you:
		robot_brain = "You too"

	elif "tell me a joke" in you:
		robot_brain = pyjokes.get_joke()

	# elif "your joke" and "lame" in you:
	# 	robot_brain = "Shush, I know"		#DEMO
	# 	joke = 0

	elif "what did I tell you to remember" in you:
		if note == "activate":
			robot_brain = "Things you noted:"
			lists = []
			with open("line.txt","r") as f1:
				lenf = f1.read()
			for i in range(int(lenf)):
				memory = linecache.getline('filetest.txt', i + 1)
				lists.append(memory)
		else:
			robot_brain = "You haven't noted anything"

	elif "remember this for me" in you:

		you = you.replace("remember this for me ", "")
		line = 0

		if os.path.exists("line.txt"):
			with open("line.txt","r") as fl:
				line_i = int(fl.read())
			note_l = line_i + 1
		else:
			note_l = 1

		if os.path.exists("filetest.txt"):
			with open("filetest.txt","a") as f:
				f.write(str(note_l) + ". " + you + "\n" )
				line += 1

		else:
			f = open("filetest.txt","x")
			with open("filetest.txt","a") as f:
				f.write(str(note_l) + ". " + you + "\n" )
				line += 1

		lists = []
		check_line(line)
		with open("line.txt","r") as f1:
			lenf = f1.read()
		for i in range(int(lenf)):
			memory = linecache.getline('filetest.txt', i + 1)
			lists.append(memory)

		robot_brain = "Okay, All noted"

		note = "activate"


	elif "go to" in you:
		you = "".join(you.split())
		you = you.replace("goto","")
		webbrowser.open_new(you+".com")
		print(you+".com")
		robot_brain = "Opening..."

	elif "good morning" in you or "good afternoon" in you or "good evening" in you or "goodnight" in you:
		time_ob = time.localtime()
		l_time = time.strftime("%H %M %S",time_ob)
		c = l_time.split()
		hour = int(c[0])
		minutes = float(int(c[1]) / 60)
		result = float(hour + minutes)
		if "morning" in you:
			if result >= 21:
				robot_brain = "Breh, don't you see? It is night time and bed time is now"
			elif result >= 18.5:
				robot_brain = "Bruh, It's night time now"
			elif result >= 11.5:
				robot_brain = "Bro, this is afternoon. Don't you know?"
			elif result >= 7:
				robot_brain = "good morning"
			elif result < 7:
				robot_brain = "Dude, why you wake up so soon?"
			else:
				robot_brain = "ehm"

		elif "afternoon" in you:
			if result >= 21:
				robot_brain = "Dude, don't you see? It is night time and bed time is now"
			elif result >= 18.5:
				robot_brain = "Bruh, It's night time now. Good evening"
			elif result >= 11.5:
				robot_brain = "good afternoon"
			elif result >= 7:
				robot_brain = "Actually, It is afternoon now, bro"
			elif result < 7:
				robot_brain = "Dude, why you wake up so soon? And It is not afternoon, bro"
			else:
				robot_brain = "ehm"

		elif "evening" in you:
			if result >= 21:
				robot_brain = "Go to sleep, bro. It's pretty late"
			elif result >= 18.5:
				robot_brain = "Good evening"
			elif result >= 11.5:
				robot_brain = "Still not night time, bruh"
			elif result >= 7:
				robot_brain = "It is fockin morning now"
			elif result < 7:
				robot_brain = "Dude, why you wake up so soon?"
			else:
				robot_brain = "ehm"

		elif "night" in you:
			if result >= 21:
				robot_brain = "Good night-Sweet dream, bro"
			elif result >= 18.5:
				robot_brain = "Hmm, still too soon to good night, bro"
			elif result >= 11.5:
				robot_brain = "Breh, It's afternoon"
			elif result >= 7:
				robot_brain = "Seriously? Have you seen that radiate in front of you?"
			elif result < 7:
				robot_brain = "Dude, why you wake up so soon? and why did you say good night when you've just wake up"
			else:
				robot_brain = "ehm"

	elif "repeat after me" in you:
		print("Robot: " + you)
		engine.say(you)
		engine.runAndWait()

		while True:
			with sr.Microphone() as mic:
				robot_ear.adjust_for_ambient_noise(mic)
				print("*------------------------------*")
				audio = robot_ear.listen(mic)
				try:
					you = robot_ear.recognize_google(audio)
				except:
					you = ""

			print("You: " + you)

			if you != "":				
				if "stop" in you:
					robot_brain = "Okay"
					break

				print("Robot: " + you)

				engine = pyttsx3.init()
				engine.say(you)
				engine.runAndWait()

			else:
				print("Robot: ")

	elif "remind me of" in you:
		if "remember to" in you:
			you = you.replace("remember to remind me of ", "")
			memory = you
		elif "later" in you:
			you = you.replace("remind me of ","")
			youlater = you
			you = youlater.replace(" later", "")
			memory = you
		else:
			you = you.replace("remind me of ", "")
			memory = you

		robot_brain = "Okay"

	elif "what" and "remind me" in you:
		if memory == "":
			robot_brain = "You didn't tell me to remind me of anything"
		else:
			robot_brain = "You told me to remind you of " + memory

	elif you == "what is your name" or you == "what your name":
		robot_brain = "My name is Zax"

	elif "my name is" in you:

		if name != "":
			you = you.replace("my name is ", "")
			name_rp = you
			if name_rp == name:
				robot_brain = "You have already told me before, dude"
			else:
				robot_brain = "Hmm, isn't your name is, " + name + "?"

		elif name == "":
			you  = you[11:]
			name = you
			you = "my name is " + str(you)
			if name ==  "":
				robot_brain = "is what?"
			else:
				robot_brain = "Nice to meet you, " + str(name)
				if os.path.exists("ai_memory.txt"):
					with open("ai_memory.txt","w") as f:
						f.write(name)
				else:
					f = open("ai_memory.txt","x")
					with open("ai_memory.txt","w") as f:
						f.write(name)

		else:
			robot_brain = "Your name is something that i don't know"

	elif "what" in you and "my name" in you:
		if name == "":
			robot_brain = "I haven't known"
		else:
			robot_brain = "Your name is " + name

#even more smart then discuss what if the opponent forget, "pls", 
#again memory = memory + str(memory) remind of this another thing
	elif "change my name to" in you:
		if name == "":
			robot_brain = "Wait, you haven't told me your name yet"
		else:
			you = you.replace("change my name to ", "")
			name = you
			robot_brain = "Okay, " + name
			with open("ai_memory.txt","w") as file:
				file.write(name)

	elif "what time" in you:

		time_ob = time.localtime()
		l_time = time.strftime("%H hours %M minutes %S seconds",time_ob)

		robot_brain = l_time

	elif you == "now":

		time_ob = time.localtime()
		l_time = time.strftime("%H hours %M minutes %S seconds",time_ob)

		robot_brain = l_time

	elif "what" in you and "today" in you:

		time_td = time.localtime()
		ltd_t = time.strftime("%B %d, %Y",time_td)

		robot_brain = ltd_t

	elif "what" in you and "equal" in you:
		if "what is" and "equal to" in you:
			result = you.replace("what is ", "")
			you = result
			result = you.replace(" equal to", "")
			print(result)

		elif "what is" in you and "equal" in you:
			result = you.replace("what is ", "")
			you = result
			result = you.replace(" equal", "")
			print(result)		

		elif "what" in you and "equal" in you:
			result = you.replace("what ", "")
			you = result
			result = you.replace(" equal", "")
			print(result)

		else:
			robot_brain = "error"

		try:
			robot_brain = "It's " + str(eval(result))
		except:
			robot_brain = "Please try again"

	elif "hello" in you:
		if name == "":
			robot_brain = "Hello, dude"
		elif name == name:
			robot_brain = "Hello, " + name

	elif "bye" in you:
		if name == "":
			robot_brain = "Bye bye"
		elif name == name:
			robot_brain = "Bye bye, " + name
		
		print("Robot: " + robot_brain)
		engine.say(robot_brain)
		engine.runAndWait()
		break

	else:
		robot_brain = "I don't understand"

	try:

		print("Robot: " + str(robot_brain))

		engine.say(robot_brain)
		if "Zax" in robot_brain and name == "":
			robot_brain = "what about you?"
			engine.say(robot_brain)
			print("Robot: " + robot_brain)
		if "noted" in robot_brain and note == "activate":
			for i in lists:
				print(i)
				engine.say(i)

	except Exception:
		pass

	engine.runAndWait()  