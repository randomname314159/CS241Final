#Yoink some code, modify to fit new data
#Examining pokemon data
import pandas
import seaborn
import matplotlib as plt



#Taking input of a line of test from Pokemon.csv, returns the name of Pokemon as a string and its stats as a list
def get_info(line):
	commas=0
	name=""
	index=-1
	for c in line:
		index+=1
		if c == ",":
			commas+=1
		elif commas==1:
			name+=c
		elif commas==4:
			break
	ret = []
	for entry in line[index:line.rfind(",")].split(","):
		try:
			r=int(entry)
			ret.append(r)
		except ValueError:
			pass
	return name, ret
	



#make the dictionary
def getd():
	d = {}
	for line in open("Pokemon.csv","r"):
		#First line holds names of categories, rest are actual pokemon
		name, stats = get_info(line)
		d[name]=stats
	return d


def make_plot():
	data=getd()
	data.pop("Name")
	df = pandas.DataFrame.from_dict(data,orient="index",columns=['Total', 'HP','Attack','Defense','Sp. Atk','Sp. Def','Speed','Stage'])
	
	plt.rcParams['figure.figsize'] = [10, 10]
	plt.rcParams['figure.dpi'] = 100
	plt.pyplot.tick_params(axis='both', which='major', labelsize=10, labelbottom = False, bottom=False, top = False, left = False, labeltop=True)
	plt.style.use("dark_background")
	
	print(df)

	p = seaborn.boxplot(x="Stage",y="Speed",data=df,palette=seaborn.color_palette("flare"))
	#(df, cmap=seaborn.color_palette("mako", as_cmap=True))
	p.get_figure().savefig("pkmn3.png",bbox_inches='tight',transparent=True)


make_plot()
