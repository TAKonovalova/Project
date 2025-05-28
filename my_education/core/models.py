from django.db import models

class Page(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    slug = models.SlugField("URL", unique=True)
    nav_title = models.CharField("Название в меню", max_length=30)
    priority = models.IntegerField("Приоритет", default=0)
    content = models.TextField("Контент")
    show_in_nav = models.BooleanField("Показывать в меню", default=True)

    class Meta:
        ordering = ['priority']
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def __str__(self):
        return self.title

class Person(models.Model):
    ROLE_CHOICES = [
        ('me', 'Я'),
        ('leader', 'Руководитель'),
        ('manager', 'Менеджер'),
        ('classmate', 'Сокурсник'),
    ]
    
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    role = models.CharField("Роль", max_length=10, choices=ROLE_CHOICES)
    full_name = models.CharField("ФИО", max_length=100)
    photo = models.ImageField("Фото", upload_to='photos/')
    email = models.EmailField("Email")
    phone = models.CharField("Телефон", max_length=20, blank=True)
    resume = models.FileField("Резюме", upload_to='resumes/', blank=True)
    description = models.TextField("Описание", blank=True)

    class Meta:
        verbose_name = "Персона"
        verbose_name_plural = "Персоны"

    def __str__(self):
        return self.full_name