from django import template

register = template.Library()


@register.filter(name='censor')
def censor(value):
    bad_words = ('редиска', 'морковка', 'проект')

    if not isinstance(value, str):
        raise TypeError(f"unresolved type '{type(value)}' expected  type 'str'")

    for word in value.split():
        if word.lower() in bad_words:
            value = value.replace(word, f"{word[0]}{'*' * (len(word) - 1)}")
    return value

# @register.filter(name='censor')
# def censor(value):
#     if isinstance(value, str):
#         result = str(value)
#         for key in words_dict.keys():
#             result = result.replace(key, words_dict[key])
#             return result
#     else:
#         raise ValueError(f'Нельзя отфильтровать тип, отличный от {type(value)}')
