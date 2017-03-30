# DRF-Spirit

A pluggable django forum application build with Django Rest Framework inspired from [Spirit](https://github.com/nitely/Spirit).

---

# Requirements

* Python (2.7.x)
* Django (1.8, 1.9, 1.10)
* Django Rest Framework (3.5+)


# Installation

Add `'drf_spirit'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = (
        ...
        'drf_spirit',
    )


# Settings
Adding ``USER_SLUG_FIELD`` configuration in the settings will allow you to use user slug instead of pk for user relationship. You can do like following:

    DRF_SPIRIT = {
        'USER_SLUG_FIELD': 'slug'
    }
