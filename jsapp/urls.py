from django.urls import path
from jsapp import views

urlpatterns = [
    path('admin_page/',views.admin_page,name="admin_page"),
    path('adminlog_page/',views.adminlog_page,name="adminlog_page"),
    path('login_page/',views.login_page,name="login_page"),
    path('logout_page/',views.logout_page,name="logout_page"),
    path('contact_delete/<int:pro_id>',views.contact_delete,name="contact_delete"),
    path('tablepage/',views.tablepage,name="tablepage"),
    path('courseform_page/',views.courseform_page,name="courseform_page"),
    path('saveform_page/',views.saveform_page,name="saveform_page"),
    path('coursedisplay_page/',views.coursedisplay_page,name="coursedisplay_page"),
    path('courseedit/<int:cou_id>/',views.courseedit,name="courseedit"),
    path('update_image/<int:pro_id>/',views.update_image,name="update_image"),
    path('delete_img/<int:pro_id>/',views.delete_img,name="delete_img")
]