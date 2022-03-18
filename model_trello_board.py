# Utilizando POO modelar un tablero con columnas y que cada columna contiene tarjetas.
# Modelar el método para mover tarjetas de una columna a otra.
from typing import List
from unittest import TestCase


class Board:

    def __init__(self):
        self.name = None
        self.colums: List[Column] = []


class Column:

    def __init__(self):
        self.name = None
        self.cards: List[Card] = []
        self.can_card_move_to_columns: List[Column] = []

    def move_card(self, card, target_column) -> bool:
        if target_column in self.can_card_move_to_columns:
            target_column.cards.append(card)
            self.cards.pop(card)
           
            return True
    
        return False


class Card:

    def __init__(self):
        self.content = None


class ColumnTestCase(TestCase):

    def setUp(self):
        pass

    def test_move_card_to_valid_column_returns_true(self):

        return_value = self.board.columns[3].move_card(
            self.board.columns[3].cards[2],
            self.board.columns[4]
        )

        self.assertTrue(return_value)

    def test_move_card_to_not_valid_column_returns_false(self):

        return_value = self.board.columns[3].move_card(
            self.board.columns[3].cards[2],
            self.board.columns[2]
        )

        self.assertFalse(return_value)
