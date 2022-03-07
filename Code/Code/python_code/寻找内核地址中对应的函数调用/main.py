

if __name__ == "__main__":
    addr = []
    with open("address", "r") as fd:
        for line in fd:
            addr.append(line.strip())

    with open("kallsyms.txt", "r") as fd:
        lines = fd.readlines()

        for i in addr:
            for count in range(1, len(i)):
                # print(i[:-count])
                address = None
                for line in lines:
                    if line.find(i[:-count]) != -1:
                        address = line.strip()
                        break;

                if address:
                    break;
            print(address)