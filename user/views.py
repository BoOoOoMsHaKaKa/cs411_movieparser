from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.
# message.debug , message.info,message.success,message.warning,message.error
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created Successfully!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'user/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        up_form = UserUpdateForm(request.POST,request.FILES,instance=request.user)# image is file
        img_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if up_form.is_valid() and img_form.is_valid():
            up_form.save()
            img_form.save()
            messages.success(request,f'Profile Updated!')
            return redirect('profile')
    else:
        up_form = UserUpdateForm(instance=request.user)
        img_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'up_form':up_form,
        'img_form':img_form,
    }
    return render(request,'user/profile.html',context)

@login_required
def user_friend(request):
    return render(request,'user/user_friend.html')
