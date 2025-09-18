import logging
import uuid

class SupportFactory:
    @staticmethod
    def getLogger(identificador: str = None):
        if not identificador:
            identificador = str(uuid.uuid4())
        logging.getLogger().setLevel(logging.DEBUG)

        file_handler = logging.FileHandler("app.log")
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        logger = logging.getLogger(identificador)
        logger.addHandler(file_handler)
        file_handler.setFormatter(formatter)

        return logger
    