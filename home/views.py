from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Images
from django.urls import reverse_lazy
from django.shortcuts import redirect, HttpResponse
from django.contrib import messages
from deepface import DeepFace
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .forms import ImageUploadForm
from django.shortcuts import render
from django.shortcuts import render
from googleapiclient.discovery import build
from django.shortcuts import render
from googleapiclient.discovery import build
import logging
from django.http import JsonResponse
import json
import requests
from django.http import JsonResponse


from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse




logger = logging.getLogger(__name__)


# views.py







class IndexView(LoginRequiredMixin, generic.FormView):
    template_name = "pages/index.html"
    form_class = ImageUploadForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Images.objects.filter(user=self.request.user)
        chat_response = self.request.session.get('chat_response', '')
        context['chat_response'] = chat_response
        return context

    def form_valid(self, form):
        form_obj = form.save(commit=False)
        form_obj.user = self.request.user
        form_obj.save()
        analysis = DeepFace.analyze(
            img_path=form_obj.image.path,
            detector_backend='retinaface',
        )
        form_obj.data = analysis
        form_obj.save()
        messages.success(self.request, 'Image uploaded successfully!')
        return redirect('index')

    def course(request, courseid):
        return HttpResponse(courseid)

#testing but failed as the account is protected 2factor    
    # send_mail(
    #     "testing mail",
    #     'here is the massage',
    #     'maryammrehman1154@gmail.com',
    #     ['arham786ch@gmail.com'],
    #     fail_silently = False,

    # )

class ImageDeleteView(LoginRequiredMixin, generic.View):
    model = Images
    success_url = reverse_lazy('index')

    def get_object(self):
        return get_object_or_404(self.model, pk=self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        self.get_object().delete()
        messages.success(self.request, 'Image deleted successfully')
        return redirect(self.success_url)




def analysis_view(request, image_id):
    # Retrieve the Images object based on the image_id
    image_obj = get_object_or_404(Images, pk=image_id)

    # Extract detailed analysis data from the object (assuming it's stored in `data` field)
    analysis_data = image_obj.data  # Adjust this based on your data structure

    # Prepare context data to pass to the template
    context = {
        'image_obj': image_obj,
        'analysis_data': analysis_data,
    }

    # Render the ana.html template with the context data
    return render(request, 'ana.html', context)





def contact_page(request):
    return render(request, 'contact.html')  # Replace 'your_app' with your app's name

def history_page(request):
    # Assuming you want to fetch all Images objects for display
    image_objects = Images.objects.all()  # Query all Images objects

    context = {
        'object_list': image_objects  # Pass the list of image objects to the template
    }

    return render(request, 'history.html', context)



def search_google_images(request):
    if request.method == 'GET':
        # Retrieve search query from GET parameters
        search_query = request.GET.get('search_query', '')
        if not search_query:
            return JsonResponse({'error': 'No search query provided'}, status=400)

        # Google Custom Search API parameters
        API_KEY = "AIzaSyBgSAo9VqzgJrfnkxHAdA1e39WXSDtN2eE"
        SEARCH_ENGINE_ID = "67260a511d6954f34"

        url = 'https://www.googleapis.com/customsearch/v1'
        params = {
            'q': search_query,
            'key': API_KEY,
            'cx': SEARCH_ENGINE_ID,
            'searchType': 'image'
        }

        try:
            # Make API request to Google Custom Search API
            response = requests.get(url, params=params)
            results = response.json().get('items', [])
            return JsonResponse(results, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
class ChatView(APIView):
    def post(self, request):
        user_message = request.data.get('message', '')
        if user_message:
            # Replace with your Replicate model's API endpoint URL
            api_url = "https://api.replicate.com/v1/models/<your-model-id>/versions/<your-version-id>/predict"

            # Replace with your Replicate API key (if required)
            headers = {'Authorization': 'Token <your-api-key>'} if required_auth else {}

            # Send user message as prompt in the request body
            data = {'prompt': user_message}

            # Send POST request to Replicate's API
            response = requests.post(api_url, headers=headers, json=data)

            if response.status_code == 200:
                # Extract chat response from successful response
                chat_response = response.json()['generated_text'][0]

                # Store chat response in session (optional)
                request.session['chat_response'] = chat_response

                return Response({'response': chat_response})
            else:
                # Handle error (e.g., log the error message)
                print(f"Error getting response from Replicate: {response.text}")
                return Response({'error': 'Failed to get response from Replicate.'})

        return Response({'response': 'No message provided.'})
    



API_KEY = "AIzaSyBgSAo9VqzgJrfnkxHAdA1e39WXSDtN2eE"
SEARCH_ENGINE_ID = ("67260a511d6954f34")


serach_query = 'asian women clothing shop'

url = 'https://www.googleapis.com/customsearch/v1'
params = {
    'q': serach_query,
    'key': API_KEY,
    'cx': SEARCH_ENGINE_ID,
    'searchType': 'image'
}

response = requests.get(url,params=params)
results = response.json()


if 'items' in results:
    for item in results['items']:
        # 'item' represents each individual search result containing image details
        if 'link' in item:
            print(item['link'])  # Print the image link for each search result
        else:
            print("Key 'link' not found in item dictionary.")
else:
    print("Key 'items' not found in results dictionary.")



from django.shortcuts import render
import requests

def display_img(request):
    # Google Custom Search API parameters
    API_KEY = "AIzaSyDuNI58-BEHTQk0NEMHeYvXRJkPJl7J1yk"
    SEARCH_ENGINE_ID = "67260a511d6954f34"
    search_query = 'asian women clothing shop'

    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_query,
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'searchType': 'image'
    }

    # Make API request
    response = requests.get(url, params=params)
    results = response.json().get('items', [])

    # Extract image links from results
    image_links = [item['link'] for item in results if 'link' in item]

    # Render the image_display.html template with image links
    return render(request, 'image_display.html', {'image_links': image_links})

def display_images(request, dominant_race=None, dominant_gender=None):
    # Google Custom Search API parameters
    API_KEY = "AIzaSyDuNI58-BEHTQk0NEMHeYvXRJkPJl7J1yk"
    SEARCH_ENGINE_ID = "67260a511d6954f34"

    # Construct the search query using dominant_race and dominant_gender
    search_query = f"{dominant_race} {dominant_gender} suits"

    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_query,
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'searchType': 'image'
    }
    

    # Make API request
    response = requests.get(url, params=params)
    results = response.json().get('items', [])

    # Extract image links from results
    image_links = [item['link'] for item in results if 'link' in item]

    # Render the image_display.html template with image links
    return render(request, 'image_display.html', {'image_links': image_links})
   
    


