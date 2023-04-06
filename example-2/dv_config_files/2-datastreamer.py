# This source file is part of the ATMEL QTouch Library

# Copyright (c) 2016 Atmel Corporation. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#	this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#	this list of conditions and the following disclaimer in the documentation
#	and/or other materials provided with the distribution.
#
# 3. The name of Atmel may not be used to endorse or promote products derived
#	from this software without specific prior written permission.
#
# 4. This software may only be redistributed and used in connection with an
#	Atmel microcontroller product.
#
# THIS SOFTWARE IS PROVIDED BY ATMEL "AS IS" AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT ARE
# EXPRESSLY AND SPECIFICALLY DISCLAIMED. IN NO EVENT SHALL ATMEL BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


import sys

#---------------------- Edit only below this ------------------------------ #

# table_title_array[] contains the headings for the table.
# Based on number of table_title_array[], that many number of tables will be created
table_title_array = ["Sensor Data", "Configurations","Status"]

# The number of rows in a table is decided by table_num_of_rows_array[] array
# This should contain same number of element as that of table_title_array[]
table_num_of_rows_array = [6,1,1]

# table_header_array contains arrays of "lists"
# number of arrays depends on number of elements in table_title_array[]
# Each "lists" element forms table's column field
# If number of rows is more than one, then row number is added to the text
# If number of rows is only one, then no numbers are added to the text


table_header_array = [["Signal", "Reference", "Delta", "Threshold", "Detect", "NoiseEnv"],
												["Period","OverSamp","Sensitivity"], ["CurrFreq","FWVersion"]]

# table_header_size_array[] contains the size/sign details of each elements in table_header_array[]
# This should contain same number of elements as that of table_header_array[]
table_header_size_array = [["D","D","-D","B","B","-D"],
														["B","B","B"],["B","B"]]

# Graph elements array
# This should contain a list which is sub-set of table_header_array[0]'s list.
graph_array = ["Delta","Threshold","NoiseEnv"]
graph_array_visible = ["1", "1", "0"]

#---------------------- Edit only above this ------------------------------ #

x_width = 60
y_width = 25
xy_gap = 1

x_pos = 0
y_pos = 0
elements_per_row = len(table_title_array)


########################################################################################################################
def print_dashboard_head(string):
		print("{")
		print("0,")
		x = list(string)
		print(",".join( repr(e) for e in x ) + ",'\\0',")
		print("0, 255, 255, 255,")
		print("200, 4,")
		print("};")

def print_table_Banner(dashboard_num,element_num, xpos, ypos, string):
		print("{")
		print("%d, // Dashboard ID" % (dashboard_num))
		print("%d, // Element ID" % (element_num))
		print("DB_TYPE_LABEL, // Element Type")
		print("0, // Z-Index (GUI stack order)")
		print("%d, 0, // X-coordinate" % (xpos))
		print("%d, 0, // Y-coordinate" % (ypos))
		print("800, 0, // Width")
		print("30, 0, // Height")
		print("20, // Font Size")
		print("3,")
		print("1, // Horizontal Alignment")
		print("1, // Vertical Alignment")
		print("255, 105, 147, 219, // Background Color")
		print("255, 0, 0, 0, // Foreground Color")
		x = list(string)
		print(",".join( repr(e) for e in x ) + ",'\\0',")
		print("};") 

def print_warning(dashboard_num,element_num, xpos, ypos, string):
		print("{")
		print("%d, // Dashboard ID" % (dashboard_num))
		print("%d, // Element ID" % (element_num))
		print("DB_TYPE_LABEL, // Element Type")
		print("0, // Z-Index (GUI stack order)")
		print("%d, 0, // X-coordinate" % (xpos))
		print("%d, 0, // Y-coordinate" % (ypos))
		print("800, 0, // Width")
		print("20, 0, // Height")
		print("12, // Font Size")
		print("3,")
		print("0, // Horizontal Alignment")
		print("1, // Vertical Alignment")
		print("255, 255, 255, 255, // Background Color")
		print("255, 255, 0, 0, // Foreground Color")
		x = list(string)
		print(",".join( repr(e) for e in x ) + ",'\\0',")
		print("};") 



