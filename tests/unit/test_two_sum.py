from algos.two_sum import two_sum_hashed


class TestTwoSumHashed:
    def test_result_exists(self):
        result = two_sum_hashed([3, 2, 1, 6, 7], 9)
        assert result[0] + result[1] == 9
        result = two_sum_hashed([2, 43, 12, 54, 32, 53], 44)
        assert result[0] + result[1] == 44
        result = two_sum_hashed([22, 23, 13, 34, 75, 53], 98)
        assert result[0] + result[1] == 98

    def test_result_not_exist(self):
        assert not two_sum_hashed([], 1)
        assert not two_sum_hashed([1, 2, 3], 10)
