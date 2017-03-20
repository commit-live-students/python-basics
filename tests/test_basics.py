import ast
import unittest

filename = '../app.py'
tree = ast.parse(''.join(open(filename)))

# exec(compile(tree, filename="<ast>", mode="exec"))

class TestBasicPython(unittest.TestCase):

    def testIntegerVaribale(self):
        test_case = "failed"
        for node in tree.body:
            if isinstance(node, ast.Assign):
                if isinstance(node.value, ast.Num):
                    if node.targets[0].id == 'a':
                        self.assertEqual(1, node.value.n)
                        test_case = "passed"

        self.assertEqual("passed", test_case)


    def testFloatVaribale(self):
        test_case = "failed"
        for node in tree.body:
            if isinstance(node, ast.Assign):
                if isinstance(node.value, ast.Num):
                    if node.targets[0].id == 'b':
                        self.assertEqual(4.5, node.value.n)
                        test_case = "passed"

        self.assertEqual("passed", test_case)


    def testStringVaribale(self):
        test_case = "failed"
        for node in tree.body:
            if isinstance(node, ast.Assign):
                if isinstance(node.value, ast.Str):
                    if node.targets[0].id == 'str':
                        self.assertEqual("GreyAtom", node.value.s)
                        test_case = "passed"

        self.assertEqual("passed", test_case)


    def testListVaribale(self):
        test_case = "failed"
        for node in tree.body:
            if isinstance(node, ast.Assign):
                if isinstance(node.value, ast.List):
                    if node.targets[0].id == 'list':
                        self.assertEqual("raindrops n roses", node.value.elts[0].s)
                        self.assertEqual("whiskers on kittens", node.value.elts[1].s)
                        test_case = "passed"

        self.assertEqual("passed", test_case)