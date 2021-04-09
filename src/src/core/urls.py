"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from home.views import index,search,upload,details
from data.views import Insert_Letter,Insert_Recommender,Insert_Statistic,AddLetter

urlpatterns = [
    path('', index, name='index'),
    path('upload', upload, name='upload'),
    path('search/', search, name='search'),
    path('admin/', admin.site.urls),
    path('addletter/', AddLetter,name='add_letter'),
    path('letter/', Insert_Letter,name='insert_letter'),
    path('recommender/', Insert_Recommender,name='insert_recommender'),
    path('statistic/', Insert_Statistic,name='insert_statistic'),
    path('accounts/', include('allauth.urls')),
    path('details/<id>', details, name='details'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
