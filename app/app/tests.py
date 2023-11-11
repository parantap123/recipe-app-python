from django.test import SimpleTestCase


class one(SimpleTestCase):
    
    def test_add_number(self):
        
        res = 5
        
        self.assertEqual(res,5)
    
    def test_add_number1(self):#test_ is kinda the prefix the test suite looks for
        
        res = 6
        
        self.assertEqual(res,6)
        

class two(SimpleTestCase):
    
    def test_add_number(self):#test_ is kinda the prefix the test suite looks for
        
        res = 6
        
        self.assertEqual(res,6)
        
    