from __future__ import unicode_literals

import logging

from celery import task
from celery.signals import task_success

from spider.ghn_spider import GHNSpider
from spider.vnpost_spider import VnpostSpider

# Get an instance of the logger
logger = logging.getLogger("api.activity")


@task()
def task_get_data_from_spider(parcel_id):
    if len(parcel_id) == 13:
        res = VnpostSpider(parcel_id)
    else:
        res = GHNSpider(parcel_id)
    return res.normalize()


@task_success.connect
def task_success_handler(result, *args, **kwargs):
    logger.debug("{} {}".format('task_success', 'task_success'))
    logger.debug("{} {}".format('task_success', result))
