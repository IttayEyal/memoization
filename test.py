import time
import random
from memoize.memoized import Memoized

# Tested functions
@Memoized()
def get_random():
    return random.random()


@Memoized()
def get_random_with_args(n):
    return random.random() + n


@Memoized()
def get_another_random_with_args(n):
    return random.random() + n


@Memoized()
def get_random_with_kwargs(n=0):
    return random.random() + n


@Memoized()
def get_random_with_args_and_kwargs(num, n=0):
    return random.random() + num + n


@Memoized()
def get_str_with_random(obj):
    return str(obj) + str(random.random())


@Memoized()
def wait_and_return_random(wait_time_seconds):
    time.sleep(wait_time_seconds)
    return random.random()


# Tests
def test_basic_memoization():
    assert get_random() == get_random()


def test_args_memoization():
    assert get_random_with_args(1) == get_random_with_args(1)
    assert get_random_with_args(1) != get_random_with_args(2)


def test_kwargs_memoization():
    assert get_random_with_kwargs(n=5) == get_random_with_kwargs(n=5)
    assert get_random_with_kwargs(n=5) != get_random_with_kwargs(n=6)


def test_args_and_kwargs_memoization():
    assert get_random_with_args_and_kwargs(1, n=2) == get_random_with_args_and_kwargs(
        1, n=2
    )
    assert get_random_with_args_and_kwargs(1, n=2) != get_random_with_args_and_kwargs(
        1, n=3
    )
    assert get_random_with_args_and_kwargs(1, n=2) != get_random_with_args_and_kwargs(
        2, n=2
    )


def test_long_running_function():
    """Are we running the function again or using the memoized version?"""
    wait_time_seconds = 0.5 + random.random() / 10
    max_memoized_duration = 0.01

    # First call should take some time
    start_time = time.time()
    wait_and_return_random(wait_time_seconds)
    duration = time.time() - start_time
    assert duration >= wait_time_seconds

    # Memoized call should be instant
    start_time = time.time()
    wait_and_return_random(wait_time_seconds)
    duration = time.time() - start_time
    assert duration <= max_memoized_duration


def test_nested_input():
    list_1 = [1, 2, 3]
    list_2 = list_1.copy()
    list_3 = [4, 5, 6]

    dict_1 = {1: 2, 3: 4}
    dict_2 = dict_1.copy()
    dict_3 = {5: 6, 7: 8}

    nested_object = {
        "dict_1": dict_1,
        "nested": {"nested": {"nested": dict_2}},
        "lists": [list_1, list_2],
    }

    # List memoization
    assert get_str_with_random(list_1) == get_str_with_random(list_2)
    assert get_str_with_random(list_1) != get_str_with_random(list_3)

    # Dict memoization
    assert get_str_with_random(dict_1) == get_str_with_random(dict_2)
    assert get_str_with_random(dict_1) != get_str_with_random(dict_3)

    # Nested object memoization
    str_1 = get_str_with_random(nested_object)
    str_2 = get_str_with_random(nested_object)
    str_3 = get_str_with_random(dict_3)
    assert str_1 == str_2
    assert str_1 != str_3


def test_function_mixup():
    """Make sure that different functions with the same args are cached under different keys"""
    assert get_random_with_args(1) != get_another_random_with_args(1)
