from django.urls import path
from api.views  import  PdfAPI

def childs_urls(tree, base:list = [], base_path = ''):
    url = base_path + tree.alias + '/'
    base.append(path(url, PdfAPI.as_view(extractor = tree, name = tree.alias.title())))
    for x in tree.childs:
        urls(x,base,url)
    return base

def urls(tree):
    paths = [path('', PdfAPI.as_view(extractor = tree, name = tree.alias.title()))]
    for x in tree.childs:
        paths.extend(childs_url(x))
    return paths
