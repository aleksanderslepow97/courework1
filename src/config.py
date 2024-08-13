import logging


def set_logger(name: str, log_file: str) -> logging.Logger:
    """Логер, включающий время,название модуля,
    уровень серьезности и сообщения,
    описывающие события или ошибки, которые произошли"""
    logger = logging.getLogger(name)
    file_handler = logging.FileHandler(log_file)
    file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    return logger
