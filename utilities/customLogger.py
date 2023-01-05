import logging

class LogGen():
    @staticmethod
    def logGen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%y %I:%M:%S %p',
                            level=logging.INFO
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger