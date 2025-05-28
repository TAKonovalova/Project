from django.shortcuts import render, get_object_or_404
from .models import Page

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    nav_pages = Page.objects.filter(show_in_nav=True).order_by('priority')
    
    # Передаем текущий slug в контекст
    return render(request, 'core/page_detail.html', {
        'page': page,
        'nav_pages': nav_pages,
        'current_slug': slug,  # Добавлено
        'me': page.person_set.filter(role='me').first(),
        'leader': page.person_set.filter(role='leader').first(),
        'managers': page.person_set.filter(role='manager'),
        'classmates': page.person_set.filter(role='classmate')
    })