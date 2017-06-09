import os, re
from django.db.models import Q
from django.utils import timezone
from pyral import Rally, rallyWorkset
from datetime import datetime
import sys

#_ENH = "F1467"
#_PRJ = "F3841"

def getApiKey():
    if 'RALLY_API_KEY' in os.environ:
        api_key = os.environ['RALLY_API_KEY']
    elif 'OPENSHIFT_HOMEDIR' in os.environ: # this will be use onece we have openshift env.
        api_key = open(os.path.expanduser('~/app-root/repo/wsgi/xfr/metrics/.rally')).read().strip()
    else:
        api_key = open(os.path.expanduser('~/djangogirls/.rally')).read().strip()

    return api_key

def initRally():
    try:
        api_key = getApiKey()
    except Exception as e:
        raise Exception("Cannot read api key from file: %s." % (str(e)))

    try:
        rallyServer = rallyWorkset([])[0]
        rally = Rally(rallyServer, apikey = api_key, workspace='Red Hat IT Workspace',project='Team: Business Operations')
    except Exception as e:
        raise Exception("Unexpected error contacting Rally: %s." % (str(e)))

    return rally

def getStory(name):
    try:
        return Story.objects.get(rallyNumber=name)
    except Story.DoesNotExist:
        return None

def closeSession(session):
    session.endDate = timezone.now()
    session.save()