def print_table_title_new(dashboard_num,element_num, xpos, ypos, width, string):
		print("{")
		print("%d, // Dashboard ID" % (dashboard_num))
		print("%d, // Element ID" % (element_num))
		print("DB_TYPE_LABEL, // Element Type")
		print("0, // Z-Index (GUI stack order)")
		print("%d, 0, // X-coordinate" % (xpos))
		print("%d, 0, // Y-coordinate" % (ypos))
		print("%d, 0, // Width"% (width))
		print("25, 0, // Height")
		print("14, // Font Size")
		print("3,")
		print("1, // Horizontal Alignment")
		print("1, // Vertical Alignment")
		print("255, 105, 147, 219, // Background Color")
		print("255, 0, 0, 0, // Foreground Color")
		x = list(string)
		print(",".join( repr(e) for e in x ) + ",'\\0',")
		print("};") 

def print_table_title(dashboard_num,element_num, xpos, ypos, string):
		print("{")
		print("%d, // Dashboard ID" % (dashboard_num))
		print("%d, // Element ID" % (element_num))
		print("DB_TYPE_LABEL, // Element Type")
		print("0, // Z-Index (GUI stack order)")
		print("%d, 0, // X-coordinate" % (xpos))
		print("%d, 0, // Y-coordinate" % (ypos))
		print("200, 0, // Width")
		print("25, 0, // Height")
		print("14, // Font Size")
		print("3,")
		print("0, // Horizontal Alignment")
		print("1, // Vertical Alignment")
		print("126, 0, 255, 255, // Background Color")
		print("255, 0, 0, 0, // Foreground Color")
		x = list(string)
		print(",".join( repr(e) for e in x ) + ",'\\0',")
		print("};") 

def print_table_element(dashboard_num,element_num, xpos, ypos, Width, Height, data_width, label_width, row_height, rows, columns):
	print("{")
	print("%d, // Dashboard ID" % (dashboard_num))
	print("%d, // Element ID" % (element_num))
	print("DB_TYPE_TABLE, // Element Type")
	print("0, // Z-Index (GUI stack order)")
	print("%d, 0, // X-coordinate" % (xpos))
	print("%d, 0, // Y-coordinate" % (ypos))
	print("%d, 0, // Width" %(Width))
	print("%d, 0, // Height" %(Height))
	print("12, // Data Font Size")
	print("12, // Label Font Size")
	print("%d,0, // Data Column Width" %(data_width))
	print("%d,0, // Label Column Width" %(label_width))
	print("%d,0, // Row Height" %(row_height))
	print("%d, // Number of Rows" % (rows))
	print("%d, // Number of Columns" % (columns))
	print("1, // AutoLabels")
	print("'\\0', // Label Configuration")
	print("0,")
	print("0, 255, 255, 255, // Background Color")
	print("255, 0, 0, 0, // Foreground Color")
	print("0, // Label Horizontal Alignment")
	print("1, // Data Horizontal Alignment")
	print("};")

def split(word):
    return [char for char in word]

def print_table_element_new(dashboard_num,element_num, xpos, ypos, Width, Height, data_width, label_width, row_height, rows, columns,temp_text):
	print("{")
	print("%d, // Dashboard ID" % (dashboard_num))
	print("%d, // Element ID" % (element_num))
	print("DB_TYPE_TABLE, // Element Type")
	print("0, // Z-Index (GUI stack order)")
	print("%d, 0, // X-coordinate" % (xpos))
	print("%d, 0, // Y-coordinate" % (ypos))
	print("%d, 0, // Width" %(Width))
	print("%d, 0, // Height" %(Height))
	print("12, // Data Font Size")
	print("12, // Label Font Size")
	print("%d,0, // Data Column Width" %(data_width))
	print("%d,0, // Label Column Width" %(label_width))
	print("%d,0, // Row Height" %(row_height))
	print("%d, // Number of Rows" % (rows))
	print("%d, // Number of Columns" % (columns))
	print("0, // AutoLabels")
	print(temp_text)
	print("4,")
	print("0, 255, 255, 255, // Background Color")
	print("255, 0, 0, 0, // Foreground Color")
	print("1, // Label Horizontal Alignment")
	print("1, // Data Horizontal Alignment")
	print("};")


