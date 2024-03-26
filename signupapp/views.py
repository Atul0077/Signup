# signupapp/views.py
from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup_success')  # Create a success page
    else:
        form = SignUpForm()

    return render(request, 'signupapp/signup.html', {'form': form})
# signupapp/views.py


def cancel(request):
    return render(request, 'signupapp/cancel.html')
