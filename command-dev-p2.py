# A- Publish settings
  # A-1 blog\models.py >>add
    # class Post(models.Model): 
    #   title = models.CharField(max_length = 100) 
      ...
      is_published = models.BooleanField(default = False)     
      # def __str__(self):

  # A-2 blog\templates\blog\post_list.html
    # {% for post in posts %}
    {% if post.is_published %}
      # ...
      {% endif %} 
    # {% endfor %} 
    # {% endblock content %} 

  # A-3
    python3 manage.py makemigrations
    python3 manage.py migrate

  # A-4 Restrict access
    # blog\views.py >>add
    from django.core.exceptions import PermissionDenied
    # ...
    def get_object(self):
      # show only published posts
      # 403 errors appear when access to non-published posts
        post = super().get_object() 
        if post.is_published: 
            return post
        else:
            raise PermissionDenied
  
  # A-5- Only Admin can view non-published posts
    # blog\templates\blog\post_list.html
      # add below {% for post in posts %}
        {% if post.is_published or user.is_authenticated %}
        # ...
        # <div class ="card-body"> 
          {% if not post.is_published %}
            <span class ="badge bg-danger"> 下書き </span> 
          {% endif %}

    # blog\views.py
      # def get_object(self):
        # post = super().get_object()
        if post.is_published or self.request.user.is_authenticated: 
          # return post

    # blog\templates\blog\post_detail.html >>add
      # <div class="mt-3">
      {% if not post.is_published %} 
        <span class ="badge bg-danger"> 下書き </span> 
      {% endif %}

# Start server
python3 manage.py runserver