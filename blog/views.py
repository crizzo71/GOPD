from django.shortcuts import render
from .utils import *
from datetime import *
def home(request):
    return render(request, 'blog/home.html')
def story_list(request):
    rally = initRally()
    #query_criteria = 'State != ""'
    query_criteria='BusOpsKanban != "Backlog" AND CreationDate > "2014-12-31T00:00:00.0Z"'
    response = rally.get('UserStory',fetch = True, query=query_criteria)
    #print (response)

    story_list = []
    if not response.errors:
        for story in response:
            #print (story.details())
            a_story={}
            #a_story['State'] = story.State.Name #if story.State else "Backlog"
            a_story['State']=story.BusOpsKanban
            a_story['id'] = story.FormattedID
            a_story['name'] = story.Name
            a_story['Opened']=datetime.strptime(story.CreationDate, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%d-%b-%Y')
            a_story['Requester']= story.Owner.Name if story.Owner else "unassigned"
           #a_story['Kanban'] = story.c_BizOpsKanbanState
            story_list.append(a_story)
    else:
        story_list = response.errors
    print(story_list[0])
    return render(request, 'blog/story_list.html', {'stories': story_list})
def graph(request):
    rally = initRally()
    response = rally.get('UserStory',fetch = True, query='BusOpsKanban != ""')
    print(response)
    story_list = []
    if not response.errors:
        for story in response:
            #print (story.details())
            a_story={}
            a_story['Kanban'] = story.BusOpsKanban
            story_list.append(a_story)
    else:
        story_list = response.errors
    print(story_list)
    return render(request, 'blog/graph.html')
