# coding: utf-8
#!/usr/bin/env python
from math import sin, cos, sqrt, atan2, radians
import sqlite3 as sqlite

class io(object):
    def __init__(self, file_route):
        self.file_route = file_route

    def connAndClose(db):
        def decorator(func):
            def decorator(self, *args, **kwargs):
                conn = sqlite.connect('%sdata/db/%s'% (self.file_route, db))
                c = conn.cursor()
                ret = func(self, c, *args, **kwargs)
                conn.commit()
                conn.close()
                return ret
            return decorator
        return decorator

    def saveImg(self, route_and_name, data):
        with open(route_and_name, 'wb') as f:
            for chunk in data:
                f.write(chunk)

    @connAndClose(db="user_log.db")
    def userLog(self, c, data):
        for item in data['events']:
            c.execute('INSERT INTO log (userId,roomId,groupId,eventType,data,timestamp) VALUES ("%s","%s","%s","%s","%s","%s")' %(item.get('source').get('userId'), item.get('source').get('roomId'), item.get('source').get('groupId'), item.get('type'), data, item.get('timestamp')))

    @connAndClose(db="user_action.db")
    def userAction(self, c, user_id):
        planing = c.execute('SELECT planing FROM route_plan WHERE user_id ="%s"'%(user_id))
        planing = planing.fetchall()
        return planing

    @connAndClose(db="user_action.db")
    def userActionPos(self, c, user_id):
        ori_pos = c.execute('SELECT pos FROM route_plan WHERE user_id ="%s"'%(user_id))
        ori_pos = ori_pos.fetchall()
        return ori_pos[0][0]

    @connAndClose(db="user_action.db")
    def userActionDelete(self, c, user_id):
        c.execute('DELETE FROM route_plan WHERE user_id ="%s"'%(user_id))

    @connAndClose(db="user_action.db")
    def checkUserRouteAction(self, c, ori_pos, ori_user_id):
        user_id = c.execute('SELECT user_id FROM route_plan WHERE user_id ="%s"'%(ori_user_id))
        user_id = user_id.fetchall()
        print(user_id)
        if user_id != []:
            print('update')
            c.execute('UPDATE route_plan SET planing ="action" WHERE user_id ="%s"'%(ori_user_id))
            c.execute('UPDATE route_plan SET pos ="%s" WHERE user_id ="%s"'%(ori_pos, ori_user_id))
        else:
            print('insert')
            c.execute('INSERT INTO route_plan (user_id,planing,pos) VALUES ("%s","action","%s")'%(ori_user_id, ori_pos))