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


signature_key = '4a9a340e68e24016a3b40bf79677b371'
#placeholder
placeholder = '1'


@csrf_exempt
def bot_view(request):
    try:
        if request.method == 'POST':
            try:
                raw_body = request.body
                signature = request.headers.get(signature_key)
                try:
                    verify_key = VerifyKey(bytes.fromhex(signature))
                    verify_key.verify(raw_body)
                except BadSignatureError as e:
                    logging.error(f"Signature verification failed: {e}")
                    return JsonResponse({'Error': 'Signature verification failed'}, status=401)

                if verify_key == verify_key:
                    logger_info = {
                        logging.debug(f"Raw Body: {raw_body}"),
                    }
                    return JsonResponse(f'logger info: {logger_info}', status=200)
                if data.get('type') == 1:
                    response_data = {
                        "type": 1,
                        }
                    return JsonResponse(response_data, safe=False)
                pass
                if placeholder == '1':
                    return JsonResponse({'Message': 'Hey!'}, status=200)
            except Exception as e:
                logging.error(f"Internal Server Error: {e}")
                return JsonResponse({'error': 'Internal Server Error'}, status=500)

        if request.method == 'GET':
            return HttpResponse("Hello, this is the interaction endpoint!")

        if request.method == 'OPTIONS':
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()

        else:
            logging.error(f"Invalid method received")
        return JsonResponse({'error': 'Invalid method received'}, status=405)

    except Exception as e:
        logging.error(f"Internal Server Error: {e}")
        return JsonResponse({'error': 'Internal Server Error'}, status=500)
