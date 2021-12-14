#!/bin/bash
sudo docker build --tag image_a py_json_to_xml

echo "Image A built"

sudo docker build --tag image_b py_decrypt_xml

echo "Image B built"

echo "Deploying container A..."

sudo docker run -it -v $(pwd)/input-output:/py_json_to_xml/container-input-output image_a

echo "JSON has been converted to XML and encrypted on container A"

echo "Deploying container B..."

sudo docker run -d -v $(pwd)/input-output:/py_decrypt_xml/container-input image_b

echo "XML has been decrypted and stored on container B"

echo "The deployment script has finished running."





