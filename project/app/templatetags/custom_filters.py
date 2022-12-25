from django import template

bad_words = ['редиска']

register = template.Library()


@register.filter(name='censor')
def censor(value: str):
    for word in value.split():
        if word.lower() in bad_words:
            value = value.replace(word, f"{word[0]}{'*' * (len(word) - 1)}")
    return value
