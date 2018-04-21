#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings
import identified

class Basemod(object):
    pass

class Admin(Basemod):
    db_path = settings.ADMIN_PATH
    def __init__(self,username,passwd):
        self.nid = identified.Admin_Nid(self.db_path)
        self.username = username
        self.password = passwd

class School(Basemod):
    db_path = settings.SCHOOL_PATH
    pass
class Classes(Basemod):
    db_path = settings.CLASSES_PATH
    pass
class Course(Basemod):
    db_path = settings.COURSE_PATH
    pass
class Teacher(Basemod):
    db_path = settings.TEACHER_PATH
    pass
class Student(Basemod):
    db_path = settings.STUDENT_PATH
    pass
class Score(Basemod):
#    db_path = settings.SCORE_PATH
    pass
class Course_to_Student(Basemod):
    db_path = settings.COURSE_TO_PATH
    pass



