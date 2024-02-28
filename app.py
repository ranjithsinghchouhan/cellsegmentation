from cellSegmentation.custom_logger import logging
from cellSegmentation.exception import AppException
logging.info("welcome to the custom log")
import sys

try:
    a=4/"6"

except Exception as e:
    raise AppException(e,sys)