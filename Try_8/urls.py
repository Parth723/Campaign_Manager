from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Campaign Admin"
admin.site.site_title = "Campaign Admin Portal"
admin.site.index_title = "Welcome to Campaign Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]
