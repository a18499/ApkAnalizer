import os
import subprocess
import sys

class  File_compare():
	def __init__(self, apkPath1,apkPath2):
		self.scan_path1 = apkPath1
		self.scan_path2 = apkPath2
		self.file_list1 = []
		self.file_list2 = []
		self.catorgary =["APP_WALLPAPER","APP_WIDGETS","BOOKS_AND_REFERENCE","BUSINESS","COMICS",
		"COMMUNICATION","EDUCATION","ENTERTAINMENT","FINANCE","Game","HEALTH_AND_FITNESS",
		"LIBRARIES_AND_DEMO","LIFESTYLE","MEDIA_AND_VIDEO","MEDICAL","MUSIC_AND_AUDIO","NEWS_AND_MAGAZINES",
		"PERSONALIZATION","PHOTOGRAPHY","PRODUCTIVITY","SHOPPING","SOCIAL","SPORTS","TOOLS","TRANSPORTATION","TRAVEL_AND_LOCAL","WEATHER"]
		file_out1 = subprocess.check_output(['ls '+self.scan_path1],shell=True)
		file_out2 = subprocess.check_output(['ls '+self.scan_path2],shell=True)
		#file_out = subprocess.check_output(['ls /home/peter/test_shell_sample/'],shell=True)	
		self.file_list1 = str(file_out1).strip("b '").strip("'").split("\\n")
		self.file_list2 = str(file_out2).strip("b '").strip("'").split("\\n")
	def start_compare(self):
		print("File_list1")
		count = 0
		for each_file1 in self.file_list1:						
				if each_file1 in self.file_list2:
					count = count+1
					print("Find the same"+each_file1)
		print(count)
if __name__ == "__main__":
	count =0
	out_list =[]
	obj = File_compare(sys.argv[1],sys.argv[2])
	obj.start_compare()
	