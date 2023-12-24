from django.db import models

class Client(models.Model):
    first_name = models.CharField('Как вас зовут?', max_length=30)
    phone_number = models.CharField('Напишите ваш номер телефона:', max_length=11)
    Sketch = models.CharField('Есть ли у вас свой эскиз?(Да/Нет)', max_length=3)
    date = models.DateTimeField('Когда будет удобно набить татушку?')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name= 'Клиент'
        verbose_name_plural= 'Клиенты'