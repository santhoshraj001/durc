# forms.py

from django import forms              # ✅ this is the correct import
from employee.models import Employee

class EmployeeForm(forms.ModelForm):  # ✅ using 'forms' here is valid now
    class Meta:
        model = Employee
        fields = "__all__"

