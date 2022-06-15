# simple-docker-project
A bash script which runs two docker containers to convert a json file to xml format and encrypt it. Just an excercise in learning docker with some bash and python scripting.

Requires docker, tested on ubuntu.

Run steps:

1. Store your test json file in the input-output folder (one has been provided named sample.json)

2. Run the deployment bash script (deploy.sh)

3. When prompted for the json file name, enter the full file name of the json file in input-output that you want to use  

(Note: To verify that the decrypted xml has been deployed to container B, I uncommented the sleep command at the bottom of the second python script and used the below commands on the running container:

- sudo docker exec <container_name> ls /py_decrypt_xml/storage/

- sudo docker exec <container_name> cat /py_decrypt_xml/storage/output.xml

)
