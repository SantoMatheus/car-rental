from django.urls import path

from car_rental.users.views import LegalRepresentativeRegisterViewSet, CompanyRegisterViewSet, \
    SearchLegalRepresentativeViewSet, SearchCompanyViewSet

app_name = 'users'

urlpatterns = [
    path('users/legalrepresentative/create', LegalRepresentativeRegisterViewSet.as_view(),
         name='legal-representative-register-viewset'),
    path('users/company/create', CompanyRegisterViewSet.as_view(), name='company-register-viewset'),
    path('users/legalrepresentative/search/<str:cpf>', SearchLegalRepresentativeViewSet.as_view(),
         name='search-legal-representative-viewset'),
    path('users/company/search/<str:cnpj>', SearchCompanyViewSet.as_view(), name='search-company-viewset')
]
