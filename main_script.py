import requests
from bs4 import BeautifulSoup

def get_info(collection,number,model):
    response = requests.get(f'https://t.me/nft/{collection}-{str(number)}')
    soup = BeautifulSoup(response.text, 'html.parser')
    list = soup.find('meta', property="og:description").get('content').split('\n')
    print(number) if "Model: " + model in list else None


user_collection = input("Enter your collection: ")
user_model = input("Enter your model: ")

response = requests.get(f'https://t.me/nft/{user_collection}-1')
soup = BeautifulSoup(response.text, 'html.parser')
text = soup.text.replace('\n', '')
arr = list(text[text.find('Quantity'):text.find('/')].replace('Quantity', ''))
if len(arr) > 3:
    arr.pop(-4)
supply = int(''.join(arr))

for i in range(supply):
    get_info(user_collection,i,user_model)