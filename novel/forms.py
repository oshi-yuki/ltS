from django import forms
from .models import Story, Category, Tag, Comment

class StoryCreateForm(forms.ModelForm):

    class Meta:
        model = Story
        exclude = ('created_at', 'update_at')

class CategoryCreateForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

class TagCreateForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'

class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

class StorySearchForm(forms.Form):
    key_word = forms.CharField(label="キーワード", required=False, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'キーワード検索'}))
    category = forms.ModelChoiceField(label="カテゴリー", required=False, queryset=Category.objects.all(),)