def print_graph_element(dashboard_num,element_num, xpos, ypos, string, num_of_plots):
	print("{")
	print("%d, // Dashboard ID" % (dashboard_num))
	print("%d, // Element ID" % (element_num))
	print("DB_TYPE_GRAPH, // Element Type")
	print("0, // Z-Index (GUI stack order)")
	print("%d, 0, // X-coordinate" % (xpos))
	print("%d, 0, // Y-coordinate" % (ypos))
	print("232, 3, // Width")
	print("244, 1, // Height")
	print("255, 255, 255, // Title color")
	print("0, 0, 0, // Background color")
	print("20, 20, 20, // Graph background color")
	x = list(string)
	print(",".join( repr(e) for e in x ) + ",'\\0',")
	print("%d," %num_of_plots)
	print("0,0,0,0, // X Minimum")
	print("0,0,32,65, // X Maximum")
	print("0,0,0,0, // Y Minimum")
	print("0,0,32,65, // Y Maximum")
	print("5,")
	print("1,")
	print("};")

def increase_y_pos(y_pos):
	return y_pos+25
def decrease_y_pos(y_pos):
	return y_pos-25
def increase_lable_cnt(label_cnt):
	label_cnt = label_cnt + 1

def getString(array, vertical):
	temp_text = ""
	if vertical == 0:
		for cnt in range(len(array)):
			temp_text += str(cnt)+":0"+":"+(array[cnt])+";"
		temp_text1 = ""
		for char in split(temp_text):
			temp_text1 += "\'"+char+"\',"
		temp_text1 += "','\\0', // Text"
	else:
		for cnt in range(len(array)):
			temp_text += "0:"+str(cnt)+":"+(array[cnt])+";"
		temp_text1 = ""
		for char in split(temp_text):
			temp_text1 += "\'"+char+"\',"
		temp_text1 += "','\\0', // Text"

	return temp_text1

curr_y_pos = 0

orig_stdout = sys.stdout
f = open('03EB00000000000000AA5501.db', 'w')
sys.stdout = f


sys.stdout = orig_stdout
f.close()

table_header_lable_cnt = 50
Banner_cnt = 100
label_cnt = 0

def printdebug(orig_std, text):
	temp = sys.stdout
	sys.stdout = orig_std
	print(text)
	sys.stdout = temp

orig_stdout = sys.stdout
f = open('03EB00000000000000AA5501.db', 'w')
sys.stdout = f
print_dashboard_head("MTCH1060 Debug")
print_table_Banner(0, Banner_cnt, 0,0, "MTCH1060 TUNE DATA")
curr_y_pos  = 50
data_width = 50
label_width = 75
row_height = 30
for temp_table_num in range(len(table_title_array)):
		
	### if number of row is zero - dont print that table
	if(table_num_of_rows_array[temp_table_num] != 0):
		row_cnt = table_num_of_rows_array[temp_table_num]
		column_cnt = len(table_header_array[temp_table_num])

		### print table title
		total_width = (label_width) * (column_cnt+1)
		if(total_width < 400):
			total_width = 400
		print_table_title_new(0, table_header_lable_cnt, 0,curr_y_pos, total_width, table_title_array[temp_table_num])
		curr_y_pos = curr_y_pos + 25
		table_header_lable_cnt = table_header_lable_cnt + 1
		#dashboard_num,element_num, xpos, ypos, Width, Height, data_width, label_width, row_height, rows, columns,debug_table_title
		### print table
		total_width = (data_width+label_width) * column_cnt
		total_height = (row_height)
		if(temp_table_num == 0):
			title = ["Channel ID"]
			temp_text = getString(title,0)
			print_table_element_new(0, table_header_lable_cnt, 0, curr_y_pos, label_width, row_height,data_width, label_width,row_height,1, 1, temp_text)
			table_header_lable_cnt = table_header_lable_cnt + 1
			temp_text = getString(table_header_array[temp_table_num],0)
			print_table_element_new(0, table_header_lable_cnt, label_width, curr_y_pos, total_width, row_height,data_width, label_width,row_height,1, column_cnt,temp_text)
		else:
			temp_text = getString(table_header_array[temp_table_num],0)
			print_table_element_new(0, table_header_lable_cnt, 0, curr_y_pos, total_width, row_height,data_width, label_width,row_height,1, column_cnt,temp_text)
		curr_y_pos = curr_y_pos + total_height
		table_header_lable_cnt = table_header_lable_cnt + 1

		total_width = (data_width+label_width) * column_cnt
		total_height = (row_height) * row_cnt
		if(temp_table_num == 0):
			title = []
			for cnt in range(len(table_header_array[temp_table_num])):
				title.append("Button "+str(cnt))
			temp_text = getString(title, 1)
			print_table_element_new(0, table_header_lable_cnt, 0, curr_y_pos, label_width, total_height,label_width, label_width,row_height,row_cnt, 1,temp_text)
			table_header_lable_cnt = table_header_lable_cnt + 1
			temp_text = getString(table_header_array[temp_table_num],0)
			temp_text = "'\\0', // Text"
			print_table_element_new(0, label_cnt, label_width, curr_y_pos, total_width, row_height,label_width, label_width,row_height,row_cnt, column_cnt,temp_text)
		else:
			temp_text = "'\\0', // Text"
			print_table_element_new(0, label_cnt, 0, curr_y_pos, total_width, total_height,label_width, label_width,row_height,row_cnt, column_cnt,temp_text)
		label_cnt = label_cnt + 1
		print("\n")
		curr_y_pos = curr_y_pos + total_height
	if(temp_table_num == 1):
		txt = "*** These values are not actual configuration values. These are ADC read values ranging from 0 (GND) to 255 (VCC)."
		print_warning(0, 255, xpos=0, ypos=curr_y_pos+5, string=txt)
	curr_y_pos = curr_y_pos + 50

