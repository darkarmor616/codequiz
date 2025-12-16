# Generated migration for CodeQuiz updates

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='alternativa',
            unique_together={('questao', 'texto')},
        ),
    ]
