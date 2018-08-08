from django.conf.urls import url
from . import views           # This line is new!

# MODIFY THE ROUTES/LOCATIONS BELOW!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add', views.generate),
    # url(r'^reset', views.reset),
]

