"""Test ASCII Train Class """

from ascii_train.train import *
import unittest

# To run locally:
# Run from asciitrain root folder > py -m tests.test_train


class TestTrain(unittest.TestCase):

    def test_passenger_train(self):
        train = Train("HPP")
        self.assertEqual("<HHHH::|OOOO|::|OOOO|", train.print())

    def test_restaurant_train(self):
        train = Train("HPRP")
        self.assertEqual("<HHHH::|OOOO|::|hThT|::|OOOO|", train.print())

    def test_double_headed_train(self):
        train = Train("HPRPH")
        self.assertEqual(
            "<HHHH::|OOOO|::|hThT|::|OOOO|::HHHH>", train.print())

    def test_modify_train(self):
        train = Train("HPRPH")
        train.detach_end()
        self.assertEqual("<HHHH::|OOOO|::|hThT|::|OOOO|", train.print())
        train.detach_head()
        self.assertEqual("|OOOO|::|hThT|::|OOOO|", train.print())

    def test_cargo_train(self):
        train = Train("HCCC")
        self.assertEqual("<HHHH::|____|::|____|::|____|", train.print())
        train.fill()
        self.assertEqual("<HHHH::|^^^^|::|____|::|____|", train.print())
        train.fill()
        self.assertEqual("<HHHH::|^^^^|::|^^^^|::|____|", train.print())
        train.fill()
        self.assertEqual("<HHHH::|^^^^|::|^^^^|::|^^^^|", train.print())
        with self.assertRaises(IllegalStateException):
            train.fill()

    def test_mixed_train(self):
        train = Train("HPCPC")
        self.assertEqual(
            "<HHHH::|OOOO|::|____|::|OOOO|::|____|", train.print())
        train.fill()
        self.assertEqual(
            "<HHHH::|OOOO|::|^^^^|::|OOOO|::|____|", train.print())
        train.fill()
        self.assertEqual(
            "<HHHH::|OOOO|::|^^^^|::|OOOO|::|^^^^|", train.print())
        with self.assertRaises(IllegalStateException):
            train.fill()


if __name__ == '__main__':
    unittest.main()
