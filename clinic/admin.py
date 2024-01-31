from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Pet, Onwer, Record, Veterinarian # импорт нашей модели

# Register your models here.

@admin.register(Pet) # регистрация нашей модели, через декоратор
class PetAdmin(admin.ModelAdmin): # класс чтобы в админе отображались параметры питомцев
    fields = ['nick_name', 'photo', 'post_photo', 'view', 'breed', 'age', 'gender']  # отображение полей формы редактирование записей объектов
    readonly_fields = ['post_photo']  # чтобы фотография выводилась в панеле редактирования
    list_display = ('id', 'nick_name', 'post_photo', 'view', 'breed', 'age', 'gender', 'weight', 'time_create') # отображение параметров из таблицы
    list_display_links = ('nick_name', ) # чтобы при нажатии мышкой отрывалось по названию, а не по id (ссылка)
    ordering = ['time_create'] # сортировка в админе - только для админа, старая сортировка в таблице также по методу в классе Meta в модели
    # list_editable = ('is_published',) # отображение значения  и возможности его редактирования в админе, но нужно поправлять в моделе параметр 'is_published', делать костыль так как нет булевого значения
    list_per_page = 5 # отображение количества статей
    # actions = ['set_published', 'set_draft'] # чтобы в действиях добавилось свое собственное действие для опубликования статьи, работа в связке со строкой 18

    @admin.display(description='История болезни', ordering='id') # декоратор для названия этого метода, 2й пар для сортировки, можно указывать только который есть в таблице
    def brief_info(self, pet: Pet): # метод для вывода в админ для контента данного питомца
        return f'История болезни {len(pet.medical_history)} символов.' #

    @admin.display(description='Фотография', ordering='nick_name')
    def post_photo(self, pet: Pet):
        if pet.photo:
            return mark_safe(f'<img src="{pet.photo.url}" width=50>') #  вывод фотографии
        else:
            return 'Без фото'

@admin.register(Onwer) # регистрация нашей модели, через декоратор
class OnwerAdmin(admin.ModelAdmin): # класс чтобы в админе отображались параметры питомцев
    list_display = ('id', 'firstname', 'lastname', 'email', 'tel') # отображение параметров из таблицы
    list_display_links = ('lastname', ) # чтобы при нажатии мышкой отрывалось по названию, а не по id (ссылка)
    ordering = ['id'] # сортировка в админе - только для админа, старая сортировка в таблице также по методу в классе Meta в модели
    # list_editable = ('is_published',) # отображение значения  и возможности его редактирования в админе, но нужно поправлять в моделе параметр 'is_published', делать костыль так как нет булевого значения
    list_per_page = 5 # отображение количества статей
    save_on_top = True  # отображение в редакторе сохранить снизу и на сверху, по умолчанию если нет этой записи только внизу
    # actions = ['set_published', 'set_draft'] # чтобы в действиях добавилось свое собственное действие для опубликования статьи, работа в связке со строкой 18

    # @admin.display(description='История болезни', ordering='medical_history') # декоратор для названия этого метода, 2й пар для сортировки, можно указывать только который есть в таблице
    # def brief_info(self, pet: Pet): # метод для вывода в админ для контента данной женщины
    #     return f'История болезни {len(pet.medical_history)} символов.' #

@admin.register(Veterinarian) # регистрация нашей модели, через декоратор
class VeterinarianAdmin(admin.ModelAdmin): # класс чтобы в админе отображались параметры питомцев
    fields = ['specialist', 'photo', 'post_photo', 'firstname', 'lastname', 'email', 'tel']
    readonly_fields = ['post_photo']  # чтобы фотография выводилась в панеле редактирования
    list_display = ('id', 'post_photo', 'specialist', 'firstname', 'lastname', 'email', 'tel') # отображение параметров из таблицы
    list_display_links = ('firstname', 'lastname',  ) # чтобы при нажатии мышкой отрывалось по названию, а не по id (ссылка)
    ordering = ['id'] # сортировка в админе - только для админа, старая сортировка в таблице также по методу в классе Meta в модели
    # list_editable = ('is_published',) # отображение значения  и возможности его редактирования в админе, но нужно поправлять в моделе параметр 'is_published', делать костыль так как нет булевого значения
    list_per_page = 5 # отображение количества статей
    save_on_top = True  # отображение в редакторе сохранить снизу и на сверху, по умолчанию если нет этой записи только внизу
    # actions = ['set_published', 'set_draft'] # чтобы в действиях добавилось свое собственное действие для опубликования статьи, работа в связке со строкой 18

    # @admin.display(description='История болезни', ordering='medical_history') # декоратор для названия этого метода, 2й пар для сортировки, можно указывать только который есть в таблице
    # def brief_info(self, pet: Pet): # метод для вывода в админ для контента данной женщины
    #     return f'История болезни {len(pet.medical_history)} символов.' #

    @admin.display(description='Фотография', ordering='nick_name')
    def post_photo(self, vet: Veterinarian):
        if vet.photo:
            return mark_safe(f'<img src="{vet.photo.url}" width=50>')  # вывод фотографии
        else:
            return 'Без фото'















