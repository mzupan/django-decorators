try:
    from functools import wraps
except:
    from django.utils.functional import wraps

from django.contrib.auth.models import Group
from django.http import Http404

def group_required(groups=[]):
    def decorator(func):
        def inner_decorator(request,*args, **kwargs):
            
            
            for group in groups:
                try:
                    if Group.objects.get(name=group) in request.user.groups.all():
                        return func(request, *args, **kwargs)
                except:
                    pass
            
            raise Http404()
        
        return wraps(func)(inner_decorator)
    
    return decorator