import json
config_file_path = 'cnc.settings.json'


def get_bind_settings():

    with open(config_file_path, 'r') as conf_file:
        config = json.load(conf_file)

    return {
            'cnc_host': config.get('cnc').get('listen_host'),
            'cnc_port': config.get('cnc').get('listen_port'),
            'cnc_if_name': str(config.get('cnc').get('cnc_if_name')),
            }


def get_agent_list():

    with open(config_file_path, 'r') as conf_file:
        config = json.load(conf_file)

    return config.get('agents')