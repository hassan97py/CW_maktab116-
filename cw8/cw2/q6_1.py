import argparse

parser = argparse.ArgumentParser(description='A basic command-line argument parser')

parser.add_argument('-filename', type=str,help='The filename to process')
parser.add_argument('-v', '--verbosity',type=int, choices=[0, 1, 2],default=0, help='Increase output verbosity')

args = parser.parse_args()

print(f'Filename: {args.filename}')
print(f'Verbosity level: {args.verbosity}')