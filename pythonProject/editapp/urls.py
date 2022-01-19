"""editproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from editapp import views

urlpatterns = [
    path('index1',views.my,name='index1'),
    # path('home',views.viewstd,name='home'),
    path('student',views.student,name='student'),
    path('home',views.student,name='home'),
    path('dlt/<int:id>/',views.dlt,name='dlt'),
    path('createstd',views.createstd,name='createstd'),
    path('updatestd/<int:id>/',views.updatestd,name='updatestd'),
    path('viewcls',views.viewcls,name='viewcls'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
