from django.shortcuts import render, resolve_url, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import Story, Category, Tag, Comment
from .forms import StoryCreateForm, CategoryCreateForm, TagCreateForm, CommentCreateForm, StorySearchForm
from django.db.models import Q
# Create your views here.
class Top(generic.TemplateView):
    template_name = 'novel/top.html'

class StoryList(generic.ListView):
    model = Story
    ordering = '-created_at'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        form =  StorySearchForm(self.request.GET or None)
        if form.is_valid():
            key_word = form.cleaned_data.get('key_word')
            if key_word:
                queryset = queryset.filter(Q(title__icontains=key_word) | Q(text__icontains=key_word))

            category = form.cleaned_data.get('category')
            if category:
                queryset = queryset.filter(category=category)


        return queryset

class StoryDetail(generic.DetailView):
    model = Story

class StoryCreate(generic.CreateView):
    model = Story
    form_class = StoryCreateForm
    success_url = reverse_lazy('novel:story_list')

class CategoryCreate(generic.CreateView):
    model = Category
    form_class = CategoryCreateForm
    success_url = reverse_lazy('novel:story_create')

class TagCreate(generic.CreateView):
    model = Tag
    form_class = TagCreateForm
    success_url = reverse_lazy('novel:story_create')

class StoryUpdate(generic.UpdateView):
    model = Story
    fields = ('text',)
    template_name = 'novel/story_update.html'


    def get_success_url(self):
        return resolve_url('novel:story_detail', pk=self.object.pk)

class CommentCreate(generic.CreateView):
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        story_pk = self.kwargs['pk']
        story = get_object_or_404(Story, pk=story_pk)
        comment = form.save(commit=False)
        comment.target = story
        comment.save()
        return redirect('novel:story_detail', pk=story_pk)


class StoryCategoryList(generic.ListView):
    model = Story
    ordering = '-created_at'
    paginate_by = 6

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return super().get_queryset().filter(category=category)

class StoryTagList(generic.ListView):
    model = Story
    ordering = '-created_at'
    paginate_by = 10

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs['pk'])
        return super().get_queryset().filter(tags=tag)

class Terms(generic.TemplateView):
    template_name = 'novel/terms.html'
