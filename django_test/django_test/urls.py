from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

import show.views as showViews

router = DefaultRouter()

router.register('', showViews.ShowViewSet)

urlpatterns = [
    path('', include('login.urls')),
    path('operation/', include(router.urls)),
    path('update/', include('update.urls')),
    path('admin/', admin.site.urls),
]
