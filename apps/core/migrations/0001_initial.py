# Generated by Django 2.1 on 2019-12-30 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.RandomCharField(blank=True, editable=False, length=8, lowercase=True, unique=True)),
                ('type', models.CharField(choices=[('0', "I'm a buyer"), ('1', "I'm a seller")], default='0', max_length=1)),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]