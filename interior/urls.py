"""interior URL Configuration

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
from django.contrib import admin
from django.urls import path, include
import fi.views
from django.conf import settings
from django.conf.urls.static import static
import part.views
import py.views 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',fi.views.home, name="home"),
    path('bed/', part.views.bed, name="bed"),
    path('bath/', part.views.bath, name="bath"),
    path('door/', part.views.door, name="door"),
    path('dressroom/', part.views.dressroom, name="dressroom"),
    path('kitchen/', part.views.kitchen, name="kitchen"),
    path('livingroom/', part.views.livingroom, name="livingroom"),
    path('twenty/', py.views.twenty, name="twenty"),
    path('thirty/', py.views.thirty, name="thirty"),
    path('forty/', py.views.forty, name="forty"),
    path('dressroom/<int:dressroom_id>', part.views.detail, name="detail"),  #드레스룸 디테일
    path('bath/<int:bath_id>', part.views.detail1, name="detail1"), #욕실 디테일
    path('bed/<int:bed_id>', part.views.detail2, name="detail2"), #침실 디테일
    path('door/<int:door_id>', part.views.detail3, name="detail3"), #중문 디테일
    path('kitchen/<int:kitchen_id>', part.views.detail4, name="detail4"), #주방 디테일
    path('livingroom/<int:livingroom_id>', part.views.detail5, name="detail5"), #거실 디테일
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
