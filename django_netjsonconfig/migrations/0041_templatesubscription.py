# Generated by Django 2.1.9 on 2019-07-28 16:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsonconfig', '0040_template_share_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateSubscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('subscriber', models.URLField(verbose_name='Subscriber URL')),
                ('is_subscription', models.BooleanField(default=True, verbose_name='Is Subscriber ?')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_netjsonconfig.Template', verbose_name='Template')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
