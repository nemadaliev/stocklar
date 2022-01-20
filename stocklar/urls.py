from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from stocklar import views
from api import  views as apiView


# router = routers.DefaultRouter()
# router.register(r'users', apiView.UserViewSet)
# router.register(r'groups', apiView.GroupViewSet)


urlpatterns = [

    path('', views.home, name='home'),

    path('companies', views.companies),
    path('admin/', admin.site.urls),

    # path('api/', include(router.urls)),

    path('api/company', apiView.company_info),
    path('api/company/search', apiView.company_search),
    path('api/company/income', apiView.company_income),
    path('api/company/debt', apiView.company_debt),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
