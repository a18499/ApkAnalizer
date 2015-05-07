import os
import sys

class Dynamic_Analizer():
	"""docstring for Dynamic_Analizer"""
	def __init__(self, apk_filepath):
		self.apk_filepath = apk_filepath
		
	def repackage(self):
		os.system("python APIMonitor-beta/apimonitor.py "+self.apk_filepath)
	def app_OB(self):
		APKdeob_path = "/home/peter/APKdeOB-v4/APKdeob.jar"
		os.system("java -jar "+APKdeob_path+"  -i "+self.apk_filepath+" -d Nexus_5_API_19 -w /home/peter/APKdeOB_tmp/")
	 
if __name__ == '__main__':
	obj = Dynamic_Analizer(sys.argv[1])
	obj.repackage()