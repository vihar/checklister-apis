# Generated by Django 2.1.2 on 2018-11-12 08:23

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('details', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='SocialProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('provider', models.CharField(choices=[('FACEBOOK', 'Facebook'), ('GOOGLE', 'Google')], max_length=255)),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'SocialProvider',
                'verbose_name_plural': 'SocialProviders',
            },
        ),
    ]