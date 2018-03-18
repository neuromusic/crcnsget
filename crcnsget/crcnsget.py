# -*- coding: utf-8 -*-

import requests

URL = 'https://portal.nersc.gov/project/crcns/download/index.php'


def create_payload(username,password,datafile):
    return dict(
        username=username,
        password=password,
        fn=datafile,
        submit='Login'
    )

def get_environ_username():
    return os.environ['CRCNS_USER']

def get_environ_password():
    return os.environ['CRCNS_PASSWORD']

def create_local_filename(dest,datafile):
    if dest is None:
        dest = os.cwd()
    return os.path.join(
        dest,
        datafile.split('/')[-1],
    )

def download(session,request_payload,local_filename):
    r = session.post(URL,data=request_payload,stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return local_filename

def fetch_crcns_datafile(datafile,dest=None,username=None,password=None,chunk_size=1024):

    local_filename = create_local_filename(dest,datafile)

    if username is None:
        username = get_environ_username()
    if password is None:
        password = get_environ_password()

    request_payload = create_payload(
        username,
        password,
        datafile,
    )

    with requests.Session() as s:
        download_file(s,request_payload,local_filename)
