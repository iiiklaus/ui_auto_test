from uiAutoTest.utils import DriverUntil
import pytest

class TestBegin:
    @pytest.mark.run(order=1000)
    def test_begin(self):
        DriverUntil._mis_quit=False