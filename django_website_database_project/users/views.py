from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, CustomerRegisterForm, VendorRegisterForm, ChooseRegisterTypeForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = ChooseRegisterTypeForm(request.POST)
        action = request.POST
        if action.get('choice') == 'Customer':
            return redirect('register_customer')
        elif action.get('choice') == 'Vendor':
            return redirect('register_vendor')
    else:
        form = ChooseRegisterTypeForm()
        action = request.GET
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)

    # if request.method == 'POST':
    #     form = UserRegisterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f'Your account has been created! You can now log in!')
    #         return redirect('login')
    # else:
    #     form = UserRegisterForm()
    # context = {
    #     'form': form
    # }
    # return render(request, 'users/register.html', context)


def register_customer(request):
    if request.method == 'POST':
        c_form = CustomerRegisterForm(request.POST)
        if c_form.is_valid():
            c_form.save()
            name = c_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {name}! You can now log in as a customer!')
            return redirect('login')
    else:
        c_form = CustomerRegisterForm()
    context = {
        'c_form': c_form
    }
    return render(request, 'users/register_customer.html', context)


def register_vendor(request):
    if request.method == 'POST':
        v_form = VendorRegisterForm(request.POST)
        if v_form.is_valid():
            v_form.save()
            name = v_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {name} You can now log in as a vendor!')
            return redirect('login')
    else:
        v_form = VendorRegisterForm()
    context = {
        'v_form': v_form
    }
    return render(request, 'users/register_vendor.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


@login_required
def customer_profile(request):
    pass


@login_required
def vendor_profile(request):
    pass