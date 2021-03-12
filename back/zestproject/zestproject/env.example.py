import os 

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': os.environ.get('GROUPNAME'),
    'USER': os.environ.get('GROUPNAME', 'root'),
    'PASSWORD': os.environ.get('PASSWORD', ''),
    'HOST': os.environ.get('MYSQL_HOST', 'localhost'),
    'PORT': os.environ.get('MYSQL_PORT', '3306'),
    'OPTIONS': {
      'charset': 'utf8mb4'
    }
  }
}