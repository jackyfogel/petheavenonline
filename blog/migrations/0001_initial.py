# Generated by Django 5.1.4 on 2025-04-06 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
                ('seo_title', models.CharField(blank=True, max_length=70, null=True)),
                ('seo_description', models.CharField(blank=True, max_length=200, null=True)),
                ('canonical_url', models.URLField(blank=True, null=True)),
                ('noindex', models.BooleanField(default=False)),
            ],
        ),
    ]
