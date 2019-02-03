from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.conf.urls.static import static
from student.models import Student,Project,DetailFunding
from investor.models import Funding
#from project.models import Project
# Create your views here.
def student_login(request):#for student login html page
    return render(request,'student/student-login.html')

def student_register(request):#for student register html page
    return render(request,'student/student-register.html')

def student_dashboard(request):#html page for profile
    if 'email' not in request.session:
        return HttpResponseRedirect(reverse('student_login'))
    else:
        email=request.session['email']
        s=Student.objects.get(email=email)
        return render(request,'student/student-dashboard.html',{
    's':s,
    })

def student_view_project(request):#html page
    if 'email' not in request.session:
        return HttpResponseRedirect(reverse('student_login'))
    else:
        email=request.session['email']
        try:
            s=Student.objects.get(email=email)
            p_dummy = Project.objects.get(student_id=s.id)
            po=Project.objects.filter(student_id=s.id)
            p=Project.objects.filter(student_id=s.id).values('id')

            p=list(p)
            t=p[0].get('id')
            rem=Funding.objects.filter(project_id=t)
            sum=0
            for i in rem:
                sum=sum+ int(i.amount)
        except Student.DoesNotExist:
            s= None
            p=[]
        except Project.DoesNotExist:
            p=None
            p=[]
            return render(request,'student/student-view-project.html',{})

        return render(request,'student/student-view-project.html',{'po':po,'sum':sum})


def student_add_project(request):#html page
    if 'email' not in request.session:
        return HttpResponseRedirect(reverse('student_login'))
    else:
        return render(request,'student/student-add-project.html')



def student_update_profile(request):#html page to update profile
    if 'email' not in request.session:
        return HttpResponseRedirect(reverse('student_login'))
    else:
        return render(request,'student/student-update-profile.html')

def student_details_about_crowdfunding(request):#html page for writing details
    if 'email' not in request.session:
        return HttpResponseRedirect(reverse('student_login'))
    else:
        return render(request,'student/student-details-about-crowdfunding.html')


def student_predict_funding(request):#html page
    if 'email' not in request.session:
        return HttpResponseRedirect(reverse('student_login'))
    else:
        return render(request,'student/student-predict-funding.html')


def student_register_action(request):
    name=request.POST.get('full_name','NULL')
    department=request.POST.get('department','NULL')
    gender=request.POST.get('gender','NULL')
    email=request.POST.get('email','NULL')
    contact=request.POST.get('phone','NULL')
    linkedin=request.POST.get('linkedin','NULL')
    github=request.POST.get('github','NULL')
    password=request.POST.get('password','NULL')
    uploadedfileurl=''
    if request.method=='POST' and request.FILES['myfile']:
        myfile=request.FILES['myfile']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploadedfileurl=fs.url(filename)
        bool=emailpresent(email)
        if contact=='NULL':
            contact=0
        if bool==True:
            s=Student(name=name,department=department,gender=gender,email=email,contact=contact,linkedin=linkedin,github=github,password=password,pic_path=uploadedfileurl)
            s.save()
            return HttpResponseRedirect(reverse('student_login'))
        else:
            return HttpResponse('Email exists')
    else:
        return HttpResponseRedirect(reverse('student_register'))

def emailpresent(email):
    if Student.objects.filter(email=email).exists():
        return False
    else:
        return True

def student_add_project_action(request):

    name=request.POST.get('name','NULL')
    description=request.POST.get('description','NULL')
    github=request.POST.get('gitlink','NULL')
    domain=request.POST.get('domain','NULL')
    efund=request.POST.get('e_fund','NULL')
    startdate=request.POST.get('start_date','NULL')
    uploadedfileurl=''
    if request.method=='POST' and request.FILES['myfile']:
        myfile=request.FILES['myfile']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploadedfileurl=fs.url(filename)

    email=request.session['email']
    s=Student.objects.get(email=email)

    s=Project(p_name=name,p_description=description,p_github=github,p_domain=domain,p_efund=efund,p_startdate=startdate,p_recommendation_pic_path=uploadedfileurl,student_id=s.id)
    s.save()
    return HttpResponseRedirect(reverse('student_add_project'))



def student_login_action(request):
    email = request.POST['email']
    password=request.POST['password']
    account=Student.objects.filter(email=email, password=password)
    if len(account) :
        request.session['email']=email #session started
        return HttpResponseRedirect(reverse('student_dashboard'))
    else:
        #messages.warning(request, 'Something went wrong ! \nTry again with proper credentials')
        return HttpResponseRedirect(reverse('student_login')+'?login_failure=true')


def logout_action(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('home'))

def student_details_about_crowdfunding_action(request):
    detail=request.POST.get('detail','NULL')
    email=request.session['email']
    s=Student.objects.get(email=email)
    if len(DetailFunding.objects.filter(id=s.id))>0:
        DetailFunding.objects.filter(id=s.id).update(detail=detail,)
    else:
        d = DetailFunding(detail=detail,student_id=s.id)
        d.save()
    return HttpResponseRedirect(reverse('student_dashboard'))


def list_of_investors(request):
    return render(request,'student/list_of_investors.html')
