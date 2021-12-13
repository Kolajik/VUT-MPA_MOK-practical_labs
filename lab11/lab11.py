import numpy as np
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

VERBOSE = 0


def readf():
    txt = open('./edu.txt', 'r')  # read file
    LIST = txt.readlines()
    txt.close()

    data = []  # create data set from read file
    for x in LIST:
        data.extend([x.split()])
    for j in range(len(data)):
        for i in range(4, 11):
            if ((data[j][i] != ":") and (j != 0)):
                data[j][i] = float(data[j][i])
    del data[0]  # remove the name of the attributes
    return data


def statistics(data):
    new_data = []

    for i in range(len(data)):
        if i == 0:
            new_data.append([' ', 0, 0, 0, 0, 0, 0, 0, 0])
            new_data[i][0] = data[0][1]
            lang = 0
            for j in range(8):
                if data[i][j + 4] != ':':
                    new_data[i][1 + j] = round(float(new_data[i][1 + j]) + float(data[i][j + 4]), 1)
            if VERBOSE == 1: print(new_data[lang])
        elif data[i][1] == data[i - 1][1]:
            for j in range(8):
                if data[i][j + 4] != ':':
                    new_data[lang][1 + j] = round(float(new_data[lang][1 + j]) + float(data[i][j + 4]), 1)
            if VERBOSE == 1: print(new_data[lang])
        else:
            new_data.append([' ', 0, 0, 0, 0, 0, 0, 0, 0])
            lang = lang + 1
            new_data[lang][0] = data[i][1]
            for j in range(8):
                if data[i][j + 4] != ':':
                    new_data[lang][1 + j] = round(float(new_data[lang][1 + j]) + float(data[i][j + 4]), 1)
            if VERBOSE == 1: print(new_data[lang])
        nr_data = new_data[0:31]
        pc_data = new_data[32:62]
    return nr_data, pc_data


def plot_bar(data, lang):  # data = nr computed above and lang = list of languages to plot

    unit = []
    for l in lang:
        tdata = np.transpose(data)
        pos = list(tdata[0]).index(l)
        new = data[pos][1]
        unit.append(new)

    plt.xticks(rotation=90)
    plt.bar(lang, unit)
    plt.show()


def exercise1(data, language):
    years_sum = {"2012": 0,
                 "2013": 0,
                 "2014": 0,
                 "2015": 0,
                 "2016": 0,
                 "2017": 0,
                 "2018": 0,
                 "2019": 0
                 }
    for row in data:
        if row[0].upper() == 'NR':
            if row[1].upper() == language:
                for i in range(4, 12):
                    if row[i] == ':':
                        row[i] = 0
                years_sum['2019'] += int(row[4])
                years_sum['2018'] += int(row[5])
                years_sum['2017'] += int(row[6])
                years_sum['2016'] += int(row[7])
                years_sum['2015'] += int(row[8])
                years_sum['2014'] += int(row[9])
                years_sum['2013'] += int(row[10])
                years_sum['2012'] += int(row[11])

    return years_sum


def exercise2(data, language):
    unit = []
    print(data, "\n")
    for l in language:
        tdata = np.transpose(data)
        pos = list(tdata[0]).index(l)
        new = round(data[pos][1])
        print(new)
        if new > 150000:
            new = 150000
        if new < 5000:
            new = 5000
        unit.append(new)

    print(unit)
    plt.xticks(rotation=90)
    plt.bar(language, unit)
    plt.show()


if __name__ == '__main__':
    edu_data = readf()
    # print(edu_data[0])
    attributes = np.transpose(edu_data)
    # print(attributes)

    lang = set(attributes[1])
    lang.remove("TOTAL")
    lang.remove("OTH")
    language_list = list(lang)
    # print(language_list)

    exerciseOne_result = exercise1(edu_data, "FIN")
    print("Exercise one results: \n{}\n".format(exerciseOne_result))

    numbers, percentages = statistics(edu_data)
    # plot_bar(numbers, language_list)

    exercise2(numbers, language_list)
