# Generated by Django 4.0.3 on 2022-04-12 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_alter_post_created_at_alter_post_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('taluko', models.CharField(max_length=50)),
                ('village', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
