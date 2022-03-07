def ch1(num):
	s = []
	for i in range(4):
		s.append(str(int(num %256)))
		num /= 256
	return '.'.join(s)

if __name__ == "__main__":
    inputTmp = input()
    try:
        num = int(inputTmp)
        print(ch1(num))
    except:
        ip = inputTmp
        
    else:
        pass