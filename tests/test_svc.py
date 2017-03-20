import ast
import unittest

filename = '../svc.py'
tree = ast.parse(''.join(open(filename)))

# exec(compile(tree, filename="<ast>", mode="exec"))

class TestDatasets(unittest.TestCase):

    def testImportSklearn(self):
        test_case = "failed"
        for node in tree.body:
            if isinstance(node, ast.Expr) and isinstance(node.value.func, ast.Name):
                self.assertEqual("SVC", node.value.func.id)
                test_case = "passed"
                break
        self.assertEqual("passed", test_case)