from .views import bot_view
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', lambda request: HttpResponse("Test URL works!")),
    path('aminointer/', bot_view, name='bot_view'),
    path('', lambda request: HttpResponse("This is an angel of electricity blood getting back to you." "\n Hey, welcome!" " \nCookies?")),
    ]

