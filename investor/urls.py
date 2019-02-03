from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('investor-login/',views.investor_login,name='investor_login'),
    path('investor-login-action/',views.investor_login_action,name='investor_login_action'),
    path('investor-register/',views.investor_register,name='investor_register'),
    path('investor-register-action/',views.investor_register_action,name='investor_register_action'),
    path('investor-dashboard/',views.investor_dashboard,name='investor_dashboard'),
    path('investor-explore-project/',views.investor_explore_project,name='investor_explore_project'),
    path('investor-project-funded/',views.investor_project_funded,name='investor_project_funded'),
    path('view_student_profile/<str:name>',views.view_student_profile,name='view_student_profile'),
    path('investor-fundform/<str:pid>',views.investor_fundform,name='investor_fundform'),
    path('investor-fundform-action/<str:pid>',views.investor_fundform_action,name='investor_fundform_action'),
    path('investor-project-search/',views.investor_project_search,name='investor_project_search'),



]
