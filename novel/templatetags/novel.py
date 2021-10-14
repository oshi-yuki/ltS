from django import template
from novel.models import Category, Tag
from novel.forms import StorySearchForm

register = template.Library()

@register.inclusion_tag('novel/category_and_tag_list.html')
def create_category_and_tags_list():
    return {
        'category_list': Category.objects.all(),
        'tag_list': Tag.objects.all(),
    }

@register.inclusion_tag('novel/search_form.html')
def story_search(request):
    form = StorySearchForm(request.GET or None)
    return {'form': form}

@register.simple_tag
def url_replace(request, field, value):
    url_dict = request.GET.copy()
    url_dict[field] = str(value)
    return url_dict.urlencode()
