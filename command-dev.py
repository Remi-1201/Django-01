# Make new app
python3 manage.py startapp blog

# config\settings.py
# Change LANGUAGE_CODE & TIME_ZONE 
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'

# config\settings.py
# add to INSTALLED_APPS
'blog.apps.BlogConfig',

# A - Create models
  # A-1- blog\models.py - define the model
class Post(models.Model): 
  title = models.CharField(max_length = 100) 
  content = models.TextField() 
  # TextField = no need to define max length
  created_at = models.DateTimeField(auto_now_add = True) 
  updated_at = models.DateTimeField(auto_now = True)
  
  def __str__(self):
    # show post title in index page
    return self.title

  # A-2- Make migrations file
  python3 manage.py makemigrations
  # A-3- Submit to the database
  python3 manage.py migrate


# B - Create Admin page
python3 manage.py createsuperuser
  # B-1- Use models in Admin page
    # blog\admin.py
      from blog.models import Post
      # Register your models here.
      admin.site.register(Post)


# C - Make the blog visible to users
  # C-1- blog\views.py >add
    from django.views.generic import ListView
    from blog.models import Post

    class PostList(ListView): 
      model = Post 
      # In case changing the default file name >>add
      template_name = "blog/index.html"

  # C-2- config\urls.py >add
    from django.urls import path, include
    # urlpatterns = [
    #     path('admin/', admin.site.urls),
        path("", include("blog.urls"))
    # ]

  # C-3- Make blog\urls.py
    from django.urls import path 
    from blog.views import PostList 

    urlpatterns = [
        path("", PostList.as_view(), name ="post_list"),
    ]
  
  # C-4- Make blog/post_list.html
    mkdir -p blog/templates/blog
    
    touch blog/templates/blog/post_list.html

  # C-5- Edit HTML
    <h1> ブログ一覧 </h1> 
    <hr> 
    {% for post in object_list %} 
      <h2>{{ post.title }}</h2> 
      <p>{{ post.content }}</p> 
    {% endfor %}

  # C-6- ListView settings
    # blog\views.py >> add to change default url name
    template_name = "blog/index.html"
    # change default object name
    context_object_name = "posts"

# D - Create Detail View (2.8)
  # D-1- blog\views.py
  from django.views.generic import ListView, DetailView

  from blog.models import Post

  class PostList(ListView): 
      model = Post 
      context_object_name = "posts"

  class PostDetail(DetailView): #this
      model = Post
      context_object_name = "posts"
  
  # D-2- blog\urls.py 
  from django.urls import path 
  from blog.views import PostList, PostDetail 

  urlpatterns = [
      path("", PostList.as_view(), name ="post_list"),
      path("post/<int:pk>/", PostDetail.as_view(), name ="post_detail"),
  ]
    # /<int:pk>/ = post_id

  # D-3- edit post_list.html
    # Add >> {% for post in object_list %} 
    #   <h2>{{ post.title }}</h2> 
    #   <p>{{ post.content }}</p>
      <a href ="{% url 'post_detail' post.pk %}">続きを読む</a> 
    # {% endfor %}


# Start server
python3 manage.py runserver