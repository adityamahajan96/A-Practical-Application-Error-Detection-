import socket
import sys
import pickle
import helper

def decoding(input_str):
	enc_dict = {'A': 1, 'B': 2, 'C' : 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11,
			'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
			'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26 , ' ': 27}
	
	dec_dict = dict((v,k) for k,v in enc_dict.items())
	return dec_dict[input_str]
	
if __name__ == "__main__":
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
	ip = str(sys.argv[1]) 
	port = int(sys.argv[2]) 
	server.bind((ip, port)) 
	server.listen(50)
	conn, addr = server.accept()
	while True:
		A_inv = [[1, 0, 1], [4, 4, 3], [-4, -3, -3]]

		message = conn.recv(2048)
		data = pickle.loads(message)
		Tp = data["Tp"]
		E = data["E"]

		p = helper.matmul(A_inv, Tp)
		#print (p)
		input_str = ""
		p = helper.transpose(p)
		for i in p:
			for j in i:
				input_str = input_str + decoding(int(j))
		
		input_str = input_str.strip()
		
		bytedata =(''.join(format(ord(x), 'b') for x in input_str)) 
		#print (bytedata) 
		key = "101101"
		dividend = bytedata + E
		#print(dividend)
		E = helper.binaryDivision(dividend,key)
		#print(E)
		err_flag = False
		for i in E:
			if i != "0":
				err_flag = True
				break
		
		if err_flag:
			print("Some Error Detected. Received message is:\n", input_str,"\n")
			conn.send(b'SOME ERROR DETECTED!')
		
		else :
			print("No Error Detected. Received message is:\n", input_str,"\n")
			conn.send(b'SUCCESS!')
			
		#if validateChecksum(input_str, E):
		#	print("No Error Detected. Received message is:\n", input_str,"\n")
		#	conn.send(b'SUCCESS!')
		#else :
		#	print("Some Error Detected. Received message is:\n", input_str,"\n")
		#	conn.send(b'SOME ERROR DETECTED!')
		
	
	server.close()
