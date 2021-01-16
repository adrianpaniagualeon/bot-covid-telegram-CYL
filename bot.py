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

		url = 'https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&q=&rows=10&sort=fecha&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_65mas_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&refine.municipio=Sahag%C3%BAn'


		respuesta = requests.get(url)
		open('respuesta.json', 'wb').write(respuesta.content)
		f = open('respuesta.json')
		json_file = json.load(f)
		json_str = json.dumps(json_file)
		resp = json.loads(json_str)

		fecha_json = resp['records'][0]['fields']['fecha']
		fecha = datetime.strptime(fecha_json, '%Y-%m-%d')
		fecha = fecha.strftime('%d-%m-%Y')

		ia14 = 	resp['records'][0]['fields']['ia14_boe']
		ia14_valoracion = 	resp['records'][0]['fields']['ia14_boe_65mas_valoracion']	
		ia7 =resp['records'][0]['fields']['ia7_boe']
		ia7_valoracion = resp['records'][0]['fields']['ia7_boe_65mas_valoracion']
		casos_7d = resp['records'][0]['fields']['casos_ultima_semana']
		positividad = resp['records'][0]['fields']['positividad']
		positividad_valoracion = resp['records'][0]['fields']['positividad_valoracion']
		trazabilidad = resp['records'][0]['fields']['porc_trazabilidad']
		trazabilidad_valoracion = resp['records'][0]['fields']['porc_trazabilidad_valoracion']


		url = 'https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=prevalencia-coronavirus&q=sahagun&sort=fecha&facet=fecha&facet=zbs_geo&facet=provincia'

		respuesta = requests.get(url)
		open('respuesta.json', 'wb').write(respuesta.content)
		f = open('respuesta.json')
		json_file = json.load(f)
		json_str = json.dumps(json_file)
		resp = json.loads(json_str)


		prevalencia = 	resp['records'][0]['fields']['prevalencia']


		url = 'https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=tasa-enfermos-acumulados-por-areas-de-salud&q=&sort=fecha&facet=fecha&facet=nombregerencia&facet=zbs_geo&facet=tipo_centro&facet=municipio&facet=centro&refine.centro=C.S.+SAHAGUN+CAMPOS'
		respuesta = requests.get(url)
		open('respuesta.json', 'wb').write(respuesta.content)
		f = open('respuesta.json')
		json_file = json.load(f)
		json_str = json.dumps(json_file)
		resp = json.loads(json_str)

		pcr_realizados = 	resp['records'][0]['fields']['pcr_realizados']
		pcr_positivos  = 	resp['records'][0]['fields']['pcr_positivos']
		enfermos_14dias = resp['records'][0]['fields']['totalenfermedad_14dias']
		enfermos_7dias = resp['records'][0]['fields']['totalenfermedad_7dias']

		mensaje_datos = "Datos del Municipio de Sahagún\n📅 Fecha de Datos: "+str(fecha)+"\n\n Incidencia Acumulada (14 dias)\n👉 "+str(ia14)+" ("+ia14_valoracion+")\n\n Incidencia Acumulada (7 dias)\n"+"👉 "+str(ia7)+" ("+ia7_valoracion+")\n\n Positividad: "+"\n👉 "+str(positividad)+" ("+positividad_valoracion+")\n\n Casos última semana: "+"\n👉 "+str(casos_7d)+"\n\n Trazabilidad : \n👉 "+str(trazabilidad)+"% ("+trazabilidad_valoracion+")\n\nDatos Zona Básica de Sahagún\nPCR Realizados Hoy\n👉🏻 "+str(pcr_positivos)+"\nPCR Positivos Hoy\n👉🏻 "+str(pcr_positivos)+"\nPersonas enfermas en los últimos 14 dias\n👉🏻 "+str(enfermos_14dias)+"\nPersonas enfermas en los últimos 7 dias\n👉🏻 "+str(enfermos_7dias)+"\nPrevalencia\n👉🏻 "+prevalencia
		
	else:
		bot.send_message(ADMIN_ID, "Los Datos no han sido enviados")

		
