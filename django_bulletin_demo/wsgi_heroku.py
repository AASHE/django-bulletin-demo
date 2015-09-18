from django.core.wsgi import get_wsgi_application
from dj_static import Cling
import os

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "django_bulletin_demo.settings",
)

os.environ["CONSTANT_CONTACT_API_KEY"] = 'cebapx2qfecpphqzzybekjz3'
os.environ["CONSTANT_CONTACT_ACCESS_TOKEN"] = '6866da43-917e-4d50-a620-d29b98773a51'
os.environ["CONSTANT_CONTACT_FROM_EMAIL"] = 'bulletin@aashe.org'
os.environ["CONSTANT_CONTACT_REPLY_TO_EMAIL"] = 'bulletin@aashe.org'
os.environ["CONSTANT_CONTACT_USERNAME"] = 'aashelist'
os.environ["CONSTANT_CONTACT_PASSWORD"] = 'AASHEsusty9'

application = Cling(get_wsgi_application())
