from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    # path('', include('MiniMemo.urls')),
    # path('MiniMemo/', include('MiniMemo.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('MiniMemo.urls')), 
    path('', TemplateView.as_view(template_name='index.html'))
]
