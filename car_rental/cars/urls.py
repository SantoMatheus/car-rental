from django.urls import path

from car_rental.cars.views import CarRegisterViewSet, CategorieRegisterViewSet, CategorieEditViewSet, \
    GetCategorieViewSet, GetCarViewSet

app_name = 'cars'

urlpatterns = [
    path('cars/register', CarRegisterViewSet.as_view(), name='car-register-viewset'),
    path('cars/categorie-register', CategorieRegisterViewSet.as_view(), name='categorie-register-viewset'),
    path('cars/categorie-edit/<str:id_categorie>', CategorieEditViewSet.as_view(), name='categorie-edit-viewset'),
    path('cars/get-categorie/CarCategorie', GetCategorieViewSet.as_view(), name='get-categorie-viewset'),
    path('cars/get-car/<str:car_plate>', GetCarViewSet.as_view(), name='get-car-viewset'),
]