@bot.message_handler(commands={"datos"})
def datos(message):
	mensaje = message.text
	cid = message.chat.id

	url = 'https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&q=&rows=10&sort=fecha&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_65mas_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&refine.municipio=Sahag%C3%BAn'

	respuesta = requests.get(url)
	open('respuesta.json', 'wb').write(respuesta.content)
	f = open('respuesta.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	resp = json.loads(json_str)

	fecha_json = resp['records'][0]['fields']['fecha']
	fecha = datetime.strptime(fecha_json, '%Y-%m-%d')
	fecha = fecha.strftime('%d-%m-%Y')

	ia14 = 	resp['records'][0]['fields']['ia14_boe']
	ia14_valoracion = 	resp['records'][0]['fields']['ia14_boe_65mas_valoracion']	
	ia7 =resp['records'][0]['fields']['ia7_boe']
	ia7_valoracion = resp['records'][0]['fields']['ia7_boe_65mas_valoracion']
	casos_7d = resp['records'][0]['fields']['casos_ultima_semana']
	positividad = resp['records'][0]['fields']['positividad']
	positividad_valoracion = resp['records'][0]['fields']['positividad_valoracion']
	trazabilidad = resp['records'][0]['fields']['porc_trazabilidad']
	trazabilidad_valoracion = resp['records'][0]['fields']['porc_trazabilidad_valoracion']

	url = 'https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=prevalencia-coronavirus&q=sahagun&sort=fecha&facet=fecha&facet=zbs_geo&facet=provincia'

	respuesta = requests.get(url)
	open('respuesta.json', 'wb').write(respuesta.content)
	f = open('respuesta.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	resp = json.loads(json_str)


	prevalencia = 	resp['records'][0]['fields']['prevalencia']


	url = 'https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=tasa-enfermos-acumulados-por-areas-de-salud&q=&sort=fecha&facet=fecha&facet=nombregerencia&facet=zbs_geo&facet=tipo_centro&facet=municipio&facet=centro&refine.centro=C.S.+SAHAGUN+CAMPOS'
	respuesta = requests.get(url)
	open('respuesta.json', 'wb').write(respuesta.content)
	f = open('respuesta.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	resp = json.loads(json_str)

	pcr_realizados = 	resp['records'][0]['fields']['pcr_realizados']
	pcr_positivos  = 	resp['records'][0]['fields']['pcr_positivos']
	enfermos_14dias = resp['records'][0]['fields']['totalenfermedad_14dias']
	enfermos_7dias = resp['records'][0]['fields']['totalenfermedad_7dias']




	mensaje_datos = "Datos del Municipio de Sahagún\n📅 Fecha de Datos: "+str(fecha)+"\n\n Incidencia Acumulada (14 dias)\n👉 "+str(ia14)+" ("+ia14_valoracion+")\n\n Incidencia Acumulada (7 dias)\n"+"👉 "+str(ia7)+" ("+ia7_valoracion+")\n\n Positividad: "+"\n👉 "+str(positividad)+" ("+positividad_valoracion+")\n\n Casos última semana: "+"\n👉 "+str(casos_7d)+"\n\n Trazabilidad : \n👉 "+str(trazabilidad)+"% ("+trazabilidad_valoracion+")\n\nDatos Zona Básica de Sahagún\nPCR Realizados Hoy\n👉🏻 "+str(pcr_positivos)+"\nPCR Positivos Hoy\n👉🏻 "+str(pcr_positivos)+"\nPersonas enfermas en los últimos 14 dias\n👉🏻 "+str(enfermos_14dias)+"\nPersonas enfermas en los últimos 7 dias\n👉🏻 "+str(enfermos_7dias)+"\nPrevalencia\n👉🏻 "+prevalencia
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
