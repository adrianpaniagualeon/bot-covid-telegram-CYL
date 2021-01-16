import telebot
import requests
from telebot import types
from flask import Flask, request
import os
import json
from datetime import datetime, timedelta

TOKEN = os.environ['TOKEN']

ADMIN_ID = os.environ['ADMIN_ID']

GROUP_ID = os.environ['GROUP_ID']

WEBHOOK = os.environ['WEBHOOK']

PUEBLO = os.environ['PUEBLO']



bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands={"enviocovidgrupo"})
def enviomensajes(message):
	cid = message.chat.id

	if cid == ADMIN_ID:
		msg = bot.reply_to(message, "¿Esta seguro de que desea enviar los datos del COVID al grupo?")
		respuesta = types.ForceReply(selective=False)
		
		bot.register_next_step_handler(msg, confirmacion)
		
	else:
		bot.send_message(cid, "NO TIENES PERMIS PARA EJECUTAR ESTA ACCIÓN")

def confirmacion(message):
	mensaje = message.text
	respuesta2 = types.ForceReply(selective=False)
	if mensaje == "SI":
		try:
			yesterday = datetime.now() - timedelta(1)
			yesterday_1 = str(datetime.strftime(yesterday, '%Y-%m-%d'))
			yesterday_2 = datetime.strftime(yesterday, '%d-%m-%Y')
			url = 'https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&q=&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_65mas_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&facet=casos_ultima_semana&refine.municipio='+PUEBLO+'&refine.fecha='+yesterday_1


			respuesta = requests.get(url)
			open('respuesta.json', 'wb').write(respuesta.content)
			f = open('respuesta.json')
			json_file = json.load(f)
			json_str = json.dumps(json_file)
			resp = json.loads(json_str)


			ia14 = 	resp['records'][0]['fields']['ia14_boe']
			ia14_valoracion = 	resp['records'][0]['fields']['ia14_boe_65mas_valoracion']	
			ia7 =resp['records'][0]['fields']['ia7_boe']
			ia7_valoracion = resp['records'][0]['fields']['ia7_boe_65mas_valoracion']
			casos_7d = resp['records'][0]['fields']['casos_ultima_semana']
			positividad = resp['records'][0]['fields']['positividad']
			positividad_valoracion = resp['records'][0]['fields']['positividad_valoracion']
			trazabilidad = resp['records'][0]['fields']['porc_trazabilidad']
			trazabilidad_valoracion = resp['records'][0]['fields']['porc_trazabilidad_valoracion']


			mensaje_datos = "Datos del Municipio de Sahagún\n📅 Fecha de Datos: "+str(yesterday_2)+"\n\n Incidencia Acumulada (14 dias)\n👉 "+str(ia14)+" ("+ia14_valoracion+")\n\n Incidencia Acumulada (7 dias)\n"+"👉 "+str(ia7)+" ("+ia7_valoracion+")\n\n Positividad: "+"\n👉 "+str(positividad)+" ("+positividad_valoracion+")\n\n Casos última semana: "+"\n👉 "+str(casos_7d)+"\n\n Trazabilidad : \n👉 "+str(trazabilidad)+"% ("+trazabilidad_valoracion+")"
		except:
			beforeyesterday = datetime.now() - timedelta(2)
			beforeyesterday_1 = str(datetime.strftime(beforeyesterday, '%Y-%m-%d'))
			beforeyesterday_2 = datetime.strftime(beforeyesterday, '%d-%m-%Y')
			url = 'https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&q=&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_65mas_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&facet=casos_ultima_semana&refine.municipio='+PUEBLO+'&refine.fecha='+beforeyesterday_1


			respuesta = requests.get(url)
			open('respuesta.json', 'wb').write(respuesta.content)
			f = open('respuesta.json')
			json_file = json.load(f)
			json_str = json.dumps(json_file)
			resp = json.loads(json_str)


			ia14 = 	resp['records'][0]['fields']['ia14_boe']
			ia14_valoracion = 	resp['records'][0]['fields']['ia14_boe_65mas_valoracion']	
			ia7 =resp['records'][0]['fields']['ia7_boe']
			ia7_valoracion = resp['records'][0]['fields']['ia7_boe_65mas_valoracion']
			casos_7d = resp['records'][0]['fields']['casos_ultima_semana']
			positividad = resp['records'][0]['fields']['positividad']
			positividad_valoracion = resp['records'][0]['fields']['positividad_valoracion']
			trazabilidad = resp['records'][0]['fields']['porc_trazabilidad']
			trazabilidad_valoracion = resp['records'][0]['fields']['porc_trazabilidad_valoracion']


			mensaje_datos = "Datos del Municipio de Sahagún\n📅 Fecha de Datos: "+str(beforeyesterday_2)+"\n\n Incidencia Acumulada (14 dias)\n👉 "+str(ia14)+" ("+ia14_valoracion+")\n\n Incidencia Acumulada (7 dias)\n"+"👉 "+str(ia7)+" ("+ia7_valoracion+")\n\n Positividad: "+"\n👉 "+str(positividad)+" ("+positividad_valoracion+")\n\n Casos última semana: "+"\n👉 "+str(casos_7d)+"\n\n Trazabilidad : \n👉 "+str(trazabilidad)+"% ("+trazabilidad_valoracion+")"

		bot.send_message(GROUP_ID, mensaje_datos)
	else:
		bot.send_message(ADMIN_ID, "Los Datos no han sido enviados")

		
