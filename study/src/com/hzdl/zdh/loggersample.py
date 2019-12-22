#coding=utf-8
import logging
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler_warn=logging.FileHandler("warning_log.txt")
handler_warn.setLevel(logging.WARNING)

handler_info=logging.FileHandler("info_log.txt")
handler_info.setLevel(logging.INFO)

formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
handler_warn.setFormatter(formatter)
handler_info.setFormatter(formatter)

logger.addHandler(handler_warn)
logger.addHandler(handler_info)

logger.info("Information")
logger.warning("warning")
logger.debug("debug")