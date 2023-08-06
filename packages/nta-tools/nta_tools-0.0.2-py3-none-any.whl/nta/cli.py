import sys
import argparse

from data import get_all_feature_type


def main(*argv):
    if not argv:
        argv = list(sys.argv)

    parser = argparse.ArgumentParser()

    # input_parser = parser.add_mutually_exclusive_group()
    parser.add_argument('-i', '--input', metavar='<input_path>',
                        help='Set the capture file or directory to read from')
    parser.add_argument('-o', '--output', metavar='<output_path>',
                        help='Manually specify output directory')
    parser.add_argument('-e', '--extract', metavar='<feature_type>',
                        choices=get_all_feature_type(),
                        help='Extracts the specified feature type from the capture file')
    parser.add_argument('-f', '--format', metavar='<output_format>',
                        choices=['auto', 'json', 'csv', 'pickle', 'numpy', 'png'], default='auto',
                        help='Set the output format')

    args = parser.parse_args(argv[1:])

    if not args.extract:
        print("ValueError: Invalid feature type: {}.".format(args.extract),
              "\n\nTips: You need to specify '-e <feature_type>'.\n")
        exit(1)


if __name__ == '__main__':
    main(*sys.argv)
