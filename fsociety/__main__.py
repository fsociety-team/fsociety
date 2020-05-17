import argparse

parser = argparse.ArgumentParser(description='A Penetration Testing Framework')
parser.add_argument('-w', '--web', action='store_true', help='start web ui')

args = parser.parse_args()