import os, time, datetime, argparse, sys
import pandas as pd
import subprocess

# List of letters that Monica can't hear
cant_hear = ['s','t','h','c','k','f','g','p',
		'S','T','H','C','K','F','G','P']

def monify(user_text, cant_hear):

	'''
	args:
		user_text: string that is inputted by user
		cant_hear: list of letters that cant be heard

	This function turns the string into a list, iterates through the list 
	and removes any character that monica cant hear and replaces it with a space
	then joins the list and returns a string
	'''

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
	time = str(datetime.datetime.now()).split(' ')[1][:5]

	return '{}_{}'.format(date,time)

def update_data(new_time, new_monified, path='data/speech_banana.csv'):

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

	new_row = pd.Series(data={'text' : new_monified, 'timestamp' : new_time }, name='x')
	new_df = df.append(new_row, ignore_index=False)
	new_df.to_csv('data/speech_banana.csv', index=False)

def make_sexy(text):
	'''
	args: 
		text: the monified text
		
	just prints the text

	'''
	print(text)

def main():

	i =1
	while i != 2: # creating infinite loop 
		subprocess.run('xinput set-prop 12 "Device Enabled" 1', shell=True, check=True)
		print('\n' *20) #number can be changed
		user_input = input('                                                Write your sentence here!\n\n\n')
		subprocess.run('xinput set-prop 12 "Device Enabled" 0', shell=True, check=True)
		n = 0

		# loop to make time look like a robot
		while n != 3: #number = seconds
			print(".")
			#time.sleep(1)
			n += 1

		print("\n")
		monified = monify(user_input, cant_hear)
		make_sexy(monified)
		timestamp = get_time() #yyyy-mm-dd_mm-ss
		update_data(timestamp, monified)
		time.sleep(3)
		os.system('clear') #clears screen

if __name__ == '__main__':
	main()

