from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [migrations.CreateModel(name='RoommateProfile', fields=[
        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('name', models.CharField(max_length=100)), ('age', models.PositiveIntegerField(default=20)),
        ('city', models.CharField(default='Vadodara', max_length=80)), ('budget', models.PositiveIntegerField(help_text='Monthly budget in INR')),
        ('sleep', models.CharField(choices=[('early','Early sleeper'),('normal','Normal'),('late','Late sleeper')], max_length=20)),
        ('cleanliness', models.CharField(choices=[('low','Relaxed'),('medium','Moderate'),('high','Very clean')], max_length=20)),
        ('food', models.CharField(choices=[('veg','Vegetarian'),('nonveg','Non-vegetarian'),('both','Both are okay')], max_length=20)),
        ('smoking', models.CharField(choices=[('never','Never'),('sometimes','Sometimes'),('yes','Regularly')], max_length=20)),
        ('social', models.CharField(choices=[('quiet','Quiet/private'),('balanced','Balanced'),('social','Very social')], max_length=20)),
        ('noise', models.CharField(choices=[('quiet','Needs quiet'),('moderate','Moderate noise'),('loud','Okay with noise')], max_length=20)),
        ('guests', models.CharField(choices=[('rare','Rare guests'),('sometimes','Sometimes'),('often','Frequent guests')], max_length=20)),
        ('cooking', models.BooleanField(default=True)), ('study_work', models.BooleanField(default=True)),
        ('bio', models.TextField(blank=True)), ('created_at', models.DateTimeField(auto_now_add=True)), ('updated_at', models.DateTimeField(auto_now=True)),
    ], options={'ordering':['name']})]
