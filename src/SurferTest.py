import unittest
import Surfer 

class Test(unittest.TestCase):
    def testForSurfer(self):
        print("\nStarted Surfer Test\n")
        sf = Surfer() 
        assert(sf.currentTop()=="HomePage")
        assert(sf.back()=="HomePage")
        sf.push("New Article 1")
        assert(sf.currentTop()=="New Article 1")
        sf.push("New Article 2")
        sf.push("New Article 3")
        assert(sf.back()=="New Article 2")
        assert(sf.back()=="New Article 1")
        assert(sf.back()=="HomePage")
        print("\nFinished Surfer Test\n")

if __name__ == '__main__':
    unittest.main()