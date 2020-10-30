from django.db import models


class Creation(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Team(Creation):
    app_id = models.TextField()
    team_id = models.TextField(db_index=True)
    team_name = models.CharField(max_length=100)
    user_access_token = models.TextField()
    bot_access_token = models.TextField()

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = "Teams"


    def __str__(self):
        return self.team_name


class Category(Creation):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.title
