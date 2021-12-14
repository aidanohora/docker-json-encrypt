from json import load
from dicttoxml import dicttoxml
from contextlib import redirect_stdout
from pyAesCrypt import encryptFile
from os import remove

container_path="/py_json_to_xml/"

#replaced by host current dir when container is ran by bash script
host_path="/py_json_to_xml/container-input-output/"

json_filename = input("Enter json filename: ")

json_host_path = host_path + json_filename

with open(json_host_path) as j:
	json_contents = load(j) 

xml = dicttoxml(json_contents)

xml_contents = xml.decode('UTF-8')

xml_path = container_path + "output.xml"

with open(xml_path, 'w') as xf:
    	with redirect_stdout(xf):
        	print(xml_contents)
        	
encrypted_xml_host_path = host_path + "output.xml.aes"

password = "Gj3a%Zf2098"

encryptFile(xml_path, encrypted_xml_host_path, password)

remove(xml_path)




