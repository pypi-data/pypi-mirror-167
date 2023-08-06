import os #line:2
import requests #line:3
import time #line:4
import json #line:5
import re #line:6
import subprocess #line:7
import logging #line:8
try :#line:10
    from kafka import KafkaConsumer ,TopicPartition #line:11
except :#line:12
    logging .warning ('you need pip install kafka-python')#line:13
os .environ ['NLS_LANG']='SIMPLIFIED CHINESE_CHINA.UTF8'#line:15
requests .packages .urllib3 .disable_warnings ()#line:16
from airflow .settings import ETL_FILE_PATH ,KETTLE_HOME ,HIVE_HOME ,P_URL ,DATASET_TOKEN ,REFRESH_TOKEN #line:18
from airflow .utils .email import fun_email ,list_email #line:19
from airflow .common .datax import datax_cmdStr #line:20
_O0OOOO00O0O0O0O00 =f'{P_URL}/echart/dataset_api/?token={DATASET_TOKEN}&visitor=Airflow&type='#line:23
_OO00OO0OO000O0OO0 =f'{P_URL}/echart/refresh_ds/?token={REFRESH_TOKEN}&type='#line:24
class SmartPipError (Exception ):#line:27
    def __init__ (O0O0O00O0000OO0O0 ,err ='SmartPip Error'):#line:28
        Exception .__init__ (O0O0O00O0000OO0O0 ,err )#line:29
def smart_upload (O0OOO00OOOO0O0000 ):#line:33
    OO000OOOOOOO00O0O ,OOOO00OO00OOOOOO0 =os .path .split (O0OOO00OOOO0O0000 )#line:34
    OOOO00OO00OOOOOO0 =OOOO00OO00OOOOOO0 .split ('.')[0 ]#line:35
    O0O0OOOOO0OO000OO ={"title":OOOO00OO00OOOOOO0 ,"token":DATASET_TOKEN ,"visitor":"Airflow"}#line:40
    O0O000OOO0OOO0OO0 ={'file':open (O0OOO00OOOO0O0000 ,'rb')}#line:41
    O0000OO0OOOOOOOO0 =f'''{P_URL}/echart/dataset_api/?type=506&visitor=Airflow&token={DATASET_TOKEN}&param={{"uptime":"{time.time()}","filename":"{OOOO00OO00OOOOOO0}"}}'''#line:42
    O0O00O0O0O0O00O00 =60 #line:43
    O0O0000O0OO00OO00 =requests .post (f'{P_URL}/etl/api/upload_file_api/',files =O0O000OOO0OOO0OO0 ,data =O0O0OOOOO0OO000OO )#line:45
    print (O0O0000O0OO00OO00 .status_code )#line:46
    if O0O0000O0OO00OO00 .status_code ==200 :#line:47
        O0O0000O0OO00OO00 =O0O0000O0OO00OO00 .json ()#line:48
    elif O0O0000O0OO00OO00 .status_code ==504 :#line:49
        print ('timeout, try waiting...')#line:50
        O0O0000O0OO00OO00 ={"result":"error","data":"time out"}#line:51
        for OO000OO00O0000OOO in range (20 ):#line:52
            OOOOOOO00OOO0O0O0 =requests .get (O0000OO0OOOOOOOO0 ).json ()#line:53
            print (OOOOOOO00OOO0O0O0 )#line:54
            O0O0OOOOO0OO000OO =OOOOOOO00OOO0O0O0 ['data']#line:55
            if len (O0O0OOOOO0OO000OO )>1 :#line:56
                O0O0000O0OO00OO00 ={"result":"success","data":"uploaded"}#line:57
                break #line:58
            time .sleep (O0O00O0O0O0O00O00 )#line:59
    else :#line:60
        O0O0000O0OO00OO00 ={"result":"error","data":"some thing wrong"}#line:61
    print (O0O0000O0OO00OO00 )#line:62
    if O0O0000O0OO00OO00 ['result']=='error':#line:63
        raise SmartPipError ('Upload Error')#line:64
def get_dataset (O00000OOOOO0OO0OO ):#line:67
    ""#line:72
    O0O0OOOO0O0OO00O0 =requests .get (_O0OOOO00O0O0O0O00 +str (O00000OOOOO0OO0OO ),verify =False )#line:73
    O0O0OOOO0O0OO00O0 =O0O0OOOO0O0OO00O0 .json ()#line:74
    return O0O0OOOO0O0OO00O0 #line:75
def dataset (OOO00O000OOO000OO ,OO000OOOO0O0000OO ,OOOO0O00O00O00000 ,tolist =None ):#line:78
    ""#line:85
    O0O0OOO00O0O00000 =60 *15 #line:86
    OO000OO00OOO0O00O =3600 *2 #line:87
    OOO00O000O00OO0O0 =''#line:88
    try :#line:89
        while True :#line:90
            OOOO0O0O0000OO00O =requests .get (_O0OOOO00O0O0O0O00 +OO000OOOO0O0000OO ,verify =False )#line:91
            OOOO0O0O0000OO00O =OOOO0O0O0000OO00O .json ()#line:92
            O00O000OOOOOOOO0O =OOOO0O0O0000OO00O ['result']#line:93
            OOOO0O0O0000OO00O =OOOO0O0O0000OO00O ['data']#line:94
            if O00O000OOOOOOOO0O =='error':#line:95
                raise Exception (f'{OOOO0O0O0000OO00O}')#line:96
            OOO00O000O00OO0O0 =',\n'.join ([str (O000000O0O0O00O0O )for O000000O0O0O00O0O in OOOO0O0O0000OO00O ])#line:97
            print (f'Dataset: {OOO00O000O00OO0O0} ')#line:98
            if OOOO0O00O00O00000 =='e3':#line:99
                if len (OOOO0O0O0000OO00O )<2 :#line:100
                    if OO000OO00OOO0O00O <=0 :#line:101
                        raise Exception ('超时且数据为空')#line:102
                    else :#line:103
                        time .sleep (O0O0OOO00O0O00000 )#line:104
                        OO000OO00OOO0O00O =OO000OO00OOO0O00O -O0O0OOO00O0O00000 #line:105
                else :#line:106
                    break #line:107
            else :#line:108
                if len (OOOO0O0O0000OO00O )>1 :#line:109
                    if OOOO0O00O00O00000 =='e1':#line:110
                        raise Exception ('有异常数据')#line:111
                    elif OOOO0O00O00O00000 =='e2':#line:112
                        list_email (f'Info_{OOO00O000OOO000OO}',f'{OOO00O000OOO000OO}-Dataset Status',OOOO0O0O0000OO00O ,to_list =tolist )#line:113
                else :#line:114
                    if OOOO0O00O00O00000 not in ['info','e1']:#line:115
                        OOO00O000O00OO0O0 ='数据为空'#line:116
                        raise Exception (OOO00O000O00OO0O0 )#line:117
                break #line:118
    except Exception as O0000O00OOOO0O0O0 :#line:119
        fun_email (f'{OOO00O000OOO000OO}-执行Dataset校验出错',OOO00O000O00OO0O0 ,to_list =tolist )#line:120
        raise SmartPipError (str (O0000O00OOOO0O0O0 .args ))#line:121
def refresh_dash (O000O0O00O0O000O0 ,O000000O0OO00O00O ):#line:124
    ""#line:127
    try :#line:128
        O0OOO0O00O00O000O =requests .get (f'{_OO00OO0OO000O0OO0}{O000000O0OO00O00O}',verify =False )#line:129
        O0OOO0O00O00O000O =O0OOO0O00O00O000O .json ()#line:130
        print (O0OOO0O00O00O000O )#line:131
        O0OO0O00OO0OOOO0O =O0OOO0O00O00O000O ['status']#line:132
        if O0OO0O00OO0OOOO0O !=200 :#line:133
            raise SmartPipError ('refresh_dash')#line:134
    except Exception as OO0O0OOO0OO0O000O :#line:135
        fun_email (f'{O000O0O00O0O000O0}-执行re出错',str (OO0O0OOO0OO0O000O .args ))#line:136
        raise SmartPipError (str (OO0O0OOO0OO0O000O .args ))#line:137
def run_bash (OOO000OO0OOOO000O ):#line:141
    O000000O000OO0OO0 =''#line:142
    OO0OOO00000O0O00O =subprocess .Popen (OOO000OO0OOOO000O ,stdout =subprocess .PIPE ,stderr =subprocess .STDOUT ,shell =True ,cwd =ETL_FILE_PATH )#line:143
    print ('PID:',OO0OOO00000O0O00O .pid )#line:144
    for O00O0OO0OOO00OO00 in iter (OO0OOO00000O0O00O .stdout .readline ,b''):#line:145
        if OO0OOO00000O0O00O .poll ()and O00O0OO0OOO00OO00 ==b'':#line:146
            break #line:147
        O00O0OO0OOO00OO00 =O00O0OO0OOO00OO00 .decode (encoding ='utf8')#line:148
        print (O00O0OO0OOO00OO00 .rstrip ())#line:149
        O000000O000OO0OO0 =O000000O000OO0OO0 +O00O0OO0OOO00OO00 #line:150
    OO0OOO00000O0O00O .stdout .close ()#line:151
    O0OOO000O0O000O00 =OO0OOO00000O0O00O .wait ()#line:152
    print ('result code: ',O0OOO000O0O000O00 )#line:153
    return O000000O000OO0OO0 ,O0OOO000O0O000O00 #line:154
