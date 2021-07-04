from django.db import models
from datetime import datetime, date

# Masters required in transaction models
class BranchMaster(models.Model):
    short_name = models.CharField(max_length=10, unique=True)
    contact_person_name = models.CharField(max_length=20)
    gst_number = models.CharField(max_length=20)
    address1 = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    mobile = models.CharField(blank=True, null=True, max_length=20)


class DepartmentMaster(models.Model):
    name = models.CharField(max_length=20, unique=True)


class CompanyLedgerMaster(models.Model):
    name = models.CharField(max_length=32, unique=True)
    gst_number = models.CharField(max_length=20, unique=True)
    supplier_status = models.BooleanField(default=False)
    address1 = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    remarks = models.CharField(max_length=200, blank=True)


class ArticleMaster(models.Model):
    name = models.CharField(max_length=80, unique=True)
    short_name = models.CharField(max_length=50, unique=True)
    blend_pct = models.CharField(max_length=50)
    twists = models.PositiveIntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=64, blank=True)


class ColorMaster(models.Model):
    article = models.ForeignKey(ArticleMaster, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=20)
    remarks = models.CharField(max_length=64, blank=True)

# Create your models here.

count = 0

class TransactionTable(models.Model):

    TRANSACTION_STATUS = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('CLOSE', 'Close'),
    ]
    company = models.ForeignKey(CompanyLedgerMaster, on_delete=models.CASCADE, related_name='transactionCompany')
    branch = models.ForeignKey(BranchMaster, on_delete=models.CASCADE, related_name='transactionBranch')
    department = models.ForeignKey(DepartmentMaster, on_delete=models.CASCADE, related_name='transactionDepartment')
    transaction_number = models.CharField(max_length=20, blank=True, editable=True)
    transaction_status = models.CharField(max_length=20,choices=TRANSACTION_STATUS,)
    remarks = models.CharField(max_length=200, default=None)

    def save(self, *args, **kwargs):
        global count
        count += 1
        day_of_year = datetime.now().timetuple().tm_yday

        if day_of_year == 1:
            count = 0
        self.transaction_number = f'TRN{count}{date.today().year}'
        super(TransactionTable, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.id}'


class TransactionLineItem(models.Model):
    UNIT = [
        ('KG', 'KG'),
        ('METRE', 'Metre')
    ]
    transaction =models.ForeignKey(TransactionTable, on_delete=models.CASCADE)
    article = models.ForeignKey(ArticleMaster, on_delete=models.CASCADE,related_name='transactionArticle')
    colour = models.ForeignKey(ColorMaster, on_delete=models.CASCADE,related_name='transactionColor')
    required_on_date = models.DateTimeField()
    qunatity = models.DecimalField(max_digits=20,decimal_places=10)
    rate_per_unit = models.IntegerField()
    unit = models.CharField(max_length=5, choices=UNIT,)

    def __str__(self) -> str:
        return f'{self.id}'


class InventoryItem(models.Model):
    UNIT = [
        ('KG', 'KG'),
        ('METRE', 'Metre')
    ]
    transaction_line_item = models.ForeignKey(TransactionLineItem, on_delete=models.CASCADE)
    article = models.ForeignKey(ArticleMaster, on_delete=models.CASCADE,related_name='invenArticle')
    colour = models.ForeignKey(ColorMaster, on_delete=models.CASCADE,related_name='invenColor')
    company = models.ForeignKey(CompanyLedgerMaster, on_delete=models.CASCADE, related_name='invenCompany')
    gross_quantity = models.DecimalField(max_digits=20, decimal_places=10)
    net_quantity = models.DecimalField(max_digits=20, decimal_places=10)
    unit = models.CharField(max_length=5, choices=UNIT,)

    def __str__(self) -> str:
        return f'{self.id}'