from django.forms import ModelForm
from todo2.models import TODO
class TODOFORM(ModelForm):
    class Meta:
        model=TODO
        fields=["Title","Status","Priority"]