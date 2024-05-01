import pytest
from call import start
from Calculation_class import calculation

@pytest.mark.parametrize("id, div", [
    (10, 'Total for 2024-03-29 00:00:00: 69.69'),
    (11, 'Total for 2024-04-01 00:00:00: 74.13'),
    (12, 'Total for 2024-04-02 00:00:00: 76.91'),
])

def test_dividend(id, div):
    calc = calculation(id)
    result = calc.start()
    assert result == div
    del calc

if __name__ == "__main__":
    pytest.main()
