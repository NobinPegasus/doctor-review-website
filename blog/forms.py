from django import forms
from bootstrap_datepicker_plus import TimePickerInput
from django_starfield import Stars
from .models import Post
# from .widgets import BootstrapDateTimePickerInput


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','chamber','address','fees','days','start_time','end_time','image','review','rating','overall_rating']


    #     date = forms.DateTimeField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=BootstrapDateTimePickerInput()
    # )
        widgets = {
            # 'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
            # 'hours' : TimePickerInput().start_of('party time'),
            # 'hours': DateInput(attrs={'class': 'datepicker'})
            # 'hours': forms.DateField(widget=forms.DateInput(attrs={'class':'timepicker'}))
            # 'hours': TimePickerInput(),
            'start_time':TimePickerInput().start_of('party time'),
            'end_time':TimePickerInput().end_of('party time'),
            'rating': Stars,
        }
