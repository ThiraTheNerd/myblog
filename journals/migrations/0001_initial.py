# Generated by Django 3.2.7 on 2021-09-15 11:42

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('profile_pic', models.ImageField(upload_to='profile_pics/')),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post_pics/')),
                ('title', models.CharField(max_length=100)),
                ('content', tinymce.models.HTMLField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journals.editor')),
                ('tags', models.ManyToManyField(to='journals.tags')),
            ],
        ),
    ]
