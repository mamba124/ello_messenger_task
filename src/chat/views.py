from django.shortcuts import render
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "chat/chat.html"


from django.shortcuts import render
from django.http import JsonResponse

from openai import OpenAI
client = OpenAI()

def chat_with_gpt(request):
    if request.method == "POST":
        user_input = request.POST.get('user_input')
        
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user", "content": user_input
        }]
        )

#print(completion.choices[0].message)
        
        return JsonResponse(response.choices[0].message.content, safe=False)
    
    return render(request, 'chat/chat.html')