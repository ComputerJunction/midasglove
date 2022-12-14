"""institutional URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path

from . import views

urlpatterns = [

    path('', views.landing, name='landing'),

    path('cik/', views.cik.as_view(), name='cik'),

    path('cik/<int:id>', views.cik_single.as_view(), name='cik_single'),

    path('investor', views.investor.as_view(), name='investor'),

    path('investor/<int:id>', views.form_entries.as_view(), name='form_entries'),

    path('industry/', views.industry.as_view(), name='industry'),

    path('industry/<int:id>', views.industry_single.as_view(), name='industry_single'),

    path('sicnaics/', views.sic_naics.as_view(), name='sic_naics'),

    path('apple/', views.apple, name='apple'),

    path('micro/', views.micro, name='micro'),

    path('nums/', views.nums.as_view(), name='nums')

]