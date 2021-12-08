from pymongo import MongoClient
import os
import bson.binary
import numpy as np
import base64
from io import BytesIO


def main():
    myclient = MongoClient('mongodb://localhost:27017/')
    Biometix = myclient["Biometix"]
    peopleLib = Biometix.lib
    peopleLib.remove()
    for path,subdir,image in os.walk('./library'):
        for dir_name in subdir:
            dirs = os.path.join(path, dir_name)
            # files = os.listdir(dirs)
            infoFile = open(dirs + '/' + 'info.txt', "r")
            info = infoFile.read().split('%')
            # info file must be in the form of:
            # ID, NAME, AGE, LOCATION, INSTITUTION
            item = {
                '_id': info[0],
                'name': info[1],
                'age': info[2],
                'location' : info[3],
                'institution' : info[4],
                'link' : dirs
            }
            peopleLib.insert_one(item)

            """
            for file in files:
                filesname = dirs + '/' + file
                f=file.split('.')

                # encode image to base64 format
                encoded_string = image_to_base64(filesname)

                item = {
                    '_id': f[0],
                    'name': dir_name,
                    'image': encoded_string
                }
                peopleLib.insert_one(item)
            """

    # reportsLib = Biometix.reports
    # reportsLib.remove()

    re = peopleLib.find()
    for i in re:
        # print(i['_id'])
        print(peopleLib.find_one({'_id':i['_id']}))
    print(peopleLib.count())
    
    """
    ## show that the image can be decoded
    target = peopleLib.find_one({'_id':'Abdullah'})
    # print(target)
    target_image_path = './test/'+target['_id']+'_decoded.jpg'
    encoded_str = target['link']
    base64_to_image(encoded_str, target_image_path)
    """
"""
def image_to_base64(image_path):
    encoded_string = ""
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string

def base64_to_image(encoded_string, target_image_path):
    decode = base64.b64decode(encoded_string)
    image_result = open(target_image_path, 'wb')
    image_result.write(decode)
    image_result.close()
"""

if __name__ == '__main__':
       main()
                