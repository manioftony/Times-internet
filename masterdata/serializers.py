from rest_framework.serializers import ModelSerializer
from masterdata.models import *
from django.core.exceptions import ValidationError

field_data = {
    'employee': ('name', 'parent', 'is_featured', 'image','description','is_active')
}

def model_serializer_factory(mdl):
    class MasterSerializer(ModelSerializer):
        class Meta:
            model = mdl
            try:
                fields = field_data[mdl.__name__.lower()]
            except KeyError:
                pass
            error_messages = {'required': 'Please Type a Password'}

        def validate(self, attrs):
                name = attrs['name']
                if  name.isdigit():
                    raise ValidationError("  enter the %s only string"%mdl.__name__.lower())
                else:
                    checklist = mdl.objects.filter(name__iexact = name) 
                    if self.instance:
                        checklist = checklist.exclude(id=int(self.instance.id))
                    if checklist:
                        raise ValidationError("Name Already exist in %s"%mdl.__name__.lower())
                    else:
                        return attrs


    #
    return MasterSerializer



def filter_serializer_factory(mdl,filelddata):
    class FilterSerializer(ModelSerializer):
        class Meta:
            model = mdl
            try:
                fields = filelddata
            except KeyError:
                pass
            error_messages = {'required': 'Please Type a Password'}
    return FilterSerializer


