def getFromDict(self, dataDict, mapList):
        try:
            if len(mapList) == 0:
                output = ""
                return output
            else:
                output = reduce(operator.getitem, mapList, dataDict)
                return output
        except:
            return mapList[0]