def run_python (O0000O0000OO0O0O0 ,O00000O000O000O0O ,dev =''):#line:157
    OO0000O0OO0O0O0OO =O0000O0000OO0O0O0 .split ('/')#line:158
    _O000000000O0000OO ,O00OO0OO0000000O0 =run_bash ('python %s %s'%(O0000O0000OO0O0O0 ,O00000O000O000O0O ))#line:159
    if O00OO0OO0000000O0 !=0 :#line:160
        fun_email (f'{OO0000O0OO0O0O0OO[-2]}/{OO0000O0OO0O0O0OO[-1]}出错','python error')#line:161
        raise Exception ('error')#line:162
def run_dataxx (OO00OO00OOO0O00OO ,OOO0O0OOOOOO0O000 ,dev =''):#line:166
    OOO000OO0000O00OO =OO00OO00OOO0O00OO .split ('/')#line:167
    if OOO0O0OOOOOO0O000 :#line:168
        O0O0O0O00OO0OOOO0 =[f'-D{OOO00OOO00OOO0O00}:{O00O00OOO0O0O0O0O}'for OOO00OOO00OOO0O00 ,O00O00OOO0O0O0O0O in OOO0O0OOOOOO0O000 .items ()]#line:169
        OOO000O0O0O0O0OOO =' '.join (O0O0O0O00OO0OOOO0 )#line:170
        O0O0OO0O000O00000 =[f'-p"{OOO000O0O0O0O0OOO}"',OO00OO00OOO0O00OO ]#line:171
    else :#line:172
        O0O0OO0O000O00000 =[OO00OO00OOO0O00OO ]#line:173
    O00O0OOO000OO00O0 =datax_cmdStr (O0O0OO0O000O00000 )#line:174
    _OOOO0OO000OO00000 ,O0OOOOO0OOO0000O0 =run_bash (O00O0OOO000OO00O0 )#line:175
    if O0OOOOO0OOO0000O0 !=0 :#line:176
        fun_email (f'{OOO000OO0000O00OO[-2]}/{OOO000OO0000O00OO[-1]}出错','datax error')#line:177
        raise Exception ('error')#line:178
def run_datax (O0O0000O0OOO00OO0 ,O00OO000000OO0000 ,OOOOOO0000O000OOO ,OO000000O0000000O ,dev =''):#line:181
    with open (O0O0000O0OOO00OO0 ,'r',encoding ='utf8')as O000O000OO00O0OOO :#line:182
        OO0O0O0O0O0OOO0O0 =readSqlstr (O000O000OO00O0OOO .read ().strip (),para_dict =OO000000O0000000O )#line:183
    OO0O0O0O0O0OOO0O0 =OO0O0O0O0O0OOO0O0 .split ('##')#line:184
    OOOOOOOOOOO0O00OO ={}#line:185
    for OO0000O0O0000OOO0 in OO0O0O0O0O0OOO0O0 :#line:186
        O00O00O0O00OO0O00 =OO0000O0O0000OOO0 .find ('=')#line:187
        if O00O00O0O00OO0O00 >0 :#line:188
            OOOOOOOOOOO0O00OO [OO0000O0O0000OOO0 [:O00O00O0O00OO0O00 ].strip ()]=OO0000O0O0000OOO0 [O00O00O0O00OO0O00 +1 :].replace ('\n',' ').strip ()#line:189
    OO0OOOOOO0000O0OO =OOOOOOOOOOO0O00OO .keys ()#line:190
    OOOOO0OOOO0O00O00 =OOOOOOOOOOO0O00OO .pop ('template')if 'template'in OO0OOOOOO0000O0OO else 'default'#line:191
    O0OO0OOO0O000O00O =OOOOOOOOOOO0O00OO .get ('targetColumn')#line:192
    OO0O0O0OOO00OOOOO =None #line:193
    if OOOOO0OOOO0O00O00 .endswith ('hdfs'):#line:194
        OO0O0O0OOO00OOOOO =OOOOOOOOOOO0O00OO .pop ('hiveSql')if 'hiveSql'in OO0OOOOOO0000O0OO else None #line:196
        if not OO0O0O0OOO00OOOOO :#line:197
            OO0O0O0OOO00OOOOO =OOOOOOOOOOO0O00OO .pop ('postSql')if 'postSql'in OO0OOOOOO0000O0OO else None #line:198
        if O0OO0OOO0O000O00O :#line:200
            O0OO0OOO0O000O00O =O0OO0OOO0O000O00O .split (',')#line:201
            O0OO00O0OOO000OOO =[]#line:202
            for OO0000O0O0000OOO0 in O0OO0OOO0O000O00O :#line:203
                if ':'in OO0000O0O0000OOO0 :#line:204
                    OO0000O0O0000OOO0 =OO0000O0O0000OOO0 .split (':')#line:205
                    O0OO00O0OOO000OOO .append ({"name":OO0000O0O0000OOO0 [0 ].strip (),"type":OO0000O0O0000OOO0 [1 ].strip ()})#line:206
                else :#line:207
                    O0OO00O0OOO000OOO .append ({"name":OO0000O0O0000OOO0 .strip (),"type":"STRING"})#line:208
            OOOOOOOOOOO0O00OO ['targetColumn']=json .dumps (O0OO00O0OOO000OOO )#line:209
    else :#line:210
        if O0OO0OOO0O000O00O :#line:211
            O0OO0OOO0O000O00O =[O0O0000OOO00O0OO0 .strip ()for O0O0000OOO00O0OO0 in O0OO0OOO0O000O00O .split (',')]#line:212
            OOOOOOOOOOO0O00OO ['targetColumn']=json .dumps (O0OO0OOO0O000O00O )#line:213
        else :#line:214
            OOOOOOOOOOO0O00OO ['targetColumn']='["*"]'#line:215
        if OOOOO0OOOO0O00O00 .endswith ('starrocks'):#line:217
            if '.'in OOOOOOOOOOO0O00OO ['targetTable']:#line:218
                OOOOOOOOOOO0O00OO ['targetDB'],OOOOOOOOOOO0O00OO ['targetTable']=OOOOOOOOOOO0O00OO ['targetTable'].split ('.')#line:219
            else :#line:220
                OOOOOOOOOOO0O00OO ['targetDB']='Test'#line:221
    if 'preSql'in OO0OOOOOO0000O0OO :#line:223
        OOOOOOOOOOO0O00OO ['preSql']=json .dumps (OOOOOOOOOOO0O00OO ['preSql'].strip ().split (';'))#line:224
    else :#line:225
        OOOOOOOOOOO0O00OO ['preSql']=''#line:226
    if 'postSql'in OO0OOOOOO0000O0OO :#line:227
        OOOOOOOOOOO0O00OO ['postSql']=json .dumps (OOOOOOOOOOO0O00OO ['postSql'].strip ().split (';'))#line:228
    else :#line:229
        OOOOOOOOOOO0O00OO ['postSql']=''#line:230
    OO0O000000O0O00OO =O0O0000O0OOO00OO0 .split ('/')#line:231
    O00OOOO0O0OOO0OOO =OO0O000000O0O00OO [-1 ].split ('.')[0 ]#line:232
    with open (os .path .join (OOOOOO0000O000OOO ,'datax','templates',OOOOO0OOOO0O00O00 ),'r')as O000O000OO00O0OOO :#line:233
        OO0O00OOOOOO00OOO =O000O000OO00O0OOO .read ()#line:234
    O0O0000O0OOO00OO0 =os .path .join (OOOOOO0000O000OOO ,'datax',O00OOOO0O0OOO0OOO +'.json')#line:235
    with open (O0O0000O0OOO00OO0 ,'w',encoding ='utf8')as O000O000OO00O0OOO :#line:236
        O000O000OO00O0OOO .write (readSqlstr (OO0O00OOOOOO00OOO ,OOOOOOOOOOO0O00OO ))#line:237
    O0000OO0O00O0O0O0 =datax_cmdStr ([O0O0000O0OOO00OO0 ])#line:238
    _O0OO00O00O0O00O00 ,OO0O0OOOO000O0O00 =run_bash (O0000OO0O00O0O0O0 )#line:239
    if OO0O0OOOO000O0O00 !=0 :#line:240
        fun_email (f'{OO0O000000O0O00OO[-2]}/{OO0O000000O0O00OO[-1]}出错','datax error')#line:241
        raise Exception ('error')#line:242
    if OO0O0O0OOO00OOOOO :#line:243
        print (_OO00O00OO0O00O00O (OO0O0O0OOO00OOOOO .split (';'),O00OO000000OO0000 ,db_connect ='hive',dev =dev ))#line:244
def readSqlFile (O0O0O0O0OO0OO00OO ,para_dict =None ):#line:248
    if O0O0O0O0OO0OO00OO .find ('.sql')<0 :#line:249
        return 'file type error'#line:250
    with open (O0O0O0O0OO0OO00OO ,'r',encoding ='utf-8')as O0O00OOO00OO00OO0 :#line:251
        O0O0O00O00OOO00OO =O0O00OOO00OO00OO0 .read ()#line:252
    O0OO00OO0000O00OO =readSqlstr (O0O0O00O00OOO00OO ,para_dict )#line:253
    return O0OO00OO0000O00OO #line:254
