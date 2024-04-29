from unittest import TestCase, main

class UnitTestDemo(TestCase):

    def setUp(self):
        print("setUp function execting")

    def test1(self):
        print("test1 function execting")

    def tearDown(self):
        print("tearDown function execting")

main()

''' 
Note:

    1. module name  : unittest
    2. class name : TestCase
    3. method : there are 3 moethod which are - 
        1. setUp()
        2. test()
        3. tearDown()
    
    setUp() : setUp() is a predefine function where we are declear all setup like database connection, open browser..etc. this function name can be modified.
    test() : in side the test method we are declear all the funcanality to test feachers. like if we are writing test cases for login module then need to check 
             is user name and paswword is correct or not like that.we can modified this function name by using test prifix. means you can chose any name for this 
             function but before that finction name need to user test. for example: if i want to create one function whos name is 'loging' so you have to use 
             like that 'testlogin'. after tst you can chose anything.
    tearDown() : tearDown() function basically use for close the window/connection. that function name can not be modified.

'''

''' 
outPut : 
        setUp function execting
        test1 function execting
        tearDown function execting
        .
        ----------------------------------------------------------------------
        Ran 1 test in 0.000s

        OK

'''