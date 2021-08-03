from django.contrib import admin
from django.urls import path, include, re_path
from newsletter.views import mailingList


# If no API version is specified, we will return rendered HTML pages instead
# of JSON response
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^$', mailingList, name="mailing-list"),
]
