
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p!13y1r=x$87xfkbd71al6_-&l&8nex+lyk%8&(w)zzn0kd9-p'



DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'Florida',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}