from django import forms
from .models import (Account, Funds, FundsManager, Beneficiary, Due, Notification)

class BeneficiaryForm(forms.Form):
    account_id = forms.CharField(max_length=130)
    contribution = forms.DecimalField(
        decimal_places=2,
        max_digits=15
    )

class FundsForm(forms.Form):
    purpose = forms.CharField(max_length=130)
    purpose_price = forms.DecimalField(
        decimal_places=2,
        max_digits=15
    )
