from django.conf.urls import patterns, url

from . import receivers
from .views import ProfileEditView


urlpatterns = patterns("",
    url(r"^profile/edit/", ProfileEditView.as_view(), name="profiles_edit")
)
