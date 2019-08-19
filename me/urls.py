"""me URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apscheduler.schedulers.gevent import GeventScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import subprocess, sys

urlpatterns = [
    path('', include('info.urls')),
    path('info/', include('info.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^pages/', include(wagtail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


print(settings.BASE_DIR)

def spider():
    subprocess.Popen(settings.BASE_DIR + '/scrapy_start.sh', shell=True, stdout=sys.stdout)

scheduler = BackgroundScheduler()
scheduler.add_job(spider, 'interval', seconds=60*60*1)
try:
    spider()
    p = scheduler.start()
except (KeyboardInterrupt, SystemExit):
    print('apscheduler exit')
    scheduler.shutdown()
