from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from django.core.cache import caches

# cache = caches['default']  # `default` is a key from CACHES dict in settings.py
# cache.clear()


@cache_page(600, cache='default', key_prefix='')
def author_page_view(request):
    users = User.objects.all()
    print(users)
    return render(request, 'users.html', {'users': users})
