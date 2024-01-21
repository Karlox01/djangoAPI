# Generated by Django 4.2.9 on 2024-01-21 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(default='../default_profile_wfihdl', upload_to='images/')),
                ('comments', models.ManyToManyField(blank=True, related_name='profile_comments', to='comments.comment')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('posts', models.ManyToManyField(blank=True, related_name='profile_posts', to='posts.post')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
