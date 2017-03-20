import ast
import unittest

filename = '../datascience.py'
tree = ast.parse(''.join(open(filename)))

# exec(compile(tree, filename="<ast>", mode="exec"))

class TestDatasets(unittest.TestCase):

    def testImportSklearn(self):
        test_case = "failed"

        for node in tree.body:
            if isinstance(node, ast.ImportFrom):
                if node.module == 'sklearn':
                    for name in node.names:
                        self.assertEqual('datasets', name.name)
                        test_case = "passed"

        self.assertEqual("passed", test_case)


    def testIris(self):
        test_case = "failed"
        for node in tree.body:
            if isinstance(node, ast.Assign):
                if isinstance(node.value, ast.Call):
                    for name in node.targets:
                        if name.id == 'iris' and isinstance(node.value.func, ast.Attribute):
                            self.assertEqual('load_iris', node.value.func.attr)
                            self.assertEqual('datasets', node.value.func.value.id)
                            test_case = "passed"

        self.assertEqual("passed", test_case)


