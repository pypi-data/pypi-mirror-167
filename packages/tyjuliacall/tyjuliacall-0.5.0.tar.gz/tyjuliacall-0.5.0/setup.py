# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tyjuliacall', 'tyjuliasetup']

package_data = \
{'': ['*'], 'tyjuliasetup': ['src/*']}

install_requires = \
['julia-numpy>=0.4.0,<0.5.0']

setup_kwargs = {
    'name': 'tyjuliacall',
    'version': '0.5.0',
    'description': 'A Python package for Tongyuan-hacked PyCall as an engineerization for Python-Julia interops.',
    'long_description': '# TyJuliaCall\n\n[![CI](https://github.com/Suzhou-Tongyuan/tyjuliacall/actions/workflows/ci.yml/badge.svg)](https://github.com/Suzhou-Tongyuan/tyjuliacall/actions/workflows/ci.yml)\n[![codecov](https://codecov.io/gh/Suzhou-Tongyuan/tyjuliacall/branch/master/graph/badge.svg?token=NMRDY32QIC)](https://codecov.io/gh/Suzhou-Tongyuan/tyjuliacall)\n[![versions](https://img.shields.io/pypi/pyversions/tyjuliacall.svg)](https://pypi.org/project/tyjuliacall/#history)\n[![pypi](https://img.shields.io/pypi/v/tyjuliacall.svg)](https://pypi.org/project/tyjuliacall/)\n[![License](https://img.shields.io/badge/License-BSD_2--Clause-green.svg)](https://github.com/Suzhou-Tongyuan/tyjuliacall/blob/main/LICENSE)\n\n\nCalling Julia from Python for the real world.\n\nFeatures:\n\n1. **Cross-platform support for both dynamically linked Python and statically linked Python.**\n\n2. **Support Julia system images.**\n\n## Installation\n\nPrerequisites: Python (>=3.7)\n\nThen install the `tyjuliacall` Python package.\n\n```bash\npip install -U tyjuliacall\n```\n\n## Using System Images\n\n```python\nfrom tyjuliasetup import use_sysimage  # CAUTIOUS: not \'tyjuliacall\'!\nuse_sysimage(r"/path/to/sysimg")\n# if your sysimage contains TyPython,\n# you could call use_system_typython() to reduce the time cost of setting up julia.\nfrom tyjuliacall import Base\nprint(\n    "current sysimage in use",\n    Base.unsafe_string(Base.JLOptions().image_file))\n# out: /path/to/sysimg\n```\n\n## 受信赖的Python-Julia数据类型转换\n\n虽然tyjuliacall允许在Python和Julia之间传递任意数据，但由于是两门不同的语言，数据转换的类型对应关系是复杂的。\n\n为了保证代码的后向兼容性，使得规范的代码在不同版本的Syslab/tyjuliacall上都可以运行，建议只使用如下的数据类型转换。\n\n### Python数据传递到Julia\n\nPython向Julia函数传参时，推荐只使用下表左边的数据类型，以保证代码的后向兼容。\n\n|  Python Type | Julia Type  |\n|:-----:|:----:|\n| 基本类型 | |\n| `int` | `Int64`|\n| `float` | `Float64` |\n| `bool` | `Bool` |\n| `complex` | `ComplexF64` |\n| `None`  | `nothing` |\n| `str`   | `String` |\n| 组合类型 |   |\n| `numpy.ndarray` (dtype为数字或字符串或bool)  | 原生`Array` |\n| `tuple`，且元素均为表中数据类型 | `Tuple` |\n\n对于Python传递给Julia的`tuple`，其各个元素按照以上规则依次转换。\n\nTIPS: 如何传递`bytearray`或者`bytes`到Julia?\n\n1. 向Julia函数传递bytes时，可以改为传递一个uint8的数组。\n\n   无拷贝传参： `np.array(memoryview(b\'mybytes\'), dtype=np.uint8)`\n   拷贝传参： `np.array(list(b\'mybytes\'), dtype=np.uint8)`\n\n2. 向Julia函数传递bytearray时，可以改为传递一个uint8的数组。\n\n    无拷贝传参： `np.asarray(bytearray(b\'mybytes\')))`\n\n### Julia数据传递到Python\n\n当获取Julia函数返回值，或导入Julia模块的非函数对象时，将发生Julia到Python的数据传递。\n\n保证后向兼容的Julia到Python数据转换关系如下表所示：\n\n|  Julia | Python  |\n|:-----:|:----:|\n| 基本类型 |  |\n| `Integer`子类型  | `int`|\n| `AbstractFloat`子类型 | `float`|\n| `Bool` | `bool` |\n| `Complex`子类型 | `complex` |\n| `nothing`对象 | `None`  |\n| `AbstractString`子类型 | `str`   |\n| `Vector{UInt8}` | `bytearray` |\n| 组合类型 | |\n| `AbstrctArray{T}` (T见下方说明) | `numpy.ndarray` |\n| `Tuple{T1, ..., Tn}`, 且`Ti`为该表中的类型 | `tuple` |\n| 其余Julia类型            | `tyjuliacall.JV` |\n\n一个Julia AbstrctArray能转换为numpy数组，当且仅当其元素类型`T`是以下类型之一\n\n- `Int8, Int16, Int32, Int64, UInt8, UInt16, UInt32, UInt64`\n- `Float16, Float32, Float64`\n- `ComplexF16, ComplexF32, ComplexF64`\n- `Bool`\n\n注意，当类型为`Vector{String}`或者`Array{String, 2}`的Julia对象被返回给Python时，它被封装为一个`tyjuliacall.JV`类型。\n\n## 其他说明\n\n1. 不要对Julia包/模块使用`from ... import *`。\n2. `Vector{String}`传到Python是一个`tyjuliacall.JV`，这是一个纯Julia对象的包装，因此下标索引是从1开始的。\n',
    'author': 'Suzhou-Tongyuan',
    'author_email': 'support@tongyuan.cc',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
