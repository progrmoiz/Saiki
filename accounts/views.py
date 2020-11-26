# pages/views.py
from django.http.response import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse
from django.views import View
from .forms import StudentForm, TeacherForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Student
from .utils import get_current_student, get_current_teacher, is_student, is_teacher
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _
from meta.views import Meta
from saiki.utils import get_site_title

class HomePageView(View):
    template_name = 'home.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomePageView, self).dispatch(*args, **kwargs)

    def get(self, request):
        # TODO: add validation for just student login

        if request.user.is_teacher:
            return redirect('course:index')
        elif request.user.is_student:
            return redirect('announcement:index')
        
        return HttpResponseForbidden()

class ChangePasswordView(LoginRequiredMixin, View):
    redirect_field_name = 'accounts:login'
    template_name = 'accounts/change_password.html'

    def get(self, request):
        # TODO: add student login
        
        student = get_current_student(request)

        form = PasswordChangeForm(request.user)
        
        meta = Meta(
            title=get_site_title('Change password')
        )

        context = {
            'is_account_page': 'active',
            'form': form,
            'is_student': True,
            'student': student,
            'meta': meta
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Your password was successfully updated!'))
            return redirect('accounts:change_pwd')
        else:
            messages.error(request, _('Please correct the error below.'))
            return redirect('accounts:change_pwd')

class AccountView(LoginRequiredMixin, TemplateView):
    redirect_field_name = 'accounts:login'
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meta = Meta(
            title=get_site_title('Profile')
        )

        context['is_account_page'] = 'active'
        context['meta'] = meta

        if is_student(self.request):
            context['cgpa'] = get_current_student(self.request).get_cgpa()

        return context

class ForgetPasswordView(LoginRequiredMixin, TemplateView):
    redirect_field_name = 'accounts:login'
    template_name = 'accounts/forget_password.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meta = Meta(
            title=get_site_title('Forget password')
        )

        context['is_account_page'] = 'active'
        context['meta'] = meta
        return context

class AccountEditView(LoginRequiredMixin, FormView):
    redirect_field_name = 'accounts:login'
    template_name = 'accounts/edit.html'

    def get(self, request):

        if request.user.is_teacher:
            teacher = get_current_teacher(request)
            
            form = TeacherForm(initial={
                'first_name': teacher.user.first_name, 
                'last_name': teacher.user.last_name, 
                'display_name': teacher.display_name, 
                'email': teacher.user.email, 
            })
        elif request.user.is_student:
            student = get_current_student(request)

            form = StudentForm(initial={
                'first_name': student.user.first_name, 
                'last_name': student.user.last_name, 
                'display_name': student.display_name, 
                'email': student.user.email, 
                'phone_number': student.phone_number, 
                'telephone': student.telephone, 
                'address_1': student.address_1, 
                'address_2': student.address_2
            })
        else:
            return HttpResponseForbidden()
        meta = Meta(
            title=get_site_title('Edit profile')
        )

        context = {
            'is_account_page': 'active',
            'form': form,
            'meta': meta
        }

        return render(request, self.template_name, context)

    def post(self, request):
        if request.user.is_student:
            form = StudentForm(request.POST)
        elif request.user.is_teacher:
            form = TeacherForm(request.POST)
        else:
            return HttpResponseForbidden()
        
        if form.is_valid():
            data = request.POST.copy()

            if request.user.is_student:
                student = Student.objects.get(user__username=request.user.username)
                student.user.first_name = form.cleaned_data['first_name']
                student.user.last_name = form.cleaned_data['last_name']
                student.display_name = form.cleaned_data['display_name']
                student.phone_number = form.cleaned_data['phone_number']
                student.user.email = form.cleaned_data['email']
                student.telephone = form.cleaned_data['telephone']
                student.address_1 = form.cleaned_data['address_1']
                student.address_2 = form.cleaned_data['address_2']
                student.save()
                student.user.save()
            elif request.user.is_teacher:
                teacher = get_current_teacher(request)
                teacher.user.first_name = form.cleaned_data['first_name']
                teacher.user.last_name = form.cleaned_data['last_name']
                teacher.display_name = form.cleaned_data['display_name']
                teacher.user.email = form.cleaned_data['email']
                teacher.save()
                teacher.user.save()

            return redirect('accounts:edit')

class LoginView(View):
    template_name = 'accounts/login.html'

    def post(self, request):
        # TODO: add remember me feature

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                messages.success(request, 'Successfully logged in!')
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.warning(request, 'Your account was inactive.')
                return redirect('accounts:login')
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            messages.error(request, 'Invalid login details given')
            return redirect('accounts:login')

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        else:
            meta = Meta(
                title=get_site_title('Login')
            )

            context = {
                'meta': meta
            }
            return render(request, self.template_name, context)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('accounts:login'))
