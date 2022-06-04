# A- Images uploading
  # A-1- config\settings.py
    MEDIA_ROOT = BASE_DIR / "media" 
    MEDIA_URL = "/media/"
  # A-2- config\urls.py >>add
    from django.conf import settings 
    from django.conf.urls.static import static 
    # urlpatterns ...
    if settings.DEBUG: 
        urlpatterns += static( 
            settings.MEDIA_URL, document_root = settings.MEDIA_ROOT 
            )
  # A-3- blog\models.py
    image = models.ImageField( upload_to ="uploads/", null = True, blank = True)
    # def __str__(self):
    #   return self.title

  # A-4 Migrate
    pip install pillow
    python3 manage.py makemigrations
    python3 manage.py migrate
  
  # A-5 Show images in post_list
    # blog\templates\blog\post_list.html >>add
      # <div class ="card w-75 mt-3 mx-auto"> 
        {% if post.image %} 
        <img src ="{{ post.image.url }}" class=" card-img-top" alt ="{{ post.title }}"> 
        {% endif %}
  
  # A-6 Show images in post_detail
    # blog\templates\blog\post_detail.html
      # <h1>{{post.title}}</h1>
      {% if post.image %} 
        <img src ="{{ post.image.url }}" class="mb-3" width="80%" alt="{{ post.title }}"> 
      {% endif %}

# Start server
python3 manage.py runserver