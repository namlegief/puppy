import json
config_file_path = 'cnc.settings.json'


def get_agent_list_from_config():

    with open(config_file_path, 'r') as conf_file:
        config = json.load(conf_file)

    return config.get('agents')


def display():
    agents = get_agent_list_from_config()
    for agent_name, agent_attribs in agents.iteritems():
        print("agent name: {}. IP: {}".format(str(agent_name),
                                              str(agent_attribs['host'])))
