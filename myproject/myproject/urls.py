from django.contrib import admin
from django.urls import path, include
from charts import views  # Import the new view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('charts.urls')),  
    path('', views.home),  
]
