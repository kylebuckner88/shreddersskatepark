from django.contrib import admin
from django.urls import path
from rest_framework import routers
from shreddersapi.views.trick_type import TrickTypeView
from shreddersapi.views.trick import TrickView
from django.conf.urls import include

router =  routers.DefaultRouter(trailings_slash=False)
router.register(r'tricktypes', TrickTypeView, 'tricktype')
router.register(r'tricks', TrickView, 'trick')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
