from api.url_utils import childs_urls, urls
from extractor.pypfd_extractor import PyPdfExtractor




ext = PyPdfExtractor()
ext.class_alias='Main'
urlpatterns =  urls(ext)