def readSqoopFile (O0O000OOO0OO0OO00 ,para_dict =None ):#line:257
    if not O0O000OOO0OO0OO00 .endswith ('.sql'):#line:258
        return 'file type error'#line:259
    with open (O0O000OOO0OO0OO00 ,'r',encoding ='utf8')as O0OO00OO00O000O0O :#line:260
        OOO00OOOO0O0OOOOO =O0OO00OO00O000O0O .read ().strip ()#line:261
    O0OOOO0OO0OO0OOOO =re .match (r"/\*(.*?)\*/(.+)",OOO00OOOO0O0OOOOO ,re .M |re .S )#line:262
    O0OO0O0O0OOO00OO0 =readSqlstr (O0OOOO0OO0OO0OOOO .group (1 ).strip (),para_dict )#line:263
    O00OOO00OO0O0O000 =O0OOOO0OO0OO0OOOO .group (2 ).strip ()#line:264
    return O0OO0O0O0OOO00OO0 ,O00OOO00OO0O0O000 #line:265
def readSqlstr (O0OO00O0O0OOOO00O ,para_dict =None ):#line:268
    OO00O0O0O0O0OO0O0 =re .sub (r"(\/\*(.|\n)*?\*\/)|--.*",'',O0OO00O0O0OOOO00O .strip ())#line:269
    if para_dict :#line:270
        for OOO000OO0O0O000O0 ,O000000O0OO0O000O in para_dict .items ():#line:271
            OO00O0O0O0O0OO0O0 =OO00O0O0O0O0OO0O0 .replace ('$'+OOO000OO0O0O000O0 ,str (O000000O0OO0O000O ))#line:272
    return OO00O0O0O0O0OO0O0 #line:273
def run_sql_file (O0OOOOO00OOO000OO ,O000OOOOO00OO000O ,db_connect ='starrocks',para_dict =None ,dev =''):#line:276
    O0O0O000OOO000O0O =O0OOOOO00OOO000OO .split ('/')#line:277
    try :#line:278
        OO0OO0OOO0O0O0000 =readSqlFile (O0OOOOO00OOO000OO ,para_dict ).split (';')#line:279
        O00OO000OOO0O0O0O =O000OOOOO00OO000O .get (db_connect )#line:280
        if dev :#line:281
            if f'{db_connect}{dev}'in O000OOOOO00OO000O .keys ():#line:282
                O00OO000OOO0O0O0O =O000OOOOO00OO000O .get (f'{db_connect}{dev}')#line:283
        O00OOO00O0OOOO0OO =connect_db_execute ().execute_sql_list (OO0OO0OOO0O0O0000 ,db_connect ,connect_dict =O00OO000OOO0O0O0O )#line:284
        return O00OOO00O0OOOO0OO #line:285
    except Exception as OO00OO000O00O000O :#line:286
        fun_email ('{}/{}执行出错'.format (O0O0O000OOO000O0O [-2 ],O0O0O000OOO000O0O [-1 ]),str (OO00OO000O00O000O .args ))#line:287
        print (OO00OO000O00O000O .args )#line:288
        raise SmartPipError ('Run SQL Error')#line:289
def _OO00O00OO0O00O00O (O0OO0O00O00OOOO00 ,OOO00000O0OOOOOOO ,db_connect ='starrocks',para_dict =None ,dev =''):#line:292
    try :#line:293
        if isinstance (O0OO0O00O00OOOO00 ,str ):#line:294
            O0OO0O00O00OOOO00 =readSqlstr (O0OO0O00O00OOOO00 ,para_dict ).split (';')#line:295
        O0OOOO0O0OOOOO0OO =OOO00000O0OOOOOOO .get (db_connect )#line:296
        if dev :#line:297
            if f'{db_connect}{dev}'in OOO00000O0OOOOOOO .keys ():#line:298
                O0OOOO0O0OOOOO0OO =OOO00000O0OOOOOOO .get (f'{db_connect}{dev}')#line:299
        OOOOO0000OOO00000 =connect_db_execute ().execute_sql_list (O0OO0O00O00OOOO00 ,db_connect ,connect_dict =O0OOOO0O0OOOOO0OO )#line:300
        return OOOOO0000OOO00000 #line:301
    except Exception as O00000OOO0O00OOOO :#line:302
        fun_email ('SQL执行出错',f'{O0OO0O00O00OOOO00}{O00000OOO0O00OOOO.args}')#line:303
        print (O00000OOO0O00OOOO .args )#line:304
        raise SmartPipError ('Run SQL Error')#line:305
def run_kettle (OOOO0O0OO000O00O0 ,para_str ='',dev =False ):#line:309
    ""#line:316
    OO00OO0O00OO00OOO =OOOO0O0OO000O00O0 .split ('/')#line:317
    print ('kettle job start')#line:318
    if '.ktr'in OOOO0O0OO000O00O0 :#line:320
        OOO0OOO000O0OOOOO =f'{KETTLE_HOME}/pan.sh -level=Basic -file={OOOO0O0OO000O00O0}{para_str}'#line:321
    else :#line:322
        OOO0OOO000O0OOOOO =f'{KETTLE_HOME}/kitchen.sh -level=Basic -file={OOOO0O0OO000O00O0}{para_str}'#line:323
    print (OOO0OOO000O0OOOOO )#line:324
    O0OOOOO00OOO00OOO ,O0OOOO000OOOO0OOO =run_bash (OOO0OOO000O0OOOOO )#line:328
    if O0OOOO000OOOO0OOO ==0 :#line:329
        print ('{} 完成数据抽取'.format (str (OOOO0O0OO000O00O0 )))#line:330
    else :#line:331
        print ('{} 执行错误'.format (OOOO0O0OO000O00O0 ))#line:332
        fun_email ('{}/{}出错'.format (OO00OO0O00OO00OOO [-2 ],OO00OO0O00OO00OOO [-1 ]),str (O0OOOOO00OOO00OOO ))#line:333
        raise SmartPipError ('Run Kettle Error')#line:334
def hdfsStarrocks (O0OO00O00OOO0O00O ,OO0O00O0OOOOO000O ,para_dict =None ):#line:338
    ""#line:342
    O00O0OOOOOOOOOO0O =O0OO00O00OOO0O00O .split ('/')#line:343
    print ('strocks load job start')#line:344
    OO0OOOO00O000O000 ,O0O0O0OOO0OOOO00O =readSqoopFile (O0OO00O00OOO0O00O ,para_dict =para_dict )#line:345
    OO0OOOO00O000O000 =OO0OOOO00O000O000 .split ('\n')#line:346
    O0OOOOO00OOOO0O00 ={}#line:347
    O0OOOOO00OOOO0O00 ['LABEL']=f'{O00O0OOOOOOOOOO0O[-2]}{O00O0OOOOOOOOOO0O[-1][:-4]}{int(time.time())}'#line:348
    O0OOOOO00OOOO0O00 ['HDFS']=HIVE_HOME #line:349
    for OOOOO0O0000000000 in OO0OOOO00O000O000 :#line:350
        OOO0OOO0OO0000OOO =OOOOO0O0000000000 .find ('=')#line:351
        if OOO0OOO0OO0000OOO >0 :#line:352
            O0OOOOO00OOOO0O00 [OOOOO0O0000000000 [:OOO0OOO0OO0000OOO ].strip ()]=OOOOO0O0000000000 [OOO0OOO0OO0000OOO +1 :].strip ()#line:353
    OOOOO00O000OOOO0O =O0OOOOO00OOOO0O00 .get ('sleepTime')#line:355
    if OOOOO00O000OOOO0O :#line:356
        OOOOO00O000OOOO0O =int (OOOOO00O000OOOO0O )#line:357
        if OOOOO00O000OOOO0O <30 :#line:358
            OOOOO00O000OOOO0O =30 #line:359
    else :#line:360
        OOOOO00O000OOOO0O =30 #line:361
    OO0O000OO000000OO =O0OOOOO00OOOO0O00 .get ('maxTime')#line:363
    if OO0O000OO000000OO :#line:364
        OO0O000OO000000OO =int (OO0O000OO000000OO )#line:365
        if OO0O000OO000000OO >3600 :#line:366
            OO0O000OO000000OO =3600 #line:367
    else :#line:368
        OO0O000OO000000OO =600 #line:369
    _OO00O00OO0O00O00O (O0O0O0OOO0OOOO00O ,OO0O00O0OOOOO000O ,db_connect ='starrocks',para_dict =O0OOOOO00OOOO0O00 )#line:371
    time .sleep (OOOOO00O000OOOO0O )#line:372
    OO00000OO0O0O0000 =f'''show load from {O0OOOOO00OOOO0O00.get('targetDB')} where label = '{O0OOOOO00OOOO0O00['LABEL']}' order by CreateTime desc limit 1 '''#line:373
    OO0000O0OOO0OO00O ='start to check label'#line:374
    try :#line:375
        while True :#line:376
            OO0000O0OOO0OO00O =_OO00O00OO0O00O00O ([OO00000OO0O0O0000 ],OO0O00O0OOOOO000O ,db_connect ='starrocks')#line:377
            print (OO0000O0OOO0OO00O )#line:378
            OO00OOOO00000O000 =OO0000O0OOO0OO00O [1 ][2 ]#line:379
            if OO00OOOO00000O000 =='CANCELLED':#line:380
                raise Exception (f'Starrocks:{OO00OOOO00000O000}')#line:381
            elif OO00OOOO00000O000 =='FINISHED':#line:382
                print ('Load completed')#line:383
                break #line:384
            if OO0O000OO000000OO <=0 :#line:385
                raise Exception ('超时未完成')#line:386
            else :#line:387
                time .sleep (OOOOO00O000OOOO0O )#line:388
                OO0O000OO000000OO =OO0O000OO000000OO -OOOOO00O000OOOO0O #line:389
    except Exception as O00O0OOOOOO000000 :#line:390
        print ('{} 执行错误'.format (O0OO00O00OOO0O00O ))#line:391
        fun_email ('{}/{}执行出错'.format (O00O0OOOOOOOOOO0O [-2 ],O00O0OOOOOOOOOO0O [-1 ]),str (OO0000O0OOO0OO00O ))#line:392
        raise SmartPipError (str (O00O0OOOOOO000000 .args ))#line:393
