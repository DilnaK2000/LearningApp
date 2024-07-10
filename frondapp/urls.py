from django.urls import path
from frondapp import views

urlpatterns = [
    path('',views.home_page,name="home_page"),
    path('features_page/',views.features_page,name="features_page"),
    path('contact_page/',views.contact_page,name="contact_page"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('fordeveloper_page/',views.fordeveloper_page,name="fordeveloper_page"),
    path('interview_page/',views.interview_page,name="interview_page"),
    path('interview2page/',views.interview2page,name="interview2page"),
    path('sqlquiz_page/',views.sqlquiz_page,name="sqlquiz_page"),
    path('Cquiz_page/',views.Cquiz_page,name="Cquiz_page"),
    path('djangoquiz_page/',views.djangoquiz_page,name="djangoquiz_page"),
    path('javaQuiz/',views.javaQuiz,name="javaQuiz"),
    path('reactQuiz/',views.reactQuiz,name="reactQuiz"),
    path('loginsigup_page/',views.loginsigup_page,name="loginsigup_page"),
    path('saveloginsignin/',views.saveloginsignin,name="saveloginsignin"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('logout_page/',views.logout_page,name="logout_page"),
    path('topicPY_page/',views.topicPY_page,name="topicPY_page"),
    path('topicjava_page/',views.topicjava_page,name="topicjava_page"),
    path('topicC_page/',views.topicC_page,name="topicC_page"),
    path('Topicdjango_page/',views.Topicdjango_page,name="Topicdjango_page"),
    path('topicCpro_page/',views.topicCpro_page,name="topicCpro_page"),
    path('topicsql/',views.topicsql,name="topicsql"),
    path('topicds_page/',views.topicds_page,name="topicds_page"),
    path('topicfp_page/',views.topicfp_page,name="topicfp_page"),
    path('topiclinux_page/',views.topiclinux_page,name="topiclinux_page"),
    path('pyQA_page/',views.pyQA_page,name="pyQA_page"),
    path('djangoQA/',views.djangoQA,name="djangoQA"),
    path('ccQandA/',views.ccQandA,name="ccQandA"),


    path('Quizlogin/',views.Quizlogin,name="Quizlogin"),
    path('sqlquizlogin/',views.sqlquizlogin,name="sqlquizlogin"),
    path('ccquizlogin/',views.ccquizlogin,name="ccquizlogin"),
    path('djangoquizlogin/',views.djangoquizlogin,name="djangoquizlogin"),
    path('javaquizlogin/',views.javaquizlogin,name="javaquizlogin"),
    path('reactquizlogin/',views.reactquizlogin,name="reactquizlogin")
]