from .base import *  # noqa: F403
from django.conf.urls import url

local_urlpatterns = [
    url(r'^silk/', include('silk.urls', namespace='silk'))  # noqa: F405
]

urlpatterns += local_urlpatterns  # noqa: F405
