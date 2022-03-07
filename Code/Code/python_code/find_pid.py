def isRun(name):
    cmd = ' ps x|grep %s ' % name
    f = os.popen(cmd)
    lines = f.readlines()
    output = None
    count = 0
    for line in lines:
        if line.find("grep") != -1:
            continue
        output = re.findall('\\b'+name+'\\b ', line)
        #print(str(output))
        count += 1
        print(line, output)

    if count == 2:
        return True
    #cmd = " kill %s " % '   ' .join(ids)
    print(cmd)
    return False
