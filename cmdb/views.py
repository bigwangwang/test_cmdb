from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import Form, fields, widgets
from cmdb import models

# Create your views here.

def hosts(request):
    if request.method == "GET":
        host = models.Host.objects.all().order_by('id')
        p = Paginator(host, 3)
        page_num = int(request.GET.get('page', 1))
        try:
            host_list = p.page(page_num)
        except PageNotAnInteger:
            host_list = p.page(1)
        except EmptyPage:
            host_list = p.page(p.num_pages)

    return render(request, 'list.html', locals())