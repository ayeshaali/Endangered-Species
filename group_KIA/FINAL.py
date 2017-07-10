import plotly.plotly as ply
import csv
import pandas as pd 	
import random
ply.sign_in('ayeshaali', '54164bqw0n')

import matplotlib.pyplot as plt

def menu ():
	country_choice = raw_input(' \033[1m' + '''
Come Help The Animals ''' + '\033[0m' + '''

The information in this program is about endangered and threatened species throughout the world.

Your four options include:
	1. A '''+ ' \033[1m' + '''chloropleth world map'''+ '\033[0m' +''' of Endangered Species
	2. A '''+ ' \033[1m' + '''pie chart'''+ '\033[0m' +''' that shows the statistics of a country's extinct, endangered, near threatened, and least concerned species. This option is available for most countries, but not all. 
	3. A '''+ ' \033[1m' + '''chloropleth world map'''+ '\033[0m' +''' of Threatened Mammal Species. 
	4. A '''+ ' \033[1m' + '''random fact generator'''+ '\033[0m' +''' about different endangered species.  

Enter the number respective to your choice.

	If you want to quit, enter 5.

Enter your choice: ''')
	while country_choice != '5':
		if country_choice == '1':
			choropleth()
		elif country_choice == '2':
			pieChart()
		elif country_choice == '3':
			choroplethMammal()
		elif country_choice == '4':
			andom()
		else:
			print ('\033[1m'+"Sorry, that's not an option. Try again:"+'\033[0m'+'\t')
		country_choice = raw_input(' \033[1m' + '''
Come Help The Animals ''' + '\033[0m' + '''

The information in this program is about endangered and threatened species throughout the world.

Your four options include:
	1. A '''+ ' \033[1m' + '''chloropleth world map'''+ '\033[0m' +''' of Endangered Species
	2. A '''+ ' \033[1m' + '''pie chart'''+ '\033[0m' +''' that shows the statistics of a country's extinct, endangered, near threatened, and least concerned species. This option is available for most countries, but not all. 
	3. A '''+ ' \033[1m' + '''chloropleth world map'''+ '\033[0m' +''' of Threatened Mammal Species. 
	4. A '''+ ' \033[1m' + '''random fact generator'''+ '\033[0m' +''' about different endangered species.  

Enter the number respective to your choice.

	If you want to quit, enter 5.

Enter your choice: ''')

	if country_choice == '5':
		quit()


def make_autopct(fracs):
	def my_autopct(pct):
		total = sum(fracs)
		val = int(round(pct*total/100.0))
		return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
	return my_autopct

def pieChart():
	f = open("species6.csv","r")
	data = csv.reader(f)
	headers = data.next()
	data = list(data)

	#Country	Continent	Extinct	Endangered	Near_Threat	Least_Concern	Total
	labels = ['Extinct', 'Endangered', 'Near Threat', 'Least Concern']
	extinct = []
	endangered = []
	nearT = []
	leastC =[]
	cols = ['red', 'orange', 'yellow', 'lightgreen']
	
	#with pie charts, you should always set the figure size to two of the same values, otherwise it is distorted
	plt.figure(figsize =(8,8))
	
	a = ""
	while a != '1': 
		choice = raw_input('\nEnter a country: ')
		#move to separate function
		shown = False
		for row in data:
			if choice == row[0]:
				shown = True
				extinct.append(float(row[3]))
				endangered.append(float(row[4]))
				nearT.append(float(row[5]))
				leastC.append(float(row[6]))
				#autopct puts the values on the chart for easy readability!
				fracs = [sum(extinct), sum(endangered), sum(nearT), sum(leastC)]

				plt.pie(fracs, colors = cols, startangle = 45, autopct = make_autopct(fracs), shadow = True, radius = 4, )
				#(more info on autopct at http://stackoverflow.com/questions/6170246/how-do-i-use-matplotlib-autopct?rq=1)
				plt.axis('equal')
				plt.title(str(choice))
				plt.legend(labels, bbox_to_anchor = (.85, 1.05), loc=2, borderaxespad=1.0)
				plt.show()
		if shown == False:
			print ('\033[1m'+"Sorry, that's not an option. Try again:"+'\033[0m'+'\t')
		a = (raw_input('\nIf you want to quit to the menu, enter 1. Type any other character to look for another country. \n'))

	f.close()

