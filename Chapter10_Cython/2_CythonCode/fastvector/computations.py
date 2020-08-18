"""Own implementation of a vector computations.
"""
from .vector import VectorND
from .dtypes import Number
from .cython_computations import _cython_clip_vector, _naive_cython_clip_vector

def python_clip_vector(vector_in: VectorND, min_value: Number, max_value: Number, vector_out: VectorND):
    VectorND.check_vector_types(vector_in)
    VectorND.check_vector_types(vector_out)
    VectorND.check_numeric_argument(min_value)
    VectorND.check_numeric_argument(max_value)
    if min_value > max_value:
        raise ValueError("min_value must be <= max_value")
    for i in range(len(vector_in)):
        vector_out[i] = min(max(vector_in[i], min_value), max_value)

def cython_clip_vector(vector_in: VectorND, min_value: Number, max_value: Number, vector_out: VectorND):
    VectorND.check_vector_types(vector_in)
    VectorND.check_vector_types(vector_out)
    VectorND.check_numeric_argument(min_value)
    VectorND.check_numeric_argument(max_value)
    if min_value > max_value:
        raise ValueError("min_value must be <= max_value")
    _cython_clip_vector(vector_in.values, min_value, max_value, vector_out.values)

def naive_cython_clip_vector(vector_in: VectorND, min_value: Number, max_value: Number, vector_out: VectorND):
    VectorND.check_vector_types(vector_in)
    VectorND.check_vector_types(vector_out)
    VectorND.check_numeric_argument(min_value)
    VectorND.check_numeric_argument(max_value)
    if min_value > max_value:
        raise ValueError("min_value must be <= max_value")
    _naive_cython_clip_vector(vector_in.values, min_value, max_value, vector_out.values)
