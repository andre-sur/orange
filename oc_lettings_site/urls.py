"""OLD VERSION
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', views.lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', views.letting, name='letting'),
    path('profiles/', views.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', views.profile, name='profile'),
    path('admin/', admin.site.urls),
]
"""

from django.contrib import admin
from django.urls import path, include
from . import views
from django.http import HttpResponseServerError


def trigger_error(request):
    division_by_zero = 1 / 0  # provoque une erreur volontaire
    return HttpResponseServerError("This should never be seen.")


urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("admin/", admin.site.urls),
    path("force500/", views.error_500_view),
    path("sentry-debug/", trigger_error, name="sentry-debug"),
]
