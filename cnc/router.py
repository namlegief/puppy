import tasks


def process_action(user_choice, menu_type, command = None):

    if menu_type == 'main':
        if user_choice == '1':
            tasks.agents_list.display()
            next_menu_type = 'main'
            return next_menu_type
        elif user_choice == '2':
            print("\nPlease choose client, for all clients enter 0")
            tasks.agents_list.display()
            next_menu_type = 'ag_list'
            return next_menu_type ,


    elif menu_type == 'ag_list':
        if user_choice == '0':
            print("Called all clients command = {}".format(command))

