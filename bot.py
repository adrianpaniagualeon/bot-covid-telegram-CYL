import telebot
import requests
from telebot import types
from flask import Flask, request
import os
import json
from datetime import datetime, timedelta

TOKEN = os.environ['TOKEN']
URL_PUEBLO =  "Sahag%C3%BAn"
NOMBRE_PUEBLO = "Sahagún"


bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(regexp="ayuda")
def ayuda(message):
	cid = message.chat.id
	bot.send_message(cid, "Puedes obtener más ayuda en : https://github.com/adrianpaniagualeon/bot-covid-telegram-CYL")


		
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


	url = 'https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=prevalencia-coronavirus&q=sahagun&sort=fecha&facet=fecha&facet=zbs_geo&facet=provincia'

	respuesta = requests.get(url)
	open('respuesta.json', 'wb').write(respuesta.content)
	f = open('respuesta.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	resp = json.loads(json_str)


	prevalencia = 	resp['records'][0]['fields']['prevalencia']


	bercianos = 'https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&sort=fecha&q=&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&refine.municipio=Bercianos+del+Real+Camino'
	calzada ='https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&sort=fecha&q=&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&refine.municipio=Calzada+del+Coto'
	castrotierra ='https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&sort=fecha&q=&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&refine.municipio=Castrotierra+de+Valmadrigal'
	cea = 'https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&sort=fecha&q=&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&refine.municipio=Cea'
	elburgo = "https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&q=el+burgo&sort=fecha&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_65mas_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&refine.municipio=Burgo+Ranero%2C+El"
	escobar = 'https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&sort=fecha&q=&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&refine.municipio=Escobar+de+Campos'
	gordaliza = 'https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&q=&sort=fecha&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&refine.municipio=Gordaliza+del+Pino'
	grajal = 'https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&q=&sort=fecha&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&refine.municipio=Grajal+de+Campos'
	joarilla = 'https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&q=&sort=fecha&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&refine.municipio=Joarilla+de+las+Matas'
	sahagun = 'https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&q=&rows=10&sort=fecha&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&refine.municipio=Sahag%C3%BAn'
	santamaria = 'https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&q=&sort=fecha&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&refine.municipio=Santa+Mar%C3%ADa+del+Monte+de+Cea'
	vallecillo ='https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&q=&sort=fecha&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&refine.municipio=Vallecillo'
	villamartin ='https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&q=&sort=fecha&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&refine.municipio=Villamart%C3%ADn+de+Don+Sancho'
	villamol='https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&q=&sort=fecha&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&refine.municipio=Villamol'
	villaselan='https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&q=&sort=fecha&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&refine.municipio=Villasel%C3%A1n'
	villazanzo='https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=indicadores-de-riesgo-covid-19-por-municipios&q=&sort=fecha&facet=fecha&facet=municipio&facet=provincia&facet=ia14_boe_valoracion&facet=ia7_boe_valoracion&facet=ia14_boe_65mas_valoracion&facet=ia7_boe_valoracion&facet=positividad_valoracion&facet=porc_trazabilidad_valoracion&refine.municipio=Villazanzo+de+Valderaduey'


	PUEBLOS_INCIDENCIA_ALTA = ""

	respuesta = requests.get(bercianos)
	open('pueblo.json', 'wb').write(respuesta.content)
	f = open('pueblo.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	resp = json.loads(json_str)

	bercianos = resp['records'][0]['fields']['ia7_boe_valoracion']

	respuesta = requests.get(calzada)
	open('pueblo.json', 'wb').write(respuesta.content)
	f = open('pueblo.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	resp = json.loads(json_str)

	calzada = resp['records'][0]['fields']['ia7_boe_valoracion']


	respuesta = requests.get(castrotierra)
	open('pueblo.json', 'wb').write(respuesta.content)
	f = open('pueblo.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	resp = json.loads(json_str)

	castrotierra = resp['records'][0]['fields']['ia7_boe_valoracion']



	respuesta = requests.get(cea)
	open('pueblo.json', 'wb').write(respuesta.content)
	f = open('pueblo.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	resp = json.loads(json_str)

	cea = resp['records'][0]['fields']['ia7_boe_valoracion']

	respuesta = requests.get(elburgo)
	open('pueblo.json', 'wb').write(respuesta.content)
	f = open('pueblo.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	resp = json.loads(json_str)

	elburgo = resp['records'][0]['fields']['ia7_boe_valoracion']

	respuesta = requests.get(escobar)
	open('pueblo.json', 'wb').write(respuesta.content)
	f = open('pueblo.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	resp = json.loads(json_str)

	escobar = resp['records'][0]['fields']['ia7_boe_valoracion']



	respuesta = requests.get(gordaliza)
	open('pueblo.json', 'wb').write(respuesta.content)
	f = open('pueblo.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	resp = json.loads(json_str)

	gordaliza = resp['records'][0]['fields']['ia7_boe_valoracion']



	respuesta = requests.get(grajal)
	open('pueblo.json', 'wb').write(respuesta.content)
	f = open('pueblo.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	resp = json.loads(json_str)

	grajal = resp['records'][0]['fields']['ia7_boe_valoracion']



	respuesta = requests.get(joarilla)
	open('pueblo.json', 'wb').write(respuesta.content)
	f = open('pueblo.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	resp = json.loads(json_str)

	joarilla = resp['records'][0]['fields']['ia7_boe_valoracion']



	respuesta = requests.get(sahagun)
	open('pueblo.json', 'wb').write(respuesta.content)
	f = open('pueblo.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	resp = json.loads(json_str)

	sahagun = resp['records'][0]['fields']['ia7_boe_valoracion']



	respuesta = requests.get(santamaria)
	open('pueblo.json', 'wb').write(respuesta.content)
	f = open('pueblo.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	resp = json.loads(json_str)

	santamaria = resp['records'][0]['fields']['ia7_boe_valoracion']



	respuesta = requests.get(vallecillo)
	open('pueblo.json', 'wb').write(respuesta.content)
	f = open('pueblo.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	resp = json.loads(json_str)

	vallecillo = resp['records'][0]['fields']['ia7_boe_valoracion']



	respuesta = requests.get(villamartin)
	open('pueblo.json', 'wb').write(respuesta.content)
	f = open('pueblo.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	resp = json.loads(json_str)

	villamartin = resp['records'][0]['fields']['ia7_boe_valoracion']



	respuesta = requests.get(villamol)
	open('pueblo.json', 'wb').write(respuesta.content)
	f = open('pueblo.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	resp = json.loads(json_str)

	villamol = resp['records'][0]['fields']['ia7_boe_valoracion']



	respuesta = requests.get(villaselan)
	open('pueblo.json', 'wb').write(respuesta.content)
	f = open('pueblo.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	resp = json.loads(json_str)

	villaselan = resp['records'][0]['fields']['ia7_boe_valoracion']



	respuesta = requests.get(villazanzo)
	open('pueblo.json', 'wb').write(respuesta.content)
	f = open('pueblo.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	resp = json.loads(json_str)

	villazanzo = resp['records'][0]['fields']['ia7_boe_valoracion']




	if bercianos == "Muy alto":
		PUEBLOS_INCIDENCIA_ALTA += "Bercianos del Real Camino"

	if calzada == "Muy alto":
		PUEBLOS_INCIDENCIA_ALTA += " Calzada del Coto"

	if castrotierra == "Muy alto":
		PUEBLOS_INCIDENCIA_ALTA += " Castrotierra de Valmadrigal"

	if cea == "Muy alto":
		PUEBLOS_INCIDENCIA_ALTA += " Cea"

	if elburgo == "Muy alto":
		PUEBLOS_INCIDENCIA_ALTA += " El Burgo Ranero"

	if escobar == "Muy alto":
		PUEBLOS_INCIDENCIA_ALTA += " Escobar de Campos"

	if gordaliza == "Muy alto":
		PUEBLOS_INCIDENCIA_ALTA += " Gordaliza del Pino"

	if grajal == "Muy alto":
		PUEBLOS_INCIDENCIA_ALTA += " Grajal de Campos"

	if joarilla == "Muy alto":
		PUEBLOS_INCIDENCIA_ALTA += " Joarilla de las Matas"

	if sahagun == "Muy alto":
		PUEBLOS_INCIDENCIA_ALTA += " Sahagún"

	if santamaria == "Muy alto":
		PUEBLOS_INCIDENCIA_ALTA += " Santa María del Monte de Cea, "

	if vallecillo == "Muy alto":
		PUEBLOS_INCIDENCIA_ALTA += " Vallecillo"

	if villamartin == "Muy alto":
		PUEBLOS_INCIDENCIA_ALTA += " Villamartín de Don Sancho"

	if villamol == "Muy alto":
		PUEBLOS_INCIDENCIA_ALTA += " Villamol"

	if villaselan == "Muy alto":
		PUEBLOS_INCIDENCIA_ALTA += " Villaselán"

	if villazanzo == "Muy alto":
		PUEBLOS_INCIDENCIA_ALTA += " Villazanzo de Valderaduey"

	if PUEBLOS_INCIDENCIA_ALTA == "":
		PUEBLOS_INCIDENCIA_ALTA = "NINGUNO"

	url = 'https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=tasa-enfermos-acumulados-por-areas-de-salud&q=&sort=fecha&facet=fecha&facet=nombregerencia&facet=zbs_geo&facet=tipo_centro&facet=municipio&facet=centro&refine.centro=C.S.+SAHAGUN+CAMPOS'
	respuesta = requests.get(url)
	open('respuesta.json', 'wb').write(respuesta.content)
	f = open('respuesta.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	resp = json.loads(json_str)
	
	fecha_zona_json = resp['records'][0]['fields']['fecha']
	fecha_zona = datetime.strptime(fecha_zona_json, '%Y-%m-%d')
	fecha_zona = fecha_zona.strftime('%d-%m-%Y')

	pcr_realizados = 	resp['records'][0]['fields']['pcr_realizados']
	pcr_positivos  = 	resp['records'][0]['fields']['pcr_positivos']
	enfermos_14dias = resp['records'][0]['fields']['totalenfermedad_14dias']
	enfermos_7dias = resp['records'][0]['fields']['totalenfermedad_7dias']

	mensaje_datos = "📅 Datos correspondientes al dia: "+str(fecha)+"\n\n⬇️ Datos del Municipio de Sahagún\n\n Incidencia Acumulada (14 dias)\n👉 "+str(ia14)+" ("+ia14_valoracion+")\n Incidencia Acumulada (7 dias)\n"+"👉 "+str(ia7)+" ("+ia7_valoracion+")\n Positividad: "+"\n👉 "+str(positividad)+" ("+positividad_valoracion+")\n Casos última semana: "+"\n👉 "+str(casos_7d)+"\n\n⬇️ Datos Zona Básica de Sahagún\n\nPCR Realizados el "+fecha_zona+"\n👉 "+str(pcr_realizados)+"\nPCR Positivos el "+fecha_zona+"\n👉 "+str(pcr_positivos)+"\nPersonas enfermas en los últimos 14 dias\n👉 "+str(enfermos_14dias)+"\nPersonas enfermas en los últimos 7 dias\n👉 "+str(enfermos_7dias)+"\nPrevalencia\n👉 "+str(prevalencia)+ "\nPueblos con alta Incidencia\n👉 "+PUEBLOS_INCIDENCIA_ALTA+"\n\nDATOS OBTENIDOS DEL PORTAL DE DATOS ABIERTOS DE LA JUNTA DE CASTILLA Y LEÓN"
		

	bot.send_message(cid, mensaje_datos)


@bot.message_handler(commands={"start"})
def start(message):
	cid = message.chat.id
	bot.send_message(cid, "Hola. ¿Quieres ver los últimos datos del COVID-19 subidos por la Junta de Castilla y León en Sahagún? Solo tienes que hacer click sobre el siguiente comando: /datos y te los enviaré. Los datos les obtengo del portal de datos abiertos de la Junta de Castilla Y León. El bot ha sido programado por Adrián Paniagua.\n\n Puedes ver el proyecto en Github: https://github.com/adrianpaniagualeon/bot-covid-telegram-CYL")

@bot.message_handler(commands={"vacuna"})
def vacuna(message):
	cid = message.chat.id
	VACUNACION_PUEBLOS = "Próximas vacunaciones masivas en la provincia de León "
	resp = requests.get("https://www.saludcastillayleon.es/en/covid-19-poblacion/vacunacion-covid/lugares-vacunacion/leon")
	citas = resp.text.count("/en/covid-19-poblacion/vacunacion-covid/lugares-vacunacion/leon.files/")
	resp = resp.text.split('<li class="cmResourceType_pdf cmResourceItem cmOneResourceFile firstNode">')[1].split("</div>")[0]
	lugares = {}
	archivo = {}
	for i in range (citas):
		i = i+1
		lugares[i] = resp.split('<span class="resourceData2">')[i].split('</span>')[0]
		lugares[i] = lugares[i].replace("_", " ")
		lugares[i] = lugares[i].replace("compressed", "")
		lugares[i] = lugares[i].replace("-0", "")

		archivo[i] = "https://www.saludcastillayleon.es"
		archivo[i] = archivo[i] + resp.split('href="')[i].split('" class')[0]

		VACUNACION_PUEBLOS = VACUNACION_PUEBLOS + "📍 "+lugares[i]+"\nℹ️ "+archivo[i]+"\n\n"
        

	bot.send_message(cid, VACUNACION_PUEBLOS)


bot.infinity_polling()