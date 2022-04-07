# Generated by Django 4.0.3 on 2022-04-05 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_images_category_note_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='image',
        ),
        migrations.AddField(
            model_name='note',
            name='images',
            field=models.FileField(default=0, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.ForeignKey(default='animal', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_cat', to='app.category'),
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
