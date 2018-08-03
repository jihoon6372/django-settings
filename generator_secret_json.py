import json
from django.core.management.utils import get_random_secret_key

secret = {}
secret['SECRET_KEY'] = get_random_secret_key()
secret['DB_HOST'] = ''
secret['DB_USER'] = ''
secret['DB_DATABASE'] = ''
secret['DB_PASSWORD'] = ''
secret['ALLOWED_HOSTS'] = ['localhost', '127.0.0.1']

secret = json.dumps(secret)

f = open('secret.json', 'w')
f.write(secret)
f.close()
