from django.contrib import admin
from .models import Group, GroupMember, Expense, ExpenseShare, Settle, Profile

admin.site.register(Profile)
admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(Expense)
admin.site.register(ExpenseShare)
admin.site.register(Settle)
