from django.urls import path
from . import views

urlpatterns = [
   path('login_user/',views.login_user,name='login_user'),
   path('logout_user/',views.logout_user,name='logout_user'),
   path('index/',views.index,name='index'),
   path('car_form/',views.car_form,name='car_form'),
   path('cardb/',views.cardb,name='cardb'),
   path('house_form/',views.house_form,name='house_form'),
   path('house_db/',views.house_db,name='house_db'),
   path('wishlist/<id>',views.wishlist,name='wishlist'),
   path('destroy/<id>',views.destroy,name='destroy'),
   path('wishlist1/<id>',views.wishlist1,name='wishlist1'),

]