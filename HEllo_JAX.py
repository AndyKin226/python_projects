import jax.numpy as jnp
from jax import grad

# 运行一个简单的导数计算：y = x^2, 在 x=4 时的导数应该是 8
f = lambda x: x**2
print("JAX 验证结果:", grad(f)(4.0)) 
