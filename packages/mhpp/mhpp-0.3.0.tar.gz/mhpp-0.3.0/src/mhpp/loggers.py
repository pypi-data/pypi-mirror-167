import logging

def get_level(level):
    if level=="DEBUG":
        return logging.DEBUG 
    elif level == "INFO":
        return logging.INFO 
    elif level == "WARNING":
        return logging.WARNING
    elif level == "ERROR":
        return logging.ERROR
    elif level == "CRITICAL":
        return logging.CRITICAL
    return None

def loggerWrapper(level= "DEBUG", log_path=None, no_console_log=False):
    # Create a custom logger
    logging.basicConfig(level=get_level(level), format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    if no_console_log:
        logger.propagate=False
    
    if log_path:
        # Handling adding loggers to file
        f_handler = logging.FileHandler(log_path)
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)

    
    return logger
