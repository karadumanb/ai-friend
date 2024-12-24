from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Friend  # Replace with your actual model

def paginated_friends(request):
    # Get the query parameters for pagination
    page_number = request.GET.get('page', 1)  # Default to page 1
    page_size = request.GET.get('size', 10)  # Default to 10 records per page

    # Fetch all records from the model
    records = Friend.objects.all()

    # Create a paginator
    paginator = Paginator(records, page_size)

    try:
        # Get the requested page
        page = paginator.get_page(page_number)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

    # Prepare the response data
    data = {
        'page': page.number,
        'total_pages': paginator.num_pages,
        'total_records': paginator.count,
        'page_size': page_size,
        'records': list(page.object_list.values()),  # Convert records to a list of dictionaries
    }

    return JsonResponse(data, safe=False)

