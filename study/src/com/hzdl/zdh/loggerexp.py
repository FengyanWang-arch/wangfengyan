#coding=utf-8
import logging
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler=logging.FileHandler('exp_critical.txt')
handler.setLevel(logging.DEBUG)

formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

def age():
    logger.info("Inside function age()")
    
    try:
        logger.info("In the try block")
        age=int(input("请输入你当前的年龄："))
        logger.debug("Value of age is %s"%age)
        
    except ValueError as e:
        logger.critical('Invalid Input',exc_info=True)
        
if __name__=="__main__":
    age()