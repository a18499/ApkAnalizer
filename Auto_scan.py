import os
import subprocess
import sys
import time
from Apk_protect_detecter import Apk_protect_detecter

class Auto_scan():
	"""docstring for Auto_scan"""
	def __init__(self, scan_path):
		self.scan_path = scan_path
		self.file_list = []
		file_out = subprocess.check_output(['ls '+self.scan_path],shell=True)
		#file_out = subprocess.check_output(['ls /home/peter/test_shell_sample/'],shell=True)	
		self.file_list = str(file_out).strip("b '").strip("'").split("\\n")
		self.file_list.pop()
		
	def start_scan_OB(self):
		result_list = []		
		for each_word in self.file_list:
			print(each_word)
			os.system("mkdir "+self.scan_path+"/temp")
			obj =Apk_protect_detecter(self.scan_path+each_word,self.scan_path+"temp/"+each_word+"/")
			obj.Unzip()
			obj.get_all_file_name()
			result_list.append(obj.check()+": "+each_word)
			os.system("rm -r -f "+self.scan_path+"temp/")
		return result_list
	def scan_deOB(self):
		APKdeob_path = "/home/peter/APKdeOB-v4/APKdeob.jar"
		log_list = []
		x=0
		for each_word in self.file_list:
			print("OB file "+str(x))
			out = subprocess.check_output(["java -jar "+APKdeob_path+" -i "+self.scan_path+each_word+" -d Nexus_5_API_19 -w /home/peter/APKdeOB_tmp/"], shell=True)
			log_list.append(out)
			print(out,end='\n')
			print("OB file "+str(x)+"complete")
			x=x+1
			if (x % 5) == 0:
				try:
					OB = open('OB_log'+str(x)+'.txt',"w")
					print(log_list , file = OB)
					del log_list[:]
					OB.close()
				except IOError:
					print('File open error!!!')
	def scan_package(self):
		APK_tool = "/home/peter/apktool/apktool"
		for each_word in self.file_list:
			os.system(APK_tool+" b"+" "+self.scan_path+each_word+"/")
	def scan_zip(self):
		ZIP_Path ="/media/peter/3812e316-a581-434a-98a2-3ea81a27fd10/Bangle_ZIP/"
		for each_word in self.file_list:
			os.system("zip -r "+ZIP_Path+each_word+".zip "+self.scan_path+each_word+"/")
	def scan_unzip(self):
		unzip_path = ""
		os.system("mkdir "+self.scan_path+"/temp")
		for each_word in self.file_list:
			obj =Apk_protect_detecter(self.scan_path+each_word,self.scan_path+"temp/"+each_word+"/")
			obj.Unzip()
	def scan_apktool(self):
		APK_tool = "/home/peter/apktool/apktool"
		os.system("mkdir "+self.scan_path+"/temp")
		for each_word in self.file_list:
			os.system(APK_tool+" d"+" "+self.scan_path+each_word )
	def Api_monitor(self):
		API_monitor = "/home/peter/ApkAnalizer/APIMonitor-beta/apimonitor.py"
		for each_word in self.file_list:
			os.system(API_monitor+" "+self.scan_path+each_word )
	def Get_package_activity_name(self, aapt_output):
		aapt_result_list = []
		activity = ""
		package =""
		aapt_result_list = str(aapt_output).strip("b '").strip("'").split("\\n")
		for each_app in aapt_result_list:
			if"package" in each_app:
				print(each_app)
				packageDic = {} 
				each_app_package_list = str(each_app).split(":")
				for each in each_app_package_list:
					if"name" in each:
						each_app_package_list1 = str(each).strip("  ").split(" ")
						print(each_app_package_list1)
						for each_par in each_app_package_list1:
							each_par_list=each_par.split("=")
							packageDic[each_par_list[0]]=each_par_list[1]
							package = packageDic['name']
			if "launchable-activity" in each_app:
 				appDic = {} 
 				each_app_list=str(each_app).split(":")
 				for each in each_app_list:
 					if "name" in each:
 						each_app_list1 = str(each).strip("  ").split(" ")
 						for each_par in each_app_list1:	
 							if each_par != "":
 								print(each_par)
 								try:
 									each_par_list=each_par.split("=")
 									appDic[each_par_list[0]]=each_par_list[1]
 								except IndexError:
 									print("Out of range")
 								activity = appDic['name']
		return str(activity).strip("'") , str(package).strip("'")
	def  Testing_APIMoniter(self):
		aapt_tool = "/home/peter/Android/Sdk/build-tools/21.1.2/aapt"
		adb_tool = "/home/peter/Android/Sdk/platform-tools/adb" 
		count = 0
		for each_word in self.file_list:
			app_out = subprocess.check_output([aapt_tool+" d badging "+self.scan_path+each_word],shell=True)
			result_activity,result_package = self.Get_package_activity_name(app_out)
			print(result_activity)
			print(result_package)
			if result_activity == "":
				print("result_activity go wrong")
			elif result_package == "":
				print("result_package go wrong")
			else:
				#install package
				os.system(adb_tool+" install "+self.scan_path+each_word)
				os.system(adb_tool+" shell am start -n "+result_package+"/"+result_activity)
				time.sleep(5)
				os.system(adb_tool+" uninstall "+result_package)
			count = count +1
		print("Total check"+str(count))
		
if __name__ == "__main__":
	count =0
	out_list =[]
	obj = Auto_scan(sys.argv[1])
	#out_list = obj.start_scan_OB()
	
	#obj.scan_unzip()
	obj.Testing_APIMoniter()
	#for each_file in out_list:
	#	count = count +1
	#	print(each_file)
	#print("check "+str(count)+"apk")
	#print("Start apktool.....")
	#obj.scan_apktool()
