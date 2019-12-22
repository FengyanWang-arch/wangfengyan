from ddt import ddt,data,file_data,unpack
import unittest

@ddt
class MyTestDdt(unittest.TestCase):
    def setUp(self):
        print('start')
        
    @data({'value1':1,'value2':5},{'value1':2,'value2':4})
    @unpack
    def test_one(self,value1,value2):
        print(r'the @data number is:%s %s'%(value1,value2))
        
    def tearDown(self):
        print('end')
        
if __name__=='__main__':
    unittest.main(verbosity=2)
