from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from flask import jsonify, Flask
from urllib.request import urlopen
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
import json
import logging
import encodings
import os
from dotenv import load_dotenv
from flask import Blueprint, jsonify
from .Vampiremino import bot, devId

bp = Blueprint('main', __name__)


@csrf_exempt
def bot_view(request):
        try:
            @bp.route('/interactions/', methods=['POST', 'GET'])
            def interactions():
                try:
                    raw_body = request.body
                    try:
                        verify_key = VerifyKey(bytes.fromhex(devId))
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

                except Exception as e:
                    logging.error(f"Internal Server Error: {e}" + f"logger info: {logger_info}")
                    return JsonResponse({'error': 'Internal Server Error'}, status=500)
                pass

                return jsonify({"message": "Hello, this is the interaction endpoint!"})


            if request.method == 'OPTIONS':
                self.send_response(200)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
                self.send_header('Access-Control-Allow-Headers', 'Content-Type')
                self.end_headers()
            else:
                logging.warning("Invalid request method received")
                return JsonResponse({'error': 'Invalid request method'}, status=405)
