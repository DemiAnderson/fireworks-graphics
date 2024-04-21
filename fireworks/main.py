import argparse

from game import Game

def parse_args():
    parser = argparse.ArgumentParser(description='Fireworks demo animation')
    parser.add_argument('--sparks-amount-range', '-s', type=str, default='20-30',
                        help='Range of sparks amount in format MIN-MAX. Default is 20-30.')
    args = parser.parse_args()

    sparks_amount_range = tuple(map(int, args.sparks_amount_range.split('-')))
    if len(sparks_amount_range) != 2 or sparks_amount_range[0] > sparks_amount_range[1]:
        raise ValueError('Invalid format for --sparks-amount-range argument. Use MIN-MAX format.')

    return sparks_amount_range

if __name__ == '__main__':
    application = Game(parse_args())
    application.run()
