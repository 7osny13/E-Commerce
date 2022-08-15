
#run Django

pip install -r requirements.txt
python manage.py runserver
====================================
#run react 

npm install
npm start
====================================
#how to integrate react int django

1-import os in settings.py (django app)
2-in DIRS which inside TEMPLPATES add this line : os.path.join(BASE_DIR, 'frontend/build')
3-in STATICFILES_DIRS add this line : BASE_DIR / 'frontend/build/static'
====================================
#references

*Integrate React Into  Django
https://www.youtube.com/watch?v=FhkqMHxchZ8&feature=youtu.be

*contact
https://www.youtube.com/watch?v=PGyeSW6c0cA

*chat
https://www.youtube.com/watch?v=0z7CX5UWZp8&t=30s












