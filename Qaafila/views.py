from django.shortcuts import render, get_object_or_404, redirect
from .models import Darja, hashTag
from .forms import DarjaForm, CommentForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse

# Create your views here.

def home(request):
  form = DarjaForm(request.POST or None)
  tags1 =  hashTag.objects.all()[:3]
  tags2 =  hashTag.objects.all()[3:]
  # print('META----------------------------',request.META)
  query = request.GET.get('q')
  if query:
    posts = Darja.objects.filter(text__contains=query)
  else:
    posts = Darja.objects.all()
  paginator = Paginator(posts, 5) # Show 5 contacts per page
  page = request.GET.get('page')
  posts = paginator.get_page(page)
  if request.POST:
    if form.is_valid():
      instance = form.save(commit=False)
      instance.user = request.user
      instance.save()
      messages.success(request, 'Post created successfully!!!')
      return redirect('home')
  context = {'posts':posts, 'form':form, 'htags1':tags1, 'htags2':tags2}
  return render(request, 'home.html', context)

def detail(request, id):
  post = get_object_or_404(Darja, pk=id)
  form = CommentForm(request.POST or None)
  if request.POST:
    if form.is_valid():
      instance = form.save(commit=False)
      instance.commenter = request.user
      instance.post = post
      instance.save()
      return redirect(reverse('detail', kwargs={'id':instance.post.pk}))
  
  context = {'post':post, 'form':form}
  return render(request, 'detail.html', context)

def like_post(request, id):
  print('META',request.META['HTTP_REFERER'])
  post = get_object_or_404(Darja, pk=id)
  if request.user in post.likes.all():
    post.likes.remove(request.user)
  else:
    post.likes.add(request.user)
  return redirect(request.META['HTTP_REFERER'])

def get_hash_tag_data(request, tag):
  obj, created = hashTag.objects.get_or_create(tag_name=tag)
  posts = Darja.objects.filter(text__contains='#'+str(tag))
  if created:
    obj.save()
  context = {'tag_posts':posts}
  return render(request, 'tags.html', context)

# def update_top_tags(request):
#   tags =  hashTag.objects.all()[:5]
#   context = {'tags':tags}
#   return render(request, 'base.html', context)
