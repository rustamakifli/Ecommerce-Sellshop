from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class AbsrtactModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BlogCategory(models.Model):
    parent_cat = models.ForeignKey('self', related_name='category_sub_cat', on_delete=models.CASCADE,    null=True, blank=True)
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'

    def __str__(self):
        return self.title

class Blog(AbsrtactModel):
    category = models.ForeignKey(BlogCategory, related_name='blog_category', on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/blog/')
    description = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title


class BlogReviews(AbsrtactModel):
    blog = models.ForeignKey(Blog, related_name='blog_blogreviews', on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, related_name='user_blogreviews', on_delete=models.CASCADE, default=1)
    review = models.TextField()

    class Meta:
        verbose_name = 'Blog reviews'
        verbose_name_plural = 'Blog reviews'

    def __str__(self):
        return self.review


class BlogComment(AbsrtactModel):
    blog = models.ForeignKey(Blog, related_name='blog_comment', on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE, default=1)
    comment = models.TextField()
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=40)
    class Meta:
        verbose_name = 'Blog comment'
        verbose_name_plural = 'Blog comments'

    def __str__(self):
        return self.comment
