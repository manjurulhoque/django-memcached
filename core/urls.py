from django.conf import settings
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', author_page_view),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
