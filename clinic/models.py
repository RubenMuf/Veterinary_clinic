from django.db import models
from django.urls import reverse # для метода get_absolute_url(self)

# Create your models here.

class Pet(models.Model):
    view = models.CharField(max_length=10, verbose_name='Вид')
    breed = models.CharField(max_length=20, verbose_name='Порода')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None,
                              blank=True, null=True, verbose_name='Фото')
    nick_name = models.CharField(max_length=10, verbose_name='Кличка')
    age = models.IntegerField(verbose_name='Возраст лет')
    weight = models.IntegerField(verbose_name='Вес кг.')
    gender = models.CharField(max_length=10, verbose_name='Пол')
    # связи с другими таблицами
    onwer = models.ForeignKey('Onwer', on_delete=models.PROTECT, related_name='onwers', null=True, verbose_name='Хозяин') # многие к одному связываем наш класс с классом 'Onwer' через многие к одному и обязательно пишем как строка в ковычках, так как этот класс находится ниже нашего основного класса и пайчарм его попросту не увидет, вторым параметром ставим, который будет запрещать удалять категории которые не связаны с постами, 3й параметр если связываться наоборот через class Onwer c classom Pet
    time_create = models.DateTimeField(auto_now_add=True, null=True,  verbose_name='Время создания')  # параметр автоматически заполняет поле но только в момент добавление записи, тоесь показывает время появление записи
    # image = models.CharField(max_length=12, null=True, verbose_name='Фото')
    medical_history = models.TextField(max_length=1000, unique=True, null=True, verbose_name='История болезни')
    slugPet = models.SlugField(max_length=20, unique=True, db_index=True, verbose_name='Slug', null=True)  # слаг для пути 1пар - макс. длина, 2пар - уникальность, 3пар - поле индексируемое, 4пар - чтобы создавалось поле с пустым значением
    # veterinarian = models.ManyToManyField('Veterinarian', blank=True, related_name='veterinarians')  # связываем с таблицей Veterinarian через связь многие ко многим, blank=True - потому что не каждая запись питомца будет содержать ветеринара, related_name='veterinarian_' - чтобы мы могли через ветеринаров получать список питомцев которые с ними связаны. on_delete - в этой связи отсутствует. Именно через этод ветеринара всязываются записи с остальными. пример: a.veterinarian_.set([tag_br, tag_o, tag_v])

    def __str__(self):
        return f'{self.breed} {self.nick_name}'

    def get_absolute_url(self):
        return reverse('info_pet', args=[self.id, self.slugPet]) # формируем slug (берется из поля таблицы) который потом передаем в ссылку во hrev на страницу и по этой ссылке ужже создается путь в url


    class Meta: # класс для сортировки отображение на странице в данном случае по времени созданию записи (задать реверс поставить минус перед параметром)
        verbose_name = 'Питомцы' # это для кабинета админа чтобы заголовок имел такое название
        verbose_name_plural = 'Питомцы' # для того чтобы этот заголовок был без в конце 's' и был в множественном числе
        ordering = ['time_create'] # сортируем по артрибуту по убыванию по умолчанию
        indexes = [
            models.Index(fields=['time_create'])
        ]

class Onwer(models.Model):
    firstname = models.CharField(max_length=10, verbose_name='Имя')
    lastname = models.CharField(max_length=15, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='E-mail')
    tel = models.CharField(max_length=12, verbose_name='Телефон')

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    class Meta: # класс для сортировки отображение на странице в данном случае по времени созданию записи (задать реверс поставить минус перед параметром)
        verbose_name = 'Хозяин' # это для кабинета админа чтобы заголовок имел такое название
        verbose_name_plural = 'Хозяева' # для того чтобы этот заголовок был без в конце 's' и был в множественном числе
        ordering = ['id'] # сортируем по артрибуту по убыванию по умолчанию
        indexes = [
            models.Index(fields=['id'])
        ]

