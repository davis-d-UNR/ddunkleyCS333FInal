import unittest
from io import StringIO
import sys
from driver import *
  
class TestPoker(unittest.TestCase):
    
    def setUp(self):
        self.hands = [
            [Card(14, 'S'), Card(13, 'S'), Card(12, 'S'), Card(11, 'S'), Card(10, 'S')], #Royal Flush
            [Card(10, 'S'), Card(9, 'S'), Card(8, 'S'), Card(7, 'S'), Card(6, 'S')], #Straight Flush
            [Card(2, 'S'), Card(2, 'C'), Card(2, 'D'), Card(2, 'H'), Card(14, 'S')], #Four of a Kind
            [Card(3, 'S'), Card(3, 'C'), Card(3, 'D'), Card(5, 'H'), Card(5, 'S')], #Full House
            [Card(11, 'S'), Card(11, 'C'), Card(11, 'D'), Card(11, 'H'), Card(6, 'S')], #Four of a Kind
            [Card(10, 'S'), Card(9, 'S'), Card(8, 'S'), Card(7, 'S'), Card(6, 'D')], #Straight Flush
            [Card(14, 'S'), Card(13, 'H'), Card(12, 'D'), Card(11, 'C'), Card(10, 'S')] #Straight
        ]
    
    def test_isRoyal(self):
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        game = Poker(1)
        game.isRoyal(self.hands[0])
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        expected_output = 'Royal Flush\n'
        self.assertEqual(captured_output.getvalue(), expected_output)
    
    def test_isStraightFlush(self):
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        game = Poker(1)
        game.isStraightFlush(self.hands[1])
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        expected_output = 'Straight Flush\n'
        self.assertEqual(captured_output.getvalue(), expected_output)
    
    def test_isFour(self):
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        game = Poker(1)
        game.isFour(self.hands[2])
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        expected_output = 'Four of a Kind\n'
        self.assertEqual(captured_output.getvalue(), expected_output)
    
    def test_isFull(self):
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        game = Poker(1)
        game.isFull(self.hands[3])
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        expected_output = 'Full House\n'
        self.assertEqual(captured_output.getvalue(), expected_output)
    
    def test_isFour2(self):
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        game = Poker(1)
        game.isFour(self.hands[4])
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        expected_output = 'Four of a Kind\n'
        self.assertEqual(captured_output.getvalue(), expected_output)
