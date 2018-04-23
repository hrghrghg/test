#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg
import os,sys,pickle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings
import identified

class Basemod(object):

    def save(self):
        filepath = os.path.join(self.db_path,self.nid.uuid)
        with open(filepath,'wb') as f:
            pickle.dump(self,f)
    @classmethod
    def get_all_obj_list(cls):
        ret=[]
        for filename in os.listdir(cls.db_path):
            file_path = os.path.join(cls.db_path,filename)
            obj = pickle.load(open(file_path,'rb'))
            ret.append(obj)
        return ret

class Admin(Basemod):
    db_path = settings.ADMIN_PATH
    def __init__(self,username,passwd):
        self.nid = identified.Admin_Nid(self.db_path)
        self.username = username
        self.password = passwd

    def login(self):
        pass

class School(Basemod):
    db_path = settings.SCHOOL_PATH
    def __init__(self,name,addr):
        self.nid = identified.School_Nid(self.db_path)
        self.name = name
        self.addr = addr
        self.__income = 0
        self.save()
    def __str__(self):
        return self.name

class Classes(Basemod):
    db_path = settings.CLASSES_PATH
    pass
class Course(Basemod):
    db_path = settings.COURSE_PATH
    def __init__(self,name,price,period,school_nid):
        self.nid = identified.Course_Nid(self.db_path)
        self.name = name
        self.price = price
        self.period =period
        self.school_nid = school_nid.uuid
        self.save()

class Course_to_Teacher(Basemod):
    db_path = settings.COURSE_TO_PATH
    def __init__(self,course_nid,teacher_nid):
        self.nid = identified.Course_to_teacher_Nid()
        self.course_nid =course_nid
        self.teacher_nid = teacher_nid
    def get_course_to_teacher_list(self):
        ret = self.get_all_obj_list()
        res = [(obj.course_nid.get_obj_by_uuid(),obj.teacher_nid.get_obj_by_uuid())\
               for obj in ret]
        return res
class Teacher(Basemod):
    db_path = settings.TEACHER_PATH
    def __init__(self,name,level):
        self.nid = identified.Teacher_Nid(self.db_path)
        self.name = name
        self.level = level
        self.__account = 0

class Student(Basemod):
    db_path = settings.STUDENT_PATH
    pass
class Score(Basemod):
#    db_path = settings.SCORE_PATH
    pass



if __name__ == '__main__':
    s1 = School("shanghai","abc")
#    s1.save(os.path.join(settings.SCHOOL_PATH,s1.nid.uuid))
    c1 = Course("python","5800","4m",s1.nid)
    for i in c1.get_all_obj_list():
        print(i.name)
