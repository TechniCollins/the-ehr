from .base import *  # noqa: F403
import debug_toolbar

local_urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),  # noqa: F405
]

urlpatterns += local_urlpatterns  # noqa: F405
