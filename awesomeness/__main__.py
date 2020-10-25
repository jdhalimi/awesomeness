from argparse import ArgumentParser
from awesomeness import __version__


def main():
    """
    command line interface entry point
    """
    parser = ArgumentParser('awesomeness',
                            description=f'awesomeness version {__version__}')
    parser.add_argument('--version', action='version',
                        version=__version__)
    parser.parse_args()


if __name__ == '__main__':
    main()