def choropleth ():
	species = pd.read_csv('https://raw.githubusercontent.com/ayeshaali/Endangered-Species/master/group_KIA/species6.csv')

	for col in species.columns:
		species[col] = species[col].astype(str)


	geo_deets = dict(
			scope = 'world',
			projection = dict(type ='Mercator'),
			showlakes = False
		)

	map_layout = dict(
		title = '2015 Endangered Species by Country',
		geo = geo_deets
		)

	violet_scale = [[0.0, 'lavender'], [1.0, 'indigo']]

	species['text'] = species['Country']+'<br> Sum: '+species['Total']+'<br> Extinct: '+species['Extinct']+'<br> Endangered: ' +species['Endangered']+'<br> Near Threatened: ' +species['Near_Threat']+'<br> Least Concern: '+species['Least_Concern']

	stuff = [ dict(
			type = 'choropleth',
			colorscale = violet_scale,
			autocolorscale = False,
			locations = species['CODE'],
			z = species['Endangered'].astype(int),
			locationmode = 'ISO-3',
			text = species['text'],
			marker  = dict(
				line = dict(
					color = 'rgb(255,255,255)',
					width = 2
					)
				),
			colorbar = dict (
				title = 'Number of Endangered Species'
				)
		)
	]

	plotly_fig = dict(
		data = stuff,
		layout = map_layout
		)

	ply.plot(plotly_fig, filename = 'awesome-sauce-map2')

def choroplethMammal():
	species = pd.read_csv('https://raw.githubusercontent.com/ayeshaali/Endangered-Species/master/group_KIA/mammalData.csv')

	for col in species.columns:
		species[col] = species[col].astype(str)


	geo_deets = dict(
			scope = 'world',
			projection = dict(type ='Mercator'),
			showlakes = False
		)

	map_layout = dict(
		title = '2015 Threatened Mammal Species by Country',
		geo = geo_deets
		)

	violet_scale = [[0.0, 'lightblue'], [1.0, 'blue']]

	species['text'] = species['Country Name']+'<br> Sum: '+species['2015']

	stuff = [ dict(
			type = 'choropleth',
			colorscale = violet_scale,
			autocolorscale = False,
			locations = species['Country Code'],
			z = species['2015'].astype(int),
			locationmode = 'ISO-3',
			text = species['text'],
			marker  = dict(
				line = dict(
					color = 'rgb(255,255,255)',
					width = 2
					)
				),
			colorbar = dict (
				title = 'Number of Threatened Mammal Species'
				)
		)
	]

	plotly_fig = dict(
		data = stuff,
		layout = map_layout
		)

	ply.plot(plotly_fig, filename = 'awesome-sauce-map2')

	menu()


def andom():
	f= open("newfunfacts.csv", "r")
	data =csv.reader(f)
	animal = random.randint (1,30)
	for row in data:
		if animal == int(row[0]):
			print ("The animal/plant is "+ '\033[1m' + row[1]+ ".\n"+'\033[0m')
			choice= raw_input("If you want to quit to the menu, press 1. Would you like to learn about this animal/plant? If so, press 2. If you want another animal/plant, press 3. \n\n")
			if choice == "2":
				print ('\033[1m' + row[2]+'\033[0m'+'\n')
				choice1 = raw_input('If you want to quit to the menu, press 1. If you would like to learn about another animal/plant, press 2. \n\n')
				if choice1 == '2':
					andom()
				elif choice1 == '1':
					menu()
				else: 
					print ('\033[1m'+"Sorry, that's not an option. Try again:"+'\033[0m'+'\t')
					choice1 = raw_input('If you want to quit to the menu, press 1. If you would like to learn about another animal/plant, press 2. \n\n')
			elif choice == "3":
				andom()
			elif choice == "1":
				menu()
			else:
				print ('\033[1m'+"Sorry, that's not an option. Try again:"+'\033[0m'+'\t')
				choice= raw_input("If you want to quit to the menu, press 1. Would you like to learn about this animal/plant? If so, press 2. If you want another animal/plant, press 3. \n\n")

menu()
