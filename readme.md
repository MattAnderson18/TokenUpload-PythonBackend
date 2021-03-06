This is a program to receive files from the [Token Upload](https://github.com/SobanVuex/screencloud-tokenupload) plugin for [ScreenCloud](https://screencloud.net/) that goes in the directory that the screenshots are being uploaded to.

It is called whenever Token Upload sends a request to the webserver which contains the file/image data encoded in base64 format in a json packet. This code then gets the file and image data from the json and validates it to make sure that all the required data has been provided and that the token used matches the one in the code. If an error is found here, the code sends an error back to Token Upload in json format stating what the error is. Otherwise,  the code  keeps the data and uses that to get the image data in base64 format and a file name which is used to grab the file type.

Once the data has been received successfully, the program generates a random name based on a random 6 digit integer and encodes it in base64 which it then stores into a string variable in utf-8 format and appends the file type to the end. This new name is then checked against existing files in the image directory to make sure no other files exist with the same name. If a matching file is found, the program generates more random names until it gets a unique one.

Once the name has been verified, the image data is decoded from base64 into bytecode and a binary writer instance is opened using the file name that was generated. This writer instance is then used to store the bytecode in binary format to the image file and is then closed. If the upload fails at this point then an error is sent back to the Token Upload plugin on ScreenCloud.

###usage:
drag and drop into the images directory on your web server and set the 'token' variable to what you want to use (make sure it's secure and keep it secret!) and set the 'url' variable to the url used to access the images directory on the webserver from any browser
