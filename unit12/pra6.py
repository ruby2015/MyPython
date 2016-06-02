def importAs(name):
    return __import__(name)

newname = importAs('sys')
print newname.modules.keys()
