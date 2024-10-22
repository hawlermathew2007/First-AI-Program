from tkinter import *
import pyttsx3
import speech_recognition as sr
import pyjokes
import sys
import time
import math
import threading
import os
import linecache

ear = sr.Recognizer()
ear1 = sr.Recognizer()
engine = pyttsx3.init()
robot_brain = ""
you = ""
name = ""
if os.path.exists("ai_memory.txt"):
	file = open("ai_memory.txt", "r")
	if file.read != "":
		name = file.read()
	else:
		name = ""
	file.close()			#if name == "Matthew" => hello, twins
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

lisp = 10
activate = 1

def thread():
	def a_listen():

		global robot_brain

		with sr.Microphone() as mic1:
			ear1.adjust_for_ambient_noise(mic1)		#tryna make the listen in OOP
			print("*----------*")
			audio1 = ear1.listen(mic1)
			try:
				you = ear1.recognize_google(audio1)
				print("you: " + you)
			except Exception as e:
				you = ""

		if you == "":
			print("I can't hear you.")

			window.after(lisp,text_insertyou,"")
			window.after(lisp,text_insertrobot,"I can't hear you. Please try again.")

			engine.say("I can't hear you. Please try again.")
			engine.runAndWait()

			listen()

		else:
			text_area.insert(END,"You: {} \n".format(you))
			response(you)


	def response(you):

		global robot_brain
		global name
		global note
		
		
		if "hello" in you:
			if name == "":
				robot_brain = "Hello, dude"
			elif name == name:
				robot_brain = "Hello, " + name

		elif you == "good job":
			robot_brain = "Thanks"

		elif "I love you" in you:
			robot_brain = "I love you too"		#if name == "" => rb: I love you too, {name}"

		elif "haha" in you:
			robot_brain = "hahahahahahahahahahahahahahahahahahahahahahahahahahahaha"

		elif "hehe" in you:
			robot_brain = "hehe"

		elif you == "ping":
			robot_brain = "pong"

		elif "boohoo" in you:
			robot_brain = "I'm a robot, i cannot cry."

		elif "you" in you and "idiot" in you:
			robot_brain = "You too"

		elif "tell me a joke" in you:
			robot_brain = pyjokes.get_joke()

		elif "what did I tell you to remember" in you:
			if note == "activate":
				robot_brain = "Things you noted:"
				lists = []
				with open("line.txt","r") as f1:
					lenf = f1.read()
				for i in range(int(lenf)):			#repeated ;-;
					memory = linecache.getline('filetest.txt', i + 1)
					lists.append(memory)
			else:
				robot_brain = "You haven't noted anything"

		elif "remember this for me" in you:
			your = you.replace("remember this for me ", "") #ERROR # adjust Mathew #exchange "i" to "you"
			line = 0

			if os.path.exists("line.txt"):
				with open("line.txt","r") as fl:
					line_i = int(fl.read())			#get "2"
				note_l = line_i + 1			# turn to 3
			else:
				f1 = open("line.txt","x")
				with open("line.txt","w") as f1:
					f1.write("0")
				note_l = 1 		#if not exist file then note_l = 1

			if os.path.exists("filetest.txt") == False:		# will create now file
				f = open("filetest.txt","x")

			with open("filetest.txt","a") as f:		# append
				f.write(str(note_l) + ". " + your + "\n" )		#write down the note
				line += 1 			#line = 1 (not 0)

			lists = []

			f1 = open("line.txt","r")
			line_r = int(f1.read()) + line

			with open("line.txt","w") as f1:
					f1.write(str(line_r))

			robot_brain = "Okay, All noted"

			note = "activate"

		elif "remove" in you:	#multiple number problem 1,2,3,4,8 	"multiple remove"	# delete all
			try:
				if "remove all" in you:
					with open("line.txt","w") as fl:
						fl.write("0")
					with open("filetest.txt", "w") as f:
						f.write("")
					robot_brain = "Okay, remove sucessfully"
				else:
					you_r = you[7:]
					you_or = int(you_r[0:])
					you_lt = str(you_or)
					y_join = " ".join(you_lt)
					split_y = y_join.split()

					lists_r = []
					i_r = ""
					with open("line.txt","r") as f1:	#repeated
						lenf = f1.read()

					for i in range(int(lenf)):
						memory = linecache.getline('filetest.txt', i + 1)
						lists_r.append(memory)

					number = []
					j = 0
					if len(split_y) > 1: 
						for i in range(len(lists_r)):
							decimal = lists_r[i].index(".")		#no [i-j] allowed when multiple
							num = lists_r[i][:decimal]		#get the 1. => 1 ; 2. => 2 ... append in list number = []
							if num in split_y:
								lists_r.remove(lists_r[i])		# remove the element from list that have the i. string (4. )
								lists_r.insert(i, "nope")
								j += 1
							else:
								number.append(int(num))

					else:
						for i in range(len(lists_r)):	#ex: list_r = [1,2,3]; you_or = 2
							decimal = lists_r[i-j].index(".") #if there is no [i - j] => index error (i = 2 but the max index is 1)
							num = lists_r[i-j][:decimal]		#get the 1. => 1 ; 2. => 2 ... append in list number = []
							if num == str(you_or): # num == "2" => list_r = ["ddd", "sss"] => index = 0,1 not 0,1,2 (as default)
								lists_r.remove(lists_r[i])		# remove the element from list that have the i. string (4. )
								j += 1
							else:
								number.append(int(num)) 	#number = [1,3]
					if j == 0:
						robot_brain = "There is no note number {} for you to remove".format(you_or)
					elif number == []:
						robot_brain = "Okay, remove sucessfully"
						lists_r = []
					else:
						if len(split_y) > 1:
							k = 0
							for i in range(len(lists_r)):
								if lists_r[i - k] == "nope":
									lists_r.remove(lists_r[i - k])
									k += 1
							print(lists_r)
						number.sort()
						num_s1 = number[0]
						for i in range(len(number)):
							if len(number) == 1:	# ex: number = [1]
								if int(number[i]) == 1:		#can be shorten		 # if [1] == 1 
									num2 = number[i]
								else:					#if [nums] != 1
									num2 = 1
								number.remove(number[i])		#remove [nums]
								number.append(num2)				#change to [1]

							elif i == (len(number)-1):		#the last number in array of numbers #ex: [1,2,3] => i = 3
								if (number[i] - number[i-1]) != 1:		#ex: number = [1,2,4] # if (4 - 2) != 1
									i_rl = number[i-1] + 1 				# i_rl = 2 + 1
									number.remove(number[i])		# turn 1,2,3,5 => 1,2,3,4 #EXCEPTION: NUMBER 1
									number.insert(i, i_rl)		#yeah u know the result => number = [1,2,3]		=DD
							else:
								acti = "none"
								if num_s1 != 1: 		# if the first element of array != 1 #ex: number = [2,4,5,7]
									if i == 0:			# if i = 0 => when number[0] (= 2)
										i_1 = 1 		# i_1 = 1
										acti = "yes"
									elif i == 1:		# if i = 1 => when number[1] (= 4)
										if number[i] - number[i-1] != 1:	# if 4 - 1 != 1
											i_1 = number[i-1] + 1 			# i_1 = 1 + 1
											acti = "yes"
									else:			# if i != 0,1
										if number[i] - number[i-1] != 1: 	# if 5 - 2 != 1 	#other: # if 7 - 3 != 1 
											i_1 = number[i-1] + 1 			# i_1 = 2 + 1 				# i_1 = 3 + 1
											acti = "yes"

									if acti == "yes":
										number.remove(number[i])
										number.insert(i, i_1)
										acti = "none"
								else: 		# if number[0] = 1
									if number[i+1] - number[i] != 1:
										i_l = number[i] + 1
										number.remove(number[i+1])
										number.insert(i+1, i_l)

						for i in range(len(lists_r)):
							decimal1 = lists_r[i].index(".")
							print(decimal1)
							num1 = lists_r[i][decimal1+2:]		# delete the num. (1. or 2. ...)
							print(num1)
							lists_r.remove(lists_r[i])
							lists_r.insert(i, str(number[i]) + ". " + num1)		# add again 1. or 2. ... but with the sorted num
						robot_brain = "Okay, remove sucessfully"

						with open("line.txt","w") as f1:
							f1.write(str(len(lists_r)))

						with open("filetest.txt","w") as f:
							f.write("")

						with open("filetest.txt","a") as f:
							for i in range(len(lists_r)):
								f.write(lists_r[i])
			except ValueError:
				robot_brain = "Cannot remove, Please try again"
			except Exception as e:
				robot_brain = "Unknown error"

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
					robot_brain = "Actually, It is morning now, bro"
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

		elif you == "what is your name" or you == "what your name":
			robot_brain = "Bruh. Obviously, my name is Matthew"

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

		elif "bye" in you:
			if name == "":
				robot_brain = "bye bye"
			elif name == name:
				robot_brain = "bye bye, " + name
			
			window.after(lisp,text_insertyou,"Okay " + robot_brain)		#name != ""

			engine.say("Okay " + robot_brain)
			engine.runAndWait()

			time.sleep(1.5)

			window.destroy()
			sys.exit()

		else:
			robot_brain = "I don't understand."

		print("Robot: " + robot_brain)

		window.after(lisp,text_insertrobot,robot_brain)

		engine.say(robot_brain)
		if "Matthew" in robot_brain and name == "":
			robot_brain = "what about you?"
			window.after(lisp,text_insertrobot,robot_brain)
			engine.say(robot_brain)
		elif "Things you noted:" in robot_brain and note == "activate":
			for i in lists:
				window.after(lisp,text_insertrn,i) # if "you", "i", "mine","yours" use try and except + replace + maybe bool()
				engine.say(i)
			lists = []

		engine.runAndWait()

		robot_brain = ""

		listen()

	def listen():

		global you
		global robot_brain

		with sr.Microphone() as mic:
			ear.adjust_for_ambient_noise(mic)
			print("-------")
			audio = ear.listen(mic)
			try:
				you = ear.recognize_google(audio)
				print("you: " + you)
			except:
				you = "cannot be heard"

		if you == "cannot be heard":
			listen()

		elif "shut down" in you or "shutdown" in you:
			window.after(lisp,text_insertyou, you)
			window.after(lisp,text_insertrobot,"Okay")

			engine.say("Okay")
			engine.runAndWait()

			time.sleep(1.5)

			window.destroy()
			sys.exit()

		elif you == "hey Matthew" or "hey" in you:
			window.after(lisp,text_insertyou,you)
			window.after(lisp,text_insertrobot,"I'm listening.")

			engine.say("I'm listening.")
			engine.runAndWait()
			time.sleep(0.5)
			a_listen()

		else:
			window.after(lisp,text_insertyou,you)
			window.after(lisp,text_insertrobot, "Please say, hey Mathew or hey to activate. ")

			engine.say("Please say, hey Matthew or hey to activate. ")
			engine.runAndWait()

			listen()

			activate = 0

	if activate == 1:
		listen()


