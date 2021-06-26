from typing import Pattern
from django.urls import path
from est_app import views


urlpatterns=[
    
    path('',views.HomeView.as_view(),name='home'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('agent/<int:pk>/',views.AgentDetailView.as_view(),name='agent_detail'),
    path('agent/list/',views.AgentListView.as_view(),name='agent_list'),
    path('agent/new/',views.AgentCreateView.as_view(),name='agent_new'),
    path('agent/<int:pk>/edit/',views.AgentUpdateView.as_view(),name='agent_edit'),
    path('agent/<int:pk>/remove/',views.AgentDeleteView.as_view(),name='agent_remove'),
    # path('property/<int:pk>/',views.PropertyDetailView.as_view(),name='property_detail'),
    path('property/<int:pk>/',views.propertyDetailView,name='property_detail'),
    path('property/list/',views.PropertyListView.as_view(),name='property_list'),
    path('property/new/',views.PropertyCreateView.as_view(),name='property_new'),
    path('property/<int:pk>/edit/',views.PropertyUpdateView.as_view(),name='property_edit'),
    path('property/<int:pk>/remove/',views.PropertyDeleteView.as_view(),name='property_remove'),
    path('drafts/',views.PropertyDraftView.as_view(),name='property_draft_list'),
    path('property/<int:pk>/publish/',views.property_publish,name='property_publish'),
    path('search/',views.search_property,name='search'),
    path('leads/list/',views.LeadsListView.as_view(),name='leads_list'),
    # path('property/<int:pk>/enquire/',views.enquire_abt_property,name='enquire_abt_property'),
]
