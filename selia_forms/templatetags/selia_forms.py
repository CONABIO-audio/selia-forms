from django import template

from crispy_forms.templatetags.crispy_forms_filters import as_crispy_form
from widget_tweaks.templatetags.widget_tweaks import add_class as widget_tweaks_add_class

register = template.Library()


@register.filter(name='selia_form')
def selia_form(form, label_class="", field_class=""):
    return as_crispy_form(
        form,
        template_pack='bootstrap4',
        label_class=label_class,
        field_class=field_class)


@register.filter(name='add_class')
def add_class(form, css_class):
    return widget_tweaks_add_class(form, css_class)
