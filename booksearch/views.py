# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .form import SearchForm

# Create your views here.
def post_list(request):
    return render(request, 'booksearch/post_list.html', {})

def search_box(request):
    return render(request, 'booksearch/search_box.html', {})