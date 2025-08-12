from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_bulma.layout import Layout, Field
from .models import UserInfoModel

# Initialize the form for UserInfoModel
# This form will be used for data entry in the home view
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfoModel
        fields = ['name', 'age', 'title', 'hometown']
    
    def __init__(self, *args, **kwargs):
        # Initialize the form with crispy forms helper
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'user-info-form'
        self.helper.form_class = 'mt-5'
        self.helper.form_method = 'post'
        self.helper.form_action = 'table_data'
        
        # Make labels appear next to fields instead of above
        self.helper.form_horizontal = True
        # Specify styling for each field using the helper
        # In this instance, just adding the placeholder text
        self.helper.layout = Layout(
            Field('name', placeholder='Name (required)'),
            Field('age', placeholder='Age (optional)'),
            Field('title', placeholder='Job Title (required)'),
            Field('hometown', placeholder='Hometown (optional)'),
        )
        
        # Include a submit button with the form from the helper
        self.helper.add_input(Submit('submit', 'Submit', css_class='is-primary'))
