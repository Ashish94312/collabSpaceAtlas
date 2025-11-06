import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'collabSpace.settings')

try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
except Exception as e:
    import logging
    import traceback
    logging.basicConfig(level=logging.ERROR)
    logging.error(f"Error loading Django: {e}")
    logging.error(traceback.format_exc())
    raise
