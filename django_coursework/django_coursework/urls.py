from django.contrib import admin
from django.urls import path,include
from .views import *




urlpatterns = [
    path('admin/', admin.site.urls),
    

]

urlpatterns += [
    path('app/',include('app.urls'))

]

