from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

class PostDetailView(DetailView):
	model = Post

class PostListView(ListView):
	model = Post

class PostCreateView(CreateView):
	model = Post
	fields = (['title'])
	def form_valid(self,form):
		instance = form.save(commit=False)
		return super().form_valid(form)
	def get_success_url(self):
		return "/"
