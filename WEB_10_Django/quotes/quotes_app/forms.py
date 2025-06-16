from .models import Quote, Tag, Author
from django import forms


class QuoteForm(forms.ModelForm):
    quote = forms.CharField(
        max_length=255,
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
    new_author_name = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    new_tag_name = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Quote
        fields = ['quote', 'new_author_name', 'new_tag_name']

    def save(self, commit=True):
        quote = super().save(commit=False)

        if self.cleaned_data['new_author_name']:
            author, created = Author.objects.get_or_create(fullname=self.cleaned_data['new_author_name'])
            quote.author = author

        if commit:
            quote.save()
            self.save_m2m()
            if self.cleaned_data['new_tag_name']:
                tag, created = Tag.objects.get_or_create(name=self.cleaned_data['new_tag_name'])
                quote.tags.add(tag)

        return quote
