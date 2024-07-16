import requests
import certifi

url = 'https://hprera.nic.in/PublicDashboard'
try:
    response = requests.get(url, verify='ISRG Root X1.crt')
    print(response.content)
except requests.exceptions.SSLError as e:
    print("SSL Error:", e)

# soup = BeautifulSoup(response.text, 'html.parser')

# print(response.text)

# registered_projects = soup.find_all('div', class_='your-registered-projects-class')

# # Assuming that the RERA numbers are links that take you to the detail page
# projects = registered_projects.find_all('a', href=True)[:6]

