from django.urls import path
from . import views


app_name = "main"

#urls para las diferentes partes del proyecto  

urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),

	path('', views.IndexView.as_view(), name="home"),
	path('contact/', views.ContactView.as_view(), name="contact"),
	path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
	path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
	path('blog/', views.BlogView.as_view(), name="blogs"),
	path('profiles/', views.profiles.as_view(), name="profiles"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),

	]