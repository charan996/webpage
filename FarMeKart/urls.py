from django.urls import path
from FarMeKart import views
from django.contrib.auth import views as ad

urlpatterns = [
    path('',views.home,name="hm"),
    path('lg/',ad.LoginView.as_view(template_name="html/login.html"),name="lgo"),
    path('reg/',views.registration,name="rg"),
    path('lgo/',ad.LogoutView.as_view(template_name='html/logout.html'),name="logo"),
    path('ch/',views.cgf,name="cg"),
    path('pro/',views.profile,name="pf"),
    path('upr/',views.updprofile,name="upf"),
    path('ds/',views.dashboard,name="dsh"),
    path('dsf/',views.farmerdashboard,name="fdsh"),
    path('cn/',views.contact,name="ct"),
    path('ab/',views.about,name="au"),
    path('dt/',views.vegf,name="da"),
    path('infodelete/<int:et>',views.infodelete,name='infodelete'),
    path('ed/<int:y>/',views.itemupdate,name="ue"),
    path('ct/',views.cart,name="ca"),
    path('us/',views.usr,name="cb")
]