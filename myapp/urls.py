from django.urls import path
from.import views
urlpatterns=[path('pagehtml/',views.pagehtml),
             path('fsave/',views.fsave),
             path('dataread/',views.dataread),
             path('firstpage/',views.firstpage),
             path('form/',views.form),
             ]