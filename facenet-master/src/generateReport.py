# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 21:59:08 2018

@author: xyq
"""
from pymongo import MongoClient
# import uuid8
import sys
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
import shutil

def getKey(element):
    score = element.split('##')[-1]
    score = float(score)
    return score

def generateReport(reportid):

    space = 40
    scale = 200
    imageWidth = 160
    imageHight = 160
    lineGap = 26

    reportId = reportid
    print("report id: ", reportId, "\n")

    # sort the result txt file
    re = open("data\output\\"+reportId+".txt", "r")
    lines = re.readlines()
    ll = []
    for i in lines:
        ll.append(i)
    ll.sort(key = getKey, reverse = True)
    re.close()
    
    f = open("data\output\\"+reportId+".txt", "w")
    for i in ll:
        f.write(i)
    f.close()



    # call people db
    myclient = MongoClient('mongodb://localhost:27017/')
    Biometix = myclient["Biometix"]
    peopleLib = Biometix.lib
    reportsLib = Biometix.reports
    reportsLib.remove()

    file_path = '../../web_app/client/public/report/'+str(reportId)+'.pdf'

    c = canvas.Canvas('data\output\\'+str(reportId)+'.pdf', pagesize=A4)

    xlength, ylength = A4

    c.setFont('Helvetica', 25)
    c.drawCentredString(xlength/2, ylength-25, 'Report')

    f = open("data\output\\"+reportId+".txt", "r")
    line = f.readline()
    line = line[:-1]
    i = 1
    if line == "":
        c.setFont('Helvetica', 20)
        c.drawCentredString(xlength/2, ylength/2,
                            "No matching images found!!!")
    else:
        c.setFont('Helvetica', 15)
        c.drawString(space, ylength-50, "Target picture")
        c.drawString(space+scale, ylength-50, "Matching picture")
        c.drawString(space+scale*2, ylength-50, "Information")
        while line:
            if i > 4:
                c.showPage()
                c.setFont('Helvetica', 15)
                c.drawString(space, ylength-50, "Target picture")
                c.drawString(space+scale, ylength-50, "Matching picture")
                c.drawString(space+scale*2, ylength-50, "Information")
                i -= 4
            l = line.split('##')
            c.drawImage(l[0], space, ylength-50-170*i, imageWidth, imageHight)
            c.drawImage(l[1], space+scale*1, ylength -
                        50-170*i, imageWidth, imageHight)

            # get the result person's id and his/her information
            t = l[1].split('/')
            id = t[-2]

            name = peopleLib.find_one({'_id': id})['name']
            age = peopleLib.find_one({'_id': id})['age']
            location = peopleLib.find_one({'_id': id})['location']
            institution = peopleLib.find_one({'_id': id})['institution']
            link = peopleLib.find_one({'_id': id})['link']

            c.setFont('Helvetica', 10)
            c.drawString(space + scale * 2 - 20, ylength - 50 -
                         170 * (i-1) - lineGap, "Correlation: "+l[2]+"%")
            c.drawString(space + scale * 2 - 20, ylength - 50 -
                         170 * (i-1) - lineGap * 2, "Name: " + name)
            c.drawString(space + scale * 2 - 20, ylength - 50 -
                         170 * (i-1) - lineGap * 3, "Age: " + age)
            c.drawString(space + scale * 2 - 20, ylength - 50 -
                         170 * (i-1) - lineGap * 4, "Location: " + location)
            c.drawString(space + scale * 2 - 20, ylength - 50 - 170 *
                         (i-1) - lineGap * 5, "Institution: " + institution)
            c.drawString(space + scale * 2 - 20, ylength - 50 -
                         170 * (i-1) - lineGap * 6, "Link: " + link)
            i += 1

            line = f.readline()
            line = line[:-1]
        ta = l[0].split('/')[-1].split('.')[0]
        while ta[-1] != '_':
            ta = ta[:-1]
        ta = ta[:-1]
        result = {
            '_id': str(reportId),
            'target': ta,
            'path': 'data\output\\'+str(reportId)+'.pdf',
        }
        reportsLib.insert_one(result)

    f.close()
    c.showPage()
    c.save()
    
    file_path = "\\".join(os.path.dirname(os.path.realpath(__file__)).split("\\")[:-2])
    file_path = file_path + "\\web_app\\client\\public\\report\\"+ str(reportId) + '.pdf'
    print(file_path)

    shutil.copyfile('data\output\\'+str(reportId)+'.pdf',file_path)
    # os.rename('data\output'+str(reportId)+'.pdf', 'data\output'+str(t)+'.pdf')
    print('Report Generated data\output'+str(reportId) +
          '.pdf', 'data\output'+str(reportId)+'.pdf')


if __name__ == '__main__':
    generateReport(sys.argv[1])
