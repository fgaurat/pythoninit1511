import requests
from bs4 import BeautifulSoup
import glob
import re

def main_download():
    url = 'https://logs.eolem.com/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    links = [link['href'] for link in soup.find_all('a') if link['href'][0] != "?"]
    
    for link in links:
        file_url = f"{url}{link}"
        r = requests.get(file_url)
        with open(link,'w') as f:
            f.write(r.text)



def main():
    log_files = glob.glob("*.log")
    for log_file in log_files:
        with open(log_file) as f:
            for line in f:
                line = line.strip()
                # ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',line)
                m = re.findall(r'^(.+?)\s.*?\"\s(\d{3})',line)
                print(m)
                ip,status = m[0]
                if status =='404':
                    print(ip,status)


def main2():
    l = [(0,1)]
    l = [('157.7.106.165', '200')]
    ip = l[0][0]
    status = l[0][1]


if __name__ == '__main__':
    main()
    # main2()