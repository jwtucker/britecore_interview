from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from britecore import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),

    path('api/get_all_risk_types/', views.get_all_risk_types),
    path('api/get_risk_type/', views.get_risk_type),
]
