from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from frondapp.models import contactdb
from jsapp.models import coursesavedb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages

# Create your views here.
def admin_page(req):
    return render(req,"Adminpage.html")
def adminlog_page(request):
    return render(request,"adminlogin.html")
def login_page(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=pwd)
            if x is not None:
                login(request, x)
                request.session['username']=un
                request.session['password']=pwd
                return redirect(admin_page)
            else:
                return redirect(adminlog_page)
        else:
            return redirect(adminlog_page)

def logout_page(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminlog_page)

def tablepage(request):
    data = contactdb.objects.all()
    return render(request,"table_page.html",{'data':data})

def contact_delete(request,pro_id):
    x= contactdb.objects.filter(id=pro_id)
    x.delete()
    return redirect(tablepage)

def courseform_page(request):
    return render(request,"courseform.html")

def saveform_page(request):
    if request.method=="POST":
        cn = request.POST.get('coursename')
        pr = request.POST.get('price')
        img = request.FILES['Img']
        obj = coursesavedb(cname=cn,price=pr,image=img)
        obj.save()
        messages.success(request,"Category Saved Successfully...")
        return redirect(courseform_page)

def coursedisplay_page(request):
    data = coursesavedb.objects.all()
    return render(request,"Coursedisplay.html", {'data':data})

def courseedit(request,cou_id):
    data = coursesavedb.objects.get(id=cou_id)
    return render(request,"courseEdit.html",{'data':data})

def update_image(request,pro_id):
    if request.method=="POST":
        coname = request.POST.get('coursename')
        price = request.POST.get('price')
        try:
            img = request.FILES['Img']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = coursesavedb.objects.get(id=pro_id).image
        coursesavedb.objects.filter(id=pro_id).update(cname=coname,price=price,image=file)
        return redirect(coursedisplay_page)

def delete_img(request,pro_id):
    x=coursesavedb.objects.filter(id=pro_id)
    x.delete()
    return redirect(coursedisplay_page)
