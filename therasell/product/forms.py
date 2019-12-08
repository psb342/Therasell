from django import forms

from .models import Product

class ListForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('Title','Description','Category','Quantity','Size','Image','Brand','Color','Condition','Original_Price','Listing_Price',)
        # Title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'What are you selling'}),label='Title')
        # Description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Describe it'}),label='Description')
        # Category = forms.CharField()
        # Quantity = forms.CharField()
        # Size = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Dimensions'}), required=False,label='Size')
        # #Image = models.ImageField(upload_to="product/", null=True, blank=True)
        # Brand = forms.CharField(required=False,label='Brand')
        # Color = forms.CharField(required=False,label='Color')
        # Condition = forms.CharField()
        # Original_Price = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Dimensions'}), required=False,label='Original Price')
        # Listing_Price = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Dimensions'}), required=False,label='Listing Price')

