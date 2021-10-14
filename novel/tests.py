from django.test import TestCase
from django.urls import reverse

from .models import Story,Category, Comment
# Create your tests here.
class TestStoryList(TestCase):
    def test_get(self):
        category = Category.objects.create(name='カテゴリー１')
        Story.objects.create(title="テスト一", text="あの頃は確か、、、", category=category)
        Story.objects.create(title="テスト弐", text="確かあの子はどこかで", category=category)
        story = Story.objects.all()

        res = self.client.get(reverse('novel:story_list'))
        self.assertTemplateUsed(res, 'novel/story_list.html')
        self.assertContains(res, "テスト一")
        self.assertContains(res, "あの頃は確か、、、")
        self.assertContains(res, "テスト弐")
        self.assertContains(res, "確かあの子はどこかで")
        self.assertContains(res, "カテゴリー１")
        self.assertEqual(story.count(), 2 )


class TestStoryDetail(TestCase):
    def test_get(self):
        category = Category.objects.create(name="カテゴリー1")
        Story.objects.create(id=1, title="テスト１", text="こんにちは、おはようございます。", category=category)
        res = self.client.get(reverse('novel:story_detail', args=(1, )))
        self.assertTemplateUsed(res, 'novel/story_detail.html')
        self.assertContains(res, 'テスト１')
        self.assertContains(res, 'こんにちは、おはようございます。')
        self.assertContains(res, 'カテゴリー1')

    def test_404(self):
        res = self.client.get(reverse('novel:story_detail', args=(1, )))
        self.assertEqual(res.status_code, 404)



class TestCreate(TestCase):
    def test_form(self):
        category = Category.objects.create(name="カテゴリー1")
        res = self.client.post('novel:story_create', {'title':'テスト１', 'text':'hello', 'category': category})
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'novel/story_form.html')



class TestStoryUpdate(TestCase):
    def test_get(self):
        category = Category.objects.create(name="カテゴリー1")
        story = Story.objects.create(id=1, title="青春", text="おはようございます。こんにちは", category=category)
        res = self.client.get(reverse('novel:story_update', args=(1, )))
        self.assertTemplateUsed(res, 'novel/story_update.html')
        self.assertEqual(res.context['form'].instance, story)
        self.assertEqual(res.context['story'], story)

    def test_post(self):
        category = Category.objects.create(name="カテゴリー1")
        story = Story.objects.create(id=1, title="青春", text="おはようございます。こんにちは", category=category)
        res = self.client.post(reverse('novel:story_update', args=(1, )), data={'text': 'さようなら'})
        self.assertRedirects(res, reverse('novel:story_detail', args=(story.id, )))
        story.refresh_from_db()
        self.assertEqual(story.text, 'さようなら')


    def test_404(self):
        res = self.client.post(reverse('novel:story_update', args=(1, )), data={'text': 'hello'})
        self.assertEqual(res.status_code, 404)
