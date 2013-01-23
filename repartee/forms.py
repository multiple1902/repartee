from django import forms
from models import App, Behavior, OS, Protocol

class QueryForm(forms.Form):
    beginTime   = forms.DateTimeField(required = False, widget = forms.TextInput(attrs = {'class': 'dateTimeInput'}), label = u"Begin Time")
    endTime     = forms.DateTimeField(required = False, widget = forms.TextInput(attrs = {'class': 'dateTimeInput'}), label = "End Time")
    #app         = forms.ModelChoiceField(queryset = App.objects.all(), required = False)
    behavior    = forms.ModelMultipleChoiceField(queryset = Behavior.objects.all(), required = False, label = "Behavior(s)")
    os          = forms.ModelMultipleChoiceField(queryset = OS.objects.all(), required = False, label = "OS(s)")
    srcIp       = forms.CharField(required = False, label = "Source IP")
    srcPort     = forms.IntegerField(required = False, label = "Source Port")
    dstIp       = forms.CharField(required = False, label = "Destination IP")
    dstPort     = forms.IntegerField(required = False, label = "Destination Port")
    protocol    = forms.ModelMultipleChoiceField(queryset = Protocol.objects.all(), required = False, label = "Protocol(s)")
