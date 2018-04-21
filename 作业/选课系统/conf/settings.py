#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

ADMIN_PATH = os.path.join(BASE_DIR,'db','admin')
CLASSES_PATH = os.path.join(BASE_DIR,'db','classes')
COURSE_PATH = os.path.join(BASE_DIR,'db','course')
SCHOOL_PATH = os.path.join(BASE_DIR,'db','school')
STUDENT_PATH = os.path.join(BASE_DIR,'db','students')
TEACHER_PATH = os.path.join(BASE_DIR,'db','teacher')
COURSE_TO_PATH = os.path.join(BASE_DIR,'db','course_to_teacher')




