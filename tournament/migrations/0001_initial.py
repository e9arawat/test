# Generated by Django 4.2.6 on 2024-01-18 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Match",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("country", models.CharField(max_length=3, unique=True)),
                ("matches", models.IntegerField()),
                ("won", models.IntegerField()),
                ("lost", models.IntegerField()),
                ("points", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="TeamMatch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("batting_score", models.IntegerField()),
                ("batting_wickets", models.IntegerField()),
                ("batting_overs", models.IntegerField()),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="team_matches",
                        to="tournament.match",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="team_matches",
                        to="tournament.team",
                    ),
                ),
            ],
        ),
    ]
