from django.shortcuts import render

import requests
from bs4 import BeautifulSoup
from .forms import ScrapeForm

def scrape_view(request):
    form = ScrapeForm()
    titles = []
    paragraphs = [] 
    if request.method == 'POST':
        form = ScrapeForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                # Misal ambil <h2> dari halaman
                titles = [h2.get_text(strip=True) for h2 in soup.find_all('h2')]
                paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
            except Exception as e:
                titles = [f'Error: {e}']
                paragraphs = [f'Error: {e}']
        
    context = {'form': form, 'titles': titles, 'paragraphs': paragraphs}
    return render(request, 'scraper/scrape.html', context)
