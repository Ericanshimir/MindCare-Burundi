from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse
from myapp.models import Professional


# Create your views here.
def home(request):
  return render(request, 'home.html')

def room(request, room):
  username = request.GET.get('username')
  room_details = Room.objects.filter(name=room)
  return render(request, 'room.html', {
    'username': username,
    'room': room,
    'room_details': room_details
  })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
      return redirect('/'+room+'/?username='+username)
    else:
      new_room = Room.objects.create(name=room)
      new_room.save()
      return redirect('/'+room+'/?username='+username)
    

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id= request.POST['room_id']

    new_message = Message.object.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfuly')

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def get_available_slots(request, professional_id, date):
    professional = get_object_or_404(Professional, id=professional_id)

    return JsonResponse({'available_slots': professional.available_slots})
