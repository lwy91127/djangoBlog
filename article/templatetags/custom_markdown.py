# -*-coding:utf-8 -*-
import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library() #自定义filter必须加上

@register.filter(is_safe = True) #注册template filter
@stringfilter #字符串做参数
def custom_markdown(value):
    return mark_safe(markdown.markdown(value,
        extensions = ['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'],
                                       safe_mode=True,
                                       enable_attributes=False))
