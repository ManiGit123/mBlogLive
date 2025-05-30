# Generated by Django 5.2.1 on 2025-05-25 03:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_listing', '0003_alter_myimage_image'),
        ('wagtailcore', '0094_alter_page_locale'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelBlogListingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('custom_title', models.CharField(help_text='Overwrite the default title', max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='TutorailsBlogListingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('custom_title', models.CharField(help_text='Overwrite the default title', max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
