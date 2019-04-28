from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import comment
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.
def comment_show(request):
    comments = comment.objects.all().order_by('-post_date') # descending time order
    return render(request,'comment/comment_show.html',{'comments':comments})

def comment_search(request):
    #comment = MovieComment.objects.filter(comment_title= request.POST)
    #context = comment.comment_title
    query = request.GET.get('q')
    #value = "{{ request.GET.q}}"
    print("q is",query)
    #print(str(query))
    #print(str(query)=="111")
    #result = MovieComment.objects.get(comment_title = query)
    if query ==None:
        query = ' '

    results =  comment.objects.filter(Q(comment_title__icontains=query)|Q(content__icontains=query))
    print("result is ",results.values())
    if results.exists() == False:
        exist_result  = "no matching"
    else:
        exist_result  = "Search Result"
    context={'exists':exist_result,'results':results.values()}
    return render(request,'comment/comment_search.html',context)

class CommentListView(ListView):
    model = comment
    template_name = 'comment/comment_show.html' #????????????????????/
    context_object_name  = 'comments'
    ordering = ['-post_date']

class CommentDetailView(DetailView):
    model = comment
    template_name = 'comment/comment_detail.html'

class CommentCreateView(LoginRequiredMixin,CreateView):
    model = comment
    template_name = 'comment/comment_form.html'
    field = ['comment_title','content','movie_commented']
    form_class = CommentForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) # to parent class

class CommentUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = comment
    template_name = 'comment/comment_form.html'
    field = ['comment_title','content','movie_commented']
    form_class = CommentForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) # to parent class
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

class CommentDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = comment
    template_name = 'comment/comment_delete.html'
    success_url= '/'
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False