class Veterinarian(models.Model):
    specialist = models.CharField(max_length=15, verbose_name='Специалист')
    firstname = models.CharField(max_length=10, verbose_name='Имя')
    lastname = models.CharField(max_length=15, verbose_name='Фамилия')
    email = models.EmailField(max_length=20, verbose_name='E-mail')
    tel = models.CharField(max_length=12, verbose_name='Телефон')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None,
                              blank=True, null=True, verbose_name='Фото')
    history = models.TextField(max_length=1000, unique=True, null=True, verbose_name='О докторе')
    certificates = models.CharField(max_length=12, null=True)

    slugVet = models.SlugField(max_length=20, unique=True, db_index=True, verbose_name='Slug', null=True)  # слаг для пути 1пар - макс. длина, 2пар - уникальность, 3пар - поле индексируемое, 4пар - чтобы создавалось поле с пустым значением

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    def get_absolute_url(self):
        return reverse('info_vet', args=[self.id, self.slugVet])  # формируем slug (берется из поля таблицы) который потом передаем в ссылку во hrev на страницу и по этой ссылке ужже создается путь в url

    class Meta: # класс для сортировки отображение на странице в данном случае по времени созданию записи (задать реверс поставить минус перед параметром)
        verbose_name = 'Ветеринар' # это для кабинета админа чтобы заголовок имел такое название
        verbose_name_plural = 'Ветеринары' # для того чтобы этот заголовок был без в конце 's' и был в множественном числе
        ordering = ['id'] # сортируем по артрибуту по убыванию по умолчанию
        indexes = [
            models.Index(fields=['id'])
        ]

class Record(models.Model):
    veterinarian = models.ManyToManyField(Veterinarian, blank=True, related_name='veterinarians')  # связываем с таблицей Veterinarian через связь многие ко многим, blank=True - потому что не каждая запись питомца будет содержать ветеринара, related_name='veterinarian_' - чтобы мы могли через ветеринаров получать список питомцев которые с ними связаны. on_delete - в этой связи отсутствует. Именно через этод ветеринара всязываются записи с остальными. пример: a.veterinarian_.set([tag_br, tag_o, tag_v])
    pet = models.ManyToManyField(Pet, blank=True, related_name='pets') # связываем с таблицей Pet через связь многие ко многим, blank=True - потому что не каждать запись женщин будет содержать теги, related_name='tags' - чтобы мы могли через теги получать список статей которые с ними связаны. on_delete - в этой связи отсутствует. Именно через этод тэг всязываются записи с остальными. пример: a.tags2.set([tag_br, tag_o, tag_v])
    data = models.CharField(max_length=10)
    time = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.veterinarian} {self.pet} {self.data}'

class UploadFiles(models.Model): # таблица для загрузки фотографий
    file = models.FileField(upload_to='uploads_model') # параметр для указания пути в какую папку загружать


from django.contrib.auth import get_user_model

from mptt.models import MPTTModel, TreeForeignKey
User = get_user_model()
class Comment(MPTTModel):
    """
    Модель древовидных комментариев
    """

    STATUS_OPTIONS = (
        ('published', 'Опубликовано'),
        ('draft', 'Черновик')
    )

    article = models.ForeignKey(Veterinarian, on_delete=models.CASCADE, verbose_name='Ветеринар', related_name='comments')
    author = models.ForeignKey(User, verbose_name='Автор отзыва', on_delete=models.CASCADE, related_name='comments_author')
    content = models.TextField(verbose_name='Текст отзыва', max_length=3000)
    time_create = models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновления', auto_now=True)
    status = models.CharField(choices=STATUS_OPTIONS, default='published', verbose_name='Статус поста', max_length=10)
    parent = TreeForeignKey('self', verbose_name='Родительский комментарий', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    class MTTMeta:
        order_insertion_by = ('-time_create',)

    class Meta:
        db_table = 'app_comments'
        indexes = [models.Index(fields=['-time_create', 'time_update', 'status', 'parent'])]
        ordering = ['-time_create']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.author}:{self.content}'








