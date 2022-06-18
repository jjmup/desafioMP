import requests
import time
if __name__ == '__main__':
 	url = 'https://www.google.com.ar/'
 	response = requests.get(url)

 	print(response)
 	time.sleep(5)