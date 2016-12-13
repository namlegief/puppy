import sys
from cnc import menu
from cnc import router


def get_user_choice(menu_type):
    menu.dislay_menu(menu_type)
    user_choice = raw_input("->:\n")
    new_menu_type = router.process_action(user_choice, menu_type)
    return new_menu_type


def main():
    menu_type = 'main'
    while True:
        menu_type = get_user_choice(menu_type)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as err:
        print ('\nCommand interrupted: {} {}').format(err.errno, err.strerror)
        sys.exit(err.errno)