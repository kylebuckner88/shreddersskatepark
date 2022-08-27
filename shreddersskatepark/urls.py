from django.contrib import admin
from django.urls import path
from rest_framework import routers
from shreddersapi.views.trick_type import TrickTypeView
from shreddersapi.views.trick import TrickView
from django.conf.urls import include
from shreddersapi.views import register_user, login_user

router =  routers.DefaultRouter(trailing_slash=False)
router.register(r'tricktypes', TrickTypeView, 'tricktype')
router.register(r'tricks', TrickView, 'trick')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user)

]
