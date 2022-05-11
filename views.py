from base64 import decode
from cgitb import html
from urllib import response
from django.shortcuts import render
from django.http import HttpRequest

def home_page(self):
    html = response.content.decode('utf8') 
    return html