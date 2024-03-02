
import requests
import json


def main():
        
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=9KsqA7ePdhYEjDC0XdVjP6f9&client_secret=PRPD57cnsbRQD31anQBVrIQhluw1NstJ"
    
    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    

if __name__ == '__main__':
    main()
    
    # 24.6c21532002858e202d2f3fd3a495c4de.2592000.1711961933.282335-54400539