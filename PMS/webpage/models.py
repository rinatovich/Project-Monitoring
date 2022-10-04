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
    notice = models.TextField(null=True, blank=True, verbose_name="Примечание")
    customer = models.CharField(max_length=250, null=True, blank=True, verbose_name="Заказчик")
    manager = models.ManyToManyField(Manager, verbose_name="Менеджеры", null=True, blank=True)
    executor_company = models.ManyToManyField(Company, verbose_name="Ответстве", null=True, blank=True)
    deadline = models.DateField(null=True, blank=True, verbose_name="Сроки исполнения")
    cat = models.ForeignKey(Category, verbose_name="Категория", null=True, blank=True, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Статус")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Проекты'
        verbose_name_plural = 'Проекты'
        ordering = ['id']
