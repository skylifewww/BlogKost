from django.conf.urls import url
import loginsys.views

urlpatterns = [
    url(r'^register/', loginsys.views.register),
    url(r'^login/', loginsys.views.login),
    url(r'^logout/', loginsys.views.logout),
    url(r'^', include('social.apps.django_app.urls', namespace='social')),

]
