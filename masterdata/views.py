from django.shortcuts import render
from django.apps import apps
from rest_framework import generics as g
from masterdata.serializers import model_serializer_factory,filter_serializer_factory
from rest_framework.response import Response
from rest_framework.decorators import api_view
from masterdata.models import Category

# Create your views here.



class JsonManager(object):

    def dispatch(self, *args, **kwargs):
        return super(JsonManager, self).dispatch(*args, **kwargs)

    def get_mdl(self):
        myapp = apps.get_app_config('masterdata')
        return myapp.models[self.kwargs['model']]

    def get_queryset(self):
        mdl = self.get_mdl()
        return mdl.objects.all()

    def get_serializer_class(self):
        return model_serializer_factory(self.get_mdl())

    def get_object(self):
        qs = self.get_queryset()
        return qs.get(id=self.kwargs.get('object_id'))





class ListCFeed(JsonManager, g.ListAPIView):
    pass


class AddCFeed(JsonManager, g.CreateAPIView):

    pass



class EditCFeed(JsonManager, g.UpdateAPIView):
    def post(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)


class ActiveCFeed(JsonManager, g.DestroyAPIView):

    def perform_destroy(self, instance):
        instance.is_active = {0: 2, 2: 0}[instance.is_active]
        self.message = '%s %s successfully' % (
            self.kwargs.get('model'),
            {2: 'activated', 0: 'deactivated'}[instance.is_active])
        instance.save()
        return Response({"status":self.message})




@api_view(['GET'])
def category_filter(request):
    if request.method == 'GET':
        try:
            data = request.GET.get('params').split('|')
            data = [{'name':i.name,'id':i.id,'is_featured':i.is_featured} for  i in Category.objects.all()  ]
            return Response({'data':data,'status':True})
        except Exception as e:
            return Response({'data':e,'status':False})






class FilterManager(object):

    def dispatch(self, *args, **kwargs):
        return super(FilterManager, self).dispatch(*args, **kwargs)

    def get_mdl(self):
        myapp = apps.get_app_config('masterdata')
        return myapp.models['category']

    def get_queryset(self):
        return Category.objects.all()

    def get_serializer_class(self):
        fields = self.request.GET.get('params').split('|')
        return filter_serializer_factory(self.get_mdl(),fields)





class FliterFeed(FilterManager, g.ListAPIView):
    pass





