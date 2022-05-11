from django.views import TestCase
from django.views import resolve
from django.views import home_page

class HomePage():
    def url_resolve():
        found = resolve("/")