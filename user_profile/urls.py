"""user_profile URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
import map.views as map_view
import user_details.views as user_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', map_view.map_view, name='map'),
    path('signup/', user_details.signup_view, name='signup'),
    path('view_profile/', user_details.view_profile_view, name='view_profile'),
    path('edit_profile/', user_details.edit_profile_view, name='edit_profile'),

    # auth views
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='map'), name='logout'),

]
