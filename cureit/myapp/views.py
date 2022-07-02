from email import message
from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .models import Anxiety, UserDetail , WellBeing , Psychologyadjustment , Stress

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Welcome back ')
            return redirect('measurements')
        else:
            messages.error(request, 'Wrong Email or Password try again!')
            return render(request,'index.html')

    return render(request,'index.html')

def info(request):
    if request.method == 'POST':
        name = request.POST['user-name']
        email = request.POST['user-email']
        password = request.POST['user-passsword']
        age = request.POST['user-age']
        gender = request.POST['user-gender']
        institute = request.POST['user-InstituteName']
        designation = request.POST['user-Designation']
        ins = UserDetail(name=name,email=email,password=password,age=age,gender=gender,institute=institute,designation=designation)
        ins.save()
        # creating user in Users table of Django
        user = User.objects.create_user(name)
        user.set_password(password)
        user.save()
        messages.success(request,'Your accunt is Successfully created.')
        return redirect('/')

    return render(request,'info.html')

def logoutuser(request):
    logout(request)
    messages.success(request,'Logout Successful!.')
    return redirect('/')

def measurements(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        return render(request,'measurements.html')

def wellbeing(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        if request.method == 'POST':
            ans1 = request.POST['ans1']
            ans2 = request.POST['ans2']
            ans3 = request.POST['ans3']
            ans4 = request.POST['ans4']
            ans5 = request.POST['ans5']
            ans6 = request.POST['ans6']
            ans7 = request.POST['ans7']
            ans8 = request.POST['ans8']
            ans9 = request.POST['ans9']
            ans10 = request.POST['ans10']
            ans11 = request.POST['ans11']
            ans12 = request.POST['ans12']
            ans13 = request.POST['ans13']
            ans14 = request.POST['ans14']
            ans15 = request.POST['ans15']
            ans16 = request.POST['ans16']
            ans17 = request.POST['ans17']
            ans18 = request.POST['ans18']
            ins = WellBeing(q1=ans1,q2=ans2,q3=ans3,q4=ans4,q5=ans5,q6=ans6,q7=ans7,q8=ans8,q9=ans9,q10=ans10,q11=ans11,q12=ans12,q13=ans13,q14=ans14,q15=ans15,q16=ans16,q17=ans17,q18=ans18)
            ins.save()
            messages.success(request,'Thank You for submit the form.')
        return render(request,'wellbeing.html')
def psychologyadjustment(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        if request.method == 'POST':
            # current_user = request.user
            # user_name = current_user.username
            # userdetails = UserDetail.objects.filter(name=user_name).values()
            # new_name = userdetails.name
            # print(new_name)
            ans1 = request.POST['ans1']
            ans2 = request.POST['ans2']
            ans3 = request.POST['ans3']
            ans4 = request.POST['ans4']
            ans5 = request.POST['ans5']
            ans6 = request.POST['ans6']
            ans7 = request.POST['ans7']
            ans8 = request.POST['ans8']
            ans9 = request.POST['ans9']
            result = int(ans1)+int(ans2)+int(ans3)+int(ans4)+int(ans5)+int(ans6)+int(ans7)+int(ans8)+int(ans9)
            ins = Psychologyadjustment(q1=ans1,q2=ans2,q3=ans3,q4=ans4,q5=ans5,q6=ans6,q7=ans7,q8=ans8,q9=ans9,result=result)
            ins.save()
            messages.success(request,'Thank You for submit the form.')
        return render(request,'psychologyadjustment.html')

def stress(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        if request.method == 'POST':
            ans1 = request.POST['ans1']
            ans2 = request.POST['ans2']
            ans3 = request.POST['ans3']
            ans4 = request.POST['ans4']
            ans5 = request.POST['ans5']
            ans6 = request.POST['ans6']
            ans7 = request.POST['ans7']
            ans8 = request.POST['ans8']
            ans9 = request.POST['ans9']
            ans10 = request.POST['ans10']
            ins = Stress(q1=ans1,q2=ans2,q3=ans3,q4=ans4,q5=ans5,q6=ans6,q7=ans7,q8=ans8,q9=ans9,q10=ans10)
            ins.save()
            messages.success(request,'Thank You for submit the form.')
    return render(request,'stress.html')

def anxiety(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        if request.method == 'POST':   
            ans1 = request.POST['ans1']
            ans2 = request.POST['ans2']
            ans3 = request.POST['ans3']
            ans4 = request.POST['ans4']
            ans5 = request.POST['ans5']
            ans6 = request.POST['ans6']
            ans7 = request.POST['ans7']
            ans8 = request.POST['ans8']
            ans9 = request.POST['ans9']
            ans10 = request.POST['ans10']
            ans11 = request.POST['ans11']
            ans12 = request.POST['ans12']
            ans13 = request.POST['ans13']
            ans14 = request.POST['ans14']
            ans15 = request.POST['ans15']
            ans16 = request.POST['ans16']
            ans17 = request.POST['ans17']
            ans18 = request.POST['ans18']
            ans19 = request.POST['ans19']
            ans20 = request.POST['ans20']
            ans21 = request.POST['ans21']
            ans22 = request.POST['ans22']
            ans23 = request.POST['ans23']
            ans24 = request.POST['ans24']
            ans25 = request.POST['ans25']
            ans26 = request.POST['ans26']
            ans27 = request.POST['ans27']
            ans28 = request.POST['ans28']
            ans29 = request.POST['ans29']
            ans30 = request.POST['ans30']
            ans31 = request.POST['ans31']
            ans32 = request.POST['ans32']
            ans33 = request.POST['ans33']
            ans34 = request.POST['ans34']
            ans35 = request.POST['ans35']
            ans36 = request.POST['ans36']
            ans37 = request.POST['ans37']
            ans38 = request.POST['ans38']
            ans39 = request.POST['ans39']
            ans40 = request.POST['ans40']
            ins = Anxiety(q1=ans1,q2=ans2,q3=ans3,q4=ans4,q5=ans5,q6=ans6,q7=ans7,q8=ans8,q9=ans9,q10=ans10,q11=ans11,q12=ans12,q13=ans13,q14=ans14,q15=ans15,q16=ans16,q17=ans17,q18=ans18,q19=ans19,q20=ans20,q21=ans21,q22=ans22,q23=ans23,q24=ans24,q25=ans25,q26=ans26,q27=ans27,q28=ans28,q29=ans29,q30=ans30,q31=ans31,q32=ans32,q33=ans33,q34=ans34,q35=ans35,q36=ans36,q37=ans37,q38=ans38,q39=ans39,q40=ans40)
            ins.save()
            messages.success(request,'Thank You for submit the form.')
    return render(request,'anxiety.html')