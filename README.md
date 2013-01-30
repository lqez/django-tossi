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

Usage in django template
-----------------
    {% load template_korean %}
    <!-- before: 박현우(은)는 똥(을)를 쌌다. -->
    {{ message|proofread }}
    <!-- after: 박현우는 똥을 쌌다. -->
        
Author
------
- Park, Hyunwoo \<ez.amiryo at gmail.com\>

Disclaimer
----------
Distributed under MIT license.
