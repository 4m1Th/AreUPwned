import requests
import json
from emailfinder.extractor import *

# Email gathering from Google and Bing
domain = input("Enter the domain:")
emails1 = get_emails_from_google(domain)
emails2 = get_emails_from_bing(domain)

# Eleminating duplicates
em_1 = set(emails1)
em_2 = set(emails2)
em_3 = em_2 - em_1

# Merging
result = emails1 + list(em_3)

headers = {
    'Accept-Language': 'en-US,en;q=0.5',
    'If-Modified-Since': 'Wed, 05 Jan 2022 06:20:11 GMT',
    'Referer': 'https://haveibeenpwned.com/',
    'Request-Context': 'appId=cid-v1:bcc569a3-d364-4306-8bbe-83e9fe4d020e',
    'Request-Id': '|U1ime.Vdr+K',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Te': 'traillers',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0',
}

#Using HaveIBeenPwned to check the mail address breach
for mail in result:
    response = requests.get(
        f'https://haveibeenpwned.com/unifiedsearch/{mail}',
        headers=headers)
    if response.status_code == 200:
        print('\n')
        print(f'Mail: {mail}')
        res = json.loads(response.text)
        #Filtering the data
        data = [breach['Name'] for breach in res["Breaches"]]
        for dat in data:
            print(dat)
    else:
        pass
