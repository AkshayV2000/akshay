from django.urls import path
from .import views


urlpatterns=[
    path('babtrahome',views.babtrahome,name='home'),
    path('page1',views.page1,name='page1'),
    path('about',views.aboutus,name='aboutus'),
    path ('files',views.files1,name='files'),
    path('doc',views.files2,name='file2condent'),
    path('grid',views.grid1),
    path('flexgrid1',views.flex),
    path('pgnew',views.pgn),
    path('ndiv',views.ned),
    path('baabtrasyte',views.baab),
    path('boot',views.btsp),
    path('gited',views.gitt),
    path('akshay',views,akv),

]