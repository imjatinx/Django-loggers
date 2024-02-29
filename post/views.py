import logging
from django.shortcuts import render

# Get the logger instance configured in your Django settings
logger = logging.getLogger(__name__)

logger.addHandler('file')

def home(request):
    if request.method == 'POST':
        num = request.POST.get('num')
        if num == "1":
            logger.warning("===> Test home function")
        else:
            try:
                div = 4 / int(num)
                logger.info("Division result: %f", div)
            except ZeroDivisionError:
                logger.error("Division by zero occurred.")
                # Optionally, you can re-raise the exception for Django to handle it further.
                raise

    return render(request, 'post/home.html')
