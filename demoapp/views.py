from django.http import HttpResponse
import logging
from . import tasks

logger = logging.getLogger('normal')

def demo_view(request):
    logger.info('Request received...')
    logger.info('Dispatching async task to celery...')
    tasks.intensive_task.delay()
    logger.info('Returning response...')
    return HttpResponse("This is the demo view!")
