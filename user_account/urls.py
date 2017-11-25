# -*- coding: utf-8 -*-
from django.conf.urls import url
from user_account import views as user_sign_up

urlpatterns = [
                url('^signup$', user_sign_up.signup, name='signup')
]
