import socket 
import sys
import pickle
import helper

def encoding(input_str):
	enc_dict = {'A': 1, 'B': 2, 'C' : 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11,
			'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
			'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26 , ' ': 27}
	
	return enc_dict[input_str]
	
if __name__ == "__main__":
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	ip = str(sys.argv[1]) 
	port = int(sys.argv[2]) 
	server.connect((ip, port))

	while True:
		A = [[-3, -3, -4], [0, 1, 1], [4, 3, 4]]
		p = []
		ip_str = input("Enter your message: ").upper()
		#E = zlib.crc32(bytes(ip_str, 'utf-8'))
		bytedata =(''.join(format(ord(x), 'b') for x in ip_str)) 
		#print (bytedata) 
		key = "101101"
		dividend = helper.padZeroes(bytedata, key)
		#print(dividend)
		E = helper.binaryDivision(dividend,key)
		#print(E)
		temp = []
		for i in range(len(ip_str)):
			enc_str = encoding(ip_str[i])
			#print(enc_str)
			temp.append(enc_str)
			if len(temp)%3 == 0:
				#print("Appending temp ", temp)
				p.append(temp)
				temp = []
		
		
		if len(temp)%3 != 0:
			
			if (len(temp)+1) % 3 == 0:
				temp.append(27)
				
			elif (len(temp)+2) % 3 == 0:
				temp.append(27)
				temp.append(27)
			
			p.append(temp)
			
		p = helper.transpose(p)
		
		#print(p)
		
		Tp = helper.matmul(A,p)
		#print(Tp)
		
		data = {"Tp": Tp, "E": E}
		msg = server.send(pickle.dumps(data))
		recv_msg = server.recv(2048).decode()
		print(recv_msg)
	
	server.close()
