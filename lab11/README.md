# Laboratoty 11 - Data Anonymization

**Data anonymization** allows protecting private data while publishing useful information.
It is based on *Statistical Disclosure Control (SDC)* methods that aim at releasing data that preserve their
statistical validity while protecting the privacy of each data subject.

In this laboratory, we will work with **non-perturbative masking**. 

| Method  | Numerical data | Categorical data  
| ------------- | ------------- | ------------- |
| Sampling  |  | x |
| Global recoding | x | x |
| Top and bottom coding | x | x |
| Local suppression |  | x |

## The data set 

The [Adult Education Survey (AES)](https://ec.europa.eu/eurostat/web/microdata/adult-education-survey) covers adult participation in education and training and is one of the main data sources for EU lifelong learning statistics. 
We will use as input [EDU](edu.txt) data set which is a sub-data set of AES that covers the topic *Pupils by education level and modern foreign language studied - absolute numbers and % of pupils by language studied*. 
Th database is publicly available in [Eurostat](https://ec.europa.eu/eurostat/web/education-and-training/data/database) web page. 

| Unit of measure  | Language | International standard | Geopolitical entity | 2019 | 2018 | 2017 | 2016 | 2015 | 2014 | 2013 | 2012 
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Number (NR) | CZE | Primary education (ED1) | Germany (GE) |  |  |  |  |  | |  |  |
| Percentage (PC) | ENG | Lower secondary education (ED2 | Estonia (EE)  |  |  |  |  |  | |  |  |
|  | GER | Upper secondary education (ED3) | France (FR) |  |  |  |  |  | |  |  |
|  | ITA | Upper secondary education - general (ED34) | Portugal (PT)  |  |  |  |  |  | |  |  |
|  | ... | Upper secondary education - vocational (ED35) | ...  |  |  |  |  |  | |  |  

The sub-survey counts 29 Languages, 37 Geopolitical entities and it was ran for 8 years (from 2012 to 2019). 

## How to read a data set

```python
def readf():
	txt = open('./edu.txt','r')        #read file
	LIST = txt.readlines()
	txt.close()

	data = []          #create data set from read file
	for x in LIST:
		data.extend([x.split()])
	for j in range(len(data)):
		for i in range(4,12):
			if ((data[j][i] != ":") and (j!=0)):
				data[j][i] = float(data[j][i])
	del data[0] #remove the name of the attributes
	return data
```
This command allows import the data set as a python list. 
Please upload this commend in a file. In our case, we named the file data_anonym.py

```python
import data_anonym as dano 
data = dano.readf()
```

## Statistical analyses on the uploaded data set

We would like to run some statistical analyses on *data*. Below some useful commands.  

* The data set is upload in records, i.e., data[i] is a record (row) for all i. We may need to work on attributes (columns). 
we can use the function *np.transpose*
```python
import numpy as np
attr = np.transpose(data)
```

*  We would like to know the selection of Language acronyms appearing in the data set. We can use the function *set* which let you pass from a list with repetition to a set. In sets, each element appear only one time, by definition.
```python
lang = set(attr[1])
lang
len(lang)
```
* In order to have the list of languages, we need to remove *TOTAL* or *OTH* (other). 
```python
lang.remove('TOTAL') 
```
Please remove *OTH*.  
Therefore, the number of luanguages consisidered is *len(lang)* and the acronyms are:
```python
['ARA', 'BUL', 'CHI', 'CZE', 'DAN', 'DUT', 'ENG', 'EST', 'FIN', 'FRE', 'GER', 'GLE', 'GRE', 'HRV', 'HUN', 'ITA', 'JPN', 'LAV', 'LIT', 'MLT', 'POL', 'POR', 'RUM', 'RUS', 'SLO', 'SLV', 'SPA', 'SWE', 'UNK']
```
* To pass from set to list: 
```python
lang_list = list(lang)
```
### Exercise 1 (1.5p)
Create a python3 script that does as follow: 
* input: data set, *Language* (acronym in the list)
* return: count the total number of students per year (*2019*, *2018*, *2017*, *2016*, *2015*, *2014*, *2013*, *2012*).  
* try the scrypt with *data*, 'CZE'
* Hint: you are interested only in values belonging to *NR*

### Data sets to be anonymized
From data we can extract two data sets *nr* and *pc*. 
* *nr* is the data set with the total number of students studing that language per year
* *pc* is the data set with the percentage of students studing that language per year

The following code allows computing the two data sets:
```python
def statistics(data):


	new_data = []
	
	for i in range(len(data)):
		if i==0:
			new_data.append([' ',0,0,0,0,0,0,0,0])
			new_data[i][0] = data[0][1]
			lang = 0
			for j in range(8):
				if data[i][j+4] != ':':
					new_data[i][1+j] = round(new_data[i][1+j] + data[i][j+4],1) 
			if VERBOSE == 1: print(new_data[lang])		
		elif data[i][1] == data[i-1][1]:
			for j in range(8):
				if data[i][j+4] != ':':
					new_data[lang][1+j] = round(new_data[lang][1+j] + data[i][j+4],1)
			if VERBOSE == 1: print(new_data[lang]) 
		else: 
			new_data.append([' ',0,0,0,0,0,0,0,0])
			lang = lang + 1
			new_data[lang][0] = data[i][1]	 				
			for j in range(8):
				if data[i][j+4] != ':':
					new_data[lang][1+j] = round(new_data[lang][1+j] + data[i][j+4],1)
			if VERBOSE == 1: print(new_data[lang])
		nr_data = new_data[0:31]
		pc_data = new_data[32:62]
	return nr_data, pc_data
```

Try to plot the language situation for year 2019 (bar plot):
```python
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

def plot_bar(data,lang): #data = nr computed above and lang = list of languages to plot  

	unit = []
	for l in lang:
		tdata = np.transpose(data) 
		pos =  list(tdata[0]).index(l)
		new = data[pos][1]
		unit.append(new)

	plt.xticks(rotation=90)
	plt.bar(lang, unit)
	plt.show()
```
This plot helps in recognizing "dangerous" values (too big in particular). 

## Data privacy - non-perturbative masking

Some languagues present few students and others too can be reognized for the opposite situation. 
Let use apply Global Reording method to the data set *nr*. 

### Exercise 2 (1.5 p.) 
Propose an anomimyzation of *nr* by:
* identifing unsecure values (too small, too big)
* generalizing the value in a bigger cathegory
* plot the row data and the anonymized data.
* IMPORTANT: consider only the list of languages (remove *TOT*)

### Homework: data needs to be prepared (1 p.)
* choose a data set that you find interesting
* export the data set in *cleaned* .txt format 
* run some simple statistic of your interest. 
* NOTE: the best data set with analysis presented will receive bous point.      
