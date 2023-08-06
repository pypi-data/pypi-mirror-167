# Cyclomatic Complexity
Calculating cyclic complexity based on [lizard]("https://github.com/terryyin/lizard").

## Install
```
python3 -m pip install yangwangjinxin_cyclomatic_complexity
```

## Usage

```
import cyclomatic_complexity as cc
file_result = cc.analyze('main.py')
dir_result = cc.analyze('.')
print(dit_result.cyclomatic_complexity)
```

