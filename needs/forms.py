from django import forms


class AddItem(forms.Form):
    item_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "لطفا نیازمندی خود را وارد کنید"})
    )