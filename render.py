try:
    from functools import wraps
except:
    from django.utils.functional import wraps

from django.template import RequestContext
from django.shortcuts import render_to_response

def render(t):
    def decorator(func):
        def inner_decorator(request, *args, **kwargs):
            return render_to_response(t, func(request, *args, **kwargs), context_instance = RequestContext(request))
        
        return wraps(func)(inner_decorator)
    
    return decorator