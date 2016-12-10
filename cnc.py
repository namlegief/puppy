import sys
from cnc import menu


def get_user_choice():
    user_choice = raw_input("->:\n")
    print user_choice


def main():
    while True:
        menu.display_main_menu()
        get_user_choice()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as err:
        print ('\nCommand interrupted').format(err.errno, err.strerror)
        sys.exit(err.errno)