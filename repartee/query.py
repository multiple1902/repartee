from django.shortcuts import render_to_response
from django.template import loader,Context, RequestContext

from models import App, Behavior, OS, Protocol
from forms import QueryForm

def queryHome(request):
    if request.method == "POST":
        # display query.query.html which includes queryResult.inc.html
        queryForm = QueryForm(request.POST)
        print queryForm.is_valid()
        return render_to_response("query.query.html", {
                'queryForm': queryForm,
            }, context_instance = RequestContext(request))
    else:
        # display query.home.html
        queryForm = QueryForm()
        return render_to_response("query.home.html", {
                'queryForm': queryForm,
            }, context_instance = RequestContext(request))

