from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ChatLog

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
                    "role": "system", 
                    "content": """
                            You are an expert in e-sports and music, always respect the interlocutor,
                            recommend good music after each response, and start each response with a greeting in the
                            language of the request and continue the conversation in that language.
                        """
            },
                {
                "role": "user", 
                "content": user_input
            }
        ])

        chat_log = ChatLog.objects.create(user_input=user_input, bot_response=response)        
        return JsonResponse(response.choices[0].message.content, safe=False)
    
    # Retrieve all chat logs for display
    chat_logs = ChatLog.objects.all().order_by('-created_at')
    formatted_chat_logs = []
    
    for log in chat_logs:
        formatted_chat_logs.append({
            'user_input': f"Requested at {log.created_at.strftime('%d.%m.%Y %H:%M:%S')} : {log.user_input}",
            'bot_response': f"Assistant response at {log.created_at.strftime('%d.%m.%Y %H:%M:%S')} : {log.bot_response}"
        })
    
    return render(request, 'chat/chat.html', {'chat_logs': formatted_chat_logs})

