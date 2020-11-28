#!/usr/bin/python

import os
import logging
import errno
import argparse

logging.basicConfig(level=logging.INFO)

models = [
    'university.university',
    'university.department',
    'university.program',
    'university.term',
    'accounts.user',
    'accounts.guardian',
    'accounts.prevacademicrecord',
    'accounts.teacher',
    'accounts.student',
    'course.course',
    'course.courseoffering',
    'course.courseenrollment',
    'announcement.announcement',
    'announcement.announcementfilter',
    'assignment.assignment',
    'assignment.assignmentfile',
    'assignment.assignmentwork',
    'assignment.assignmentworkfile',
    'result.grade',
    'result.semestergrade',
]

def dumpdata(directory='data'):
    directory_path = os.path.join(os.getcwd(), directory)

    if not os.path.isdir(directory_path):
        os.mkdir(directory_path)

    for model in models:
        path = os.path.join(directory_path, f'{model}.json')
        logging.info(f'Dumping {directory}/{model}.json')
        os.system(f'python manage.py dumpdata {model} > {path}')

def loaddata(directory='data'):
    directory_path = os.path.join(os.getcwd(), directory)

    if not os.path.isdir(directory_path):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), directory_path)

    for model in models:
        path = os.path.join(directory_path, f'{model}.utf8.json')
        logging.info(f'Loading {directory}/{model}.utf8.json')
        os.system(f'python manage.py loaddata {path}')

def main(args):
    if args.method == "dump":
        dumpdata(args.dir)
    elif args.method == "load":
        loaddata(args.dir)
    else:
        raise argparse.ArgumentTypeError('Method undefined')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("method", help="Required positional argument")
    parser.add_argument("-d", "--dir", action="store", dest="dir", default='data')

    args = parser.parse_args()
    main(args)