from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .models import Quote, Author, Tag
from .forms import QuoteForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy


def main(request, page=1):
    quotes = Quote.objects.all()

    per_page = 10
    paginator = Paginator(quotes, per_page)

    try:
        quotes_on_page = paginator.page(page)
    except PageNotAnInteger:
        quotes_on_page = paginator.page(1)
    except EmptyPage:
        quotes_on_page = paginator.page(paginator.num_pages)

    return render(
        request,
        'quotes_app/index.html',
        {
            'quotes': quotes_on_page.object_list,
            'paginator': paginator,
            'page_obj': quotes_on_page
        }
    )


def quotes_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    quotes = Quote.objects.filter(tags=tag)

    return render(
        request,
        'quotes_app/quotes_by_tag.html',
        {
            'quotes': quotes,
            'tag': tag
        }
    )


class QuoteCreateView(CreateView):
    model = Quote
    form_class = QuoteForm
    template_name = "quotes_app/create.html"
    success_url = reverse_lazy('index')


class EditView(LoginRequiredMixin, UpdateView):
    model = Quote
    form_class = QuoteForm
    template_name = "quotes_app/edit.html"
    success_url = reverse_lazy('index')


class QuoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Quote
    template_name = "quotes_app/delete.html"
    context_object_name = "quote"
    success_url = reverse_lazy('index')


class AuthorView(DetailView):
    model = Author
    template_name = "quotes_app/author.html"
    context_object_name = "author"
