#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg
import pickle,sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from lib import commons
from conf import settings

class Nid(object):
    def __init__(self,role,db_path):
        role_list = [
            'admin','school','classes','course','teacher','student','course_to_teacher'
        ]
        if role not in role_list:
            raise Exception('角色定义不正确，选项为：%s' %','.join(role_list))
        self.role =role
        self.db_path = db_path
        self.uuid = commons.create_uuid()

    def get_obj_by_uuid(self):
        file_path = os.path.join(self.db_path,self.uuid)
        with open(file_path,'rb') as f:
            return pickle.load(f)

class Admin_Nid(Nid):
    def __init__(self,db_path):
        super(Admin_Nid,self).__init__('admin',db_path)
class School_Nid(Nid):
    def __init__(self,db_path):
        super(School_Nid,self).__init__('school',db_path)
class Classes_Nid(Nid):
    def __init__(self,db_path):
        super(Classes_Nid,self).__init__('classes',db_path)
class Course_Nid(Nid):
    def __init__(self,db_path):
        super(Course_Nid,self).__init__('course',db_path)
class Teacher_Nid(Nid):
    def __init__(self,db_path):
        super(Teacher_Nid,self).__init__('teacher',db_path)
class Student_Nid(Nid):
    def __init__(self,db_path):
        super(Student_Nid,self).__init__('student',db_path)
class Course_to_teacher_Nid(Nid):
    def __init__(self,db_path):
        super(Course_to_teacher_Nid,self).__init__('course_to_teacher',db_path)



