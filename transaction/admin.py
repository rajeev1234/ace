from django.contrib import admin
from .models import *

admin.site.register(ColorMaster)
admin.site.register(ArticleMaster)
admin.site.register(CompanyLedgerMaster)
admin.site.register(DepartmentMaster)
admin.site.register(BranchMaster)
admin.site.register(TransactionTable)
admin.site.register(TransactionLineItem)
admin.site.register(InventoryItem)