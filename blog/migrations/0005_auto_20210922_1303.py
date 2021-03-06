# Generated by Django 3.2.7 on 2021-09-22 13:03

from django.db import migrations

def migrate_author_to_contributors(apps, schema_editor):
    Blog = apps.get_model('blog', 'Blog')
    for blog in Blog.objects.all():
        if blog.author:
            blog.contributors.add(
                blog.author, through_defaults={'contribution': 'Primary Author'})


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210922_1254'),
    ]

    operations = [
        migrations.RunPython(migrate_author_to_contributors)
    ]
