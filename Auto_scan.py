import os
import subprocess
import sys
from Apk_protect_detecter import Apk_protect_detecter

class Auto_scan():
	"""docstring for Auto_scan"""
	def __init__(self, scan_path):
		self.scan_path = scan_path
		self.file_list = []
		file_out = subprocess.check_output(['ls '+self.scan_path],shell=True)
		#file_out = subprocess.check_output(['ls /home/peter/test_shell_sample/'],shell=True)	
		self.file_list = str(file_out).strip("b '").strip("'").split("\\n")
	def start_scan_OB(self):
		result_list = []		
		for each_word in self.file_list:
			print(each_word)
			os.system("mkdir "+self.scan_path+"/temp")
			obj =Apk_protect_detecter(self.scan_path+each_word,self.scan_path+"temp/"+each_word+"/")
			obj.Unzip()
			obj.get_all_file_name()
			result_list.append(obj.check())
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
if __name__ == "__main__":
	out_list =[]
	obj = Auto_scan(sys.argv[1])
	out_list = obj.start_scan_OB()
	for each_file in out_list:
		print(each_file)
