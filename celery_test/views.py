from django.shortcuts import render
from django.http import HttpResponse
from .tasks import celery_send_email

# Create your views here.

def add_task_to_celery(request):
    celery_send_email.delay(u'邮件主题','test_mail_message','1054756646@qq.com',
                            ['1054756646@qq.com'])
    return HttpResponse('hello world')
