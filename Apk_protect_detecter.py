import os
import subprocess
""""""
support_list = ["Bangcle",
		"QQ",
		"Baidu",
		"protect_360",
		"Ijiami",
		"APKProtect",
		"NAGA",
		"PayEgis",
		"NQ",
		"Ali"]
Bangcle = ["libsecexe.x86.so",
	    "libsecmain.x86.so",
	     "libsecexe.so",
	     "libsecmain.so"]
QQ = ["libshell.so"]
Baidu = ["libbaiduprotect.so"]
protect_360 = ["libprotectClass.so"]
Ijiami = ["libexecmain.so",
	"ijiami.dat",
	"libexecmain.so "]
APKProtect = ["libspkprotect2.so",
		"libAPKProtect.so"]
NAGA = ["libddog.so"]
PayEgis = ["libNSaferOnly.so"]
NQ = ["libnqshield.so"]
Ali = ["libmobisec.so"]
class Apk_protect_detecter:
	def __init__(self, apkPath,apkUnzipPath):
		self.apkPath = apkPath
		self.apkUnzipPath =apkUnzipPath
	def Unzip(self):
		os.system("unzip "+self.apkPath+"-d "+self.apkUnzipPath)
	def check(self):
		pass
