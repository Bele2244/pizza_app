from django.shortcuts import render

from .models import Topic

def index(request):
    """The homepage for Pizzeria."""
    return render(request, 'pizzas/index.html')

def topics(request):
    """Show all pizzas."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'pizzas/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'pizzas/topic.html', context)
