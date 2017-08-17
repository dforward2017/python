#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import MySQLdb

class MySQLClass(object):
    def __init__(self,host,user,passwd,db,port,charset="utf8"):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port
        self.charset = charset
        try:
            self.conn = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,port=self.port,db=self.db,charset=self.charset)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print e

    def select(self,sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            #print results
            return results
        except:
            print "Error: unable to fecth data"
        finally:
            self.conn.close() 

    def insert(self,sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            self.conn.close()

    def update(self,agent,sql):
        try:
            if agent == 'tsc_agent':
                print sql
                self.cursor.execute(sql)
                #self.conn.commit()
            elif agent == 'tmp_agent':
                print sql
                self.cursor.execute(sql1)
            else:
                pass
            self.conn.commit()
        except:
            print "Rollback in case there is any error"
            self.conn.rollback()
        finally:
            self.conn.close() 


#obj = MySQLClass('localhost','root','','basic_agent',3306)
#sql = "select * from t_basic_agent_status limit 2"
#sql = "insert into t_basic_agent_status(assetid,ip) values('%s','%s')" % ('gaafwsedfaw','172.16.0.1')
#sql = "update t_basic_agent_status set tsc_agent='%s' where assetid='%s'" % ('dead','fcawesafw')
#req = obj.insert(sql)
#req = obj.update('tsc_agent',sql)

