

class DataMixin():
    paginate_by = 3
    title_page = None
    user_first_name = 'Гость'
    avatar = None
    extra_context = {}

    def __init__(self): # иницианилизация с добавление в пустой словарь переменных для отправки в основной класс представления

        self.extra_context['avatar'] = self.avatar
        if self.title_page:
            self.extra_context['title'] = self.title_page




    # def __init__(self):
    #     self.extra_context['user_first_name'] = self.user_first_name


    # def get_mixin_context(self, context, **kwargs): # создаем словарь
    #     context['menu'] = menu # расширяем словарь стандартной информацией
    #     context['cat_selected'] = None #
    #     context.update(kwargs) # добаваляем содержимое из параметра **kwards
    #     return context