def encrypt_caesar(plaintext):
	plaintext = plaintext.lower()
	ciphertext = ""
	key = 3
	i = 0
	e = [1, 2, 3, 4, 5, 6, 7, 8]
	while i < len(plaintext):
		buf = ord(plaintext[i])
		if buf > 120 and key <= 0:
			buf -= 26
			buf += key
		elif buf >= 120:
			buf -= 26
		elif buf <= 99:
			buf += 26
		bw = buf + key
		e[i] = chr(bw)
		ciphertext=str(ciphertext)+str(e[i])
		i += 1
	return ciphertext
	
	
def decrypt_caesar(ciphertext):
	ciphertext = ciphertext.lower()
	plaintext = ""
	key = -3
	i = 0
	e = [1, 2, 3, 4, 5, 6, 7, 8]
	while i < len(ciphertext):
		buf = ord(ciphertext[i])
		if buf > 120 and key <= 0:
			buf -= 26
			buf += key
		elif buf >= 120:
			buf -= 26
		elif buf <= 99:
			buf += 26
		bw = buf + key
		e[i] = chr(bw)
		plaintext=str(plaintext)+str(e[i])
		i += 1
	return plaintext