def kafkaStarrocks (OOO00OOOOO0OO0O0O ,OO00OO0OOO0O0O0OO ,OO00O00000O000O0O ,O0OO000O0OOOO00OO ,O00OOO0OOO0OO0000 ,dev =''):#line:396
    with open (OOO00OOOOO0OO0O0O ,'r',encoding ='utf8')as OOO000O00000O0000 :#line:397
        O000O0OOOOOOO0OOO =readSqlstr (OOO000O00000O0000 .read ().strip (),para_dict =O00OOO0OOO0OO0000 )#line:398
    O000O0OOOOOOO0OOO =O000O0OOOOOOO0OOO .split ('##')#line:399
    O00O00OO00OO00O00 ={}#line:400
    for O00O00O0O0000OO00 in O000O0OOOOOOO0OOO :#line:401
        O00O0OO0OOO0O0000 =O00O00O0O0000OO00 .find ('=')#line:402
        if O00O0OO0OOO0O0000 >0 :#line:403
            OOO0000000000O0OO =O00O00O0O0000OO00 [O00O0OO0OOO0O0000 +1 :].replace ('\n',' ').strip ()#line:404
            if OOO0000000000O0OO :#line:405
                O00O00OO00OO00O00 [O00O00O0O0000OO00 [:O00O0OO0OOO0O0000 ].strip ()]=OOO0000000000O0OO #line:406
    O00O0OOOO00O0O00O =O00O00OO00OO00O00 .pop ('topic')#line:407
    O0000O00OO0O00000 =O00O00OO00OO00O00 .pop ('table')#line:408
    OO00O000OO00OO000 =O00O00OO00OO00O00 .keys ()#line:409
    if 'skipError'in OO00O000OO00OO000 :#line:410
        skipError =O00O00OO00OO00O00 .pop ('skipError')#line:411
    else :#line:412
        skipError =None #line:413
    if 'kafkaConn'in OO00O000OO00OO000 :#line:414
        OO00OOO0O000OO00O =O00O00OO00OO00O00 .pop ('kafkaConn')#line:415
    else :#line:416
        OO00OOO0O000OO00O ='default'#line:417
    if 'json_root'in OO00O000OO00OO000 :#line:418
        OO0O00OO000OO0000 =O00O00OO00OO00O00 .pop ('json_root')#line:419
    else :#line:420
        OO0O00OO000OO0000 =None #line:421
    if 'jsonpaths'in OO00O000OO00OO000 :#line:422
        O0OOOOO0O0O00O000 =O00O00OO00OO00O00 .get ('jsonpaths')#line:423
        if not O0OOOOO0O0O00O000 .startswith ('['):#line:424
            O0OOOOO0O0O00O000 =O0OOOOO0O0O00O000 .split (',')#line:425
            O0OOOOO0O0O00O000 =json .dumps (['$.'+O00O0O000O0O0OO0O .strip ()for O00O0O000O0O0OO0O in O0OOOOO0O0O00O000 ])#line:426
            O00O00OO00OO00O00 ['jsonpaths']=O0OOOOO0O0O00O000 #line:427
    O0O00O0000OOO000O =_O0OOO0O0O0O00O00O (O00O0OOOO00O0O00O ,OO00OO0OOO0O0O0OO [OO00OOO0O000OO00O ],O0OO000O0OOOO00OO )#line:428
    def OO0O0OOOO00000O00 (O00O00O00OO0OOO00 ):#line:430
        OOO00O0OO0OO0O0OO =b''#line:431
        OO0O000O00O0O0O00 =None #line:432
        if 'format'in OO00O000OO00OO000 :#line:433
            for OO0O000O00O0O0O00 in O00O00O00OO0OOO00 :#line:434
                OOOO0OO00OO0O000O =OO0O000O00O0O0O00 .value #line:435
                if OO0O00OO000OO0000 :#line:436
                    OOOO0OO00OO0O000O =json .loads (OOOO0OO00OO0O000O .decode ('utf8'))#line:437
                    OOOO0OO00OO0O000O =json .dumps (OOOO0OO00OO0O000O [OO0O00OO000OO0000 ]).encode ('utf8')#line:438
                if OOOO0OO00OO0O000O .startswith (b'['):#line:439
                    OOO00O0OO0OO0O0OO =OOO00O0OO0OO0O0OO +b','+OOOO0OO00OO0O000O [1 :-1 ]#line:440
                else :#line:441
                    OOO00O0OO0OO0O0OO =OOO00O0OO0OO0O0OO +b','+OOOO0OO00OO0O000O #line:442
                if len (OOO00O0OO0OO0O0OO )>94857600 :#line:443
                    streamStarrocks (O0000O00OO0O00000 ,OO00O00000O000O0O ,O00O00OO00OO00O00 ,OOO00O0OO0OO0O0OO ,skipError )#line:444
                    O0O00O0000OOO000O .write_offset (OO0O000O00O0O0O00 .partition ,OO0O000O00O0O0O00 .offset +1 )#line:445
                    OOO00O0OO0OO0O0OO =b''#line:446
                if OO0O000O00O0O0O00 .offset ==O0O00O0000OOO000O .end_offset -1 :#line:447
                    break #line:448
        else :#line:449
            for OO0O000O00O0O0O00 in O00O00O00OO0OOO00 :#line:450
                OOOO0OO00OO0O000O =OO0O000O00O0O0O00 .value #line:451
                if OO0O00OO000OO0000 :#line:452
                    OOOO0OO00OO0O000O =json .loads (OOOO0OO00OO0O000O .decode ('utf8'))#line:453
                    OOOO0OO00OO0O000O =json .dumps (OOOO0OO00OO0O000O [OO0O00OO000OO0000 ]).encode ('utf8')#line:454
                OOO00O0OO0OO0O0OO =OOO00O0OO0OO0O0OO +b'\n'+OOOO0OO00OO0O000O #line:455
                if len (OOO00O0OO0OO0O0OO )>94857600 :#line:456
                    streamStarrocks (O0000O00OO0O00000 ,OO00O00000O000O0O ,O00O00OO00OO00O00 ,OOO00O0OO0OO0O0OO ,skipError )#line:457
                    O0O00O0000OOO000O .write_offset (OO0O000O00O0O0O00 .partition ,OO0O000O00O0O0O00 .offset +1 )#line:458
                    OOO00O0OO0OO0O0OO =b''#line:459
                if OO0O000O00O0O0O00 .offset ==O0O00O0000OOO000O .end_offset -1 :#line:460
                    break #line:461
        print (OOO00O0OO0OO0O0OO [1 :1000 ])#line:462
        if OOO00O0OO0OO0O0OO :#line:463
            streamStarrocks (O0000O00OO0O00000 ,OO00O00000O000O0O ,O00O00OO00OO00O00 ,OOO00O0OO0OO0O0OO ,skipError )#line:464
        return OO0O000O00O0O0O00 #line:465
    O0O00O0000OOO000O .consumer_topic (OO0O0OOOO00000O00 )#line:467
