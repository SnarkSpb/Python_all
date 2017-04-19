import codecs
import os
import shutil
import re

old_path=r'File="D:\\1C_BASE\\1Cv8\\КОТ\\КОТ_бух_30"'
new_path=r'Srvr="PSQL";Ref="KOT_buh"'
directory="\\\\172.16.0.254\\C$\\Users\\"
names=os.listdir(directory)
for usr in names:
	if not(os.path.isdir(directory+usr)):
		continue
	print(usr)
	file_name_v8=directory + usr + "\\AppData\\Roaming\\1C\\1CEStart\\ibases.v8i"
	file_name_v8_old=directory + usr + "\\AppData\\Roaming\\1C\\1CEStart\\ibases_res.v8i"
	if not os.path.exists(file_name_v8):
		continue
	shutil.copy(file_name_v8,file_name_v8_old)
	file_v8=codecs.open(file_name_v8,'w',encoding='utf-8')
	file_v8_old=codecs.open(file_name_v8_old,'r',encoding='utf-8')
	data=file_v8_old.read()
	data=re.sub(old_path,new_path,data)
	file_v8.write(data)
	file_v8.close()
	file_v8_old.close()
