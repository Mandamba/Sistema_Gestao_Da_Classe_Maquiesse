from xhtml2pdf import pisa
from django.template.loader import get_template
def render_to_pdf(template_src, contex_dict={}):
    return True