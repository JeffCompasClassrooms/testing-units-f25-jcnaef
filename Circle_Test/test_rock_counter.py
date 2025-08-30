import unittest
from rock_counter import *
class test_rock_counter(unittest.TestCase):
    def test_init(self):
        rCounter = Rock_Counter()
        self.assertIsInstance(rCounter,Rock_Counter)
    
    def test_init_rock_count(self):
        rCounter = Rock_Counter()
        self.assertEqual(rCounter.get_num_rocks(),0)
    
    def test_init_rock_color_count(self):
        rCounter = Rock_Counter()
        self.assertEqual(rCounter.get_rock_color_count(),{})

    def test_get_num_rocks(self):
        rCounter = Rock_Counter()
        self.assertEqual(rCounter.get_num_rocks(),0)
    
    def test_get_num_rocks_after_find(self):
        rCounter = Rock_Counter()
        rCounter.rock_found("red")
        self.assertEqual(rCounter.get_num_rocks(),1)
    
    def test_get_num_rocks_after_loss(self):
        rCounter = Rock_Counter()
        rCounter.rock_found("red")
        rCounter.rock_lost("red")
        self.assertEqual(rCounter.get_num_rocks(),0)

    def test_get_num_color_rocks(self):
        rCounter = Rock_Counter()
        rocksFound = ["red", "blue", "blue", "green"]
        rCounter.mul_rocks_found(rocksFound)
        self.assertEqual(rCounter.get_num_color_rocks("blue"), 2)
        self.assertEqual(rCounter.get_num_color_rocks("green"), 1)

    def test_rock_found(self):
        rCounter = Rock_Counter()
        rCounter.rock_found("red")
        self.assertEqual(rCounter.get_num_rocks(),1)
        self.assertEqual(rCounter.get_rock_color_count(),{"red":1})
    
    def test_same_color_rock_found(self):
        rCounter = Rock_Counter()
        rCounter.rock_found("red")
        rCounter.rock_found("red")
        self.assertEqual(rCounter.get_num_rocks(),2)
        self.assertEqual(rCounter.get_rock_color_count(),{"red":2})
    def test_different_color_rock_found(self):
        rCounter = Rock_Counter()
        rCounter.rock_found("red")
        rCounter.rock_found("green")
        self.assertEqual(rCounter.get_num_rocks(),2)
        self.assertEqual(rCounter.get_rock_color_count(),{"red":1,"green":1})
        
    def test_different_colored_rocks_found(self):
        rCounter = Rock_Counter()
        rocksFound = ["red","red","blue","blue","green"]
        rCounter.mul_rocks_found(rocksFound)
        self.assertEqual(rCounter.get_num_rocks(),5)
        self.assertEqual(rCounter.get_num_color_rocks("red"),2)
        self.assertEqual(rCounter.get_num_color_rocks("blue"),2)
        self.assertEqual(rCounter.get_num_color_rocks("green"),1)
    
    def test_same_colored_rocks_found(self):
        rCounter = Rock_Counter()
        rocksFound = ["red","red","red","red","red"]
        rCounter.mul_rocks_found(rocksFound)
        self.assertEqual(rCounter.get_num_rocks(),5)
        self.assertEqual(rCounter.get_num_color_rocks("red"),5)
    
    def test_empty_list_rocks_found(self):
        rCounter = Rock_Counter()
        rocksFound = []
        rCounter.mul_rocks_found(rocksFound)
        self.assertEqual(rCounter.get_num_rocks(),0)
        self.assertEqual(rCounter.get_rock_color_count(),{})

    def test_rock_lost(self):
        rCounter = Rock_Counter()
        rocksFound = ["red","blue","blue","blue","green"]
        rCounter.mul_rocks_found(rocksFound)
        self.assertEqual(rCounter.get_num_rocks(),5)
        rCounter.rock_lost("blue")
        self.assertEqual(rCounter.get_num_color_rocks("blue"),2)
    
    def test_last_color_rock_lost(self):
        rCounter = Rock_Counter()
        rocksFound = ["red","blue","blue","blue","green"]
        rCounter.mul_rocks_found(rocksFound)
        rCounter.rock_lost("red")
        self.assertNotIn("red",rCounter.get_rock_color_count())
    
    def test_neg_rock_lost(self):
        rCounter = Rock_Counter()
        rocksFound = ["red","blue","blue","blue","green"]
        rCounter.mul_rocks_found(rocksFound)

        with self.assertRaisesRegex(Exception, "You didn't have a rock of this color to lose"):
            rCounter.rock_lost("yellow")

    def test_mul_same_color_rocks_lost(self):
        rCounter = Rock_Counter()
        rocksFound = ["red","blue","blue","blue","green"]
        rCounter.mul_rocks_found(rocksFound)
        rCounter.mul_rocks_lost(["blue","blue"])
        self.assertEqual(rCounter.get_num_color_rocks("blue"),1)
    
    def test_dif_color_rocks_lost(self):
        rCounter = Rock_Counter()
        rocksFound = ["red","blue","blue","blue","green","red"]
        rCounter.mul_rocks_found(rocksFound)
        rCounter.mul_rocks_lost(["red","blue"])
        self.assertEqual(rCounter.get_num_color_rocks("blue"),2)
        self.assertEqual(rCounter.get_num_color_rocks("red"),1)
    
    def test_empty_list_rocks_lost(self):
        rCounter = Rock_Counter()
        rocksFound = ["red","blue","blue","blue","green","red"]
        rCounter.mul_rocks_found(rocksFound)
        rCounter.mul_rocks_lost([])
        self.assertEqual(rCounter.get_num_rocks(),6)
        self.assertEqual(rCounter.get_rock_color_count(),{"red":2,"blue":3,"green":1})
    
    def test_get_total_num_of_rock_colors(self):
        rCounter = Rock_Counter()
        rocksFound = ["red","blue","green","red","red","yellow","blue"]
        rCounter.mul_rocks_found(rocksFound)
        self.assertEqual(rCounter.get_total_num_rock_colors(),4)

    def test_same_color_get_rock_color_count(self):
        rCounter = Rock_Counter()
        rocksFound = ["red","red","red","red","red"]
        rCounter.mul_rocks_found(rocksFound)
        self.assertEqual(rCounter.get_rock_color_count(),{"red":5})

    def test_dif_color_get_rock_color_count(self):
        rCounter = Rock_Counter()
        rocksFound = ["red","blue","green","red","red","yellow","blue"]
        rCounter.mul_rocks_found(rocksFound)
        self.assertEqual(rCounter.get_rock_color_count(),{"red":3,"blue":2,"green":1,"yellow":1})
    
    def test_get_rock_color_count_after_loss(self):
        rCounter = Rock_Counter()
        rocksFound = ["red","blue","green","red","red","yellow","blue"]
        rCounter.mul_rocks_found(rocksFound)
        rCounter.rock_lost("red")
        self.assertEqual(rCounter.get_rock_color_count(),{"red":2,"blue":2,"green":1,"yellow":1})
    
    def test_get_rock_color_count_after_loss_last_rock(self):
        rCounter = Rock_Counter()
        rocksFound = ["red","blue","green","red","red","yellow","blue"]
        rCounter.mul_rocks_found(rocksFound)
        rCounter.rock_lost("yellow")
        self.assertEqual(rCounter.get_rock_color_count(),{"red":3,"blue":2,"green":1})

    def test_has_rock_of_color(self):
        rCounter = Rock_Counter()
        rocksFound = ["red","blue","green","red","red","yellow","blue"]
        rCounter.mul_rocks_found(rocksFound)
        self.assertTrue(rCounter.has_rock_of_color("red"))
        self.assertFalse(rCounter.has_rock_of_color("teal"))
    
    def test_lost_all_rocks(self):
        rCounter = Rock_Counter()
        rocksFound = ["red","blue","green","red","red","yellow","blue"]
        rCounter.mul_rocks_found(rocksFound)
        rCounter.lost_all_rocks()
        self.assertEqual(rCounter.get_rock_color_count(),{})
        self.assertEqual(rCounter.get_num_rocks(),0)
    
    def test_lost_all_color_rocks_true(self):
        rCounter = Rock_Counter()
        rocksFound = ["red","blue","green","red","red","yellow","blue"]
        rCounter.mul_rocks_found(rocksFound)
        rCounter.lost_all_color_rocks("red")
        self.assertEqual(rCounter.get_num_rocks(),4)
        self.assertEqual(rCounter.get_rock_color_count(),{"blue":2,"green":1,"yellow":1})

    def test_lost_all_color_rocks_false(self):
        rCounter = Rock_Counter()
        rocksFound = ["red","blue","green","red","red","yellow","blue"]
        rCounter.mul_rocks_found(rocksFound)

        with self.assertRaisesRegex(Exception, "You didn't have a rock of this color to lose"):
            rCounter.lost_all_color_rocks("teal")
        

