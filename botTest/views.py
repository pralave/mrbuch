import json,requests
from pprint import pprint

from django.shortcuts import render
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

class botTestingView(generic.View):
	def get(self, request, *args, **kwargs):
		if self.request.GET.get('hub.verify_token','') == 'mrbuch##':
			return HttpResponse(self.request.GET['hub.challenge'])
		else:
			return HttpResponse('okay, we are cool!')

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		incoming_message = json.loads(self.request.body.decode('utf-8'))
		for entry in incoming_message['entry']:
			for message in entry['messaging']:
				if 'message' in message:
					pprint(message)
					post_facebook_message(message['sender']['id'], message['message']['text'])
		return HttpResponse()

def post_facebook_message(fbid, recieved_message):
	post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAZAaxBGLb9oBAFZBzPRA9GNyyeV1rtl8rbYnWPaCgY3vQG23IppuEZAaMa3NZAChAg28q05haZBFhoBLvefntLyaZAQhDh7RBtKVTQsmDqdHmGvPe1RZB65PkNEiEO8ga472xF6cAoQmNE8men1Iz0CuEROnZAQYlpGAHKgr5u7HwZDZD'
	response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":recevied_message}})
	status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
	pprint(status.json())

	 
