from flask_admin.contrib.sqla import ModelView
from wtforms import TextAreaField
from wtforms.widgets import TextArea


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += " ckeditor"
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)

class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()

class PageModelView(ModelView):
    form_overrides = dict(contents=CKTextAreaField)
    create_template = 'admin/ckeditor.html'
    edit_template = 'admin/ckeditor.html'