def apiStarrocks (O000OOO0O0O000000 ,O000OOOO0OOOOOO00 ,OOO00O0O00OO00000 ,O000000OOOO0OO000 ):#line:470
    with open (O000OOO0O0O000000 ,'r',encoding ='utf8')as O00OOO000OOOOOO0O :#line:471
        OO0OO00OO00OO000O =readSqlstr (O00OOO000OOOOOO0O .read ().strip (),para_dict =O000000OOOO0OO000 )#line:472
    OO0OO00OO00OO000O =OO0OO00OO00OO000O .split ('##')#line:473
    O00O0O00O00000OOO ={}#line:474
    for O0000O0000OOOOO00 in OO0OO00OO00OO000O :#line:475
        OO0000O00OO0O0O0O =O0000O0000OOOOO00 .find ('=')#line:476
        if OO0000O00OO0O0O0O >0 :#line:477
            OOOOOOOO00OOO0OO0 =O0000O0000OOOOO00 [OO0000O00OO0O0O0O +1 :].replace ('\n',' ').strip ()#line:478
            if OOOOOOOO00OOO0OO0 :#line:479
                O00O0O00O00000OOO [O0000O0000OOOOO00 [:OO0000O00OO0O0O0O ].strip ()]=OOOOOOOO00OOO0OO0 #line:480
    O0O0OOO0OO0000OO0 =O00O0O00O00000OOO .pop ('table')#line:481
    O00OOO00O00000000 =O00O0O00O00000OOO .keys ()#line:482
    if 'param'in O00OOO00O00000000 :#line:483
        O000000O0OOO0OO00 =O00O0O00O00000OOO .pop ('param')#line:484
    else :#line:485
        O000000O0OOO0OO00 =None #line:486
    if 'apiConn'in O00OOO00O00000000 :#line:487
        OO000000OOO00OO00 =O00O0O00O00000OOO .pop ('kafkaConn')#line:488
    else :#line:489
        OO000000OOO00OO00 ='default'#line:490
    if 'skipError'in O00OOO00O00000000 :#line:491
        skipError =O00O0O00O00000OOO .pop ('skipError')#line:492
    else :#line:493
        skipError =None #line:494
    if 'jsonpaths'in O00OOO00O00000000 :#line:495
        OO00O00OOO0OO0O00 =O00O0O00O00000OOO .get ('jsonpaths')#line:496
        if not OO00O00OOO0OO0O00 .startswith ('['):#line:497
            OO00O00OOO0OO0O00 =OO00O00OOO0OO0O00 .split (',')#line:498
            OO00O00OOO0OO0O00 =json .dumps (['$.'+O0O0OOOO0O0OO0000 .strip ()for O0O0OOOO0O0OO0000 in OO00O00OOO0OO0O00 ])#line:499
            O00O0O00O00000OOO ['jsonpaths']=OO00O00OOO0OO0O00 #line:500
    OO00O00OOO00OO0OO =O000OOOO0OOOOOO00 [OO000000OOO00OO00 ](O000000O0OOO0OO00 )#line:501
    if OO00O00OOO00OO0OO :#line:502
        streamStarrocks (O0O0OOO0OO0000OO0 ,OOO00O0O00OO00000 ,O00O0O00O00000OOO ,OO00O00OOO00OO0OO ,skipError )#line:503
    else :#line:504
        print ('无数据')#line:505
def streamStarrocks (O0O0O0O00O0OO0OOO ,OO0OO00000OOO0OOO ,O0O00000OOO00O0OO ,O00O000O0OOO00OO0 ,skipError =False ):#line:508
    ""#line:511
    import base64 ,uuid #line:512
    O0OO0O0O00OO000OO ,O0O0O0O00O0OO0OOO =O0O0O0O00O0OO0OOO .split ('.')#line:513
    O000OO000O0O00O0O =str (base64 .b64encode (f'{OO0OO00000OOO0OOO["user"]}:{OO0OO00000OOO0OOO["password"]}'.encode ('utf-8')),'utf-8')#line:514
    O00O000O0OOO00OO0 =O00O000O0OOO00OO0 .strip ()#line:515
    if O00O000O0OOO00OO0 .startswith (b','):#line:516
        O0O00000OOO00O0OO ['strip_outer_array']='true'#line:517
        O00O000O0OOO00OO0 =b'['+O00O000O0OOO00OO0 [1 :]+b']'#line:518
    OO00OOOOO000OO00O ={'Content-Type':'application/json','Authorization':f'Basic {O000OO000O0O00O0O}','label':f'{O0O0O0O00O0OO0OOO}{uuid.uuid4()}',**O0O00000OOO00O0OO }#line:524
    OO000OOOOO0O000OO =f"{OO0OO00000OOO0OOO['url']}/api/{O0OO0O0O00OO000OO}/{O0O0O0O00O0OO0OOO}/_stream_load"#line:525
    print ('start loading to starrocks....')#line:526
    O0O000OOOO0O0O000 =requests .put (OO000OOOOO0O000OO ,headers =OO00OOOOO000OO00O ,data =O00O000O0OOO00OO0 ).json ()#line:527
    print (O0O000OOOO0O0O000 )#line:528
    if O0O000OOOO0O0O000 ['Status']=='Fail':#line:529
        if skipError :#line:530
            print (f'Starrocks Load Error, Skip this offset')#line:531
        else :#line:532
            raise Exception ('Starrocks Load Error')#line:533
def routineStarrocks (OOOOOOOO000OO000O ,O000000OO00O0O000 ,flag =''):#line:536
    O0O00O00OOO00O00O =_OO00O00OO0O00O00O ([f'SHOW ROUTINE LOAD FOR {O000000OO00O0O000}'],OOOOOOOO000OO000O ,db_connect ='starrocks')#line:537
    O0O00O00OOO00O00O =dict (zip (O0O00O00OOO00O00O [0 ],O0O00O00OOO00O00O [1 ]))#line:538
    print ('状态:',O0O00O00OOO00O00O ['State'])#line:539
    print ('统计:',O0O00O00OOO00O00O ['Statistic'])#line:540
    print ('进度:',O0O00O00OOO00O00O ['Progress'])#line:541
    if O0O00O00OOO00O00O ['State']!='RUNNING':#line:542
        print ('ERROR: ',O0O00O00OOO00O00O ['ReasonOfStateChanged'])#line:543
        if not flag :#line:544
            raise Exception ('Starrocks Routin Load')#line:545
from airflow .utils .session import provide_session #line:551
@provide_session #line:552
def point_test (O0O00OOOOO0OO00O0 ,sleeptime ='',maxtime ='',session =None ):#line:553
    ""#line:560
    if sleeptime :#line:561
        sleeptime =int (sleeptime )#line:562
        sleeptime =sleeptime if sleeptime >60 else 60 #line:563
    if maxtime :#line:564
        maxtime =int (maxtime )#line:565
        maxtime =maxtime if maxtime <60 *60 *2 else 60 *60 *2 #line:566
    else :#line:567
        maxtime =0 #line:568
    try :#line:569
        OOO000OOOOOO0O000 =f"select start_date,state from dag_run where dag_id ='{O0O00OOOOO0OO00O0}' ORDER BY id desc LIMIT 1"#line:570
        while True :#line:571
            OOOO000OOOO0O0000 =session .execute (OOO000OOOOOO0O000 ).fetchall ()#line:572
            if OOOO000OOOO0O0000 [0 ][1 ]!='success':#line:573
                if maxtime >0 and OOOO000OOOO0O0000 [0 ][1 ]!='failed':#line:574
                    print ('waiting...'+OOOO000OOOO0O0000 [0 ][1 ])#line:575
                    time .sleep (sleeptime )#line:576
                    maxtime =maxtime -sleeptime #line:577
                else :#line:578
                    O00O0000OO00OO000 =OOOO000OOOO0O0000 [0 ][0 ].strftime ("%Y-%m-%d %H:%M:%S")#line:579
                    OOOO0OOO0OOOOO0OO ='所依赖的dag:'+O0O00OOOOO0OO00O0 +',状态为'+OOOO000OOOO0O0000 [0 ][1 ]+'.其最新的执行时间为'+O00O0000OO00OO000 #line:580
                    fun_email (OOOO0OOO0OOOOO0OO ,'前置DAG任务未成功')#line:581
                    print (OOOO0OOO0OOOOO0OO )#line:582
                    raise SmartPipError ('Run DAG validate Error')#line:583
            else :#line:584
                print ('success...')#line:585
                break #line:586
    except Exception as O00O0000O0OO0OO00 :#line:587
        print (O00O0000O0OO0OO00 .args )#line:588
        raise SmartPipError ('DAG validate Error')#line:589
