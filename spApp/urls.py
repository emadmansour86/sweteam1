from . import views
from django.urls import path # type: ignore
from django.contrib.auth import views as auth_views  # type: ignore # Import this for auth_views

urlpatterns = [
path('index',views.index, name='index'),
path('about/',views.about, name='about'),
path('courses/',views.courses, name='courses'),
path('course/<int:course_id>/', views.course_details, name='course_details'),
path('contactUs/',views.contactUs, name='contactUs'),
path('submit-contact', views.submit_contact, name='submit_contact'),
path('login/', auth_views.LoginView.as_view(template_name='spApp/login.html'), name='login'),
path('logout/', views.logout, name='logout'),
path('signup/', views.signup, name='signup'),
path('dashboard/', views.dashboard, name='dashboard'), 
path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),
path('course_content/<int:course_id>/', views.course_content, name='course_content'),
]