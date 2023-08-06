# SNG Tools Kit

SNG开发套件，内部 python 开发通用接口。

## 模块列表

- general
- log
- config

引入示例：

```python
import sng_tk as stk
```

## 使用方法

首先安装：

```shell
python3 setup.py install
```

如果需要更新也可在代码更新后执行上面这行命令。

### 通用模块

示例：

```python
import sng_tk as stk

# 打印公司Logo
stk.general.print_header()
# 处理路径中特殊的格式（目前可以将~解析为主目录)
print(stk.general.parse_path("~/sng/log"))
```

### 日志模块

示例：

```python
import sng_tk as stk

log = stk.Log("sng-tools-kit")
log.info("normal log")
log.debug("debug log")
log.warning("warning log")
log.error("error log")
log.critical("critical log")
```

上面的示例需要在`/etc/sng`中存在`sng-tools-kit.yaml`配置文件，其中包含以下配置：

> 或者也可传入一个dict类型的数据作为配置文件，但要求必须与以下文件保持一致。

```yaml
# 日志模块相关配置
Log:

  # 关闭日志输出（不建议设置为true），若该项设置为true，则完全关闭日志输出，下面的所有配置也无法生效。
  Close: false

  # 日志输出等级，有以下选项，从上到下越来越高：
  #    0. DEBUG: 调试日志
  #    1. INFO: 普通日志（默认）
  #    2. WARNING: 警告日志
  #    3. ERROR: 错误日志
  #    4. CRITICAL: 严重错误日志
  # 系统将输出指定等级及其更高等级的日志。
  Level: 1

  # 日志文件统一的输出目录，其中会包含来自各个模块的日志。
  # 需要注意的是，程序必须拥有这里提供的路径的写权限，否则程序将无法正常运行。
  Directory: "~/sng/log"

  # 日志的最大尺寸，单位：MB
  MaxSize: 10
```

### 配置文件模块

示例：

```python
import sng_tk as stk

config_data = stk.Config("sng-tools-kit").read()
print("Config test:", config_data["config"]["test"])
```

上面的示例需要在`/etc/sng`中存在`sng-tools-kit.yaml`配置文件，其中包含以下配置：

```yaml
config:
  test: "config read success!"
```