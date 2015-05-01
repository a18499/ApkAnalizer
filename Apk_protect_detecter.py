import os
import subprocess
import sys
""""""

Bangcle = ["libsecexe.x86.so",
	    "libsecmain.x86.so",
	     "libsecexe.so",
	     "libsecmain.so"]
QQ = ["libshell.so"]
Baidu = ["libbaiduprotect.so"]
protect_360 = ["libprotectClass.so"]
Ijiami = ["libexecmain.so",
	"ijiami.dat",
	"libexec.so "]
APKProtect = ["libspkprotect2.so",
		"libAPKProtect.so"]
NAGA = ["libddog.so"]
PayEgis = ["libNSaferOnly.so"]
NQ = ["libnqshield.so"]
Ali = ["libmobisec.so"]
"""
Now support 
網秦,梆梆
愛加密,阿里
通付盾,Apk_protect
百度,娜迦
360,QQ
"""
support_list = {"Bangcle":Bangcle,
		"QQ":QQ,
		"Baidu":Baidu,
		"protect_360":protect_360,
		"Ijiami":Ijiami,
		"APKProtect":APKProtect,
		"NAGA":NAGA,
		"PayEgis":PayEgis,
		"NQ":NQ,
		"Ali":Ali}
class Apk_protect_detecter:
	def __init__(self, apkPath,apkUnzipPath):
		self.apkPath = apkPath
		self.apkUnzipPath =apkUnzipPath
		self.scan_path = ""
		print(self.apkPath)
		print(self.apkUnzipPath)
		self.all_file_name = {}
		self.all_dir_name = {}
		
	def Unzip(self):
		os.system("unzip "+self.apkPath+" -d "+self.apkUnzipPath)
	def get_all_file_name(self):
		for root, dirs, files in os.walk(self.apkUnzipPath):
			for file in files:
				self.all_file_name[file] = ""
			for dir in dirs:
				self.all_dir_name[dir] = ""

	def check(self):
		Result = ""
		for each_support in support_list.keys():
			for each_characteristic in support_list[each_support]:
				if each_characteristic in self.all_file_name:
					Result = each_support
		os.system("rm -r -f "+self.scan_path+"temp/")
		if Result == "":
			return "APK is Not OB"
		else:
			return Result			


if __name__ == "__main__":
     
    obj = Apk_protect_detecter(sys.argv[1],sys.argv[2])
    #obj.auto_scan(sys.argv[3])
    obj.Unzip()
    obj.get_all_file_name()
    Result1 = obj.check()
    print(Result1)
