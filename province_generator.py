#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image

import os
import codecs

prov_dir = os.getcwd()+"\\shatterednippon\\history\\provinces\\"
local_dir = os.getcwd()+"\\shatterednippon\\localisation\\"
map_dir = os.getcwd()+"\\shatterednippon\\map\\"

local_file = open(local_dir + "prov_names_l_english.yml", "w")
local_file.write("l_english:\n")

definitions = open(map_dir + "definition.csv", "w")
definitions.write("province;red;green;blue;x;x\n")

im = Image.open(map_dir+"provinces.bmp")
colors = []

image_size = im.size

for x in range(0, image_size[0]):
	for y in range(0, image_size[1]):
		cord = (x,y)
		pixel = im.getpixel(cord)
		if pixel not in colors and not (pixel[0:3] == (255,255,255) or pixel[0:3] == (0,0,0)): # excluding pure white and black
			colors.append(pixel) 

land_tiles = 451
sea_tiles = 91
provinces = len(colors)

x = 0
for color in colors:
	letter = (x%26) + 65
	out = "%d - " % (x+1)
	if x > 25:
		out += chr((x//26) + 64)
	out += chr(letter)
	if (x < land_tiles):
		f = open(prov_dir + out + ".txt", "w")
		f.write	(
"""# {0}

owner = JAP
add_core = JAP
controller = JAP

is_city = yes
hre = no

religion = shinto
culture = japanese

base_tax = 2
base_production = 2
base_manpower = 2

trade_goods = silk

capital = "{1}"

discovered_by = chinese""".format(out, out.split(" - ")[1]))
	local_file.write(' PROV{0}:0 "{1}"\n'.format(x+1, out.split(" - ")[1]))
	
	definitions.write("%d;%s;%s;%s;;%s\n" % (x+1, color[0], color[1], color[2], out.split(" - ")[1]))
	
	f.close()

	x += 1
	
local_file.close()
definitions.close()
