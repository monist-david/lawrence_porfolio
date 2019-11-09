# -*- coding: utf-8 -*-

from django.shortcuts import redirect


# 将localhost：8000 直接连接到home app的页面去
def login_redirect(request):
    return redirect('/porfolio/')
