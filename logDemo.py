import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
logger.addHandler(console)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")
logger.critical("this is your")
logger.fatal("this is a fatal error")
logger.error("this is a error")
try:
    open("text.txt","rb")
except (SystemExit,KeyboardInterrupt):

    raise
except Exception:
    '''logger.error("Faild to open sklearn.txt from logger.error",exc_info = True)'''
    raise