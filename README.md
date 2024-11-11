Permisos -> sudo chown -R dave /home/dave/Escritorio/Programación/Django/my_project

Pasos para iniciar
- Iniciar el proyecto -> docker-compose run web django-admin startproject my_project .
- Configurar el settings:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bd_dave',  nombre de bd
        'USER': 'dave',
        'PASSWORD': 'dave_password',
        'HOST': 'db',  El nombre del servicio de MySQL en Docker
        'PORT': '3306',
    }
}