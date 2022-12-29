from django_filters import FilterSet, CharFilter, DateTimeFilter, ModelMultipleChoiceFilter

from django.forms import DateTimeInput, CheckboxSelectMultiple

from .models import Post, Category


class PostFilter(FilterSet):
    title_filter = CharFilter(
        label='По названию',
        field_name='title',
        lookup_expr='icontains',
    )

    category_filter = ModelMultipleChoiceFilter(
        label='По категории',
        field_name='post_category__id',
        to_field_name='id',
        queryset=Category.objects.all(),
        widget=CheckboxSelectMultiple,
    )

    date_filter = DateTimeFilter(
        label='Опубликовано позднее',
        field_name='created_at',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = (
            'title_filter', 'category_filter', 'date_filter'
        )
