import requests
from bs4 import BeautifulSoup

url = 'https://hprera.nic.in/PublicDashboard'
try:
    response = requests.get(url, verify='combined_cert_chain.pem')
except requests.exceptions.SSLError as e:
    print("SSL Error:", e)

soup = BeautifulSoup(response.text, 'html.parser')

modal_content = soup.find('div', {'id': 'modal-data-preview-content'})
print(modal_content)

name = modal_content.find('span', {'id': 'modal-name-id'}).text.strip()
 pan_no = modal_content.find('span', {'id': 'modal-pan-id'}).text.strip()
gstIn = modal_content.find('span', {'id': 'modal-gst-in'}).text.strip()

print(f"Name: {name}")
 print(f"PAN No: {pan_no}")
print(f"GSTIN: {gstIn}") 
    
else:
print("Modal content not found or request failed.")
