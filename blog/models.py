from django.db import models

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
    # blog = models.ForeignKey(Blog, related_name='blogreviews', on_delete=models.CASCADE)
    # user = models.ForeignKey(User, related_name='blogreviews', on_delete=models.CASCADE)