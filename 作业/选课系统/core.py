#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg

import pickle,hashlib,time
class School(object):
    def __init__(self,name):
        self.name = name
        self.uuid = self.create_md5()
        # School.addr = addr
        # School.city =city
        print('admin create school: ',self.name)
    def __str__(self):
        return self.name
    def create_md5(self):
        m = hashlib.md5()
        m.update(bytes(str(time.time()),encoding='utf8'))
        return m.hexdigest()
    def save(self):
        with open("db/%s.file" %self.uuid,'wb') as f:
            pickle.dump(self.name,f)

class Course(School):
    pass
    # def __init__(self,name,addr,city,course_name,course_price,course_outline):
    #     super(Course,self).__init__(name,addr,city)
    #     self.course_name =course_name
    #     self.course_price = course_price
    #     self.course_outline = course_outline
    #     School.create_course(self,course_name,course_price,course_outline)



s1 = School("北京分校")
s1.save()
s2 = School("上海分校")
print(s1)
