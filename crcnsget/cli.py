# -*- coding: utf-8 -*-

import click
import crcnsget

@click.command()
@click.option('--username', prompt='Your crcns.org username',
              help='Your crcns.org username.')
@click.option('--password', prompt='Your crcns.org password',
              help='Your crcns.org password.',
              hide_input=True)
@click.option('--dataset', prompt='Path to a crcns.org dataset',
              help='Your crcns.org dataset.')
def main(username,password,dataset):
    """Console script for crcnsget"""
    crcnsget.download(dataset,username,password)

if __name__ == "__main__":
    main()
