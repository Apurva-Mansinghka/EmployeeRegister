from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullName','contactNumber','emailID','dateOfBirth','address','bloodGroup')
        labels = {
             'fullName':'Full Name',
             'contactNumber':'Contact Number',
             'emaildID':'Email ID',
             'dateOfBirth':'Date Of Birth',
             'address':'Address',
             'bloodGroup' :'Blood Group'
        }

    def __init__(self, *args, **kwargs):
         super(EmployeeForm,self).__init__(*args, **kwargs)
         self.fields['bloodGroup'].empty_label = "Select your Blood Group"

