# general document for work day
import shutil
import os

class WorktoCreateDocument:
    def __init__(self) -> None:
        self.path = os.getcwd()

    def genera_dir(self, path):
        for i in range(0,4):
            dirweek = os.path.join(path, """{} week""".format(i))
            
            for j in ["Plan", "Data", "Done"]:
                dirname = os.path.join(dirweek, j)
                try:
                    os.makedirs(dirname)
                except:
                    pass
            os.chdir(dirweek)
            fd = open("ReadMe.txt", "w")
            fd.close()
        os.chdir(path)
    
    def work(self):
        import calendar
        for i in calendar.month_name:
            if not i:
                continue
            path = os.path.join(self.path, i)
            try:
                os.mkdir(path)
            except:
                pass

            if not os.path.isdir(path):
                continue
            
            self.genera_dir(path)

if __name__ == "__main__":
    work = WorktoCreateDocument()
    work.work()

    
        