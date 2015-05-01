import binascii
import os
import sys

class Dex_Analysis():
	def __init__(self):
		pass
	def dex_search(self,core_path):
		flag=0
		count =0
		Dex_start =0
		size = []
		with open(core_path,'rb') as data1:
			while 1:
				raw_byte = data1.read(8)
				byte = binascii.hexlify(raw_byte)
				if raw_byte ==binascii.unhexlify("6465780a30333500"):
					print(byte.strip())
					flag =1
					data1.read(24)
					size.append(binascii.hexlify(data1.read(1)))
					size.append(binascii.hexlify(data1.read(1)))
					size.append(binascii.hexlify(data1.read(1)))
					size.append(binascii.hexlify(data1.read(1)))
					dex_size = size[3]+size[2]+size[1]+size[0]
					print(int(size[2], 16))
					dex_size2 = int(size[3], 16) *16*16*16*16*16*16+int(size[2], 16) *16*16*16*16+int(size[1], 16)*16*16 +int(size[0], 16)
					data1.read(4)
					print("dex_size "+str(dex_size))
					print("dex_size2 "+str(dex_size2))
					print("Dex_start: "+str(Dex_start))
					print(raw_byte)
					dir_path = os.getcwd()
					save_path = os.path.join(dir_path,"dex/"+str(count)+".dex")
					print(save_path) 
					os.system("dd if="+core_path+" bs=1 count="+str(dex_size2)+" skip="+str(Dex_start)+" of="+save_path)
					count = count+1
					Dex_start = Dex_start +40
					size.pop()
					size.pop()
					size.pop()
					size.pop()
				elif byte:
					Dex_start = Dex_start +8
					pass
				else:
					Dex_start = Dex_start +8
					if flag ==1:
						print("Find dex header!!!")
						print(count)
					break

		data1.close()

if __name__ == "__main__":
   
    obj = Dex_Analysis()
    obj.dex_search(sys.argv[1])