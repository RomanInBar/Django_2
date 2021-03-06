from django import forms

from pagesapp.models import Product, ProductCategory
from Userapp.forms import ShopUserEditForm
from Userapp.models import ShopUser


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = "__all__"


class ProductCategoryEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    class Meta:
        model = Product
        fields = "__all__"
