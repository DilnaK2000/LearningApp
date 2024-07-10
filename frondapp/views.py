from django.shortcuts import render,redirect
from frondapp.models import contactdb,loginsignupdb
from jsapp.models import coursesavedb
from django.contrib import messages

# Create your views here.

def home_page(req):
    data = coursesavedb.objects.all()
    return render(req,"Home.html",{'data':data})

def features_page(req):
    data = coursesavedb.objects.all()
    return render(req,"Features.html",{'data':data})

def contact_page(request):
    return render(request,"Contact.html")

def save_contact(request):
    if request.method=="POST":
        un= request.POST.get('yname')
        ue = request.POST.get('email')
        st = request.POST.get('subject')
        me = request.POST.get('message')
        obj = contactdb(Username=un,Email=ue,Subject=st,Message=me)
        obj.save()
        messages.success(request,"Ok Saved..")
        return redirect(contact_page)

def fordeveloper_page(request):
    return render(request,"fordeveloper.html")

def interview2page(request):
    return render(request,"INTERVIEWPAGE.html")

# *******************
def interview_page(request):
    messages.success(request,"Are You Ready")
    return render(request,"PythoninterviewQue.html")
# **************************
def sqlquiz_page(req):
    messages.success(req,"Are You Ready")
    return render(req,"SQLQuiz.html")

def Cquiz_page(req):
    messages.success(req,"Are You Ready")
    return render(req,"C++Quiz.html")

def djangoquiz_page(req):
    messages.success(req,"Are You Ready")
    return render(req,"DjangoQuiz.html")
def javaQuiz(re):
    messages.success(re,"Are You Ready")
    return render(re,"javascriptQuiz.html")

def reactQuiz(request):
    messages.success(request,"Are You Ready")
    return render(request,"ReactQuiz.html")

def loginsigup_page(request):
    return render(request,"LoginSignup.html")

def saveloginsignin(request):
    if request.method=="POST":
        UN= request.POST.get('username')
        EM = request.POST.get('email')
        PASS = request.POST.get('pass')
        PASS1 = request.POST.get('pass1')
        obj = loginsignupdb(uname=UN,email=EM,password=PASS,cpassword=PASS1)
        obj.save()
        messages.success(request,"Saved Successfully..! ")
        return redirect(loginsigup_page)

def userlogin(request):
    if request.method=="POST":
        un = request.POST.get('uname')
        pas = request.POST.get('password')
        if loginsignupdb.objects.filter(uname=un,password=pas).exists():
            request.session['uname']=un
            request.session['password']=pas
            messages.success(request,"Welcome..!")
            return redirect(home_page)
        else:
            messages.error(request, "Invalid Password..!")
            return redirect(loginsigup_page)
    else:
        messages.warning(request, "User not Found..!")
        return redirect(loginsigup_page)

def logout_page(request):
    del request.session['uname']
    del request.session['password']
    messages.success(request, "Logout Successfully")
    return redirect(home_page)


def Quizlogin(request):
    if request.method=="POST":
        un = request.POST.get('uname')
        pas = request.POST.get('password')
        if loginsignupdb.objects.filter(uname=un,password=pas).exists():
            request.session['uname']=un
            request.session['password']=pas
            messages.success(request, "Welcome..!")
            return redirect(interview_page)
        else:
            messages.error(request, "Invalid Password..!")
            return redirect(loginsigup_page)
    else:
        messages.warning(request, "User not Found..!")
        return redirect(loginsigup_page)

def sqlquizlogin(request):
    if request.method=="POST":
        un = request.POST.get('uname')
        pas = request.POST.get('password')
        if loginsignupdb.objects.filter(uname=un,password=pas).exists():
            request.session['uname']=un
            request.session['password']=pas
            messages.success(request, "Welcome..!")
            return redirect(sqlquiz_page)
        else:
            messages.error(request, "Invalid Password..!")
            return redirect(loginsigup_page)
    else:
        messages.warning(request, "User not Found..!")
        return redirect(loginsigup_page)

def djangoquizlogin(request):
    if request.method=="POST":
        un = request.POST.get('uname')
        pas = request.POST.get('password')
        if loginsignupdb.objects.filter(uname=un,password=pas).exists():
            request.session['uname']=un
            request.session['password']=pas
            messages.success(request, "Welcome..!")
            return redirect(djangoquiz_page)
        else:
            messages.error(request, "Invalid Password..!")
            return redirect(loginsigup_page)
    else:
        messages.warning(request, "User not Found..!")
        return redirect(loginsigup_page)

def ccquizlogin(request):
    if request.method=="POST":
        un = request.POST.get('uname')
        pas = request.POST.get('password')
        if loginsignupdb.objects.filter(uname=un,password=pas).exists():
            request.session['uname']=un
            request.session['password']=pas
            messages.success(request, "Welcome..!")
            return redirect(Cquiz_page)
        else:
            messages.error(request, "Invalid Password..!")
            return redirect(loginsigup_page)
    else:
        messages.warning(request, "User not Found..!")
        return redirect(loginsigup_page)


def javaquizlogin(request):
    if request.method=="POST":
        un = request.POST.get('uname')
        pas = request.POST.get('password')
        if loginsignupdb.objects.filter(uname=un,password=pas).exists():
            request.session['uname']=un
            request.session['password']=pas
            messages.success(request, "Welcome..!")
            return redirect(javaQuiz)
        else:
            messages.error(request, "Invalid Password..!")
            return redirect(loginsigup_page)
    else:
        messages.warning(request, "User not Found..!")
        return redirect(loginsigup_page)


def reactquizlogin(request):
    if request.method=="POST":
        un = request.POST.get('uname')
        pas = request.POST.get('password')
        if loginsignupdb.objects.filter(uname=un,password=pas).exists():
            request.session['uname']=un
            request.session['password']=pas
            messages.success(request, "Welcome..!")
            return redirect(reactQuiz)
        else:
            messages.error(request, "Invalid Password..!")
            return redirect(loginsigup_page)
    else:
        messages.warning(request, "User not Found..!")
        return redirect(loginsigup_page)




def topicPY_page(re):
    return render(re,"TopicPy.html")

def topicjava_page(re):
    return render(re,"topicjava.html")
def topicC_page(re):
    return render(re,"Topicc++.html")

def Topicdjango_page(re):
    return render(re,"Topicdjango.html")

def topicCpro_page(re):
    return render(re,"TopicC.html")
def topicsql(re):
    return render(re,"TopicSQL.html")

def topicds_page(re):
    return render(re,"TopicDS.html")
def topicfp_page(re):
    return render(re,"TopicFP.html")
def topiclinux_page(re):
    return render(re,"TopicLinux.html")

def pyQA_page(request):
    return render(request,"pythonQandA.html")

def djangoQA(re):
    return render(re,"djangoQandA.html")
def ccQandA(re):
    return render(re,"C++QandA.html")


