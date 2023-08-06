# This file is placed in the Public Domain.
# pylint: disable=R0903

"composition tests"


import os
import unittest


from opl import Db, Object, Wd, dump, load


class Composite(Object):

    def __init__(self):
        super().__init__()
        self.db = Db()


class TestComposite(unittest.TestCase):

    def test_composite(self):
        composite = Composite()
        path = dump(composite, os.path.join(Wd.workdir, "compositetest"))
        composite2 = Composite()
        load(composite2, path)
        self.assertEqual(type(composite2.db), Db)
