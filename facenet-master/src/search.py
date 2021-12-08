import os
import sys
import argparse

os.chdir(os.path.dirname(os.path.realpath(__file__)))

def main(args):

    id = args.reportId

    models = "models\\20180408-102900"
    command = "python compare.py" + " " + models
    count = -1
    pic_list = []

    for path, subdir, image in os.walk("./data/target/"+id+"/abc"):
        for i in image:
            command += " " + path + "/" + i
            count += 1
    
    if count == -1:
        print('No target faces!')
        os._exit()

    command_front = command

    for path, subdir, image in os.walk("./data/library"):
        for j in subdir:
            for p, sub, pic in os.walk("./data/library/" + j):
                for i in pic:
                    ext = i.split('.')[-1]
                    if ext != 'txt':
                        pic_list.append(" " + p + "/" + i)
                        # command += " " + p + "/" + i

    # command += " " + str(count)+" "+id
    f = open("demofile.txt", "a")
    f.write(command)
    # print(command)
    for i in range(len(pic_list)):
        command += pic_list[i]
        if (i+1) % 100 == 0:
            command += " " + str(count)+" "+id
            os.system(command)
            command = command_front

    command += " " + str(count)+" "+id
    os.system(command)

    # os.system(command)

def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('reportId', type=str,
                        help='The report ID')
    return parser.parse_args(argv)

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    main(parse_arguments(sys.argv[1:]))
