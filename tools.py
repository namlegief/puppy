import json

config_file_path = 'settings.json'


def parse_config():

    with open(config_file_path, 'r') as conf_file:
        config = json.load(conf_file)

    agent_host = config.get('agent').get('listen_host')
    agent_port = config.get('agent').get('listen_port')

    cnc_host = config.get('cnc').get('listen_host')
    cnc_port = config.get('cnc').get('listen_port')

    return {'agent_host': agent_host,
            'agent_port': agent_port,
            'cnc_host': cnc_host,
            'cnc_port': cnc_port,
            }