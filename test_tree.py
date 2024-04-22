#/bin/python3
import pytest
from node import Node
from tree import Tree

@pytest.fixture
def create_tree():
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(-1)

    return tree

def test_find_1(create_tree):
    node: Node = create_tree.find(0)

    assert node is create_tree.getRoot()

def test_find_2(create_tree):
    node: Node = create_tree.find(1)

    assert node.data == 1
