# Label Studio
1. 針對標記需求修改
2. 可以單純在 local file 執行，不需 pip install label studio (修改 dependentency)
3. 串接客製化 ML 模型
4. 修改 output 輸出 JSON 座標表示格式
5. 串接外部模型服務，實現預標記功能

## 基本設定
```bash
# 基本環境安裝
pip install requirements.txt
``` 

若是在 VM 環境下執行，需將 server.py 
- 第 965、967、978 行的 localhost 更改為 ip位置

請使用 python=3.6
強制結束 Control + c

## Quick Start - 啟動一般標記工具

```bash
# 啟動一般標記工具

# 移動到 label_tool 資料夾下
cd label_tool

# Requires >=Python3.6
# --force 會強制覆蓋先前啟動的 labeling_project
python server.py start labeling_project --init --force  
```

## Quick Start - 串接 ML 模型，以 dummy_model 為例

```bash

# 移動到 label_tool/ml 資料夾下
cd ml

# 初始化 my_ml_backend_random
# --force 會強制覆蓋先前啟動的 my_ml_backend_random
# --script 後方放入需啟用的model 相對路徑
# :DummyModel, :後方為 class name
python server.py init my_ml_backend_random --force --script examples/dummy_model.py:DummyModel 

# 啟動 my_ml_backend_random 後端服務
# 啟用 port 為 9090
python server.py start my_ml_backend_random

# 開啟另一個 terminal 
# 移動到 label_tool 資料夾下
cd label_tool

# 啟動標記工具，並設定後端為 ml 9090 的 port
python server.py start random_choice_project --init --ml-backend http://localhost:9090 --force
```

## Modify
2020.07.22 JamesXChang

## License

This software is licensed under the [Apache 2.0 LICENSE](/LICENSE) © [Heartex](https://www.heartex.ai/). 2020

<img src="https://github.com/heartexlabs/label-studio/blob/master/images/opossum_looking.png?raw=true" title="Hey everyone!" height="140" width="140" />
