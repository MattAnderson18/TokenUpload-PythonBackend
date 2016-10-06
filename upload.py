#!/usr/bin/env python
import base64
import cgi
import json
import os
import random
import string
import sys

TOKEN = "{0c7W8pC8~}V5TPG05Y6mV,q9^,@4+x!$y4;]13'7'O{eb5+8,ig;}q).@42U(^`664)9=1H!<$R135V@;01%:!85l40('75a`'w26*89P1/0%5@;16,>xL`v}U1c6"
URL = "https://scrnsht.xyz/"

def output(returnData = []):
    print("Content-Type: application/json")
    print()
    print(json.dumps(returnData))

def generateName(filetype):
    valid = False

    while not valid:
        name = str(random.randint(10000, 99999)).encode()
        hashName = base64.b64encode(name).decode("utf-8")
        for char in hashName:
            if char in string.punctuation:
                hashName = hashName.replace(char, "")
        name = hashName + "." + filetype
        if not os.path.exists("./" + name):
            valid = True
    return name

if __name__ == "__main__":
    try:
        data = json.loads(sys.stdin.read())
        if len(data) == 0 or data['image'] == None or data['token'] == "" or data['name'] == "":
            output({"error": "Invalid input."})

        else:
            if data['token'] != TOKEN:
                output({"error": "Invalid token."})

            else:
                filetype = data['name'].split(".")[1]
                filename = generateName(filetype)
                image = base64.b64decode(data['image'])

                try:
                    with open(filename, 'wb') as imgFile:
                        imgFile.write(image)

                    output({"href": URL + filename})

                except IOError as e:
                    output({"error": e})
    except:
        cgi.print_exception()
