import google.generativeai as palm
from django.conf import settings
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(settings.BASE_DIR, "gen-lang-client-0996968251-c3f5eecb19cd.json")

palm.configure(api_key=settings.PAML_API_KEY)

def get_response(prompt):
    response = palm.chat(messages=prompt)
    if response:
        return response.last
    else:
        return response('not response ')
