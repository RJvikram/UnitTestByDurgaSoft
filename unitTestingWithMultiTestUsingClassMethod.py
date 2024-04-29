from unittest import TestCase, main

class TestCaseDemo(TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUp class method execution.")

    def test1(self):
        print("test1 method execution.")

    def test2(self):
        print("test2 method execution.")

    def test3(self):
        print("test3 method execution.")

    @classmethod
    def tearDownClass(cls):
        print("tearDown class method execution.")

main()

"""
Note :
    in this Script we also call multi test case in one script by using setUpClass() and tearDownclass() method. 
    when we use setUpClass() and tearDownClass() method so when this script will run that time that both function 
    will call only one time and not will be excute for each test. mens it will 1st run setUpClass() after that test 
    will be excuted and multi pule tst have on that script then all test will excuteed then tearDownClass will be excute.
    eg : 

    setUpClass() -----------------> test1() -----------------> test2() -----------------> test3() -----------------> tearDownClass()

OutPut : 

    setUp class method execution.
    test1 method execution.
    .test2 method execution.
    .test3 method execution.
    .tearDown class method execution.

"""