class connect_db_execute ():#line:594
    def __init__ (OO000OOO0O0OOO000 ,dev =False ,db =''):#line:595
        OO000OOO0O0OOO000 .dev =dev #line:596
    def insert_contents (OO00000O00OOO0O0O ,O0000OOO0OOOO00OO ,OO00OO0OO0OOOOOOO ,per_in =1000 ,connect_dict =None ):#line:598
        O0OO00000O0OO0O0O =time .time ()#line:599
        logging .info ('starting to execute insert contents...')#line:600
        if isinstance (connect_dict ,dict ):#line:601
            O0OO0OO00O00OO0OO =connect_dict ['dbtype']#line:602
        else :#line:603
            if connect_dict =='':#line:604
                O0OO0OO00O00OO0OO ='oracle'#line:605
            else :#line:606
                O0OO0OO00O00OO0OO =connect_dict #line:607
            connect_dict =None #line:608
        O0000OO0O00O00O00 =getattr (OO00000O00OOO0O0O ,'insert_contents_'+O0OO0OO00O00OO0OO )#line:609
        OOO0O00O0O000OOO0 =O0000OO0O00O00O00 (O0000OOO0OOOO00OO ,OO00OO0OO0OOOOOOO ,per_in ,connect_dict )#line:610
        logging .info ('execute insert contents time : {}ms'.format (time .time ()-O0OO00000O0OO0O0O ))#line:611
        return OOO0O00O0O000OOO0 #line:612
    def impala (OOOOOO00OOO0OO000 ,OO0O0OO0O00O000OO ,connect_dict =None ):#line:614
        ""#line:615
        from impala .dbapi import connect as impala #line:616
        OOOOO0O000OO000O0 =impala (user =connect_dict ['user'],password =connect_dict ['password'],host =connect_dict ['host'],port =int (connect_dict ['port']),auth_mechanism ='PLAIN')#line:623
        OOOO00O000000O000 =OOOOO0O000OO000O0 .cursor ()#line:624
        O000000O0OOOOO000 =r'^insert\s|^update\s|^truncate\s|^delete\s|^load\s|^refresh\s|^upsert\s'#line:625
        OO000O0OOO00OO000 =None #line:626
        for O0O00O00O0O0OO0OO in OO0O0OO0O00O000OO :#line:627
            print (O0O00O00O0O0OO0OO )#line:628
            O0O00O00O0O0OO0OO =O0O00O00O0O0OO0OO .strip ()#line:629
            if not O0O00O00O0O0OO0OO :#line:630
                continue #line:631
            if re .search (O000000O0OOOOO000 ,O0O00O00O0O0OO0OO ,re .I |re .IGNORECASE ):#line:632
                OOOO00O000000O000 .execute (O0O00O00O0O0OO0OO )#line:633
            else :#line:634
                OOOO00O000000O000 .execute (O0O00O00O0O0OO0OO )#line:635
                try :#line:636
                    OO000O0OOO00OO000 =OOOO00O000000O000 .fetchall ()#line:637
                except Exception as O00OO0OO00O0OOOO0 :#line:638
                    print (O00OO0OO00O0OOOO0 .args )#line:639
        OOOOO0O000OO000O0 .close ()#line:640
        return OO000O0OOO00OO000 #line:641
    def hive (O0O000OOOOOO0OOOO ,O00O0000OO0000OOO ,connect_dict =None ):#line:643
        ""#line:644
        from impala .dbapi import connect as impala #line:645
        OOOOOO0OOO00OO000 =impala (user =connect_dict ['user'],password =connect_dict ['password'],host =connect_dict ['host'],port =int (connect_dict ['port']),auth_mechanism ='PLAIN')#line:652
        OO000O0OO0O00O00O =OOOOOO0OOO00OO000 .cursor ()#line:653
        OOO00O0O00OOOOO00 =r'^insert\s|^update\s|^truncate\s|^delete\s|^load\s'#line:654
        OO0OOOOOOOOO000OO =None #line:655
        for OO0O00O00OO00000O in O00O0000OO0000OOO :#line:656
            OO0O00O00OO00000O =OO0O00O00OO00000O .strip ()#line:657
            if not OO0O00O00OO00000O :#line:658
                continue #line:659
            print (OO0O00O00OO00000O )#line:660
            if OO0O00O00OO00000O .startswith ('refresh'):#line:661
                connect_dict ['port']=21050 #line:662
                O0O000OOOOOO0OOOO .impala ([OO0O00O00OO00000O ],connect_dict =connect_dict )#line:663
            else :#line:664
                if re .search (OOO00O0O00OOOOO00 ,OO0O00O00OO00000O ,re .I |re .IGNORECASE ):#line:665
                    OO000O0OO0O00O00O .execute (OO0O00O00OO00000O )#line:666
                else :#line:667
                    OO000O0OO0O00O00O .execute (OO0O00O00OO00000O )#line:668
                    try :#line:669
                        OO0OOOOOOOOO000OO =OO000O0OO0O00O00O .fetchall ()#line:670
                    except Exception as OOO0O0O0O0000000O :#line:671
                        print (OOO0O0O0O0000000O .args )#line:672
        OOOOOO0OOO00OO000 .close ()#line:673
        return OO0OOOOOOOOO000OO #line:674
    def mysql (O0O00O0OOOO0O0O00 ,O000O0OO00000O000 ,connect_dict =None ):#line:676
        import pymysql #line:677
        OOOOO000O0OO0O0OO =pymysql .connect (user =connect_dict ['user'],password =connect_dict ['password'],host =connect_dict ['host'],port =connect_dict ['port'],database =connect_dict ['db'])#line:684
        try :#line:685
            O00OOO0O0000OO0O0 =OOOOO000O0OO0O0OO .cursor ()#line:686
            O00O00OO000OO0O0O =r'^insert\s|^update\s|^truncate\s|^delete\s|^load\s'#line:687
            for O0O0OOO00O00OOOOO in O000O0OO00000O000 :#line:688
                O0O0OOO00O00OOOOO =O0O0OOO00O00OOOOO .strip ()#line:689
                if not O0O0OOO00O00OOOOO :#line:690
                    continue #line:691
                print (O0O0OOO00O00OOOOO )#line:692
                if re .search (O00O00OO000OO0O0O ,O0O0OOO00O00OOOOO ,re .I |re .IGNORECASE ):#line:693
                    try :#line:694
                        O00OOO0O0000OO0O0 .execute (O0O0OOO00O00OOOOO )#line:695
                        OOOOO000O0OO0O0OO .commit ()#line:696
                    except Exception as OOO0OO0O000OO0O0O :#line:697
                        OOOOO000O0OO0O0OO .rollback ()#line:698
                        raise OOO0OO0O000OO0O0O #line:699
                else :#line:700
                    O00OOO0O0000OO0O0 .execute (O0O0OOO00O00OOOOO )#line:701
                    O00OOOOOO000OOO0O =O00OOO0O0000OO0O0 .fetchall ()#line:702
                    O00OOOOOO000OOO0O =[[O0O000OOO00OO00OO [0 ]for O0O000OOO00OO00OO in O00OOO0O0000OO0O0 .description ]]+list (O00OOOOOO000OOO0O )#line:703
                    return O00OOOOOO000OOO0O #line:704
        except Exception as OOOOO0O0000OO0000 :#line:705
            raise OOOOO0O0000OO0000 #line:706
        finally :#line:707
            OOOOO000O0OO0O0OO .close ()#line:708
    def starrocks (OOOO0OO0OOOOO0O00 ,OOOO00OO000OOO0OO ,connect_dict =None ):#line:710
        return OOOO0OO0OOOOO0O00 .mysql (OOOO00OO000OOO0OO ,connect_dict )#line:711
    def oracle (OO00O00000O00000O ,O0OOO0O0000O0OOO0 ,connect_dict =None ):#line:713
        import cx_Oracle #line:714
        O00OO000O000OO0OO ='{}/{}@{}/{}'.format (connect_dict ['user'],connect_dict ['password'],connect_dict ['host'],connect_dict ['db'])#line:719
        O00OOO0OO000O0OOO =cx_Oracle .connect (O00OO000O000OO0OO )#line:720
        try :#line:721
            OO0OO00O0O0000O0O =O00OOO0OO000O0OOO .cursor ()#line:722
            OO0O000O0OO0OO00O =r'^insert\s|^update\s|^truncate\s|^delete\s|^comment\s'#line:723
            for O0000OO000000OO00 in O0OOO0O0000O0OOO0 :#line:724
                O0000OO000000OO00 =O0000OO000000OO00 .strip ()#line:725
                if not O0000OO000000OO00 :#line:726
                    continue #line:727
                if re .search (OO0O000O0OO0OO00O ,O0000OO000000OO00 ,re .I ):#line:728
                    try :#line:729
                        OO0OO00O0O0000O0O .execute (O0000OO000000OO00 )#line:730
                        O00OOO0OO000O0OOO .commit ()#line:731
                    except Exception as OOO00O0O0O0O00O0O :#line:732
                        if O0000OO000000OO00 .startswith ('comment'):#line:733
                            print ('err:',O0000OO000000OO00 )#line:734
                            continue #line:735
                        O00OOO0OO000O0OOO .rollback ()#line:736
                        raise OOO00O0O0O0O00O0O #line:737
                else :#line:738
                    OO0OO00O0O0000O0O .execute (O0000OO000000OO00 )#line:739
                    O0O0O0O0OO0O000OO =OO0OO00O0O0000O0O .fetchall ()#line:740
                    O0O0O0O0OO0O000OO =[[OOO0O0O0O00OOOO00 [0 ]for OOO0O0O0O00OOOO00 in OO0OO00O0O0000O0O .description ]]+list (O0O0O0O0OO0O000OO )#line:741
                    return O0O0O0O0OO0O000OO #line:742
        except Exception as O0OO0OO0OO000OO0O :#line:743
            raise O0OO0OO0OO000OO0O #line:744
        finally :#line:745
            O00OOO0OO000O0OOO .close ()#line:746
    def gp (O0OO000OOOO0O0OOO ,O000OOOOOO00O000O ,connect_dict =None ):#line:748
        import psycopg2 #line:749
        O0OO0OOOOO0O0OOOO =psycopg2 .connect (user =connect_dict ['user'],password =connect_dict ['password'],host =connect_dict ['host'],port =connect_dict ['port'],database =connect_dict ['db'])#line:756
        try :#line:757
            OO0OOO000000O0OOO =O0OO0OOOOO0O0OOOO .cursor ()#line:758
            OOOO0OO00OO0OOO0O =r'^insert\s|^update\s|^truncate\s|^delete\s'#line:759
            for OO0OO00OOO0000O0O in O000OOOOOO00O000O :#line:760
                OO0OO00OOO0000O0O =OO0OO00OOO0000O0O .strip ()#line:761
                if not OO0OO00OOO0000O0O :#line:762
                    continue #line:763
                if re .search (OOOO0OO00OO0OOO0O ,OO0OO00OOO0000O0O ,re .I |re .IGNORECASE ):#line:764
                    try :#line:765
                        OO0OOO000000O0OOO .execute (OO0OO00OOO0000O0O )#line:766
                        O0OO0OOOOO0O0OOOO .commit ()#line:767
                    except Exception as O000OOOO00OO0O0O0 :#line:768
                        O0OO0OOOOO0O0OOOO .rollback ()#line:769
                        raise O000OOOO00OO0O0O0 #line:770
                else :#line:771
                    OO0OOO000000O0OOO .execute (OO0OO00OOO0000O0O )#line:772
                    O00OO00000O0OOO0O =OO0OOO000000O0OOO .fetchall ()#line:773
                    O00OO00000O0OOO0O =[[OO00O00OO0O0O00O0 [0 ]for OO00O00OO0O0O00O0 in OO0OOO000000O0OOO .description ]]+list (O00OO00000O0OOO0O )#line:774
                    return O00OO00000O0OOO0O #line:775
        except Exception as O0O000OOO0OOO0OOO :#line:776
            raise O0O000OOO0OOO0OOO #line:777
        finally :#line:778
            O0OO0OOOOO0O0OOOO .close ()#line:779
    def mssql (OOOO00OOOO000OO00 ,OOO0O00O0OO0O000O ,connect_dict =None ):#line:781
        import pymssql #line:782
        if connect_dict ['port']:#line:783
            OOO000OO0O0OOO000 =pymssql .connect (user =connect_dict ['user'],password =connect_dict ['password'],host =connect_dict ['host'],port =int (connect_dict ['port']),database =connect_dict ['db'],charset ="utf8",)#line:791
        else :#line:792
            OOO000OO0O0OOO000 =pymssql .connect (user =connect_dict ['user'],password =connect_dict ['password'],host =connect_dict ['host'],database =connect_dict ['db'],charset ="utf8",)#line:799
        try :#line:800
            OOO0O000OOO000O00 =OOO000OO0O0OOO000 .cursor ()#line:801
            OOOO0OO0OO0000O00 =r'^insert\s|^update\s|^truncate\s|^delete\s'#line:802
            for O0O0OOO0O00000O0O in OOO0O00O0OO0O000O :#line:803
                O0O0OOO0O00000O0O =O0O0OOO0O00000O0O .strip ()#line:804
                if not O0O0OOO0O00000O0O :#line:805
                    continue #line:806
                if re .search (OOOO0OO0OO0000O00 ,O0O0OOO0O00000O0O ,re .I |re .IGNORECASE ):#line:807
                    try :#line:808
                        OOO0O000OOO000O00 .execute (O0O0OOO0O00000O0O )#line:809
                        OOO000OO0O0OOO000 .commit ()#line:810
                    except Exception as OOO00O000O0O0O0OO :#line:811
                        OOO000OO0O0OOO000 .rollback ()#line:812
                        raise OOO00O000O0O0O0OO #line:813
                else :#line:814
                    OOO0O000OOO000O00 .execute (O0O0OOO0O00000O0O )#line:815
                    O0OO0O0O0O0O00O0O =OOO0O000OOO000O00 .fetchall ()#line:816
                    O0OO0O0O0O0O00O0O =[[O0000OO0000OO000O [0 ]for O0000OO0000OO000O in OOO0O000OOO000O00 .description ]]+list (O0OO0O0O0O0O00O0O )#line:817
                    return O0OO0O0O0O0O00O0O #line:818
        except Exception as OO0O0O000O0OOO000 :#line:819
            raise OO0O0O000O0OOO000 #line:820
        finally :#line:821
            OOO000OO0O0OOO000 .close ()#line:822
    def execute_sql_list (OOO00O000OO0OOOO0 ,OOO0000OOO00OOOOO ,db_connect ='',connect_dict =None ):#line:824
        if db_connect =='':db_connect ='oracle'#line:825
        O0O000OO000OOO0OO =getattr (OOO00O000OO0OOOO0 ,db_connect )#line:826
        return O0O000OO000OOO0OO (OOO0000OOO00OOOOO ,connect_dict =connect_dict )#line:827
    def excute_proc (OO00OO0O0O0OOO000 ,O000O0OOOOOO00O00 ,O00O00O0OO0000OO0 ,proc_para =None ):#line:829
        import cx_Oracle #line:830
        O0O00OOO00OOO0O00 ='{}/{}@{}/{}'.format (O00O00O0OO0000OO0 ['user'],O00O00O0OO0000OO0 ['password'],O00O00O0OO0000OO0 ['host'],O00O00O0OO0000OO0 ['db'])#line:836
        OO0OO000OOO0OOOO0 =cx_Oracle .connect (O0O00OOO00OOO0O00 )#line:837
        try :#line:839
            OOO0OO000O0O0OOO0 =OO0OO000OOO0OOOO0 .cursor ()#line:840
            print ("开始执行过程:{}  参数: {}".format (O000O0OOOOOO00O00 ,proc_para ))#line:841
            if proc_para is None :#line:842
                O0OOO0000OOOO0OO0 =OOO0OO000O0O0OOO0 .callproc (O000O0OOOOOO00O00 )#line:843
                OO0OO000OOO0OOOO0 .commit ()#line:844
            else :#line:845
                O0OOO0000OOOO0OO0 =OOO0OO000O0O0OOO0 .callproc (O000O0OOOOOO00O00 ,proc_para )#line:847
                OO0OO000OOO0OOOO0 .commit ()#line:848
            OOO0OO000O0O0OOO0 .close ()#line:849
            OO0OO000OOO0OOOO0 .close ()#line:850
            print (O0OOO0000OOOO0OO0 )#line:851
        except Exception as O00O0OOO0O0O00000 :#line:852
            OO0OO000OOO0OOOO0 .rollback ()#line:853
            OO0OO000OOO0OOOO0 .close ()#line:854
            raise O00O0OOO0O0O00000 #line:856
        return True #line:857
    def insert_contents_oracle (O0O0O0O0OO00000OO ,OOO0OO0OOOOOOOOOO ,O000OO0OO00O000O0 ,per_in =100 ,connect_dict =None ):#line:859
        import cx_Oracle #line:860
        O00OOO0OOOO0OOOOO ='{}/{}@{}:{}/{}'.format (connect_dict ['user'],connect_dict ['password'],connect_dict ['host'],connect_dict ['port'],connect_dict ['db'])#line:866
        OOO00OOOO000OOOOO =cx_Oracle .connect (O00OOO0OOOO0OOOOO )#line:867
        OOOOOO00000OOO0OO =OOO00OOOO000OOOOO .cursor ()#line:868
        O00O0O000OOO000O0 =' into {} values {}'#line:869
        OO0O0OOO0O0OOOO00 =''#line:870
        O0O0O000O0OOO00OO =len (OOO0OO0OOOOOOOOOO )#line:871
        logging .info ("total {} records need to insert table {}: ".format (O0O0O000O0OOO00OO ,O000OO0OO00O000O0 ))#line:872
        try :#line:873
            for OO000OOOO0OO0OOOO in range (O0O0O000O0OOO00OO ):#line:874
                OO0O0OOO0O0OOOO00 =OO0O0OOO0O0OOOO00 +O00O0O000OOO000O0 .format (O000OO0OO00O000O0 ,tuple (OOO0OO0OOOOOOOOOO [OO000OOOO0OO0OOOO ]))+'\n'#line:875
                if (OO000OOOO0OO0OOOO +1 )%per_in ==0 or OO000OOOO0OO0OOOO ==O0O0O000O0OOO00OO -1 :#line:876
                    O000OO0O0OOOOOO00 ='insert all '+OO0O0OOO0O0OOOO00 +'select 1 from dual'#line:877
                    logging .debug (O000OO0O0OOOOOO00 )#line:878
                    OOOOOO00000OOO0OO .execute (O000OO0O0OOOOOO00 )#line:879
                    OOO00OOOO000OOOOO .commit ()#line:880
                    OO0O0OOO0O0OOOO00 =''#line:881
            return str (O0O0O000O0OOO00OO )#line:882
        except Exception as OO000O0O00OOO000O :#line:883
            try :#line:884
                OOO00OOOO000OOOOO .rollback ()#line:885
                OOOOOO00000OOO0OO .execute ("delete from {} where UPLOADTIME = '{}'".format (O000OO0OO00O000O0 ,OOO0OO0OOOOOOOOOO [0 ][-1 ]))#line:886
                OOO00OOOO000OOOOO .commit ()#line:887
            except Exception :#line:888
                logging .error ('can not delete by uploadtime')#line:889
            finally :#line:890
                raise OO000O0O00OOO000O #line:891
        finally :#line:892
            OOO00OOOO000OOOOO .close ()#line:893