@bot.message_handler(commands={"datos"})
def datos(message):
	try:
		mensaje = message.text
		cid = message.chat.id

		yesterday = datetime.now() - timedelta(1)
		yesterday_1 = str(datetime.strftime(yesterday, '%Y-%m-%d'))
		yesterday_2 = datetime.strftime(yesterday, '%d-%m-%Y')
		before
		url = 'https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&q=&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_65mas_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&facet=casos_ultima_semana&refine.municipio=Sahag%C3%BAn&refine.fecha='+yesterday_1

		respuesta = requests.get(url)
		open('respuesta.json', 'wb').write(respuesta.content)
		f = open('respuesta.json')
		json_file = json.load(f)
		json_str = json.dumps(json_file)
		resp = json.loads(json_str)


		ia14 = 	resp['records'][0]['fields']['ia14_boe']
		ia14_valoracion = 	resp['records'][0]['fields']['ia14_boe_65mas_valoracion']	
		ia7 =resp['records'][0]['fields']['ia7_boe']
		ia7_valoracion = resp['records'][0]['fields']['ia7_boe_65mas_valoracion']
		casos_7d = resp['records'][0]['fields']['casos_ultima_semana']
		positividad = resp['records'][0]['fields']['positividad']
		positividad_valoracion = resp['records'][0]['fields']['positividad_valoracion']
		trazabilidad = resp['records'][0]['fields']['porc_trazabilidad']
		trazabilidad_valoracion = resp['records'][0]['fields']['porc_trazabilidad_valoracion']


		mensaje_datos = "Datos del Municipio de Sahagún\n📅 Fecha de Datos: "+str(yesterday_2)+"\n\n Incidencia Acumulada (14 dias)\n👉 "+str(ia14)+" ("+ia14_valoracion+")\n\n Incidencia Acumulada (7 dias)\n"+"👉 "+str(ia7)+" ("+ia7_valoracion+")\n\n Positividad: "+"\n👉 "+str(positividad)+" ("+positividad_valoracion+")\n\n Casos última semana: "+"\n👉 "+str(casos_7d)+"\n\n Trazabilidad : \n👉 "+str(trazabilidad)+"% ("+trazabilidad_valoracion+")"
	except:
		mensaje = message.text
		cid = message.chat.id

		beforeyesterday = datetime.now() - timedelta(2)
		beforeyesterday_1 = str(datetime.strftime(beforeyesterday, '%Y-%m-%d'))
		beforeyesterday_2 = datetime.strftime(beforeyesterday, '%d-%m-%Y')
		before
		url = 'https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&q=&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_65mas_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&facet=casos_ultima_semana&refine.municipio=Sahag%C3%BAn&refine.fecha='+beforeyesterday_1

		respuesta = requests.get(url)
		open('respuesta.json', 'wb').write(respuesta.content)
		f = open('respuesta.json')
		json_file = json.load(f)
		json_str = json.dumps(json_file)
		resp = json.loads(json_str)


		ia14 = 	resp['records'][0]['fields']['ia14_boe']
		ia14_valoracion = 	resp['records'][0]['fields']['ia14_boe_65mas_valoracion']	
		ia7 =resp['records'][0]['fields']['ia7_boe']
		ia7_valoracion = resp['records'][0]['fields']['ia7_boe_65mas_valoracion']
		casos_7d = resp['records'][0]['fields']['casos_ultima_semana']
		positividad = resp['records'][0]['fields']['positividad']
		positividad_valoracion = resp['records'][0]['fields']['positividad_valoracion']
		trazabilidad = resp['records'][0]['fields']['porc_trazabilidad']
		trazabilidad_valoracion = resp['records'][0]['fields']['porc_trazabilidad_valoracion']


		mensaje_datos = "Datos del Municipio de Sahagún\n📅 Fecha de Datos: "+str(beforeyesterday_2)+"\n\n Incidencia Acumulada (14 dias)\n👉 "+str(ia14)+" ("+ia14_valoracion+")\n\n Incidencia Acumulada (7 dias)\n"+"👉 "+str(ia7)+" ("+ia7_valoracion+")\n\n Positividad: "+"\n👉 "+str(positividad)+" ("+positividad_valoracion+")\n\n Casos última semana: "+"\n👉 "+str(casos_7d)+"\n\n Trazabilidad : \n👉 "+str(trazabilidad)+"% ("+trazabilidad_valoracion+")"

	bot.send_message(cid, mensaje_datos)


@bot.message_handler(commands={"start"})
def start(message):
	cid = message.chat.id
	bot.send_message(cid, "Hola. ¿Quieres ver los últimos datos del COVID-19 subidos por la Junta de Castilla y León en Sahagún? Solo tienes que hacer click sobre el siguiente comando: /datos y te los enviaré. Los datos les obtengo del portal de datos abiertos de la Junta de Castilla Y León. El bot ha sido programado por Adrián Paniagua  ")

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK+ TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
