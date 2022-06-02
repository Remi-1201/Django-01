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

# Start server
python3 manage.py runserver