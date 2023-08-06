'''
####       ####	  ######			##	####    ##	 ######	  ###########	    ###			######           ###    ##        ##   ######    ######
#####     #####   ##    ##			##	#####   ##  ##    		  ##          ##  ##	   ##		       ##  ##    ##      ##    ##        ##    #
##	##	 ##  ##   ##    ###	  ###	##	##  ##  ##	 ######	      ##	    ##    ##		######       ##    ##     ##    ##     #####     #######
##	 #####   ##   ##    ## 			##	##   #####        ##	  ##      ##########			 ##    ##########      ##  ##      ##        ##   ##
##	  ###    ##   ######			##	##    ####   ######		  ##	##        ##        ######    ##       ##       ####       ######    ##    ##
'''

from bs4 import BeautifulSoup
from colorama import Fore
import requests
import time
import re

instagram = 'https://www.instagram.com/'

def profile_download(username: str) -> str:
	link = ''
	# like @mahdiedtr
	while link == '':
		print(Fore.YELLOW + '\rProcessing', end='')
		time.sleep(0.2)
		print(Fore.YELLOW+'\rProcessing .', end='')
		time.sleep(0.2)
		print(Fore.YELLOW+'\rProcessing ..', end='')
		time.sleep(0.2)
		print(Fore.YELLOW+'\rProcessing ...', end='')
		try:
			username = username.replace('@', '')
			account_link = f'{instagram + username}'
			response = requests.get(account_link)
			beautiful_response = BeautifulSoup(response.content, 'html.parser')
			bad_links = str(beautiful_response).replace('\\', '')
			links = str(re.findall('profile_pic_url.+', bad_links)).strip("[']")
			print(Fore.GREEN+'\rDONE!', end='')
			link = 'username accepted!'
			profile_link = links.split(',')[0]
			profile = profile_link.split(':"')[1].strip('"')
			return f'\r{profile}'

		except:
			return Fore.RED + f"\rERROR: Invalid Instagram Username!\n{Fore.BLUE+username} {Fore.RED}is not valid!"
