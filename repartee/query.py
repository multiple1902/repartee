from django.shortcuts import render_to_response
from django.template import loader,Context, RequestContext
from django.db.models import Q
import md5

from models import Flow, App, Behavior, OS, Protocol
from forms import QueryForm

def queryHome(request):
    if request.method == "POST":
        # display query.query.html which includes queryResult.inc.html
        queryForm = QueryForm(request.POST)

        print queryForm.is_valid()
        queryID = md5.new(str(queryForm.cleaned_data)).hexdigest()

        if "queries" not in request.session:
            request.session["queries"] = {}

        request.session["queries"][queryID] = queryForm

        flows = Flow.objects.filter(getQFromQueryForm(queryForm))

        return render_to_response("query.query.html", {
                'queryForm': queryForm,
                'queryID': queryID,
                'resultsCount': len(flows),
            }, context_instance = RequestContext(request))

    else:
        # display query.home.html
        queryForm = QueryForm()
        return render_to_response("query.home.html", {
                'queryForm': queryForm,
            }, context_instance = RequestContext(request))

def getQFromQueryForm(queryForm):
    q = Q()

    if queryForm.cleaned_data["beginTime"] and queryForm.cleaned_data["endTime"]:
        q = q | Q(beginTime__gte = queryForm.cleaned_data["beginTime"],
                  beginTime__lte = queryForm.cleaned_data["endTime"])

    return q
