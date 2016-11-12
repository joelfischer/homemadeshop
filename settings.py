# Django settings for homemadeshop project.
import os, socket
#ROOT_PATH = os.path.dirname(__file__)
ROOT_PATH = os.path.dirname(__file__)
gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('jef', 'jef@cs.nott.ac.uk'),
)

MANAGERS = ADMINS

devHosts = ['Sartre.local']
hostname = socket.gethostname()

HOSTING = 'DEV'
if hostname not in devHosts:
    HOSTING = 'PROD'
else:
    HOSTING = 'DEV'

if HOSTING =='DEV':
    DATABASES = {
                 'default': {
                             'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
                             'NAME': '/Users/jef/Dev/homemadeshop/db/sqlite.db',                      # Or path to database file if using sqlite3.
                             'USER': '',                      # Not used with sqlite3.
                             'PASSWORD': '',                  # Not used with sqlite3.
                             'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
                             'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
                             }
                 }
    #EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    #EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    
else:
    DATABASES = {
                 'default': {
                             'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
                             'NAME': 'homemadeshop_db',                       # Or path to database file if using sqlite3.
                             'USER': 'homemade',                      # Not used with sqlite3.
                             'PASSWORD': 'h0mem4de!',                  # Not used with sqlite3.
                             'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
                             'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
                             }
                 }
    import email_settings
    EMAIL_USE_TLS = email_settings.EMAIL_USE_TLS
    EMAIL_HOST = email_settings.EMAIL_HOST 
    EMAIL_HOST_PASSWORD = email_settings.EMAIL_HOST_PASSWORD 
    EMAIL_HOST_USER = email_settings.EMAIL_HOST_USER 
    EMAIL_PORT = email_settings.EMAIL_PORT 
    
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-uk'

LANGUAGES = [('en', 'en')]
DEFAULT_LANGUAGE = 0

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
if HOSTING == 'DEV':
    MEDIA_ROOT = os.path.join(ROOT_PATH, 'media')
else:
    MEDIA_ROOT = '/home/jef/homemade/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/jef/homemade/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
#ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'y$v^#+q(nk#ty**9g_2ar^q17m4ku+n%tdx*-8+ayyp0uduo3p'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
#    'cms.context_processors.media',
#    'sekizai.context_processors.sekizai',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
#    'cms.middleware.page.CurrentPageMiddleware',
#    'cms.middleware.user.CurrentUserMiddleware',
#    'cms.middleware.toolbar.ToolbarMiddleware',
)

if HOSTING=='DEV':
    ROOT_URLCONF = 'homemadeshop.urls'
    TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(ROOT_PATH, 'templates'),
    os.path.join(ROOT_PATH, 'templates/blog'),
    os.path.join(ROOT_PATH, 'templates/shop'),
#    os.path.join(PROJECT_PATH, 'homemadeshop/templates/blog'),
)
else:
    ROOT_URLCONF = 'homemadeshop.apache.urls_production'
    TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/var/www/homemade/homemadeshop/templates',
    '/usr/local/lib/python2.7/dist-packages/django/contrib/admin/templates',
    '/var/www/homemade/homemadeshop/templates/shop',
    '/var/www/homemade/homemadeshop/templates/admin',
    #'/var/www/foody/food_diary/diary/templates/admin',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'homemadeshop.shop', #our app.
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
#    'cms',
#    'menus',
#    'mptt',
#    'south',
#    'cms.plugins.text',
#    'cms.plugins.picture',
#    'cms.plugins.link',
#    'cms.plugins.file',
#    'cms.plugins.snippet',
#    'cms.plugins.googlemap',
#    'sekizai',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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
