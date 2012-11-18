# encoding:utf-8

from django.shortcuts import render_to_response
from models import Forum
from django.core.paginator import Paginator,InvalidPage,EmptyPage
def mk_paginator(request,items,num_items):
    paginator=Paginator(items,num_items)
    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page=1
    try:
        items=paginator.page(page)
    except (InvalidPage,EmptyPage):
        items=paginator.page(paginator.num_pages)
    return items

def main(request):
    forums = Forum.objects.all()
    return render_to_response("forum/list.html", dict(forums=forums, user=request.user))


