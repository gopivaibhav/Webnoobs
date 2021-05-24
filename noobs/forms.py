from django.forms import ModelForm
from .models import Query

class Queryform(ModelForm):
    class Meta:
        model=Query
        fields='__all__'