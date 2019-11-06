class ReadTxtUtil:
    @classmethod
    def readTxt(cls, path):
        # 读取txt返回测试用例列表
        with(open(path,"r")) as readFile:
            cls.readlines = readFile.readlines()
        cls.datas=[]
        for line in cls.readlines:
            data = line.strip("\n").split(":")
            cls.datas.append(data)

        return cls.datas

