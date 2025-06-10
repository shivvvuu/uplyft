from django.shortcuts import render
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from products.models import Product
from products.utils import parse_user_sentence
import json 
from .models import Messages

# Create your views here.
@csrf_exempt  # Use with caution, consider using CSRF tokens in production
def login(request):
    if request.method == 'POST':
         data = json.loads(request.body)
         username = data.get('username')
         password = data.get('password')
         # Here you would typically authenticate the user
         from django.contrib.auth import authenticate, login as auth_login
         user = authenticate(request, username=username, password=password)
         if user is not None:
              auth_login(request, user)
              refresh_token = RefreshToken.for_user(user)
              return JsonResponse({
                   'message': 'Data fetched successfully',
                    'access': str(refresh_token.access_token),
                    'refresh': str(refresh_token),
                   }, status=200)
         else:
              return JsonResponse({'error': 'Invalid credentials'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)



@csrf_exempt  # Use with caution, consider using CSRF tokens in production
def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get("message", "")
        if user_input:
            user_input = user_input.strip()
            Messages.objects.create(user=request.user, message=user_input)
        else:
            return JsonResponse({"error": "Message cannot be empty."}, status=400)
        query = parse_user_sentence(user_input)
        products = Product.objects.all()
        if query["category"]:
            products = products.filter(category__icontains=query["category"])
        if query["max_price"]:
            products = products.filter(price__lte=query["max_price"])

        response = [
            {
                "name": p.name,
                "price": float(p.price)
            }
            for p in products
        ]
        print(response)
        if not response:
            return JsonResponse({"message": "No products found matching your criteria."}, status=404)
        return JsonResponse({"products": response[:10]},status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)