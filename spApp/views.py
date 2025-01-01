#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404,HttpResponse # type: ignore
from django.contrib import messages # type: ignore
from .models import *
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib.auth import logout # type: ignore
from .models import CourseTbl,Subscription
from django.contrib.auth.models import auth # type: ignore


def index(request):
 courses = CourseTbl.objects.order_by('-rate')[:4]
 return render(request, 'spApp/Home Page.html', {'courses': courses})


def course_details(request, course_id): 
    user = request.user 
    course = get_object_or_404(CourseTbl, pk=course_id) 
    is_subscribed = Subscription.objects.filter(user=user, course=course).exists() 
    return render(request, 'spApp/course_details.html', { 'course': course, 'is_subscribed': is_subscribed })


def dashboard(request): 
    user = request.user
    subscriptions = Subscription.objects.filter(user=user)
    courses = [subscription.course for subscription in subscriptions]
    return render(request, 'spApp/dashboard.html', {'courses': courses,'user':user})

#def courses(request):
 #   if request.user.is_authenticated:
 #      courses = CourseTbl.objects.all()  
 #     return render(request, 'spApp/courses.html', {'courses': courses})
 # else:
 #   return redirect('login')
    

def courses(request):
    if request.user.is_authenticated:
        user = request.user
        all_courses = CourseTbl.objects.all()
        courses_with_status = []

        for course in all_courses:
            is_subscribed = Subscription.objects.filter(user=user, course=course).exists()
            courses_with_status.append({
                'course': course,
                'is_subscribed': is_subscribed
            })
        return render(request, 'spApp/courses.html', {'courses': courses_with_status})
    else:
        return redirect('login')

def logout(request):
    auth.logout(request)
    return redirect('index')


def enroll_course(request, course_id):
    if request.user.is_authenticated:
        user = request.user
        course = get_object_or_404(CourseTbl, pk=course_id)
        Subscription.objects.get_or_create(user=user, course=course)
        return redirect('dashboard')
    else:
        return redirect('login')
    
def course_content(request, course_id): 
    course = get_object_or_404(CourseTbl, pk=course_id) 
    contents = course.contents.all() 
    return render(request, 'spApp/content.html', {'course': course, 'contents': contents})
    #-----------

def logout(request):
 auth.logout(request)
 return redirect('index')


def about(request):
 context = {}
 return render(request, 'spApp/About.html', context)

def contactUs(request):
 context = {}
 return render(request, 'spApp/contact us.html', context)
# End of project pages Requests------------------------------

# Authentication-----------------------------



from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        context = {'username': username,'email': email,'password': password,'confirm_password': confirm_password}
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists.")
            else:
                hashed_password = make_password(password)
                user = User(username=username, email=email, password=hashed_password)
                user.save()
                messages.success(request, "Your account has been created!")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match.")
            return render(request, 'spApp/signup.html', context)

    return render(request, 'spApp/signup.html')






























#sending email message of contact us
from django.core.mail import send_mail
from django.http import HttpResponse

def submit_contact(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Compose the email
        subject = f"New Contact Form Submission from {name}"
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        recipient_list = ['ahmedbakry23@gmial.com']  # Replace with the email to receive messages

        # Send the email
        send_mail(
            subject,
            full_message,
            'edulearnform@gmail.com',  # Sender email
            recipient_list,
            fail_silently=False,
        )

        # Return a success response
        return HttpResponse('Message sent successfully!')

    return HttpResponse('Invalid request method.')