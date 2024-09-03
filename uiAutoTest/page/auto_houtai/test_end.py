from uiAutoTest.utils import DriverUntil
import pytest
@pytest.mark.run(order=1010)
class TestEnd:
    def test_end(self):
        DriverUntil._mis_quit=True