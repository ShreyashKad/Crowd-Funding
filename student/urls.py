from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('student-login/',views.student_login,name='student_login'),
    path('student-register/',views.student_register,name='student_register'),
    path('student-dashboard/',views.student_dashboard,name='student_dashboard'),
    path('student-add-project/',views.student_add_project,name='student_add_project'),
    path('student-update-profile/',views.student_update_profile,name='student_update_profile'),
    path('student-view-project/',views.student_view_project,name='student_view_project'),

    path('student-detail-about-crowdfunding/',views.student_details_about_crowdfunding,name='student-detail-about-crowdfunding'),
    path('student-predict-funding/',views.student_predict_funding,name='student_predict_funding'),
    path('student_register_action/',views.student_register_action,name='student_register_action'),
    path('student_add_project_action/',views.student_add_project_action,name='student_add_project_action'),
    path('student_login_action/',views.student_login_action,name='student_login_action'),
    path('logout_action/',views.logout_action,name='logout_action'),
    path('student-detail-about-crowdfunding-action/',views.student_details_about_crowdfunding_action,name='student-detail-about-crowdfunding-action'),
    path('list_of_investors/',views.list_of_investors,name='list_of_investors'),




]
