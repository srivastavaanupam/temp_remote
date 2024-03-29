"""templateinhepro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from templateinheapp import views
from django.conf.urls import url

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home_page_view),
    url(r'^home/',views.home_page_view),
    url(r'^contact/',views.contact_page_view),
    url(r'^services/',views.services_page_view),
    url(r'^feedback',views.feedback_page_view)
]
