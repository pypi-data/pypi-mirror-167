# jd-HTMLTestRunner

jd-HTMLTestRunner for Python3 unittest 

[![PyPI version](https://badge.fury.io/py/jd-HTMLTestRunner.svg)](https://pypi.python.org/pypi/jd-HTMLTestRunner)
[![PyPI version](https://img.shields.io/pypi/pyversions/jd-HTMLTestRunner)](https://pypi.python.org/pypi/jd-HTMLTestRunner)
[![PyPI version](https://img.shields.io/pypi/dm/jd-HTMLTestRunner)](https://pypi.python.org/pypi/jd-HTMLTestRunner)


## 安装

```
pip install jd-HTMLTestRunner
```

## 示例

```
from jd_HTMLTestRunner import HTMLTestRunner

suite = unittest.TestLoader().discover(".", "test_*.py")
file = open(r"test01.html", "wb")
runner = HTMLTestRunner(stream=file, title="我的测试报告")
runner.run(suite)
file.close()
```


## 模块内方法说明

| 函数、对象名称            | 类型    | 说明                          |
|---------------------------|---------|-------------------------------|
| HTMLTestRunner            | 对象    | 主测试执行对象   |

