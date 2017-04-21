from config import config
from logbook import Logger,\
                    FileHandler, \
                    SyslogHandler


def get_debug_logfile(service):
    return config(service)['logging']['log_file']

def setup_logger(service):

    if config(service)['logging']['log_level'] == 'debug':
        log_handler = FileHandler(get_debug_logfile(service))
    else:
        log_handler = SyslogHandler(application_name=service)

    log_handler.push_application()
    log = Logger(service)
    return log
