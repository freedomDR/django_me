from django.conf import settings
from apscheduler.schedulers.gevent import GeventScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import subprocess, sys, os
import django
sys.path.append('me')
os.environ['DJANGO_SETTINGS_MODULE'] = 'me.settings'
django.setup()

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

