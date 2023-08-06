import preface


def test_set_dict_without_nested_dict() -> None:
    dct = {}

    key = "a.b.c"

    value = 1

    expected = {"a": {"b": {"c": 1}}}
    preface.dict.set(dct, key, value)

    assert dct == expected


def test_merge_dict_without_nested() -> None:
    a = {"a": 1}
    b = {"b": 2}

    expected = {"a": 1, "b": 2}
    actual = preface.dict.merge(a, b)

    assert actual == expected


def test_merge_dict_with_nested():
    a = {"a": {"b": 1}}
    b = {"b": 2, "a": {"c": 3}}

    expected = {"a": {"b": 1, "c": 3}, "b": 2}
    actual = preface.dict.merge(a, b)

    assert actual == expected


def test_pop_dict_with_nested_dict() -> None:
    dct = {"a": {"b": 1}}

    expected_value = 1
    expected_dct = {"a": {}}

    actual_value = preface.dict.pop(dct, "a.b")

    assert actual_value == expected_value
    assert dct == expected_dct
