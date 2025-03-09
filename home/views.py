from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User

import os
from .models import SignUp


def home(request):
    return render(request, 'home.html')  # Public Home Page

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')

        # Debugging print statement
        print(f"Received: name={name}, email={email}, phone={phone}, role={role}")

        if not name:
            messages.error(request, "Name field is required!")
            return redirect('signup')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if SignUp.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('signup')

        hashed_password = make_password(password)
        user = SignUp.objects.create(
            name=name,
            email=email,
            phone=phone,
            password=hashed_password,
            role=role
        )
        user.save()

        messages.success(request, "Signup successful! Please log in.")
        return redirect('login')

    return render(request, 'signup.html')


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if user exists
        user = SignUp.objects.filter(email=email).first()
        if user and check_password(password, user.password):
            request.session['user_id'] = user.id  # Store user session
            request.session['user_email'] = user.email
            request.session['user_role'] = user.role  # Store user role
            messages.success(request, "Login successful!")
            return redirect('main_page')  # Redirect to Main Page
        else:
            messages.error(request, "Invalid email or password!")
            return redirect('login')

    return render(request, 'login.html')

def logout(request):
    request.session.flush()  # Clear session
    messages.success(request, "Logged out successfully!")
    return redirect('login')

def main_page(request):
    if 'user_id' not in request.session:  # Restrict access
        messages.error(request, "Please login to continue.")
        return redirect('login')

    return render(request, 'main_page.html')  # Main Page Template

def upload_report(request):
    if 'user_id' not in request.session:  # Restrict access
        messages.error(request, "Please login to continue.")
        return redirect('login')

    if request.method == "POST":
        uploaded_file = request.FILES.get("report")
        if uploaded_file:
            # Validate file type
            allowed_extensions = ['.pdf', '.jpg', '.jpeg', '.png']
            ext = os.path.splitext(uploaded_file.name)[1].lower()
            if ext not in allowed_extensions:
                messages.error(request, "Invalid file type! Only PDF and image files are allowed.")
                return redirect("upload_report")

            # Save the file
            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)
            messages.success(request, "File uploaded successfully!")
            return redirect("analysis")  # Redirect to the analysis page after upload

    return render(request, "upload_report.html")

def analysis(request):
    if 'user_id' not in request.session:  # Restrict access
        messages.error(request, "Please login to continue.")
        return redirect('login')

    return render(request, 'analysis.html')

def aboutUs(request):
    return render(request, 'aboutUs.html')

def contact(request):
    return render(request, 'contact.html')

