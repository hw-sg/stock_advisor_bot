# Generated by Django 3.1.2 on 2021-09-06 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rasa_chatbot', '0004_bursalist_trading_view_symbol'),
    ]

    operations = [
        migrations.CreateModel(
            name='option1_selection',
            fields=[
                ('auto_increment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('current_price', models.BooleanField()),
                ('price_change', models.BooleanField()),
                ('price_change_percentage', models.BooleanField()),
                ('previous_close_price', models.BooleanField()),
                ('open_price', models.BooleanField()),
                ('daily_low', models.BooleanField()),
                ('daily_high', models.BooleanField()),
                ('yearly_high', models.BooleanField()),
                ('yearly_low', models.BooleanField()),
                ('get_50_days_moving_average_price', models.BooleanField()),
                ('get_200_days_moving_average_price', models.BooleanField()),
                ('current_volume', models.BooleanField()),
                ('get_10_days_average_volume', models.BooleanField()),
                ('get_3_months_average_volume', models.BooleanField()),
                ('market_cap', models.BooleanField()),
                ('pe_ratio', models.BooleanField()),
                ('rsi_14', models.BooleanField()),
                ('rsi_28', models.BooleanField()),
                ('percentage_price_oscillator', models.BooleanField()),
                ('percentage_volume_oscillator', models.BooleanField()),
                ('rate_of_change', models.BooleanField()),
                ('stochastic_oscillator', models.BooleanField()),
                ('willianR', models.BooleanField()),
                ('ADI', models.BooleanField()),
                ('chaikin_money_flow', models.BooleanField()),
                ('negative_volume_index', models.BooleanField()),
                ('On_balance_volume', models.BooleanField()),
                ('volume_price_trend', models.BooleanField()),
                ('volume_weighted_average_price_14days', models.BooleanField()),
            ],
        ),
    ]
