from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название категории") #поле для хранения названия категории (уникальное)

    def __str__(self):
        return self.name

class Request(models.Model):
    STATUS_CHOICES = [  #статусы
        ('new', 'Новая'),
        ('in_progress', 'Принята в работу'),
        ('completed', 'Выполнена'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь:") #заявка и пользователь(связь)
    title = models.CharField(max_length=200, verbose_name="Название заявки:") #текстовое поле до 200 сим-ов
    description = models.TextField(verbose_name="Описание:") #текстовое поле
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория:") #заявка и категории(связь)
    image = models.ImageField(upload_to='uploads/', verbose_name="Фотография помещения") #фото
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания:") #автомат-я дата заявки
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Статус") #статусы(прописаны выше)

    def __str__(self):
        return self.title
