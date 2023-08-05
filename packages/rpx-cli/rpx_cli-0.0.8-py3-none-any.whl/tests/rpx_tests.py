import unittest

from click.testing import CliRunner
from rpx_cli import rpx


class RpxTests(unittest.TestCase):

    def test_create_vite(self):
        runner = CliRunner()
        result = runner.invoke(
            rpx, ["vite", "-n", "app", "-t", "react-ts", "-s", "styled-components"])
        self.assertEqual(result.exit_code, 0)

    def test_create_components(self):
        runner = CliRunner()
        result = runner.invoke(rpx, ["component", "-n", "Header"])
        self.assertEqual(result.exit_code, 0)

    def test_create_component_unknown(self):
        name = 'unknown'
        runner = CliRunner()
        result = runner.invoke(rpx, ["vite", "-n", name])
        self.assertNotEqual(result.exit_code, 0)
        self.assertEqual(result.output, f'Name {name} not found!\n')

    def test_create_vite_unknown(self):
        name = 'unknown'
        type = 'unknown'
        style = 'unknown'
        runner = CliRunner()
        result = runner.invoke(
            rpx, ["vite", "-n", name, "-t", type, "-s", style])
        self.assertNotEqual(result.exit_code, 0)
        self.assertEqual(result.output, f'Name {name} not found!\n')
        self.assertEqual(result.output, f'Type {type} not found!\n')
        self.assertEqual(result.output, f'Style {style} not found!\n')


if __name__ == '__main__':
    unittest.main()
