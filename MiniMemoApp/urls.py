from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path('', include('MiniMemo.urls')),
    # path('MiniMemo/', include('MiniMemo.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('MiniMemo.urls')), 
]
