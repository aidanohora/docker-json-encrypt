from pyAesCrypt import decryptFile

#the path below has been mapped to the location of the encrypted xml on the host by the deployment bash script
encrypted_xml_path="/py_decrypt_xml/container-input/output.xml.aes"

password = "Gj3a%Zf2098"

decryptFile(encrypted_xml_path, "/py_decrypt_xml/storage/output.xml", password)

#enable if you'd like to use docker exec to verify that the decrpyted xml is stored on the image, in /py_decrypt_xml/storage/
#from time import sleep
#sleep(1000)




