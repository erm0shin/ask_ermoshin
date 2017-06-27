# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-27 03:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='question',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('-added_at',)},
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='content',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='content',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='popularity',
        ),
        migrations.AddField(
            model_name='answer',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='about_me',
            field=models.TextField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='profile',
            name='questions_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='count_answers',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='question_dislike', to='questions.Profile'),
        ),
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='question_like', to='questions.Profile'),
        ),
        migrations.AddField(
            model_name='question',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='short_text',
            field=models.TextField(default='', max_length=85),
        ),
        migrations.AddField(
            model_name='tag',
            name='counts',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tag',
            name='questions',
            field=models.ManyToManyField(blank=True, to='questions.Question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_author', to='questions.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='uploads/newavatar.png', null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_author', to='questions.Profile'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]