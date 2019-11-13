#!/usr/bin/env python3

import argparse
import subprocess
import sys

parser = argparse.ArgumentParser(description='Dump the output of `brew outdatet` to an SQL database.')
parser.add_argument('action', choices=['dump', 'ls'])

args = parser.parse_args()

if args.action == 'dump':
    subprocess.run(['bash', '-c', '''su - user -c "psql -c 'DELETE FROM schema_.packages;'"'''], check=True)
    subprocess.run(['bash', '-c', r"""brew outdatet -1 --versions | awk '{ print "INSERT INTO schema_.packages VALUES ('\\\''"$1"'\\\'', '\\\''"$2"'\\\'');" }' | xargs -I % su - user -c 'psql -c "%"'"""], check=True)
elif args.action == 'ls':
    subprocess.run(['bash', '-c', '''su - user -c "psql -c 'SELECT * from schema_.packages;'"'''], check=True)
