django-template-korean
======================
Django template filter for Korean via sublee/korean module.

* http://github.com/sublee/korean


Installation
------------
via pip:

    $ pip install django-template-korean

Add the app to your istalled apps:

    INSTALLED_APPS = (
        ...
        'template_korean',
        ...
    )

Usage
-----
    {% load template_korean %}

    {{ message|proofread }}
        
Author
------
- Park, Hyunwoo \<ez.amiryo at gmail.com\>

Disclaimer
----------
Distributed under MIT license.
