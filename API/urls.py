from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.patient, name='patient'),

    path('api/record1/', views.careplan1,  name='careplan1'),

    path('api/record2/', views.careplan2,  name='careplan2'),

    path('api/record3/', views.careplan3,  name='careplan3'),

    path('api/record4/', views.careplan4,  name='careplan4'),

    path('api/record5/', views.careplan5,  name='careplan5'),

    path('api/record6/', views.careplan6,  name='careplan6'),

    path('api/record7/', views.careplan7,  name='careplan7'),

    path('api/record8/', views.careplan8,  name='careplan8'),

    path('api/record9/', views.careplan9,  name='careplan9'),

    path('api/record10/', views.careplan10,  name='careplan10'),

    path('api/record11/', views.careplan11,  name='careplan11'),

    path('api/record12/', views.careplan12,  name='careplan12'),

    path('api/esporta_csv/', views.esporta_csv, name='esporta_csv'),

    path('api/record1/esporta_csv2/', views.esporta_csv2, name='esporta_csv2'),

    path('api/record1/esporta_csv3/', views.esporta_csv3, name='esporta_csv3'),

    path('api/record2/esporta_csv2/', views.esporta_csv2, name='esporta_csv2'),

    path('api/record2/esporta_csv3/', views.esporta_csv3, name='esporta_csv3'),

    path('api/record3/esporta_csv2/', views.esporta_csv2, name='esporta_csv2'),

    path('api/record3/esporta_csv3/', views.esporta_csv3, name='esporta_csv3'),

    path('api/record4/esporta_csv2/', views.esporta_csv2, name='esporta_csv2'),

    path('api/record4/esporta_csv3/', views.esporta_csv3, name='esporta_csv3'),

    path('api/record5/esporta_csv2/', views.esporta_csv2, name='esporta_csv2'),

    path('api/record5/esporta_csv3/', views.esporta_csv3, name='esporta_csv3'),

    path('api/record6/esporta_csv2/', views.esporta_csv2, name='esporta_csv2'),

    path('api/record6/esporta_csv3/', views.esporta_csv3, name='esporta_csv3'),

    path('api/record7/esporta_csv2/', views.esporta_csv2, name='esporta_csv2'),

    path('api/record7/esporta_csv3/', views.esporta_csv3, name='esporta_csv3'),

    path('api/record8/esporta_csv2/', views.esporta_csv2, name='esporta_csv2'),

    path('api/record8/esporta_csv3/', views.esporta_csv3, name='esporta_csv3'),

    path('api/record9/esporta_csv2/', views.esporta_csv2, name='esporta_csv2'),

    path('api/record9/esporta_csv3/', views.esporta_csv3, name='esporta_csv3'),

    path('api/record10/esporta_csv2/', views.esporta_csv2, name='esporta_csv2'),

    path('api/record10/esporta_csv3/', views.esporta_csv3, name='esporta_csv3'),

    path('api/record11/esporta_csv2/', views.esporta_csv2, name='esporta_csv2'),

    path('api/record11/esporta_csv3/', views.esporta_csv3, name='esporta_csv3'),

    path('api/record12/esporta_csv2/', views.esporta_csv2, name='esporta_csv2'),

    path('api/record12/esporta_csv3/', views.esporta_csv3, name='esporta_csv3'),

]