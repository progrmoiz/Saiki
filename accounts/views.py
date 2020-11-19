# pages/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse
from django.views import View
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Student
from .utils import get_current_student, is_student, is_teacher
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _

class HomePageView(View):
    template_name = 'home.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomePageView, self).dispatch(*args, **kwargs)

    def get(self, request):
        # add validation for just student login

        if is_teacher(request):
            return redirect('course')

        return redirect('announcement')

class ChangePasswordView(View):
    template_name = 'accounts/change_password.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ChangePasswordView, self).dispatch(*args, **kwargs)

    def get(self, request):
        student = get_current_student(request)

        form = PasswordChangeForm(request.user)

        context = {
            'is_account_page': 'active',
            'form': form,
            'student': student,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Your password was successfully updated!'))
            return redirect('change_password')
        else:
            messages.error(request, _('Please correct the error below.'))
            return redirect('change_password')

class AccountView(TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_account_page'] = 'active'
        context['student'] = get_current_student(self.request)
        context['cgpa'] = get_current_student(self.request).get_cgpa()
        return context

class ForgetPasswordView(TemplateView):
    template_name = 'accounts/forget_password.html'

class AccountEditView(FormView):
    template_name = 'accounts/edit.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AccountEditView, self).dispatch(*args, **kwargs)

    def get(self, request):
        student = get_current_student(request)

        if student:
            form = StudentForm(initial={'display_name': student.display_name, 'phone_number': student.phone_number, 'telephone': student.telephone, 'address_1': student.address_1, 'address_2': student.address_2})
        else:
            form = StudentForm()

        context = {
            'is_account_page': 'active',
            'form': form,
            'student': student,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid:
            data = request.POST.copy()
            print(data)

            student = Student.objects.get(user__username=request.user.username)
            student.display_name = data.get('display_name')
            student.phone_number = data.get('phone_number')
            student.telephone = data.get('telephone')
            student.address_1 = data.get('address_1')
            student.address_2 = data.get('address_2')
            student.save()

            return HttpResponse('submitted')

class LoginView(View):
    template_name = 'accounts/login.html'

    def post(self, request):
        # TODO: add remember me feature

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        # TODO: only if user is student can logged in right now
        if user:
            if user.is_active:
                login(request,user)
                messages.success(request, 'Successfully logged in!')
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.warning(request, 'Your account was inactive.')
                return redirect('login')
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            messages.error(request, 'Invalid login details given')
            return redirect('login')

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, self.template_name, {})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))
