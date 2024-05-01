#import pytest
#from read_database import count_rows, total, calculation

#@pytest.mark.parametrize("id, rows, stocks, div", [
    #(10, "Number of records processed: 19", "Total number of stocks processed: 8232", "Total dividend payments: 0.82p"),
    #(11, "Number of records processed: 22", "Total number of stocks processed: 8676", "Total dividend payments: 0.86p"),
    #(12, "Number of records processed: 29", "Total number of stocks processed: 8953", "Total dividend payments: 0.89p"),
#])

#def test_dividend(id, rows, stocks, div):
    #assert count_rows(id) == rows
    #assert total(id) == stocks
    #assert calculation(id) == div

#if __name__ == "__main__":
    #pytest.main()
