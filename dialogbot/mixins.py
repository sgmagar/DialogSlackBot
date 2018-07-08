import json
import logging

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from dialogbot.models import Team


class SlackMixin:
    set_team_obj = False

    def __init__(self):
        self.client_id = settings.DIALOG_APP['client_id']
        self.client_secret = settings.DIALOG_APP['client_secret']
        self.verification_token = settings.DIALOG_APP['verification_token']
        self.scopes = settings.DIALOG_APP['scopes']

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if self.set_team_obj:
            self.data = request.POST
            logging.info(self.data)
            if not self.data.get("token"):
                self.data = json.loads(self.data['payload'])
            if self.data['token'] != self.verification_token:
                logging.warning("Incorrect token received.")
                return HttpResponse(status=403, content=b"Token does not match.")
            team_id = self.data.get('team_id', None)
            if not team_id:
                team_id = self.data['team']['id']
            self.team = get_object_or_404(Team, team_id=team_id, app_id=self.client_id)
        return super().dispatch(request, *args, **kwargs)

    def get_redirect_url(self):
        proto = "https" if self.request.is_secure() else "http"
        return f"{proto}://{self.request.get_host()}{reverse('oauth_callback')}"
