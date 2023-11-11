# -*- coding: utf-8 -*-

import requests
from tqdm import tqdm

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
        total_size = int(r.headers.get('Content-Length', 0))

        with open(local_filename, 'wb') as f, tqdm(
                desc=local_filename,
                total=total_size,
                unit='B',
                unit_scale=True,
                unit_divisor=1024) as bar:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    bar.update(len(chunk))
        print(f"{local_filename} downloaded successfully.")
