from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class AbsrtactModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Blog(AbsrtactModel):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/blog/')
    description = models.CharField(max_length=255)
    content = models.TextField()


class BlogReviews(AbsrtactModel):
    review = models.TextField()
<<<<<<< HEAD
    # blog = models.ForeignKey(Blog, related_name='blogreviews', on_delete=models.CASCADE)
    # user = models.ForeignKey(User, related_name='blogreviews', on_delete=models.CASCADE)
=======
    blog = models.ForeignKey(Blog, related_name='blogreviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='blogreviews', on_delete=models.CASCADE)
>>>>>>> rustamakifli
