# Generated by Django 2.2.1 on 2019-07-28 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('browse', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderpackagelist',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='browse.Package', verbose_name='Package'),
        ),
        migrations.AddField(
            model_name='order',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.RestaurantBranch', verbose_name='Branch'),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Delivery', verbose_name='Delivery Info'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Payment', verbose_name='Payment Info'),
        ),
        migrations.AddField(
            model_name='order',
            name='pkg_list',
            field=models.ManyToManyField(through='accounts.OrderPackageList', to='browse.Package', verbose_name='Packages in Order'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Person To Deliver'),
        ),
        migrations.AddField(
            model_name='deliveryman',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='delivery',
            name='deliveryman',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.DeliveryMan', verbose_name='Delivery Man'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]