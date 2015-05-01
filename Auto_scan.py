import os
import subprocess
import sys
from Apk_protect_detecter import Apk_protect_detecter

class Auto_scan():
	"""docstring for Auto_scan"""
	def __init__(self, scan_path):
		self.scan_path = scan_path
	def start_scan(self):
		file_list = []
		file_out = subprocess.check_output(['ls '+self.scan_path],shell=True)
		#file_out = subprocess.check_output(['ls /home/peter/test_shell_sample/'],shell=True)	
		file_list = str(file_out).strip("b '").strip("'").split("\\n")

		for each_word in file_list:
			print(each_word)
			os.system("mkdir "+self.scan_path+"/temp")
			obj =Apk_protect_detecter(self.scan_path+each_word,self.scan_path+"temp/"+each_word+"/")
			obj.Unzip()
			obj.get_all_file_name()
			obj.check()
			
			os.system("rm -r -f "+self.scan_path+"temp/")
if __name__ == "__main__":
	obj = Auto_scan(sys.argv[1])
	obj.start_scan()
