# A file upload application for DjangoRestFramework

### Installation
```bash
python3 -m pip install drf_fileupload
```

### Usage
- edit `project/settings.py`

```python
INSTALL_APPS += [
    'drf_fileupload',
]

MEDIA_ROOT = 'data/'  # default: /

FILE_UPLOAD_TO = 'upload/%Y/%m/%d'   # support strftime format, default: MEDIA_ROOT
MAX_FILE_UPLOAD = '10M'              # limit max file size, default: None
```

- edit `project/urls.py`

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/fileupload/', include('drf_fileupload.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### API
![](https://suqingdong.github.io/drf_fileupload/gallery/api.png))

### Demo
```bash
git clone https://github.com/suqingdong/drf_fileupload

cd demo

python3 -m pip install -r requirements.txt

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver
```


