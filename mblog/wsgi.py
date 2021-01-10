"""
WSGI config for mblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
"""
是与  虚拟主机中的网页服务器 沟通的接口，，，网站上线会用到此设置
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings')

application = get_wsgi_application()
