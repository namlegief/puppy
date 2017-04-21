import toml


def config(service_name):
    config_file = '../cfg/{}.toml'.format(service_name)

    with open(config_file) as conffile:
        config = toml.loads(conffile.read())

    return config
