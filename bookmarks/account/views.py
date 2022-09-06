from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib import messages


# User Login View
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
            password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


# User Dashboard View
@login_required
def dashboard(request):
    template_name = 'account/dashboard.html'
    context = {
        'section': 'dashboard'
    }
    return render(request,template_name, context)



# User Logout View
def logout_view(request):
    logout(request)
    template_name = 'account/logout.html'
    return render(request,template_name)


# User Registration View
def register(request):
    template_name = 'account/register.html'
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,'account/register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    context={
        'user_form': user_form
    }
    return render(request,template_name,context)

@login_required
def edit(request):
    profile, created = Profile.objects.get_or_create(user = request.user)
    # print(profile)
    if created:
        profile.save()
    if request.method == 'POST':
        # print(request.POST)
        user_form = UserEditForm(instance=request.user,
        data=request.POST)
        profile_form = ProfileEditForm(
        instance=profile,
        data=request.POST,
        files=request.FILES)
        if user_form.is_valid():
            user_form.save()
            # print("User save")
        if  profile_form.is_valid():
            profile_form.save()

        # messages.success(request, "Changes has been updated successfully.")
        # mess
            # print("Profile save")
        # return render(request,
        # 'account/edit.html',
        # {'user_form': user_form,
        # 'profile_form': profile_form})
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm( instance=profile)

    # print(profile_form)
    return render(request,
    'account/edit.html',
    {'user_form': user_form,
    'profile_form': profile_form})