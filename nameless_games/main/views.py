from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from .models import (
		UserProfile,
		Blog,
		Portfolio,
		#Testimonial,
		
	)

from django.views import generic


from . forms import  CreateUserForm , ContactForm #, BlogForm, TestimonialForm

#aqui se hacen un monton de form para el usuario login etc 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect

#se agregan el register page y el login 
def registerPage(request):
	if request.user.is_authenticated:
		return redirect("main:home")
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('main:login')
			

		context = {'form':form}
		return render(request, 'main/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect("main:home")
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect("main:home")
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'main/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('main:login')

class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		#eliminacion de certificate y testimonial
		#testimonials = Testimonial.objects.filter(is_active=True)
		#certificates = Certificate.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)
		
		#eliminacion de certificate y testimonial x2
		#context["testimonials"] = testimonials
		#context["certificates"] = certificates
		context["blogs"] = blogs
		context["portfolio"] = portfolio
		return context
#para la parte de contact 
class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Apuesto fue el perro 7.7 hmmp.')
		return super().form_valid(form)

#para la parte de blogs 
class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"

#para la parte de portfolios

class profiles(generic.ListView):
	model = UserProfile
	template_name = "main/profiles.html"



class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "main/portfolio.html"
	paginate_by = 10
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)

class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "main/portfolio-detail.html"
