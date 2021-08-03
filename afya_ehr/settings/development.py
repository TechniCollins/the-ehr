from .base import *  # noqa: F403

DEBUG_APPS = [
    'debug_toolbar'
]

INSTALLED_APPS += DEBUG_APPS  # noqa: F405

DEVELOPMENT_MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

MIDDLEWARE += DEVELOPMENT_MIDDLEWARE  # noqa: F405

ROOT_URLCONF = 'afya_ehr.urls.development'

# debug toolbar needs this config
INTERNAL_IPS = [
    '127.0.0.1',
]
