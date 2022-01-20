from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.myfun,name='myfun'),

    path('/abouts/',views.abouts,name='abouts'),
    path('/home/',views.home,name='home'),
    path('/contact/',views.contact,name='contact'),
    
    
    path('/air/',views.air,name='air'),
    path('/all/',views.all,name='all'),
    path('/fashion/',views.fashion,name='fashion'),
    path('/beauty',views.beauty,name='beauty'),
    path('/bike/',views.bike,name='bike'),
    path('/camera/',views.camera,name='camera'),
    path('/car/',views.car,name='car'),
    path('/car1/',views.car1,name='car1'),
    path('/contact1/',views.contact1,name='contact1'),
    path('/electronics/',views.electronics,name='electronics'),
    path('/furniture/',views.furniture,name='furniture'),
    path('/furniture1/',views.furniture1,name='furniture1'),
    path('/furniture2/',views.furniture2,name='furniture2'),
    path('/gallery/',views.gallery,name='gallery'),
    path('/headphone/',views.headphone,name='headphone'),
    path('/kids/',views.kids,name='kids'),
    path('/laptop/',views.laptop,name='laptop'),
    path('/mobile/',views.mobile,name='mobile'),
    path('/mens/',views.mens,name='mens'),
    path('/shoes/',views.shoes,name='shoes'),
    

    path('/toys/',views.toys,name='toys'),
    path('/tv/',views.tv,name='tv'),
    path('/vaccum/',views.vaccum,name='vaccum'),
    path('/washing/',views.washing,name='washing'),
    path('/watch/',views.watch,name='watch'),
    path('/womens/',views.womens,name='womens'),
    path('/intro/',views.intro,name='intro'),
    path('/cycle/',views.cycle,name='cycle'),
    path('/top/',views.top,name='top'),
    path('/popular/',views.popular,name='popular'),
    path('signup',views.handleSignUp,name='handleSignUp'),
    path('/login/', views.handeLogin, name='handleLogin'),
    path('/logout/', views.handelLogout, name='handleLogout'),
    path('/search/', views.search, name='search'),
    path('/checkout/', views.checkout, name='checkout')
]

