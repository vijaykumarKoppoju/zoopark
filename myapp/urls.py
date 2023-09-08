from django.urls import path
from . import views

urlpatterns = [
    path("mainpage",views.mainpage,name="main_page"),
    path("homepage",views.homepage,name="home_page"),
    path('tickets',views.ticketspage,name="tickets_page"),
    path("tickets/payment",views.paymentpage,name="payments_page"),
    path("aboutus",views.aboutpage,name="about_page"),
    path("zoopark/animals",views.animals_page,name="animal_section"),
    path("zoopark/birds",views.bird_page,name="bird_section"),
    path("zoopark/reptiles",views.reptile_page,name="reptile_section"),
    path("zoopark/aquatics",views.aquatic_page,name='aquatic_section'),
    path("zoopark/<slug:name>",views.animal_detail,name="animal_detail")
]
