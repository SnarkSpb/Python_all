# -*- coding: utf-8 -*-
import codecs
import os

#old_path="D:\\1C_BASE\\Нептун\\Buh"
old_path="D:\\1C_BASE\\1Cv8\\КОТ\\КОТ_бух_30"
directory="\\\\172.16.0.254\\C$\\Users\\"
names=os.listdir(directory)
for usr in names:
	if not(os.path.isdir(directory+usr)):
		continue
	file_name_v8=directory+ usr + "\\AppData\\Roaming\\1C\\1CEStart\\ibases.v8i"
	if os.path.exists(file_name_v8):
		file_v8=codecs.open(file_name_v8,'r',encoding='utf-8')
		rs=file_v8.readlines()
		for l in rs:
			if l.find(old_path)>0:
				print(usr)
		file_v8.close()