class _O0OOO0O0O0O00O00O (object ):#line:897
    connect =None #line:898
    def __init__ (O00OOO00O0O00O0OO ,OO0OO00O0O0O000O0 ,O00O000OOOO00OO00 ,OOO00O0OOO0O00OOO ):#line:900
        O00OOO00O0O00O0OO .end_offset =None #line:901
        O00OOO00O0O00O0OO .db_err_count =0 #line:902
        O00OOO00O0O00O0OO .topic =OO0OO00O0O0O000O0 #line:903
        O00OOO00O0O00O0OO .kafkaconfig =O00O000OOOO00OO00 #line:904
        O00OOO00O0O00O0OO .offsetDict ={}#line:905
        O00OOO00O0O00O0OO .current_dir =OOO00O0OOO0O00OOO #line:906
        try :#line:907
            O00OOO00O0O00O0OO .consumer =O00OOO00O0O00O0OO .connect_kafka_customer ()#line:908
        except Exception as OO0O00O000000O000 :#line:909
            OO0O00O000000O000 ='kafka无法连接','ErrLocation：{}\n'.format (OO0OO00O0O0O000O0 )+str (OO0O00O000000O000 )+',kafka消费者无法创建'#line:910
            raise OO0O00O000000O000 #line:911
    def get_toggle_or_offset (OO0O00O00000000O0 ,O0O00O0OO000O00O0 ,O0OOOO00O00OOO0O0 ):#line:913
        ""#line:914
        O0OO0OOO00O000000 =0 #line:915
        try :#line:916
            O0OOOO0O0OOO0OOOO =f"{OO0O00O00000000O0.current_dir}/kafka/{O0O00O0OO000O00O0}_offset_{O0OOOO00O00OOO0O0}.txt"#line:917
            if os .path .exists (O0OOOO0O0OOO0OOOO ):#line:918
                O00O0OOOOO00O0OO0 =open (O0OOOO0O0OOO0OOOO ).read ()#line:919
                if O00O0OOOOO00O0OO0 :#line:920
                    O0OO0OOO00O000000 =int (O00O0OOOOO00O0OO0 )#line:921
            else :#line:922
                with open (O0OOOO0O0OOO0OOOO ,encoding ='utf-8',mode ='a')as O0O000OO000OO0000 :#line:923
                    O0O000OO000OO0000 .close ()#line:924
        except Exception as OOO00O0OOO000OOOO :#line:925
            print (f"读取失败：{OOO00O0OOO000OOOO}")#line:926
            raise OOO00O0OOO000OOOO #line:927
        return O0OO0OOO00O000000 #line:928
    def write_offset (OOO00OOOO0OOOO000 ,O0O0OO00O0O00O00O ,offset =None ):#line:930
        ""#line:933
        if OOO00OOOO0OOOO000 .topic and offset :#line:934
            O000OOOO0OOOOO000 =f"{OOO00OOOO0OOOO000.current_dir}/kafka/{OOO00OOOO0OOOO000.topic}_offset_{O0O0OO00O0O00O00O}.txt"#line:936
            try :#line:937
                with open (O000OOOO0OOOOO000 ,'w')as O000O000O00OO0000 :#line:938
                    O000O000O00OO0000 .write (str (offset ))#line:939
                    O000O000O00OO0000 .close ()#line:940
            except Exception as O00OOOO0OO0O000O0 :#line:941
                print (f"写入offset出错：{O00OOOO0OO0O000O0}")#line:942
                raise O00OOOO0OO0O000O0 #line:943
    def connect_kafka_customer (OOOO00O0OO00OOO00 ):#line:945
        ""#line:946
        OO000000000000O00 =KafkaConsumer (**OOOO00O0OO00OOO00 .kafkaconfig )#line:947
        return OO000000000000O00 #line:948
    def parse_data (O0OO0O0O000OOOOO0 ,OOOO0000OOOO0O00O ):#line:950
        ""#line:955
        return dict ()#line:956
    def gen_sql (OOOOO00000000OOOO ,OOO00OOO0O0OO0O00 ):#line:958
        ""#line:963
        OOO00000OOO0O00O0 =[]#line:964
        for OO000O00000OO00O0 in OOO00OOO0O0OO0O00 :#line:965
            OOO00000OOO0O00O0 .append (str (tuple (OO000O00000OO00O0 )))#line:967
        return ','.join (OOO00000OOO0O00O0 )#line:968
    def dispose_kafka_data (OOOO0OO0O0OO00OOO ,O0O0OOO0000OO0O00 ):#line:970
        ""#line:975
        pass #line:976
    def get_now_time (OOOOO0OO00O0O000O ):#line:978
        ""#line:982
        O00O00000OOOO0OOO =int (time .time ())#line:983
        return time .strftime ('%Y-%m-%d %H:%M:%S',time .localtime (O00O00000OOOO0OOO ))#line:984
    def tran_data (O00000000OO00OOO0 ,O0O0O0O0O00OOOOO0 ,O0O0OOOOO0OO0000O ):#line:986
        ""#line:992
        O00000OO0OO00O00O =O0O0O0O0O00OOOOO0 .get (O0O0OOOOO0OO0000O ,"")#line:993
        O00000OO0OO00O00O =""if O00000OO0OO00O00O is None else O00000OO0OO00O00O #line:994
        return str (O00000OO0OO00O00O )#line:995
    def consumer_data (OOOOOOO00O0O00OO0 ,OOO0000OOO0OOO0O0 ,OOOO0OO0OO000O0OO ,OOO0000000000OOOO ):#line:997
        ""#line:1004
        if OOOOOOO00O0O00OO0 .consumer :#line:1005
            OOOOOOO00O0O00OO0 .consumer .assign ([TopicPartition (topic =OOOOOOO00O0O00OO0 .topic ,partition =OOO0000OOO0OOO0O0 )])#line:1006
            O000OO00O0OOOOO0O =TopicPartition (topic =OOOOOOO00O0O00OO0 .topic ,partition =OOO0000OOO0OOO0O0 )#line:1008
            OO00O0O0O00000O0O =OOOOOOO00O0O00OO0 .consumer .beginning_offsets ([O000OO00O0OOOOO0O ])#line:1009
            O000OO0O0O0OO0000 =OO00O0O0O00000O0O .get (O000OO00O0OOOOO0O )#line:1010
            O0O00O0OOO000000O =OOOOOOO00O0O00OO0 .consumer .end_offsets ([O000OO00O0OOOOO0O ])#line:1011
            O0O000O0OOOO0000O =O0O00O0OOO000000O .get (O000OO00O0OOOOO0O )#line:1012
            print (f'建立消费者, {OOO0000OOO0OOO0O0}分区, 最小offset:{O000OO0O0O0OO0000}, 最大offset:{O0O000O0OOOO0000O}')#line:1013
            if OOOO0OO0OO000O0OO <O000OO0O0O0OO0000 :#line:1014
                print (f'Warning: 消费offset：{OOOO0OO0OO000O0OO} 小于最小offset:{O000OO0O0O0OO0000}')#line:1015
                OOOO0OO0OO000O0OO =O000OO0O0O0OO0000 #line:1016
            if OOOO0OO0OO000O0OO >=O0O000O0OOOO0000O :#line:1017
                print (f'消费offset：{OOOO0OO0OO000O0OO} 大于最大offset:{O0O000O0OOOO0000O}, 本次不消费')#line:1018
                return #line:1019
            OOOOOOO00O0O00OO0 .end_offset =O0O000O0OOOO0000O #line:1020
            OOOOOOO00O0O00OO0 .consumer .seek (TopicPartition (topic =OOOOOOO00O0O00OO0 .topic ,partition =OOO0000OOO0OOO0O0 ),offset =OOOO0OO0OO000O0OO )#line:1021
            print (f'消费{OOO0000OOO0OOO0O0}分区, 开始消费offset：{OOOO0OO0OO000O0OO}!')#line:1022
            O00OOOOOO000OOOO0 =OOO0000000000OOOO (OOOOOOO00O0O00OO0 .consumer )#line:1023
            OOOO0OO0OO000O0OO =O00OOOOOO000OOOO0 .offset +1 #line:1024
            OOOOOOO00O0O00OO0 .offsetDict [OOO0000OOO0OOO0O0 ]=OOOO0OO0OO000O0OO #line:1027
            OOOOOOO00O0O00OO0 .write_offset (OOO0000OOO0OOO0O0 ,OOOO0OO0OO000O0OO )#line:1028
            OOOOOOO00O0O00OO0 .offsetDict [OOO0000OOO0OOO0O0 ]=OOOO0OO0OO000O0OO #line:1031
            OOOOOOO00O0O00OO0 .write_offset (OOO0000OOO0OOO0O0 ,OOOO0OO0OO000O0OO )#line:1032
    def consumer_topic (O00OOO0OO000O00O0 ,OO0O0O00OOOO0000O ):#line:1034
        print (f"topic: {O00OOO0OO000O00O0.topic}")#line:1035
        print ('开始解析。')#line:1036
        O0O00O0O00O0OOO0O =O00OOO0OO000O00O0 .consumer .partitions_for_topic (topic =O00OOO0OO000O00O0 .topic )#line:1038
        for O000OOO0O000O0O00 in O0O00O0O00O0OOO0O :#line:1039
            OO00O0OOO00O000OO =O00OOO0OO000O00O0 .get_toggle_or_offset (O00OOO0OO000O00O0 .topic ,O000OOO0O000O0O00 )#line:1040
            O0O00O0O0OOOO0OOO =None if OO00O0OOO00O000OO <0 else OO00O0OOO00O000OO #line:1042
            O00OOO0OO000O00O0 .consumer_data (O000OOO0O000O0O00 ,O0O00O0O0OOOO0OOO ,OO0O0O00OOOO0000O )#line:1043
    def save_all_offset (O00O0OOOOO00000O0 ):#line:1045
        for OOOO0OO0OOO0OOO0O ,O000OOO0OO0OO0O0O in O00O0OOOOO00000O0 .offsetDict :#line:1046
            O00O0OOOOO00000O0 .write_offset (OOOO0OO0OOO0OOO0O ,O000OOO0OO0OO0O0O )#line:1047
