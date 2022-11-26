from django.urls import path

from . import views


urlpatterns = [
    path('', views.list_biens, name='index'),
    path('inventaire/', views.list_biens1, name='inventaire'),
    # path('liste_vente/', views.list_biens_vente, name='ventebien'),
    # path('location_biens/<slug:category_slug>/', views.list_cat_location, name='locationcatbien'),
    # path('liste_location/', views.list_biens_location, name='locationbien'),
    path('<int:id>/<slug:goods_slug>/', views.immodetail, name='goodsdetails'),
    # path('login/', views.CustomLoginView.as_view(), name='mlogin'),
    # path('logout/', views.logout, name='logout'),
    path('ajoutez_image/', views.addimage, name='ajoutez_image'),
    path('<int:id>/', views.addimage1, name='ajoutezimage'),
    path('client/', views.clientRecord, name='clientrec'),
    path('Alert/', views.alertRecord, name='alertrec'),
    path('Alert/<int:pk>/', views.ClientAlertUpdateView.as_view(), name='alert_update'),
    path('recherche/', views.SearchList, name='recherche'),
    path('alert/', views.newAlert, name='alert'),
    path('alert_liste/', views.Alertlist, name='alertlist'),
    ]