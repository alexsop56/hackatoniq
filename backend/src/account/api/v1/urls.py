# account/urls.py

from django.urls import path

from account.api.v1.views import send_code, check_code

urlpatterns = [path('auth/send-code/', send_code, name='send_code'),
    path('auth/check-code/', check_code, name='check_code'), ]
