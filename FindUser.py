# -*- coding: utf-8 -*-
import codecs
import os

#old_path="D:\\1C_BASE\\Нептун\\Buh"
old_path="D:\\1C_BASE\\PKO\\PKO_UNF"
file_name_usr="D:\\users.txt"
with open(file_name_usr) as file_usr:
	names=file_usr.readlines()
	for usr in names:
		file_name_v8="\\\\172.16.0.254\\C$\\Users\\" + usr.rstrip() + "\\AppData\\Roaming\\1C\\1CEStart\\ibases.v8i"
		if os.path.exists(file_name_v8):
			file_v8=codecs.open(file_name_v8,'r',encoding='utf-8')
			rs=file_v8.readlines()
			for l in rs:
				if l.find(old_path)>0:
					print(usr.rstrip())
			file_v8.close()
file_usr.close()