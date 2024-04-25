from celery import shared_task
from time import sleep
import logging

logger = logging.getLogger('normal')

@shared_task
def intensive_task():
    logger.info('Performing intensive task...')    
    sleep(10)
    logger.info('Intensive task completed...')    
