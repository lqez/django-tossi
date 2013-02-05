django-template-korean
======================
Django template filter for Korean via sublee/korean module.
sublee/korean module을 통해 제공되는 Django template filer입니다.

* http://github.com/sublee/korean

Notice
------
I wrote better version of this module within sublee/korean, and it had been merged into master.
So, if you're using latest version of sublee/korean, just use shipped korean.ext.django module. Thanks.

향상된 기능을 제공하는 버전이 sublee/korean의 master 브랜치에 병합되었습니다.
해당 모듈의 최신 버전을 사용하는 경우, 이 프로젝트보다 korean 모듈에 내장된 korean.ext.django 를 사용해주세요. 감사합니다.

Installation
------------
via pip:

    $ pip install django-template-korean

and add to your apps

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
- Park Hyunwoo \<ez.amiryo at gmail.com\>

Disclaimer
----------
Distributed under MIT license.
