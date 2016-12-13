import tools


def process_action(user_choice, menu_type):

    if user_choice == '1':
        menu_type = show_agents()
    elif user_choice == '2':
        pass
    elif user_choice == '3':
        pass
    else:
        pass

    new_menu_type = menu_type
    return new_menu_type


def show_agents():
    agents = tools.get_agent_list()
    for agent_name, agent_attribs in agents.iteritems():
        print("agent name: {}. IP: {}".format(str(agent_name),
                                              str(agent_attribs['host'])))
    return 'sub'