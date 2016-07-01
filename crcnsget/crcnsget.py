# -*- coding: utf-8 -*-

import requests

URL = 'https://portal.nersc.gov/project/crcns/download/index.php'

def download(datafile,username,password):

    login_data = dict(
        username=username,
        password=password,
        fn=datafile,
        submit='Login' 
        )

    with requests.Session() as s:
        local_filename = login_data['fn'].split('/')[-1]
        r = s.post(URL,data=login_data,stream=True)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print local_filename