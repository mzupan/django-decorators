# Django-Decorators

## Overview

This is just a collection of custom decorators I have created for various projects that I wanted all in
one place that I can easily update and also share with the Django community.

## Installation

If you clone this project in your project application add the following to your INSTALLED_APPS

projectname.django-decorators

## Usage

### group_required

<code><pre>
from django-decorators.auth import django-decorators

@group_required(["group1", "group2"])
def show_index(request):
    ....
</code></pre>
