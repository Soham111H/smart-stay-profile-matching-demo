from django import template
register=template.Library()
@register.filter
def pct(value): return int(round(float(value)*100))
