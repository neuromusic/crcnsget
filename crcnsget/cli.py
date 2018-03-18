# -*- coding: utf-8 -*-

import click
from .crcnsget import fetch_crcns_datafile

@click.command()
@click.option('--username', prompt='Your crcns.org username',
              help='Your crcns.org username.', default=None)
@click.option('--password', prompt='Your crcns.org password',
              help='Your crcns.org password.',
              hide_input=True, default=None)
@click.option('--dataset', prompt='Path to a crcns.org dataset',
              help='Your crcns.org dataset.')
def main(username,password,dataset):
    """Console script for crcnsget"""
    fetch_crcns_datafile(dataset,username,password)

if __name__ == "__main__":
    main()
