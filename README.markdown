# Django-Decorators

## Overview

This is just a collection of custom decorators I have created for various projects that I wanted all in
one place that I can easily update and also share with the Django community.

## Installation

If you clone this project in your project application add the following to your INSTALLED_APPS

projectname.django-decorators

## Usage

### auth.group_required

<pre><code>from django-decorators.auth import group_required

@group_required(["group1", "group2"])
def show_index(request):
    view_code_here</code></pre>

### render.render

This is a decorator that makes it easy to render quick templates where you just want 
to push in quick data from a model

<pre><code>from django-decorators.render import render

@render("path/to/template.html")
def show_index(request):
    return {'objects': Model.objects.all()}</code></pre>
    
