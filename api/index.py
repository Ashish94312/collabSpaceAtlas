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
    import sys as sys_module
    
    error_msg = f"Error loading Django: {str(e)}\n"
    error_msg += f"Traceback:\n{traceback.format_exc()}\n"
    error_msg += f"Python path: {sys.path}\n"
    error_msg += f"BASE_DIR: {BASE_DIR}\n"
    error_msg += f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE')}\n"
    
    print(error_msg, file=sys_module.stderr)
    raise
