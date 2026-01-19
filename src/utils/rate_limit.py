import time
from src.config.settings import REQUEST_DELAY

def throttle():
    time.sleep(REQUEST_DELAY)
