import logging
#import FileHandler

class LogGen:
    @staticmethod
    def log():
        ''' logging.basicConfig(filename=".//Logs//automation12.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',)
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        return logger
        '''

        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler(".//Logs//automation.log")

        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger








