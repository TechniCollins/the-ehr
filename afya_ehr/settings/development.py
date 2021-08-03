from .base import *  # noqa: F403

DEBUG_APPS = [
    'silk'
]

INSTALLED_APPS += DEBUG_APPS  # noqa: F405

DEVELOPMENT_MIDDLEWARE = [
    'silk.middleware.SilkyMiddleware',
]

MIDDLEWARE += DEVELOPMENT_MIDDLEWARE  # noqa: F405

ROOT_URLCONF = 'afya_ehr.urls.development'
