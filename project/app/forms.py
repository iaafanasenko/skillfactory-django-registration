from django.forms import ModelForm, CharField, ChoiceField, \
    ModelChoiceField, ModelMultipleChoiceField, \
    CheckboxSelectMultiple, Textarea

from .models import Post, Author, Category, POST_TYPES


class CustomAuthorName(ModelChoiceField):
    def label_from_instance(self, author):
        return "%s" % author.user.username


class CustomCategoryName(ModelMultipleChoiceField):
    def label_from_instance(self, category):
        return "%s" % category.name


class PostForm(ModelForm):
    author = CustomAuthorName(
        label='Автор',
        queryset=Author.objects.all(),
        empty_label=None,
    )

    title = CharField(
        label='Заголовок',
        max_length=255,
    )

    text = CharField(
        label='Текст',
        max_length=1000,
        widget=Textarea,
    )

    post_category = CustomCategoryName(
        label='Категории',
        queryset=Category.objects.all(),
        widget=CheckboxSelectMultiple,
    )

    type = ChoiceField(
        label='Тип текста',
        choices=POST_TYPES,
    )

    class Meta:
        model = Post
        fields = ['author', 'title', 'text',
                  'post_category', 'type']
