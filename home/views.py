from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SignUp
from django.contrib.auth.hashers import check_password, make_password

def home(request):
    return render(request, 'home.html')  # Public Home Page

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        # Check if user already exists
        if SignUp.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('signup')

        # Save user with hashed password
        user = SignUp(name=name, email=email, password=make_password(password))
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

    return render(request, 'upload_report.html')

def analysis(request):
    if 'user_id' not in request.session:  # Restrict access
        messages.error(request, "Please login to continue.")
        return redirect('login')

    return render(request, 'analysis.html')

def aboutUs(request):
    return render(request, 'abouts.html')

def contact(request):
    return render(request, 'contact.html')
