#0=id, 1=year, 2=firstname, 3=last, 4=team, 5=leag, 6=gp, 7=min, 8=pts, 9=oreb, 10=dreb
#11=reb,12=asts, 13=stl, 14=blk, 15=turnover, 16=pf, 17=fga, 18=fgm, 19=fta, 20=ftm, 21=tpa, 22=tpm

import csv
reader = csv.reader(open('player_regular_season.csv','rU'))
data_list = list(reader) # csv_reader is a list of each of the rows in the file


y = data_list.readline()
print y

efficiency = [] #list of efficiency values
named_efficiency = [] #lists (efficiency, name of player) tuples



#def efficiency_data():
#	for rows in pd:
#		p_e = ((int(rows[8])+int(rows[11])+int(rows[12])+int(rows[13])+int(rows[14])))-((int(rows[17])-int(rows[18]))+(int(rows[19])-int(rows[20])))/int(rows[6])
#		efficiency.append(p_e)