### print graph
curr_y_pos = curr_y_pos + 25
element_num = len(table_title_array)
print_graph_element(0,label_cnt,0,curr_y_pos,"MTCH1060 Graph",len(graph_array)*table_num_of_rows_array[0])
label_cnt = label_cnt + 1

sys.stdout = orig_stdout
f.close()

print(label_cnt)


########################################################################################################################


########################################################################################################################
def print_one_script(ch_num,ele_cnt,array_num):
		temp = table_header_array[array_num]
		temp1 = table_header_size_array[array_num]

		temp_ch_num = 0
		for cnt in range(array_num):
				temp_ch_num = temp_ch_num + table_num_of_rows_array[cnt]
		temp_ch_num = temp_ch_num + ch_num

		if(table_num_of_rows_array[array_num] == 1):
				print("%s" %temp1[ele_cnt] + "," + "%d" %(temp_ch_num+2) + "," + "%d" %(ele_cnt+1) + "," + "%s" %temp[ele_cnt])
		else:
				print("%s" % temp1[ele_cnt] + "," + "%d" % (temp_ch_num + 2) + "," + "%d" % (ele_cnt + 1) + "," + "%s" % temp[
					ele_cnt] + "%d" % (ch_num))

orig_stdout = sys.stdout
f = open('03EB00000000000000AA5501.ds', 'w')
sys.stdout = f

### print header
print("B,1,1,framestart")
print("\n")

### print channel dependent
for array_num in range(len(table_title_array)):
		cnt = 0
		elements_per_row = len(table_header_array[array_num])

		for ch_num in range(table_num_of_rows_array[array_num]):
				for ele_cnt in range(elements_per_row):
						print_one_script(ch_num,ele_cnt,array_num)
				print("\n")

### print footer
print("B,1,2,frameend")

sys.stdout = orig_stdout
f.close()
########################################################################################################################

########################################################################################################################
def print_one_graph_conn(ele_cnt,row_cnt,ele_num,visibilty):
		print("%s" %graph_array[ele_cnt] + "%d" %row_cnt + "," + "%d" %ele_num, "(visible:%s)" %visibilty)


def print_one_table_conn(ele_num, ele_cnt,ch_cnt,row, column):
		temp_list = table_header_array[ele_num]

		if(table_num_of_rows_array[ele_num] == 1):
				print("%s" %temp_list[ele_cnt] + "," + " %d" %ele_num + " (Column:"+ "%d" %column + ";Row:" + "%d" %row + ")")
		else:
					print("%s" % temp_list[
							ele_cnt] + "%d" % ch_cnt + "," + " %d" % ele_num + " (Column:" + "%d" % column + ";Row:" + "%d" % row + ")")

orig_stdout = sys.stdout
f = open('03EB00000000000000AA5501.sc', 'w')
sys.stdout = f

for temp_table_num in range(len(table_title_array)):
		for ch_cnt in range(table_num_of_rows_array[temp_table_num]):
				for ele_cnt in range(len(table_header_array[temp_table_num])):
						print_one_table_conn(temp_table_num,ele_cnt,ch_cnt,ch_cnt,ele_cnt)
				print("\n")

ele_cnt = len(table_title_array)

for cnt in range(len(graph_array)):
		for ch_num in range(table_num_of_rows_array[0]):
				print_one_graph_conn(cnt, ch_num, ele_cnt,graph_array_visible[cnt])

print("\n")

sys.stdout = orig_stdout
f.close()
########################################################################################################################
