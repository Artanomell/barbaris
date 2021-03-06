# -*- coding: utf-8 -*-
"""
###############################################################################
# Copyright 2012 Grigoriy Kramarenko.
###############################################################################
# This file is part of Barbaris.
#
#    Barbaris is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Barbaris is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Barbaris.  If not, see <http://www.gnu.org/licenses/>.
#
# Этот файл — часть Barbaris.
#
#   Barbaris - свободная программа: вы можете перераспространять ее и/или
#   изменять ее на условиях Стандартной общественной лицензии GNU в том виде,
#   в каком она была опубликована Фондом свободного программного обеспечения;
#   либо версии 3 лицензии, либо (по вашему выбору) любой более поздней
#   версии.
#
#   Barbaris распространяется в надежде, что она будет полезной,
#   но БЕЗО ВСЯКИХ ГАРАНТИЙ; даже без неявной гарантии ТОВАРНОГО ВИДА
#   или ПРИГОДНОСТИ ДЛЯ ОПРЕДЕЛЕННЫХ ЦЕЛЕЙ. Подробнее см. в Стандартной
#   общественной лицензии GNU.
#
#   Вы должны были получить копию Стандартной общественной лицензии GNU
#   вместе с этой программой. Если это не так, см.
#   <http://www.gnu.org/licenses/>.
###############################################################################
"""
# Django settings for this project.

from django.utils.translation import ugettext_lazy as _
import os

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
def abspath(*paths):
    return os.path.abspath(os.path.join(PROJECT_PATH, *paths)).replace('\\','/')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Grigoriy Kramarenko', 'root@rosix.ru'),
)
MANAGERS = ADMINS

try:
    f = open(abspath('AUTHORS'), 'rb')
    AUTHORS = f.readlines()
    f.close()
except:
    AUTHORS = ('Webmaster Name', 'Manager Name')
COPYRIGHT = u'Григорий Крамаренко / www.rosix.ru'
COPYRIGHT_YEAR = 2010 # start year of copyright
PROJECT_NAME = u'АИС «Барбарис»'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': abspath('sqlite.db'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Vladivostok' #'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

LOCALE_PATHS = (
    # abspath('locale'),
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = abspath('..', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = abspath('..', 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #abspath('static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'generate-this-unique-key!!!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    abspath("templates"),
    abspath("app","templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = ('django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    # append:
    'django.core.context_processors.request'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    #~ 'project.auth_fix',
    'project.app',
    'pytils',
)

# Settings for applications:

START_YEAR = 2011
DEFAULT_ANALYSE_DAYS = 7

STATE_ORDER_CREATE   = 1
STATE_ORDER_ACCEPT   = 2
STATE_ORDER_CLOSE    = 3
STATE_ORDER_CANCEL   = 4
STATE_ORDER_TRASH    = 5
STATE_ORDER_CHOICES = (
        (STATE_ORDER_CREATE, u'Создан'),
        (STATE_ORDER_ACCEPT, u'Принят'),
        (STATE_ORDER_CLOSE,  u'Закрыт'),
        (STATE_ORDER_CANCEL, u'Отменён'),
        (STATE_ORDER_TRASH,  u'Удалён'),
    )
SELECT_LIST_ORDERS = [1,2,3,4]
SELECT_WORK_ORDERS = [2,3]

STATE_INVOICE_CREATE   = 1
STATE_INVOICE_AVANCE   = 2
STATE_INVOICE_PAYMENT  = 3
STATE_INVOICE_TRASH    = 4
STATE_INVOICE_CHOICES = (
        (STATE_INVOICE_CREATE,  u'Создан'),
        (STATE_INVOICE_AVANCE,  u'Аванс'),
        (STATE_INVOICE_PAYMENT, u'Оплачен'),
        (STATE_INVOICE_TRASH,   u'Удалён'),
    )
SELECT_INVOICES = [1,2,3]
SELECT_WORK_INVOICES = [1,2,3]
SELECT_CASH_INVOICES = [2,3]

PAYMENT_INVOICE_CASH      = 1
PAYMENT_INVOICE_CASHLESS  = 2
PAYMENT_INVOICE_CARD      = 3
PAYMENT_INVOICE_CHOICES = (
        (PAYMENT_INVOICE_CASH,     u'Наличный'),
        (PAYMENT_INVOICE_CASHLESS, u'Безналичный'),
        (PAYMENT_INVOICE_CARD,     u'Карта банка'),
    )

DIVIDER_DAY   = 1
DIVIDER_HOUR  = 2
DIVIDER_MONTH = 3
DIVIDER_PRICE_CHOICES = (
        (DIVIDER_DAY, u'Сутки'),
        (DIVIDER_HOUR, u'Час'),
        (DIVIDER_MONTH, u'Месяц'),
    )

CATEGORY_CHOICES = (
        (u'Hotel',u'Гостиница'),
        (u'Sauna',u'Сауна'),
        (u'Kitchen',u'Кухня'),
        (u'Parking',u'Автостоянка'),
    )

DOCUMENT_CHOICES = (
        ('act', u'Акт'),
        ('invoice', u'Счёт'),
        ('person', u'Карточка персоны'),
        ('org', u'Карточка организации'),
    )

STATE_ROOM_FREE                 = u'Свободен сейчас и в дальнейшем.'
STATE_ROOM_NONFREE              = u'Свободен сейчас, но заказан в дальнейшем.'
STATE_ROOM_RELEASED_FREE        = u'Освобождается сегодня, свободен в дальнейшем.'
STATE_ROOM_RELEASED_NONFREE     = u'Освобождается сегодня, но заказан в дальнейшем.'
STATE_ROOM_NONRELEASED_FREE     = u'Занят, нет дальнейших заказов.'
STATE_ROOM_NONRELEASED_NONFREE  = u'Занят, есть дальнейшие заказы.'

BUTTON_CLASSES_STATE_ROOM = {
    STATE_ROOM_FREE: 'btn btn-success',
    STATE_ROOM_NONFREE: 'btn',
    STATE_ROOM_RELEASED_FREE: 'btn btn-info',
    STATE_ROOM_RELEASED_NONFREE: 'btn btn-warning',
    STATE_ROOM_NONRELEASED_FREE: 'btn btn-primary',
    STATE_ROOM_NONRELEASED_NONFREE: 'btn btn-danger',
}

ESTIMATED_TIME = True
ESTIMATED_TIME_HOUR = 12
ESTIMATED_TIME_MINUTE = 0

GROUP_ADMINS = u'Администраторы'
GROUP_MANAGERS = u'Менеджеры'
GROUP_OPERATORS = u'Операторы'
SELECT_WORK_GROUPS = (
    GROUP_MANAGERS, GROUP_OPERATORS,
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# This import re-definition current top settings, 
# e.g. DATABASES, SECRET_KEY, etc.
# Default path: ../securesettings.py
# outer from project paths and unavailable in Mercurial repository. 
try:
    from securesettings import *
except:
    pass
