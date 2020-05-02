from django.shortcuts import render, redirect
from .models import Album
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .Abcd import UserForm
from django.contrib.auth import authenticate, login

class IndexView(generic.ListView):
	template_name = 'menu/index.html'

	def get_queryset(self):
		return Album.objects.all()

class CreateAlbum(CreateView):
	model = Album
	fields = ['title', 'artist', 'year']

class UpdateAlbum(UpdateView):
	model = Album
	fields = ['title', 'artist', 'year']
	
class DeleteAlbum(DeleteView):
	model = Album
	success_url = reverse_lazy('index')

class UserFormView(View):
	form_class = UserForm
	template_name = 'menu/index.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			
			user.set_password(password)
			user.save()

			# if Credential are correct
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('index')
		return render(request, self.template_name, {'form':form})