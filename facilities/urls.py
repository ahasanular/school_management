from django.urls import path
from .views import facilityList, facilityDetails, FacilityList, FacilityDetails

urlpatterns = [
    path('', facilityList),
    path('details/<str:id>/', facilityDetails),
    #api
    path('facility_list_api/', FacilityList.as_view()),
    path('facility_details_api/<str:id>/', FacilityDetails.as_view()),
]