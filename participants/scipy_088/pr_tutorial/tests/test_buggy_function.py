from pr_tutorial.buggy_function import angle_to_sexigesimal


def test_decimals():
    for decimals in range(1, 10):
        after_decimal = angle_to_sexigesimal(144, decimals=decimals).split(".")[1]
        assert len(after_decimal) == decimals


def test_extremes():
    assert angle_to_sexigesimal(0) == "0:0:0.000"
    assert angle_to_sexigesimal(360) == "24:0:0.000"
