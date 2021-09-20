import requests
import os
import redis
import shutil
import pandas as pd
import redis
import time

url = 'http://www.bseindia.com/download/BhavCopy/Equity/EQ050321_CSV.ZIP'




# if os.path.exists("Stocks.ZIP"):
#   os.remove("Stocks.ZIP")
# else:
#   print("The file does not exist")
# r = requests.get(url, stream=True,headers={'User-agent': 'Mozilla/5.0'})
# print(r.status_code)

# #add exception handling

# if r.status_code == 200:
#     with open("Stocks.ZIP", 'wb') as f:
#         r.raw.decode_content = True
#         shutil.copyfileobj(r.raw, f)
#         print(os.getcwd()+"\Stocks.ZIP")
#         shutil.unpack_archive(os.getcwd()+"\Stocks.ZIP",os.getcwd(),"zip")
#         parseFile()


def download_Parse():
    if os.path.exists("Stocks.ZIP"):
        os.remove("Stocks.ZIP")
    else:
        print("The file does not exist")
    r = requests.get(url, stream=True,headers={'User-agent': 'Mozilla/5.0'})
    print(r.status_code)

#add exception handling

    if r.status_code == 200:
        with open("Stocks.ZIP", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
            print(os.getcwd()+"\Stocks.ZIP")
            shutil.unpack_archive(os.getcwd()+"\Stocks.ZIP",os.getcwd(),"zip")
            parseFile()


redisInstance =redis.Redis(host='127.0.0.1',port=6375)

# print(redisInstance.keys())


def parseFile():
    df =pd.read_csv("EQ050321.CSV",header=0,squeeze=True,usecols=[0,1,4,5,6,7])
    bef_time = time.ctime(time.time())
    print(len(df))
    for i in range(len(df)):
    # print(df.iloc[i,0],df.iloc[i,1],df.iloc[i,2],df.iloc[i,3],df.iloc[i,4],df.iloc[i,5])
    # print(df.iloc[i,0])
        redisInstance.hset(str(df.iloc[i,1]).rstrip(),mapping={"Code":str(df.iloc[i,0]),"Name":(str(df.iloc[i,1]).rstrip()),"Open":str(df.iloc[i,2]),"High":str(df.iloc[i,3]),"Low":str(df.iloc[i,4]),"Close":str(df.iloc[i,5])})
    # print(redisInstance.hgetall(str(df.iloc[i,0])))
    aft_time=time.ctime(time.time())
    # print(bef_time," :  ",aft_time)             

download_Parse()
