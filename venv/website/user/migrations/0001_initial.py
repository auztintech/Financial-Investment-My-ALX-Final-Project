# Generated by Django 4.2.5 on 2023-10-02 09:24

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('payment_option', models.CharField(blank=True, choices=[('bitcoin address', 'bitcoin address'), ('perfect money account', 'perfect money account')], max_length=30)),
                ('payment_address', models.CharField(blank=True, max_length=300)),
                ('deposited', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('profit', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('total_packages', models.PositiveIntegerField(default=0)),
                ('bonus', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('active_packages', models.PositiveIntegerField(default=0)),
                ('ref_bonus', models.DecimalField(decimal_places=2, default=10.0, max_digits=20)),
                ('account_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('active_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('pending_withdrawal', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('total_withdraw', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('total_earned', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('last_deposit', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('total_deposit', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('last_withdrawal', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('-date_joined',),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(default='no-picture.png', upload_to='profile_pictures/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='KYCApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_card_or_passport', models.ImageField(blank=True, null=True, upload_to='kyc/idimg/')),
                ('proof_of_address', models.ImageField(blank=True, null=True, upload_to='kyc/addressimg/')),
                ('identification_doc', models.CharField(choices=[('ID', 'National ID'), ('passport', 'International passport')], max_length=50)),
                ('address_doc', models.CharField(choices=[('utility_bill', 'Utility Bill'), ('bank_reference', 'Bank Reference'), ('proof_of_residence', 'Proof of Residence'), ('driver_or_residence_permit', 'Driver or Residence Permit'), ('other', 'Other')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='KYCVerification', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Help_desk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=400)),
                ('category', models.CharField(choices=[('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal'), ('Earning', 'Earning'), ('Referral', 'Referral'), ('Account', 'Account'), ('Other', 'Other')], default='Other', max_length=20)),
                ('priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Low', max_length=400)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Resolved', 'Resolved')], default='Pending', max_length=20)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
