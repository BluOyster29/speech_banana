import os, time, datetime, argparse, sys
import pandas as pd
import subprocess
from pyfiglet import Figlet
import textwrap
import shutil
import gtts, vlc
from num_cipher import encrypt

f = Figlet(font='big')

# List of letters that Monica can't hear

def gen_banana(cols):
    banana = r'''
     _
    //\
    V  \
     \  \_
      \,'.`-.
       |\ `. `.       
       ( \  `. `-.                        _,.-:\
        \ \   `.  `-._             __..--' ,-';/
         \ `.   `-.   `-..___..---'   _.--' ,'/
          `. `.    `-._        __..--'    ,' /
            `. `-_     ``--..''       _.-' ,'
              `-_ `-.___        __,--'   ,'
                 `-.__  `----"""    __.-'
                      `--..____..--'
    '''

    lines = banana.splitlines()
    banana = padRight(lines)
    banana = padToCenter(banana, cols)

    return banana

def padRight(l:list)->list:
    maxLength = max(len(x) for x in l)
    return [ x.ljust(maxLength) for x in l]

def padToCenter(l:list,w:int)->str:
    """Manual centering"""
    padding =  ' '*(w//2) # a 1 char line would need at most w/2 spaces in front
    parts = [ padding[0: (w-len(p))//2+1]+p for p in l]
    return '\n'.join(parts)

def padToCenter2(l:list,w:int)->str:
    return '\n'.join('-'+x.center(w)+'-' for x in l)

def monify(user_text):

	'''
	args:
		user_text: string that is inputted by user
		cant_hear: list of letters that cant be heard

	This function turns the string into a list, iterates through the list 
	and removes any character that monica cant hear and replaces it with a space
	then joins the list and returns a string
	'''
	cant_hear = ['s','t','h','c','k','f','g','p',
		'S','T','H','C','K','F','G','P']

	text_list = [i for i in user_text]
	new_list = []
	for i in text_list:
		if i in cant_hear:
			new_list.append(' ')
		else:
			new_list.append(i)	
	return "".join(new_list)

def get_time():

	'''
	Function that just returns the datetime in a nice format for saving
	'''

	date = str(datetime.datetime.now()).split(' ')[0]
	time = '_'.join(str(datetime.datetime.now()).split(' ')[1][:5].split(':'))

	return '{}_{}'.format(date,time)

def update_data(new_time, new_monified, encrypted, path='data/speech_banana.csv'):

	'''
		args:
			new_time: timestamp from when user used program
			new_monified: monified input
			path: path to the csv file where text is saved - no need to change

	This function updates the data file, and if the file doesn't exist it creates a new one
	'''

	try:
		df = pd.read_csv(path)
		
	except:
		df = pd.DataFrame(data={'text' : [], 'timestamp' : []})

	new_row = pd.Series(data={'text' : new_monified, 'timestamp' : new_time ,'ecnrypted_input' : encrypted}, name='x')
	new_df = df.append(new_row, ignore_index=False)
	new_df.to_csv('data/speech_banana.csv', index=False)

def make_sexy(text, cols, height):
	'''
	args: 
		text: the monified text
		
	just prints the text

	'''
	print(text.center(cols))
	
	for i in range(7):
		print('.'.center(cols))

		time.sleep(0.7)
	time.sleep(1.5)

def main():
	cols, rows, = get_dims()
	
	banana = gen_banana(cols)

	i =1
	
	while i != 2: # creating infinite loop 
		print(banana)

		subprocess.run('xinput set-prop 11 "Device Enabled" 1', shell=True, check=True)
		print('\n'*3)
		text = 'Type your sentence below!'
		print('{}Hello!\n{}Do you want to see how I hear?'.format(' '*(int(cols/2-(6 /2))), ' '*(int(cols/2-(29 /2)))))		
		user_input = input('{}{}\n\n\n{}'.format(' '*(int(cols/2- (len(text)/ 2))), text,' '*(int(cols/4))).center(int(cols/4)))
		if user_input == 'quit this fucker':
			exit(0)
		
		subprocess.run('xinput set-prop 11 "Device Enabled" 0', shell=True, check=True)
		n = 0

		# loop to make time look like a robot
		while n != 5: #number = seconds
			print(".".center(cols))
			time.sleep(0.5)
			n += 1

		print("\n")
		timestamp = get_time()#yyyy-mm-dd_mm-ss
		#audio_path = 'data/audio/{}.mp3'.format(timestamp)

		monified = monify(user_input)
		#monified_audio = gtts.gTTS(monified)
		#monified_audio.save(audio_path)
		#p = vlc.MediaPlayer(audio_path)
		#p.play()
		make_sexy(monified, cols,rows)
		encrypted_input = encrypt(user_input)
		update_data(timestamp, monified, encrypted_input)
		os.system('clear') #clears screen

def get_dims():

	cols, rows = shutil.get_terminal_size()
	return cols, rows

if __name__ == '__main__':
	
	while 1 != 2:
		try:
		
			main()
		except KeyboardInterrupt:
			continue
	
