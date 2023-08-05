from dataclasses import field

import jax
import jax.tree_util as jtu
import pytest
from jax import numpy as jnp

import pytreeclass as pytc
from pytreeclass._src.tree_util import _tree_fields, _tree_structure


def test_true_field_only():
    @pytc.treeclass
    class Linear:
        weight: jnp.ndarray
        bias: jnp.ndarray

        def __init__(self, key, in_dim, out_dim):
            self.weight = jax.random.normal(key, shape=(in_dim, out_dim)) * jnp.sqrt(
                2 / in_dim
            )
            self.bias = jnp.ones((1, out_dim))

    @pytc.treeclass(field_only=True)
    class StackedLinear:
        def __init__(self, key, in_dim, out_dim, hidden_dim):
            keys = jax.random.split(key, 3)
            self.l1 = Linear(key=keys[0], in_dim=in_dim, out_dim=hidden_dim)
            self.l2 = Linear(key=keys[1], in_dim=hidden_dim, out_dim=hidden_dim)
            self.l3 = Linear(key=keys[2], in_dim=hidden_dim, out_dim=out_dim)

    model = StackedLinear(key=jax.random.PRNGKey(0), in_dim=2, out_dim=2, hidden_dim=2)
    _tree_structure(model)

    assert "l1" not in model.__dataclass_fields__
    assert "l1" not in model.__undeclared_fields__

    @pytc.treeclass(field_only=True)
    class StackedLinear:
        l4: Linear = field(default=1)
        l5: Linear

        def __init__(self, key, in_dim, out_dim, hidden_dim):
            ...

    with pytest.raises(AttributeError):
        # l5 is not declared
        model = StackedLinear(
            key=jax.random.PRNGKey(0), in_dim=2, out_dim=2, hidden_dim=2
        )
        model.__pytree_structure__


def test_false_field_only():
    @pytc.treeclass
    class Linear:
        weight: jnp.ndarray
        bias: jnp.ndarray

        def __init__(self, key, in_dim, out_dim):
            self.weight = jax.random.normal(key, shape=(in_dim, out_dim)) * jnp.sqrt(
                2 / in_dim
            )
            self.bias = jnp.ones((1, out_dim))

    @pytc.treeclass(field_only=False)
    class StackedLinear:
        def __init__(self, key, in_dim, out_dim, hidden_dim):
            keys = jax.random.split(key, 3)
            self.l1 = Linear(key=keys[0], in_dim=in_dim, out_dim=hidden_dim)
            self.l2 = Linear(key=keys[1], in_dim=hidden_dim, out_dim=hidden_dim)
            self.l3 = Linear(key=keys[2], in_dim=hidden_dim, out_dim=out_dim)

    model = StackedLinear(key=jax.random.PRNGKey(0), in_dim=2, out_dim=2, hidden_dim=2)

    assert "l1" in _tree_fields(model)

    @pytc.treeclass(field_only=False)
    class StackedLinear:
        l4: Linear

        def __init__(self, key, in_dim, out_dim, hidden_dim):
            keys = jax.random.split(key, 3)

            # Declaring l1,l2,l3 as dataclass_fields is optional
            # as l1,l2,l3 are Linear class that is wrapped with @pytc.treeclass
            self.l1 = Linear(key=keys[0], in_dim=in_dim, out_dim=hidden_dim)
            self.l2 = Linear(key=keys[1], in_dim=hidden_dim, out_dim=hidden_dim)
            self.l3 = Linear(key=keys[2], in_dim=hidden_dim, out_dim=out_dim)

    with pytest.raises(AttributeError):
        # l4 is not declared
        model = StackedLinear(
            key=jax.random.PRNGKey(0), in_dim=2, out_dim=2, hidden_dim=2
        )
        model.__pytree_structure__


def test_hash():
    @pytc.treeclass
    class T:
        a: jnp.ndarray

    # with pytest.raises(TypeError):
    hash(T(jnp.array([1, 2, 3])))


def test_post_init():
    @pytc.treeclass
    class Test:
        a: int = 1

        def __post_init__(self):
            self.a = 2

    t = Test()

    assert t.a == 2


def test_subclassing():
    @pytc.treeclass
    class L0:
        a: int = 1
        b: int = 3
        c: int = 5

        def inc(self, x):
            return x

        def sub(self, x):
            return x - 10

    @pytc.treeclass
    class L1(L0):
        a: int = 2
        b: int = 4

        def inc(self, x):
            return x + 10

    l1 = L1()

    assert jtu.tree_leaves(l1) == [2, 4, 5]
    assert l1.inc(10) == 20
    assert l1.sub(10) == 0


def test_overriding_setattr():

    with pytest.raises(AttributeError):

        @pytc.treeclass
        class Test:
            a: int = 1

            def __setattr__(self, name, value):
                super().__setattr__(name, value)
