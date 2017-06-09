import codecs
import os
import shutil
import re

# КОТ_бух_30
# old_path=r'File="D:\\1C_BASE\\1Cv8\\КОТ\\КОТ_бух_30"'
# new_path=r'Srvr="PSQL";Ref="KOT_buh"'
# ПКО УНФ 2017-05-05
#old_path = r'File="D:\\1C_BASE\\PKO\\PKO_UNF"'
#new_path = r'Srvr="PSQL";Ref="PKO_unf"'
#НИИРПИ зуп 25
#old_path = r'File="D:\\1C_BASE\\1Cv8\\HRM"'
#new_path = r'Srvr="PSQL";Ref="NIIRPI_zup_25"'
#НИИРПИ зуп 3
#old_path = r'File="D:\\1C_BASE\\1Cv8\\NIIRPI_ZUP_3"'
#new_path = r'Srvr="PSQL";Ref="NIIRPI_zup_3"'
#КОТ зуп 25
#old_path = r'File="D:\\1C_BASE\\1Cv8\\KOT_ZUP"'
#new_path = r'Srvr="PSQL";Ref="KOT_zup_25"'
#КОТ зуп 3
#old_path = r'File="D:\\1C_BASE\\1Cv8\\KOT_ZUP_3"'
#new_path = r'Srvr="PSQL";Ref="KOT_zup_3"'
#НИИРПИ бух
#old_path = r'File="D:\\1C_BASE\\1Cv8\\Buh_n"'
#new_path = r'Srvr="PSQL";Ref="NIIRPI_buh"'
#ПКО зуп
old_path = r'File="D:\\1C_BASE\\PKO\\PKO_ZUP"'
new_path = r'Srvr="PSQL";Ref="PKO_zup"'




directory = "\\\\172.16.0.254\\C$\\Users\\"
names = os.listdir(directory)
for usr in names:
    if not (os.path.isdir(directory + usr)):
        continue
    file_name_v8 = directory + usr + "\\AppData\\Roaming\\1C\\1CEStart\\ibases.v8i"
    file_name_v8_old = directory + usr + "\\AppData\\Roaming\\1C\\1CEStart\\ibases_res.v8i"
    if not os.path.exists(file_name_v8):
        continue
    # Проверка наличия нужной строки поиска
    file_v8 = codecs.open(file_name_v8, 'r', encoding='utf-8')
    data = file_v8.read()
    result=re.findall(old_path,data)
    file_v8.close()
    if result==[]:
        continue
    print(usr)
#раскомментировать если тестировать
#    if usr != "S.Sizov":
#        continue
#    print("ТЕСТ пройден!")
#    continue
#конец теста
    shutil.copy(file_name_v8, file_name_v8_old)
    file_v8 = codecs.open(file_name_v8, 'w', encoding='utf-8')
    file_v8_old = codecs.open(file_name_v8_old, 'r', encoding='utf-8')
    data = file_v8_old.read()
    data = re.sub(old_path, new_path, data)
    file_v8.write(data)
    file_v8.close()
    file_v8_old.close()
