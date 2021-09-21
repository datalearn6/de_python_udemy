"""Running the Xetra ETL application"""
import logging
import logging.config
import yaml



def main():
    """
    entry point to run the job
    """
    #PArsing YANML file
    config_path = 'C:/dev/ws/python/de_python_udemy/configs/report1_config.yml'
    config = yaml.safe_load(open(config_path))
    print(config)
    # Configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info("This is a test.")


if __name__ == '__main__':
    main()