# Generated by Django 5.0.7 on 2024-08-14 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redbox_core', '0035_aisettings_chat_backend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='business_unit',
            field=models.CharField(blank=True, choices=[("Prime Minister's Office", "Prime Minister's Office"), ('Delivery Group', 'Delivery Group'), ('National Security Secretariat', 'National Security Secretariat'), ('Economic and Domestic Secretariat', 'Economic and Domestic Secretariat'), ('Propriety and Constitution Group', 'Propriety and Constitution Group'), ('Government in Parliament', 'Government in Parliament'), ('Joint Intelligence Organisation', 'Joint Intelligence Organisation'), ('Intelligence and Security Committee', 'Intelligence and Security Committee'), ('Government Digital Service', 'Government Digital Service'), ('Central Digital and Data Office', 'Central Digital and Data Office'), ('Government Communication Service', 'Government Communication Service'), ('Government People Group', 'Government People Group'), ('Government Security Group', 'Government Security Group'), ('UKSV', 'UKSV'), ('Government Commercial and Grants Function', 'Government Commercial and Grants Function'), ('Civil Service Human Resources', 'Civil Service Human Resources'), ('Infrastructure and Projects Authority', 'Infrastructure and Projects Authority'), ('Office of Government Property', 'Office of Government Property'), ('Government Business Services', 'Government Business Services'), ('Borders Unit', 'Borders Unit'), ('Equality Hub', 'Equality Hub'), ('Public Sector Fraud Authority', 'Public Sector Fraud Authority'), ('CO Chief Operating Officer', 'CO Chief Operating Officer'), ('Flexible CS Pool', 'Flexible CS Pool'), ('CO People and Places', 'CO People and Places'), ('CO Strategy, Finance, and Performance', 'CO Strategy Finance, and Performance'), ('Central Costs', 'Central Costs'), ('CO HMT Commercial', 'CO HMT Commercial'), ('CO Digital', 'CO Digital'), ('Public Bodies and Priority Projects Unit', 'Public Bodies and Priority Projects Unit'), ('Public Inquiry Response Unit', 'Public Inquiry Response Unit'), ('CS Modernisation and Reform Unit', 'CS Modernisation and Reform Unit'), ("Office for Veterans' Affairs", "Office for Veterans' Affairs"), ('Grenfell Inquiry', 'Grenfell Inquiry'), ('Infected Blood Inquiry', 'Infected Blood Inquiry'), ('Covid Inquiry', 'Covid Inquiry'), ('Civil Service Commission', 'Civil Service Commission'), ('Equality and Human Rights Commission', 'Equality and Human Rights Commission'), ('Government Property Agency', 'Government Property Agency'), ('Office of the Registrar of Consultant Lobbyists', 'Office of the Registrar of Consultant Lobbyists'), ('Crown Commercial Service', 'Crown Commercial Service'), ('Union and Constitution Group', 'Union and Constitution Group'), ('Geospatial Commission', 'Geospatial Commission'), ('Commercial Models', 'Commercial Models'), ('COP Presidency', 'COP Presidency'), ('Inquiries Sponsorship Team', 'Inquiries Sponsorship Team'), ('Other', 'Other')], max_length=64, null=True),
        ),
    ]
