import logging


logger = logging.getLogger()
_handler = logging.StreamHandler()
_formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
_handler.setFormatter(_formatter)
logger.addHandler(_handler)
logger.setLevel(logging.DEBUG)
