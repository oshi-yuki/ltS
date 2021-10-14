from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField('タグ名', max_length=255, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=255, unique=True)

    def __str__(self):
        return self.name


class Story(models.Model):
    title = models.CharField('タイトル', max_length=50)
    text = models.TextField('ストーリー')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='カテゴリ')
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    update_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField('コメント')
    target = models.ForeignKey(Story, on_delete=models.PROTECT, verbose_name='感想')

    def __str__(self):
        return self.text[:10]
