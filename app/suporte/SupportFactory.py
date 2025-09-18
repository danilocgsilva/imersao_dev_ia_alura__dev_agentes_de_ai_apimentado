import logging

class SupportFactory:
    @staticmethod
    def getLogger():
        logging.getLogger().setLevel(logging.DEBUG)

        file_handler = logging.FileHandler("app.log")
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        logger = logging.getLogger("agentes ia Alura")
        logger.addHandler(file_handler)
        file_handler.setFormatter(formatter)

        return logger
    