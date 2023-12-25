from django.db import models
class News(models.Model):
    title = models.CharField('Название', max_length=100)
    preview = models.CharField('Превью:', max_length=300)
    text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name ='Акция'
        verbose_name_plural ='Акции'

