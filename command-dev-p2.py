# A- Draft settings
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



# Start server
python3 manage.py runserver