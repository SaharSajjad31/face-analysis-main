from django import forms
from home.models import Images
from crispy_forms import helper, layout


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = helper.FormHelper()
        self.helper.layout = layout.Layout(
            'image',
            layout.Column(
                layout.Submit('submit', 'Upload', css_class='m-0'),
                css_class="p-0 d-flex justify-content-end"
            )
        )


