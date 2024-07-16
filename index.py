import requests
from bs4 import BeautifulSoup

url = 'https://hprera.nic.in/PublicDashboard'
try:
    response = requests.get(url, verify='combined_cert_chain.pem')
except requests.exceptions.SSLError as e:
    print("SSL Error:", e)

soup = BeautifulSoup(response.text, 'html.parser')

# Extract information from the modal content
modal_content = soup.find('div', {'id': 'modal-data-preview-content'})
print(modal_content)

# if modal_content:
#     # Assuming the modal content has details like name, PAN number, etc.
#     name = modal_content.find('span', {'id': 'modal-name-id'}).text.strip()
#     pan_no = modal_content.find('span', {'id': 'modal-pan-id'}).text.strip()
#     # Add more fields as needed

#     # Print or process the extracted data
#     print(f"Name: {name}")
#     print(f"PAN No: {pan_no}")
#     # Print or process other fields
    
# else:
#     print("Modal content not found or request failed.")
