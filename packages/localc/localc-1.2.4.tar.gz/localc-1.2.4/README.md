# Localc (Logic Calculator)

## 介绍
一个简单的逻辑计算器。能进行逻辑表达式（即**命题**```Proposition```）的求解运算。

## 安装方法

本项目已上传至[PYPI](https://pypi.org/project/localc/)，直接利用```pip```（```Python```的**包管理器**即可安装）。

只需在控制台输入如下命令：

```
pip install localc
```

即可安装最新版本的*localc*。

## 文档

### 快速开始

*localc*是一个小巧的逻辑计算器，使用起来非常简单。

安装完成后，直接在控制台使用：

```
python -m localc
```

即可打开下面的用户界面：

```
Localc (Logic Calculator), Version 1.2.3
In [1]:
```

你可以直接使用以下构造函数：

```python
Proposition("true and false")
```

这样会生成一个命题实例，其中的字符串描述了这个命题。你可以计算这个命题的值，只需要使用：

```python
p = Proposition("true and false")
print(p.calc())
```

或者更简便地，利用命题对象的```value```属性：

```python
print(Proposition("true and false").value)
```

得到的结果均为```False```，当然，这是因为“真 与 假”这个命题的结果为**假**

更特别地，你可以使用变量名来表示子命题，如：

```python
p = Proposition("x and not y or z")
```

其中的```x```，```y```，```z```都是变量名，表示了一个子命题。注意，此时计算命题```p```的值，会引发异常。因为其子命题```x```，```y```，```z```的值均未确定。

不过，你却可以打印出基于这三个变量的真值表，只需要使用命题对象的```table```属性：

```python
p = Proposition("x and not y or z")
print(p.table)
```

你就会得到如下输出：

```
+-------+-------+-------+-------+----------+----------------+
|  [x]  |  [y]  |  [z]  |  ¬[y] | [x]∧¬[y] | [x]∧¬[y] ∨ [z] |
+-------+-------+-------+-------+----------+----------------+
| False | False | False |  True |  False   |     False      |
| False | False |  True |  True |  False   |      True      |
| False |  True | False | False |  False   |     False      |
| False |  True |  True | False |  False   |      True      |
|  True | False | False |  True |   True   |      True      |
|  True | False |  True |  True |   True   |      True      |
|  True |  True | False | False |  False   |     False      |
|  True |  True |  True | False |  False   |      True      |
+-------+-------+-------+-------+----------+----------------+
```

这展示了真值表以及原命题的计算过程。

另外，你还可以指定一个变量的值。只需要使用```variable:value```的语法。

例如，在上例中，将```z```变量的值赋值为```true```，其余均不变，则使用：

```python
p = Proposition("x and not y or z:true")
print(p.table)
```

则会得到```z```列恒为```True```的真值表

```
+-------+-------+------+-------+----------+----------------+
|  [x]  |  [y]  | [z]  |  ¬[y] | [x]∧¬[y] | [x]∧¬[y] ∨ [z] |
+-------+-------+------+-------+----------+----------------+
| False | False | True |  True |  False   |      True      |
| False |  True | True | False |  False   |      True      |
|  True | False | True |  True |   True   |      True      |
|  True |  True | True | False |  False   |      True      |
+-------+-------+------+-------+----------+----------------+
```

最后，直接打印命题，可以得到用于计算该命题的树状结构。例如：

```python
p = Proposition("(true and x) and not y or z:true")
print(p)
```

会得到以下树状结构：

```
OR
├─── AND
│    ├─── GROUP
│    │    └─── AND
│    │         ├─── True
│    │         └─── [ x ]
│    └─── NOT
│         └─── [ y ]
└─── [ z -> True ]
```

### 更多

#### 命名空间与项目结构

想要使用*localc*，就必须导入```localc```包。

```localc```包中包含了如下组件：

- ```node```，包含了用于存储抽象语法树的数据结构
- ```operators```，用于操作符英语与数学表示的相互转换
- ```parser```，利用*token*流，构建抽象语法树
- ```proposition```，**主用户接口**
- ```scanner```，任务是生成*token*流

我并不建议你使用除了```proposition```以外的其他包，除非你知道自己在做什么。对于大多数用户而言，你只需要在*Python*代码文件的头部加上：

```python
from localc import Proposition
```

#### 命题

使用*localc*计算器的核心是命题。

命题是这样的字符串，它包含了：

- 逻辑运算符
- 表示子命题的变量名
- 用于修改运算符优先级顺序的圆括号

##### 逻辑运算符

为了方便输入，逻辑运算符都是用英文单词表示的。目前可用的逻辑运算符（按照优先级从低到高排列）有：

| 优先级 |            运算符            | 描述                     |
|:---:|:-------------------------:|:-----------------------|
|  1  |         ```iff```         | 当且仅当（*If and Only If*） |
|  2  |         ```if```          | 每当（*If*）               |
|  3  |         ```oif```         | 仅当（*Only If*）          |
|  4  |        ```xor```          | 异或                     |
|  5  |         ```or```          | 逻辑或                    |
|  6  |         ```and```         | 逻辑与                    |
|  7  |         ```not```         | 逻辑非                    |
|  8  |  ```(some_expression)```  | 分组                     |

##### 变量名

变量名是用于表示子命题的单词，它可以包含任意的数字，字母，特殊符号，且遵循特定的规则。其规则是：

- 变量名不能以左圆括号```(```开头
- 变量名不能以右圆括号```)```结尾
- 变量名不能含有冒号```:```

例如，下面的变量名都是合法的：

```p```、```a_proposition```、```!%@#&$^(```

以下变量名则是非法的，因为他们违反了上面的规则：

```(left```、```right)```、```abc:def```

##### 变量名赋值

通过```variable:value```的语法，可以给子命题赋值。其中```value```可以是：

- ```true```，表示该子命题为真
- ```false```，表示该子命题为假

##### 展示命题

新建```Proposition```命题对象后，可以直接打印该命题对象：

```python
print(Proposition("true and false"))
```

会生成该命题对应的树状结构：

```
AND
├─── True
└─── False
```

注意，该树状结构可以任意复杂，如：

```python
p = Proposition("true and x:true or (y:false and not z)")
print(p)
```

会得到：

```
OR
├─── AND
│    ├─── True
│    └─── [ x -> True ]
└─── GROUP
     └─── AND
          ├─── [ y -> False ]
          └─── NOT
               └─── [ z ]
```

或者，使用内置的```repr```函数，获得可用于重建该命题的字符串（只需再利用```eval```）函数：

```python
p = Proposition("true and false")
print(repr(p))
```

最后输出可直接用于```eval```函数的字符串：

```
Proposition("true and false")
```

##### 生成真值表

直接打印命题的```table```属性，就可以得到该命题对应的真值表，如：

```python
p = Proposition("w and x and (y or not z)")
print(p.table)
```

将生成：

```
+-------+-------+-------+-------+-------+---------+------------+--------------+----------------------+
|  [w]  |  [x]  |  [y]  |  [z]  |  ¬[z] | [w]∧[x] | [y] ∨ ¬[z] | ([y] ∨ ¬[z]) | [w]∧[x]∧([y] ∨ ¬[z]) |
+-------+-------+-------+-------+-------+---------+------------+--------------+----------------------+
| False | False | False | False |  True |  False  |    True    |     True     |        False         |
| False | False | False |  True | False |  False  |   False    |    False     |        False         |
| False | False |  True | False |  True |  False  |    True    |     True     |        False         |
| False | False |  True |  True | False |  False  |    True    |     True     |        False         |
| False |  True | False | False |  True |  False  |    True    |     True     |        False         |
| False |  True | False |  True | False |  False  |   False    |    False     |        False         |
| False |  True |  True | False |  True |  False  |    True    |     True     |        False         |
| False |  True |  True |  True | False |  False  |    True    |     True     |        False         |
|  True | False | False | False |  True |  False  |    True    |     True     |        False         |
|  True | False | False |  True | False |  False  |   False    |    False     |        False         |
|  True | False |  True | False |  True |  False  |    True    |     True     |        False         |
|  True | False |  True |  True | False |  False  |    True    |     True     |        False         |
|  True |  True | False | False |  True |   True  |    True    |     True     |         True         |
|  True |  True | False |  True | False |   True  |   False    |    False     |        False         |
|  True |  True |  True | False |  True |   True  |    True    |     True     |         True         |
|  True |  True |  True |  True | False |   True  |    True    |     True     |         True         |
+-------+-------+-------+-------+-------+---------+------------+--------------+----------------------+
```

##### 计算命题

命题的值存储在```Proposition```对象的```value```属性中。

若该命题中所有子命题都有值，或没有其他子命题，则该命题可以计算。若该命题可以计算，则命题的值已经在创建该命题的时候提前算出；若该命题不能计算，则```value```属性的值为```None```。

特别地，如果你需要重算命题的值，可使用```calc```方法。调用```calc```方法后，```value```属性也会相应更新。

例如：

```python
p = Proposition("true and not false")
print(p.calc())
```

你将得到：

```
True
```

##### 修改命题

修改命题是指，改变命题中的标识符对应的值。当然，最简单的方法是新建一个全新的命题，并在命题描述语句中给这些命题的标识符赋值。否则，你可能需要以下知识：

为了得到命题中标识符节点的引用，你可以使用```identifiers```属性（一个记录了所有标识符对象引用的列表），或```unspecified```
属性（一个记录了所有未赋值标识符引用的列表），并修改这些节点的```value```属性。

另外，标识符的```name```属性记录了该标识符的名称。这在赋值的时候很有用。

最后，当你通过这种方式修改命题后，请务必调用命题对象的```init```方法：

```python
p = Proposition("a and b and not c")
print("Original proposition:")
print(p, '\n')

print("Modifying proposition...")
values = {"a": True, "b": True, "c": False}
for identifier in p.identifiers:
    identifier.value = values[identifier.name]
p.init()

print("After modifying:")
print(p)
print("With a value of {}".format(p.value))
```

你会得到：

```
Original proposition:
AND
├─── AND
│    ├─── [ a ]
│    └─── [ b ]
└─── NOT
     └─── [ c ]

Modifying proposition...
After modifying:
AND
├─── AND
│    ├─── [ a -> True ]
│    └─── [ b -> True ]
└─── NOT
     └─── [ c -> False ]
With a value of True
```

#### 其他

由于这只是个简单的小项目，若你还需要更多功能和自由度，欢迎阅读该项目的源代码，或者提出Issue。
