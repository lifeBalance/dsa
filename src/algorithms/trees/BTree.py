from BTNode import BTNode

class BTree:
  def __init__(self, value):
    if value:
        self.root = BTNode(value)
    else:
        self.root = None
    