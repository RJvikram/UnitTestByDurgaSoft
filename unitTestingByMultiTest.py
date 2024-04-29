from unittest import TestCase, main

class TestCaseDemo(TestCase):

    def setUp(self):
        print("setUp method executing.")

    def test1(self):
        print("test1 method executing.")

    def test2(self):
        print("test2 method executing.")
    
    def tearDown(self):
        print("tearDown method executing.")


main()

"""

Note : in this script we are witeen multi test case in this class. if we user "setUp() and tearDown() 
        for multi test case then remember setUp() and tearDown() mentored will alwase call for each test cases. eg : 
        
       setUp() ------------------> test1() ------------------> tearDown()
       setUp() ------------------> test2() ------------------> tearDown()

OutPut : 
======================================================================
setUp method executing.
test1 method executing.
tearDown method executing.
.setUp method executing.
test2 method executing.
tearDown method executing.
.
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

"""