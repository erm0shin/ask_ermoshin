from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class QuestionManager(models.Manager):
    def get_all(self):
        return self.order_by("creation_date")

    def get_hot(self):
        rated_questions = Rating.objects.values_list("question_id").distinct().all()
        rating_list = []
        for question in rated_questions:
            rating_list.append((question[0], Rating.objects.filter(question=question[0]).count()))
        rating_list.sort(key=lambda tup: tup[1], reverse=True)
        return [self.filter(pk=r[0]) for r in rating_list]

    # def get_by_id(self, question_id):
    #     return self.filter(pk=question_id)[0]


class Profile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=15)
    popularity = models.IntegerField(default=0)


class Question(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(default=now())
    author = models.ForeignKey(Profile)
    tags = models.ManyToManyField(Tag)
    objects = QuestionManager()

    def get_absolute_url(self):
        return "/question/%d/" % self.pk

    def get_author(self):
        return self.author.user

    def get_author_avatar(self):
        return self.author.avatar

    def get_tags(self):
        return self.tags.values("pk", "name")

    def get_n_answers(self):
        return Answer.objects.filter(question=self.pk).count()

    def get_rating(self):
        return Rating.objects.filter(question=self.pk).count()


class Answer(models.Model):
    content = models.TextField()
    creation_date = models.DateTimeField(default=now())
    author = models.ForeignKey(Profile)
    question = models.ForeignKey(Question)


class Rating(models.Model):
    user = models.ForeignKey(Profile)
    question = models.ForeignKey(Question, null=True, blank=True)
    answer = models.ForeignKey(Answer, null=True, blank=True)
