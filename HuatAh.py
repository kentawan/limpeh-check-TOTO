import argparse
parser = argparse.ArgumentParser(description='You can win TOTO!')
parser.add_argument(
    '--my_buy',
    type=str,
    dest='my_buy',
    default="1,2,3,4,5,6",
    help='provide a list (default: (1,2,3,4,5,6))')
parser.add_argument(
    '--my_result',
    dest='my_result',
    type=str,
    default="1,2,3,4,5,6",
    help='provide a list (default: (1,2,3,4,5,6))')

args = parser.parse_args()
buy = args.my_buy
result = args.my_result

huat = (buy == result)

if huat is True:
    print("Huat Ah!")
else:
    print("Too bad!")
