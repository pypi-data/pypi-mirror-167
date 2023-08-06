import argparse

from . collection import find_unique_elements
from . file_handler import read_file


def parse_args() -> argparse:
    """
    Parse cli arguments with argparse
    :param:
    :return instance of argparse:
    """
    parser = argparse.ArgumentParser(prog='CLI Interface to collection framework',
                                     usage='%(prog)s cli_interface.py \'[-t "string", -f filename]\'',
                                     description='Find unique elements in string or txt file')
    parser.add_argument('-t', '--text',
                        type=str,
                        help='any sequence of chars  with using quotes for example "test text"',
                        default=None)
    parser.add_argument('-f', '--file',
                        type=str,
                        help='path to .txt file',
                        default=None)
    args = parser.parse_args()
    return args


def print_result(qty: int, args_type: str) -> None:
    """Print result of find_unique_elements"""
    print('*' * 50)
    print(f'Unique elements in {args_type}: {qty}')
    print('*' * 50)


def main(text=None, file=None):
    """Main controller"""
    if text is None and file is None:
        print('Nothing to do. Use -h option for help.')

    if text is not None:
        result_text = find_unique_elements(text)
        print_result(result_text, 'string')

    if file is not None:
        try:
            result_data = read_file(file)
            result_file = find_unique_elements(result_data)
            print_result(result_file, 'txt file')
        except FileNotFoundError as e:
            print(f'{e.filename} not found')
        except UnicodeError:
            print(f'{file} is not txt file')


if __name__ == '__main__':
    args = parse_args()
    text = args.text
    file = args.file
    main(text, file)