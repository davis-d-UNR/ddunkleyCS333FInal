import unittest
from driver import Card, Deck, Poker

class TestCard(unittest.TestCase):

    def test_init(self):
        card = Card(14, 'S')
        self.assertEqual(card.rank, 14)
        self.assertEqual(card.suit, 'S')

    def test_str(self):
        card = Card(14, 'S')
        self.assertEqual(str(card), 'AS')
        
    def test_eq(self):
        card1 = Card(14, 'S')
        card2 = Card(14, 'H')
        self.assertEqual(card1, card2)
        
    def test_ne(self):
        card1 = Card(14, 'S')
        card2 = Card(13, 'S')
        self.assertNotEqual(card1, card2)
        
    def test_lt(self):
        card1 = Card(12, 'S')
        card2 = Card(14, 'S')
        self.assertLess(card1, card2)
        
    def test_le(self):
        card1 = Card(14, 'S')
        card2 = Card(14, 'H')
        self.assertLessEqual(card1, card2)
        
    def test_gt(self):
        card1 = Card(14, 'S')
        card2 = Card(12, 'S')
        self.assertGreater(card1, card2)
        
    def test_ge(self):
        card1 = Card(14, 'S')
        card2 = Card(14, 'H')
        self.assertGreaterEqual(card1, card2)
        

class TestDeck(unittest.TestCase):

    def test_init(self):
        deck = Deck()
        self.assertEqual(len(deck.deck), 52)

    def test_shuffle(self):
        deck1 = Deck()
        deck2 = Deck()
        deck2.shuffle()
        self.assertNotEqual(deck1.deck, deck2.deck)
        
    def test_len(self):
        deck = Deck()
        self.assertEqual(len(deck), 52)
        
    def test_deal(self):
        deck = Deck()
        card = deck.deal()
        self.assertEqual(len(deck), 51)

class TestPoker(unittest.TestCase):
    
    def test_point(self):
        hand = [Card(14, 'C'), Card(13, 'H'), Card(12, 'D'), Card(11, 'S'), Card(10, 'C')]
        poker = Poker(1)
        self.assertEqual(poker.point(hand), 430596)
        
    def test_isRoyal(self):
        hand = [Card(14, 'C'), Card(13, 'C'), Card(12, 'C'), Card(11, 'C'), Card(10, 'C')]
        poker = Poker(1)
        poker.isRoyal(hand)
        self.assertIn(poker.tlist[0], [4143526, 10_975_936, 11_202_998])
        
    def test_isStraightFlush(self):
        hand = [Card(9, 'D'), Card(8, 'D'), Card(7, 'D'), Card(6, 'D'), Card(5, 'D')]
        poker = Poker(1)
        poker.isStraightFlush(hand)
        self.assertIn(poker.tlist[0], [ 3_617_528 ,77_535, 78_624, 79_713])
        
    def test_isFour(self):
        hand = [Card(11, 'D'), Card(11, 'H'), Card(11, 'C'), Card(11, 'S'), Card(10, 'D')]
        poker = Poker(1)
        poker.isFour(hand)
        self.assertIn(poker.tlist[0], [3310694,68_145, 69_655, 71_165])
        
    def test_isFull(self):
        hand = [Card(13, 'S'), Card(13, 'C'), Card(13, 'H'), Card(9, 'H'), Card(9, 'D')]
        poker = Poker(1)
        poker.isFull(hand)
        self.assertIn(poker.tlist[0], [3_001_228,30_913, 31_739, 32_565])

  class InterTestPoker(unittest.TestCase):
    
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
        
                
        
if __name__ == '__main__':
    unittest.main()
