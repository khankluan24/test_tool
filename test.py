from bs4 import BeautifulSoup
import requests

insta_link = input("Nhập link insta cần tìm: ")

def sanitize_info(data):
	
	dict = {}
	data = data.split("-")[0]
	data = data.split(" ")
	dict['Followers'] = data[0]
	dict['Following'] = data[2]
	dict['Posts'] = data[4]
	
	return dict

def fetch_info(username):
	
	result = requests.get(insta_link.format(username))
	
	converted_text = BeautifulSoup(result.text, "html.parser")
	
	meta = converted_text.find("meta", property ="og:description")
	
	return sanitize_info(meta.attrs['content'])

if __name__=="__main__":
	
	username = "geeks_for_geeks"
	
	data = fetch_info(username)
	
	print(data)
