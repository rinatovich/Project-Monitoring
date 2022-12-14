from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse


class Manager(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Менеджеры'
        verbose_name_plural = 'Менеджеры'


class Company(models.Model):
    objects = None
    title = models.CharField(max_length=250, verbose_name='Название организации')
    image = models.FileField(upload_to='images/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Организации'
        verbose_name_plural = 'Организации'


class Status(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    className = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class FieldItem(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поля категорий'
        verbose_name_plural = 'Поля категорий'
        ordering = ['id']


class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True, blank=True)
    fields = models.ManyToManyField(FieldItem, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True, blank=True)
    text = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user} прокоментировал {self.text}'


class Project(models.Model):
    COMPLETED = 'Завершено'
    SUSPENDED = 'Приостановлено'
    IN_PROGRESS = 'В процессе'
    STATUS_CHOICES = [
        (COMPLETED, 'Завершено'),
        (SUSPENDED, 'Приостановлено'),
        (IN_PROGRESS, 'В процессе'),
    ]
    title = models.CharField(max_length=250, null=True, blank=True, verbose_name="Наименование объекта")
    work_statement = models.TextField(null=True, blank=True, verbose_name="Описание работ")
    contract_id = models.CharField(max_length=250, null=True, blank=True, verbose_name="№ договора")
    customer = models.CharField(max_length=250, null=True, blank=True, verbose_name="Заказчик")
    executor_company = models.ManyToManyField(Company, verbose_name="Ответстве", null=True, blank=True)
    deadline = models.DateField(null=True, blank=True, verbose_name="Сроки исполнения")
    cat = models.ForeignKey(Category, verbose_name="Категория", null=True, blank=True, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Статус")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True, blank=True)
    note = models.ManyToManyField(Note, verbose_name="Поручение", null=True, blank=True, )
    system = models.CharField(max_length=250, null=True, blank=True, verbose_name="Система")
    state = models.CharField(max_length=300, null=True, blank=True, verbose_name="Состояние")
    problems = models.CharField(max_length=300, null=True, blank=True, verbose_name="Проблемные вопросы")
    activities = models.CharField(max_length=300, null=True, blank=True, verbose_name="Мероприятия")
    finance = models.CharField(max_length=300, null=True, blank=True, verbose_name="Финансовые вопросы")
    work_reason = models.CharField(max_length=300, null=True, blank=True, verbose_name="Основания для выполнения работ")
    notice = models.TextField(null=True, blank=True, verbose_name="Примечание")
    manager = models.ManyToManyField(Manager, verbose_name="Менеджеры", null=True, blank=True)


    def alert(self):
        current_datetime = datetime.now()
        for n in self.note.all():
            if n.created_at.day == current_datetime.day and n.created_at.month == current_datetime.month:
                return True
        return False

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Проекты'
        verbose_name_plural = 'Проекты'
        ordering = ['id']


