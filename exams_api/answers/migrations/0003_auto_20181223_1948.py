# Generated by Django 2.1.4 on 2018-12-23 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0002_remove_answer_examtask_int'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='examowner',
        ),
        migrations.AddField(
            model_name='answer',
            name='examowner_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]