from rest_framework_nested import routers as nested_router
from v1.company.urls import router
from v1.db.views import LandingPageDBViewSets


companies_router = nested_router.NestedDefaultRouter(router, r'companies', lookup='company')
companies_router.register(r'landing_dbs', LandingPageDBViewSets, basename='landing-db')
