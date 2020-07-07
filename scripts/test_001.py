import pytest

class Test_ABC:

    def setup_class(self):
        print(">>>>>>>setup_class")
        print(12222222222222222222222)
    def teardown_class(self):
        print(">>>>>>>teardown_class")
    @pytest.mark.run(order=-1)
    def test_a(self):
        print(">>>>>>test_a")
        assert True
    def test_b(self):
        print(">>>>>>>test_b")
        assert True

if __name__ == '__main__':
    pytest.main("-s test_001.py")