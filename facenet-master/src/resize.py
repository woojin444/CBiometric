import os
import sys
import argparse
import shutil


def main(args):

    id = args.reportId

    target = os.path.exists("data/target/"+id+"/")
    if target:
        shutil.rmtree("data/target/"+id+"/")

    command = "python align/align_dataset_mtcnn.py"

    command += " data/initial_image/"

    command += " --image_size 160 --margin 32 --random_order --gpu_memory_fraction 0.25"

    command += " data/target/"+id+"/"

    command += " --detect_multiple_faces true"

    print(command)
    os.system(command)


def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('reportId', type=str,
                        help='The report ID')
    return parser.parse_args(argv)


if __name__ == '__main__':
    print(1)
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    print(2)
    main(parse_arguments(sys.argv[1:]))
    print(3)
