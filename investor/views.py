from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.conf.urls.static import static
from investor.models import Investor
from django.core.files.storage import FileSystemStorage
from student.models import Student,Project,DetailFunding
from investor.models import Funding

# Create your views here.
def investor_login(request):#for investor login html page
    return render(request,'investor/investor_login.html')

def investor_register(request):#for investor register html page
    return render(request,'investor/investor_register.html')

def investor_dashboard(request):#for investor profile html page
    if 'email' not in request.session:
        return HttpResponseRedirect(reverse('investor_login'))
    else:
        email=request.session['email']
        i=Investor.objects.get(email=email)
        return render(request,'investor/investor-dashboard.html',{'i':i})

def investor_fundform(request,pid):
    if 'email' not in request.session:
        return HttpResponseRedirect(reverse('investor_login'))
    else:
        return render(request,'investor/investor_fundform.html',{'pid':pid,})

def investor_explore_project(request):#html page for exploring projects
    if 'email' not in request.session:
        return HttpResponseRedirect(reverse('student_login'))
    else:
        p=Project.objects.all()
        length=len(p)
        l=[]
        main=[]
        for i in p:
            s=Student.objects.get(id=i.student_id)
            l.append(s)

        main=zip(p,l)

        return render(request,'investor/investor-explore-project.html',{'main':main})


def investor_project_funded(request):
    if 'email' not in request.session:
        return HttpResponseRedirect(reverse('student_login'))
    else:
        try:
            l=[]
            email = request.session['email']
            i=Investor.objects.get(email=email)#get that investers address
            a=Funding.objects.filter(investor_id=i.id)#get all the project funded by that investors
            #p=Project.objects.filter(id=i.id)
            #for j in a:

                #if Project.objects.filter(id=j.id).exists():
                    #t=Project.objects.get(id=j.id)
                    #l.append(t)
            #main=zip(a,l)#a-fund obj, l-project obj
            l=[]
            p=Project.objects.all()
            for i in a:
                for j in p:
                    if i.project_id == j.id:
                        l.append(j.p_name)
                        continue
            main=zip(a,l)#a-fund obj, l-project obj
        except Investor.DoesNotExist:
            return render(request,'investor/investor-project-funded.html',{})

        return render(request,'investor/investor-project-funded.html',{'main':main,})

def investor_register_action(request):
    name=request.POST.get('full_name','NULL')
    country=request.POST.get('country','NULL')
    company=request.POST.get('company','NULL')
    gender=request.POST.get('gender','NULL')
    email=request.POST.get('email','NULL')
    contact=request.POST.get('phone','NULL')
    password=request.POST.get('password','NULL')
    uploadedfileurl=''
    print("aa"+str(request.FILES['mypic']))
    if request.method=='POST' and request.FILES['mypic']:
        mypic=request.FILES['mypic']
        fs=FileSystemStorage()
        filename=fs.save(mypic.name,mypic)
        uploadedfileurl=fs.url(filename)
        bool=emailpresent(email)
        if contact=='NULL':
            contact=0
        if bool==True:
            account = Investor(name=name,country=country,gender=gender,email=email,contact=contact,company=company,password=password,pic_path=uploadedfileurl)
            account.save()
            return HttpResponseRedirect(reverse('investor_login'))
        else:
            return HttpResponse('Email exists')
    else:
        return HttpResponseRedirect(reverse('investor_register'))


def emailpresent(email):
    if Investor.objects.filter(email=email).exists():
        return False
    else:
        return True

def investor_login_action(request):
    email = request.POST['email']
    password = request.POST['password']
    account=Investor.objects.filter(email=email, password=password)
    if len(account) :
        request.session['email']=email #session started
        return HttpResponseRedirect(reverse('investor_dashboard'))
    else:
        #messages.warning(request, 'Something went wrong ! \nTry again with proper credentials')
        return HttpResponseRedirect(reverse('investor_login')+'?login_failure=true')


def view_student_profile(request,name):#html-page
    s=Student.objects.get(name=name)
    p=Project.objects.filter(student_id=s.id)
    try:
        c=DetailFunding.objects.get(student_id=s.id)
    except DetailFunding.DoesNotExist:
        c = None

    return render(request,'investor/view_student_profile.html',{'s':s,'p':p,'c':c})

def investor_fundform_action(request,pid):
    try:
        p=Project.objects.get(id=pid)
        email=request.session['email']
        i=Investor.objects.get(email=email)
        amount= request.POST['amount']
        fund = Funding(project_id=pid,investor_id=i.id,amount=amount)
        fund.save()
    except Investor.DoesNotExist:
        return HttpResponseRedirect(reverse('investor_dashboard'))
    return HttpResponseRedirect(reverse('investor_dashboard'))


def investor_project_search(request):

    search=request.POST.get('search','NULL')
    projects = Project.objects.filter(p_name__icontains=search)
    return investor_explore_project_search(request,projects)

def investor_explore_project_search(request,projects):#html page for exploring projects
    if 'email' not in request.session:
        return HttpResponseRedirect(reverse('student_login'))
    else:
        p=projects
        length=len(p)
        l=[]
        main=[]
        for i in p:
            s=Student.objects.get(id=i.student_id)
            l.append(s)

        main=zip(p,l)

        return render(request,'investor/investor-explore-project.html',{'main':main})
