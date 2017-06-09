from django.shortcuts import render
from .utils import *
def home(request):
    return render(request, 'blog/home.html')
def story_list(request):
    rally = initRally()
    query_criteria = 'BusOpsKanban = "Backlog"'
    #'BusOpsKanban != "Backlog"
    response = rally.get('UserStory',fetch = True, query=query_criteria)
    print (response)
    story_list = []
    if not response.errors:
        for story in response:
            #print (story.details())
            a_story={}
            a_story['Kanban'] = story.BusOpsKanban
            a_story['id'] = story.FormattedID
            a_story['name'] = story.Name
            a_story['Opened']=story.CreationDate
            a_story['Requester']=story.Owner     
           #a_story['Kanban'] = story.c_BizOpsKanbanState
            story_list.append(a_story)
    else:
        story_list = response.errors
    print(story_list)
    return render(request, 'blog/story_list.html', {'stories': story_list})
def graph(request):
    return render(request, 'blog/graph.html')
