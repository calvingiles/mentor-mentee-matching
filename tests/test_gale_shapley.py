from web.gale_shapley import find_stable_match


def test_find_stable_match():
    or_a = "or_a"
    or_b = "or_b"
    or_c = "or_c"
    ee_a = "ee_a"
    ee_b = "ee_b"
    ee_c = "ee_c"

    assert find_stable_match({}, {}) == []

    assert find_stable_match({
        or_a: [ee_a]
    }, {
        ee_a: [or_a]
    }) == [[or_a, ee_a]]

    assert find_stable_match({
        or_a: [ee_a, ee_b],
        or_b: [ee_a, ee_b],
    }, {
        ee_a: [or_a, or_b],
        ee_b: [or_a, or_b],
    }) == [[or_a, ee_a], [or_b, ee_b]]

    assert find_stable_match({
        ee_a: [or_a, or_b],
        ee_b: [or_a, or_b],
    },
    {
        or_a: [ee_b, ee_a],
        or_b: [ee_b, ee_a],
    }) == [[ee_b, or_a], [ee_a, or_b]]

    assert find_stable_match({
        or_a: [ee_b, ee_a],
        or_b: [ee_b, ee_a],
    },
    {
        ee_a: [or_a, or_b],
        ee_b: [or_a, or_b],
    }) == [[or_a, ee_b], [or_b, ee_a]]
