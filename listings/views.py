from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, vehicle_choices, state_choices
from .models import Listing
from reviews import signals, get_review_model, get_review_form, get_review_user_weight
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST


def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }


  return render(request, 'listings/listings.html', context)


def listing(request, listing_id , next=None, using=None):
  listing = get_object_or_404(Listing, pk=listing_id)
  form = get_review_form()

  context = {
    'listing': listing,
    'form' : form
  }
  return render(request, 'listings/listing.html', context)

def search(request):
  queryset_list = Listing.objects.order_by('-list_date')
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET :
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)

  # Bedrooms
  if 'vehicle_type' in request.GET:
    vehicle_type = request.GET['vehicle_type']
    if vehicle_type:
      queryset_list = queryset_list.filter(Vehicle_type__iexact=vehicle_type)

  # Price
  if 'category' in request.GET:
    category = request.GET['category']
    if category:
      queryset_list = queryset_list.filter(category__icontains=category)


  context = {
    'state_choices': state_choices,
    'vehicle_choices': vehicle_choices,
    'price_choices': price_choices,
    'listings': queryset_list,
    'values': request.GET,
    'city': city,
    'category':category,
    'vehicle_type':vehicle_type,
  }
  return render(request, 'listings/search.html', context)