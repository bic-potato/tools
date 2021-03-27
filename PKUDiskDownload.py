import hashlib
import json
import os
import zipfile
from urllib.request import urlretrieve
import requests


def getFileMD5(filePath):
    with open(filePath, "rb") as fp:
        md5obj = hashlib.md5()
        md5obj.update(fp.read())
        file_md5 = md5obj.hexdigest()
        return file_md5


request = dict(name="2021_定量分析化学课程资料.zip", reqhost="disk.pku.edu.cn", usehttps=True, files=[],
               dirs=["gns://1B657F7EAF4745D5BE0B5C1C4F595D96/F95DAFB797C940159AAB897781E6A378"],
               link="A4EAAC5254D48E5BF6579439AFC04485", password="")
head = {
    "Host": "disk.pku.edu.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
    "Content-Type": "text/plain;charset=utf-8",
    "Content-Length": "244",
    "Origin": "https://disk.pku.edu.cn",
    "Connection": "keep-alive",
    "Referer": "https://disk.pku.edu.cn/"
}
gets = requests.post(url="https://disk.pku.edu.cn/api/v1/link?method=batchdownload", headers=head,
                     data=json.dumps(request))
response = gets.json()
urls = response["url"]
if not os.path.exists("./hash.json"):
    with open("./hash.json", mode="w") as f:
        f.write(json.dumps({"hash": ""}))
        f.flush()
        f.close()
with open("./hash.json", mode="r") as f:
    a = json.load(f)["hash"]
    urlretrieve(url=urls, filename="./temp.zip")
    if a != getFileMD5("./temp.zip"):
        f.close()
        os.replace("./temp.zip", "./2021_定量分析化学课程资料.zip")
        with open("./hash.json", mode="w+") as f:
            f.write(json.dumps({"hash": getFileMD5("./2021_定量分析化学课程资料.zip")}))
            f.flush()
    else:
        os.remove("./temp.zip")
f.close()
zFile = zipfile.ZipFile("./2021_定量分析化学课程资料.zip", "r")
for fileM in zFile.namelist():
    zFile.extract(fileM, path="./2021_定量分析化学课程资料")
zFile.close();