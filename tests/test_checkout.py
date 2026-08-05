from checkout import calculate_total


def test_bulk_discount_at_threshold():
    assert calculate_total(10, 10) == 90
