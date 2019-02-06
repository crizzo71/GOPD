from django.shortcuts import render
from .utils import *
from datetime import *
import json
def home(request):
    return render(request, 'blog/home.html')
def story_list(request):
    rally = initRally()
    #query_criteria='c_BusOpsKanban != "Verified" AND CreationDate > "2014-06-01T00:00:00.0Z"'
    response = rally.get('Artifact', fetch = True)
    #query=query_criteria, order="DragAndDropRank")
    #response_defect = rally.get('Defect', fetch = True, query=query_criteria)
    story_list = []
    if not response.errors:
        for story in response:
            #print (story.details())
            a_story={}
            #a_story['State'] = story.State.Name #if story.State else "Backlog"
            a_story['Rank']=story.DragAndDropRank if story.DragAndDropRank else "none"
            #a_story['State']=story.BusOpsKanban if story.BusOpsKanban else "unassigned"
            #a_story['Status']=Story.Status if story.Status else "unassigned"
            a_story['id'] = story.FormattedID
            a_story['name'] = story.Name
            a_story['Opened']=(datetime.strptime(story.CreationDate, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%d-%b'))
            a_story['Requester']= story.Owner.Name if story.Owner else "unassigned"
            a_story['Blocked']= story.Blocked
            a_story['Service']= getattr(story.ServiceNowID,'LinkID','N/A')
            story_list.append(a_story)
    #if not response_defect.errors:
        #for story in response_defect:
            #a_story={}
            #a_story['State']=story.BusOpsKanban if story.BusOpsKanban else "unassigned"
            #a_story['id'] = story.FormattedID
            #a_story['name'] = story.Name
            #a_story['Opened']=(datetime.strptime(story.CreationDate, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%d-%b'))
            #a_story['Requester']= story.Owner.Name if story.Owner else "unassigned"
            #a_story['Blocked']= story.Blocked
            #a_story['Service']= getattr(story.ServiceNowID,'LinkID','N/A')
            #story_list.append(a_story)
    #else:
        #story_list = response.errors
    #print(story_list[0])
    return render(request, 'blog/story_list.html', {'stories': story_list})

def graph(request):
#     rally = initRally()
#     response = rally.get('UserStory',fetch = True, query='BusOpsKanban != ""')
#     print(response)
#     story_list = []
#     if not response.errors:
#         for story in response:
#             #print (story.details())
#             a_story={}
#             a_story['Kanban'] = story.BusOpsKanban
#             story_list.append(a_story)
#     else:
#         story_list = response.errors
#     print(story_list)
    return render(request, 'blog/graph.html')
