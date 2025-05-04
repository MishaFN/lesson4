from django.urls import path,include
from .views import newslist,homepage,detail,category,reg,log_in,log_out
urlpatterns=[
    path('',homepage,name='home'),
    path('detail/<int:id>',detail,name='dev'),
    path('category/<int:id>',category,name='category'),
    path('reg/',reg,name='reg'),
    path( 'log/',log_in,name='log'     ),
    path( 'logo/',log_out,name='logo'     )
]