def text_insertyou(you):
	text_area.insert(END,"You: {} \n".format(you)) 	#Fix window.after()

def text_insertrobot(rb):
	text_area.insert(END,"Mathew: {} \n".format(rb))

def text_insertrn(rb):
	text_area.insert(END,"{} \n".format(rb))

x = threading.Thread(target= thread, args=(), daemon=True)
x.start()

window = Tk()
window.title("Mathew_AI")
window.resizable(False,False)
window.config(background="#181818")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (1050 / 2))
y = int((screen_height / 2) - (700 / 1.75))

window.geometry(f'{1050}x{700}+{x}+{y}')

canvas = Canvas(window,bg="#181818",width=200,height=110,bd=0)
canvas.place(x= 940,y=7)

label = Label(window, text="Conversation:", font=("Arial", 40,"bold"),bg="#181818",fg="#F5D10D", padx=10, pady=10)
label.place(x= 0, y= 20)

num = 9
for i in range(5):
	rec = canvas.create_rectangle(num, num, 100, 100, fill="#181818", outline="#F5D10D")
	num += 1

txt = canvas.create_text(55, 55, text="AI", font=("Arial", 45,"bold"), fill="#F5D10D")

mathew = Label(window, text="Mathew", font=("Arial", 45, "bold"),bg="#181818",fg="#F5D10D", padx=10, pady=3)
mathew.place(x=700,y=20)

text_area = Text(window,font=("Arial",20),width=45, height=16.5)
text_area.place(x=15, y= 120)

window.mainloop()

# install later REMEMBER TO LINK THE FILE PATH

# Bug: Im listening not show, program closed when else execute,
# future addtion "---waiting for order---", "----LISTENING----"
# Features: Hey, Matthew, let have a talk
# listening none reapeatedly, how to make the GUI responding



# import webbrowser
# import wikipedia
# wolfarm
# storing memory of the specific speech
# tell me a joke
# send message  # check import request
# play music
# automate your house ???!!! # GET THE FOCKING BRIDGE ID
# change robot name option

# tryna findout how they connect to other device