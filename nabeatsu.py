#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(argv):

    
    for i, v in enumerate(argv):
        
            try: #整数に変換可能なら変換する
                n = int(v)
            except: #そもそも整数でない場合なら
                print "invalid"
                continue
            flag_3n = 0 #３の倍数かどうかを記録しておく
            flag_3 = 0 #３がつく数かどうかを記録しておく
            if n % 3== 0: #３の倍数であるかどうか判定する
                flag_3n = 1
            if "3" in v: #３のつく数かどうか判定する
                flag_3 = 1
            if flag_3 == 1:
                if flag_3n == 1:
                    print "dumb"
                else:
                    print "stupid"
            elif flag_3n == 1:
                print "idiot"
            else:
                print "smart"
