from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('patients/', views.patients_index, name='patients_index'),
    path('patients/<int:patient_id>/', views.patients_detail, name='patients_detail'),
    path('patients/create/', views.PatientsCreate.as_view(), name='patients_create'),
    path('patients/<int:pk>/update/', views.PatientsUpdate.as_view(), name='patients_update'),
    path('patients/<int:pk>/delete/', views.PatientsDelete.as_view(), name='patients_delete'),
    path('patients/<int:patient_id>/add_prescriptionsGiven/', views.add_prescriptionsGiven, name='add_prescriptionsGiven'),
    path('prescription/create/', views.PrescriptionsCreate.as_view(), name='prescriptions_create'),
    path('prescriptions/', views.PrescriptionsIndex.as_view(), name='prescriptions_index'),
    path('prescriptions/<int:pk>/', views.PrescriptionsDetail.as_view(), name='prescriptions_detail'),
    path('prescriptions/<int:pk>/update/', views.PrescriptionsUpdate.as_view(), name='prescriptions_update'),
    path('prescriptions/<int:pk>/delete/', views.PrescriptionsDelete.as_view(), name='prescriptions_delete'),
    path('patients/<int:patient_id>/assoc_prescription/<int:prescription_id>/', views.assoc_prescription, name='assoc_prescription'),
    path('patients/<int:patient_id>/remove_prescription/<int:prescription_id>/', views.remove_prescription, name='remove_prescription'),
    path('patients/<int:patient_id>/add_photo/', views.add_photo, name='add_photo'),
    path('patients/<int:patient_id>/delete_photo/<int:pk>/', views.PhotoDelete.as_view(), name='delete_photo'),
    path('accounts/signup/', views.signup, name='signup'),
]