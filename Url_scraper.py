import requests
from bs4 import BeautifulSoup
import pandas as pd
from requests.exceptions import RequestException, HTTPError, Timeout
import time
import re





headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}



email_regex = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
phone_regex = re.compile(r"\+?\d{1,3}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}")


with open('path to txt file', 'r') as file:
    urls = set(line.strip() for line in file)

df = pd.DataFrame(columns=['Website', 'Seitentitel', 'E-mail', 'Telefonnummer'])

start_time = time.time()  

for url in urls:
    url_start_time = time.time()

    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()

        
        if 'text/html' in response.headers.get('Content-Type', ''):
            soup = BeautifulSoup(response.text, 'lxml-xml')

            emails = email_regex.findall(soup.text)
            phones = phone_regex.findall(soup.text)

            email = emails[0] if emails else ''
            phone = phones[0] if phones else ''

            
            parts = url.split('//')[-1].split('.')
            name = parts[1] if parts[0] == 'www' else parts[0]

        else:
            continue  

    except Timeout:
        print(f"Processing of {url} timed out.")
        continue  
    except (HTTPError, RequestException) as e:
        name = email = phone = f'Error: {e}'


    new_row = pd.DataFrame({'Website': [url], 'Seitentitel': [name], 'E-mail': [email], 'Telefonnummer': [phone]})
    df = pd.concat([df, new_row], ignore_index=True)

    elapsed_time = time.time() - url_start_time
    print(f"Processed {url} in {elapsed_time:.2f} seconds.")

total_elapsed_time = time.time() - start_time
print(f"Total time taken: {total_elapsed_time:.2f} seconds.")


kategorie_value = "Kategorie_value"
df['Kategorie'] = kategorie_value


column_order = ['Kategorie'] + [col for col in df.columns if col != 'Kategorie']
df = df[column_order]



for column in df.columns:
    df = df[~df[column].astype(str).str.contains('Error', na=False)]
sequences = ['amazon', '.de', 'locaverse', 'wiki', 'wifiwien', 'xing', 
             'instagram', 'facebook', 'ausbildung', 'webdesign', 'wko', 
             'workinaustria', 'ams', 'karriere', 'willhaben', 'pdf', 
             'herold', 'linkedin', 'statista']


regex_pattern = '|'.join(sequences)

filtered_df = df[~df['Website'].str.contains(regex_pattern, case=False, na=False)]
filtered_df = filtered_df.dropna(subset=['Telefonnummer', 'E-mail'], how='all')


csv_filename = f"{kategorie_value}.csv"
filtered_df.to_csv(csv_filename, index=False)

print(filtered_df)