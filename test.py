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


def test_function_mixup():
    """Make sure that different functions with the same args are cached under different keys"""
    assert get_random_with_args(1) != get_another_random_with_args(1)
