import time
import logging

logger = logging.getLogger('django')
class TimerMiddleware:
    def __init__(self, get_response: callable):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        #Before response
        start_time = time.monotonic()
        response = self.get_response(request, *args, **kwargs)  #callae view
        #After response
        end_time = time.monotonic()
        logger.info(f'time:  {end_time - start_time}')
        return response
