# coding: utf-8
import requests
import time
import json
import csv
import sys
import os

with open("CEP.csv") as file:
	
	reader = csv.DictReader(file)
	cont = 0

	file_new = open("log.txt", "w")
	for row in reader:
		
		cep_line = str(row['cep'])
		
		r = requests.get("https://viacep.com.br/ws/" + cep_line + "/json/")
		a = r.text
		b = json.loads(a)
		
		final = str(cep_line) + ", " + str(b["bairro"] +  ", " + str(b["localidade"]) +  ", " + str(b["uf"])+ "\n")
		print(final)
		
		# Adicionar aqui o limitador de tempo
		# time.sleep(2)

		file_new.writelines(final)
	
	file_new.close()
