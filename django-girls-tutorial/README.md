# django-tutorial

설치 및 실행
> cd django-girls-tutorial 
> python3 -m venv myvenv
> source myvenv/bin/activate
> python3 -m pip install --upgrade pip
> pip install django~=2.0.0
> python manage.py runserver



모델 만들기
> blog/models.py 조작
> 
> python manage.py makemigrations blog 
> python manage.py migrate blog
> source myvenv/bin/activate
> python3 -m pip install --upgrade pip
> pip install django~=2.0.0
> python manage.py runserver

쉘 조작
> python manage.py shell
> from blog.models import Post
> Post.objects.all()
> Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
