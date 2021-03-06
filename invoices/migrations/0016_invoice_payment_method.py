# Generated by Django 2.1.5 on 2019-02-10 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("invoices", "0015_invoice_payment_condition")]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="payment_method",
            field=models.CharField(
                choices=[
                    ("MP01", "contanti"),
                    ("MP02", "assegno"),
                    ("MP03", "assegno circolare"),
                    ("MP04", "contanti presso Tesoreria"),
                    ("MP05", "bonifico"),
                    ("MP06", "vaglia cambiario"),
                    ("MP07", "bollettino bancario"),
                    ("MP08", "carta di pagamento"),
                    ("MP09", "RID"),
                    ("MP10", "RID utenze"),
                    ("MP11", "RID veloce"),
                    ("MP12", "RIBA"),
                    ("MP13", "MAV"),
                    ("MP14", "quietanza erario"),
                    ("MP15", "giroconto su conti di contabilità speciale"),
                    ("MP16", "domiciliazione bancaria"),
                    ("MP17", "domiciliazione postale"),
                    ("MP18", "bollettino di c/c postale"),
                    ("MP19", "SEPA Direct Debit"),
                    ("MP20", "SEPA Direct Debit CORE"),
                    ("MP21", "SEPA Direct Debit B2B"),
                    ("MP22", "Trattenuta su somme già riscosse"),
                ],
                default="MP01",
                max_length=5,
                verbose_name="Payment method",
            ),
            preserve_default=False,
        )
    ]
