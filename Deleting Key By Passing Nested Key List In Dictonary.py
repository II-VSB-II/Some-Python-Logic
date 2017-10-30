def DeleteKey(Dictonary,KeyList):
  sub = Dictonary
  for i in KeyList[:-1]:
    sub = sub[i]
  del sub[key_list[-1]]

D={'key1':{'key2':{'key3':'value3', 'key4':'value4'}, 'key5':'value5'}}
key_list = ['key1', 'key2', 'key4']
DeleteKey(D,key_list)
