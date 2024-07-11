from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from urllib.request import urlopen
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
import json
import logging
import encodings
import os
from dotenv import load_dotenv


devId = '19DDCCD74FD9DAF165A96046950D899B1CB1FE1D0B8A1BA53C914175EE59D36D106C7AA7396A521EC3'
verify_key = 1      #placeholder

@csrf_exempt
def bot_view(request):
    if request.method in ['POST', 'GET']:
        try:
            raw_body = request.body
           # try:
               # verify_key = VerifyKey(bytes.fromhex(devId))
               # verify_key.verify(raw_body)
           # except BadSignatureError as e:
               # logging.error(f"Signature verification failed: {e}")
              #  return JsonResponse({'Error': 'Signature verification failed'}, status=401)

            if verify_key == 1:
                logger_info = {
                    logging.debug(f"Raw Body: {raw_body}"),
                }
                return JsonResponse(f'logger info: {logger_info}', status=200)

            if data.get('type') == 1:
                response_data = {
                    "type": 1,
                    }
                return JsonResponse(response_data, safe=False)

        except Exception as e:
            logging.error(f"Internal Server Error: {e}")
            return JsonResponse({'error': 'Internal Server Error'}, status=500)

        return HttpResponse("Hello, this is the interaction endpoint!", safe=False)

    if request.method == 'OPTIONS':
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    else:
        logging.warning("Invalid request method received")
        return JsonResponse({'error': 'Invalid request method'}, status=405)

