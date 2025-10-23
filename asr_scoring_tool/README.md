# ASR 打分工具（ASR Scoring Tool）🎤📊

一款用于自动评测 ASR（自动语音识别）模型性能的工具，支持 **CER（字符错误率）** 和 **WER（词错误率）** 计算，可灵活替换 ASR 模型（如 Whisper、Vosk、Wav2Vec 2.0 等），适配中英文数据集！🚀

## 一、项目功能 ✨

- **多指标智能计算** 📈：中文自动算 CER（字符错误率），英文自动算 WER（词错误率），无需手动切换逻辑；
- **ASR 模型自由换** 🔄：通过统一接口支持 Whisper、Vosk、Wav2Vec 2.0 等主流模型，新增模型仅需简单扩展；
- **文本标准化全自动** 🧹：自动处理中英文文本（繁转简、去空格、去标点、数字统一），消除格式差异对评分的干扰；
- **批量数据集评测** 📦：支持 en/zh 分目录数据集，自动加载音频 + 参考文本，批量输出平均评分，效率拉满；
- **轻量部署无压力** 💻：支持 CPU/GPU 运行，无需复杂环境配置，快速验证 ASR 模型性能。

## 二、项目结构 📂

```
asr_scoring_tool/
│
├── .pytest_cache/          # pytest 缓存目录（自动生成）📦
│
├── asr/                    # ASR 模型接口模块🎤
│   ├── base_asr.py         # ASR 基类，定义统一接口⚙️
│   ├── vosk_asr.py         # Vosk ASR 模型实现📘
│   └── whisper_asr.py      # Whisper ASR 模型实现📗
│
├── examples/               # 示例脚本目录🌟
│   ├── score_dataset.py    # 批量数据集评测（核心脚本）📊
│   └── score_texts.py      # 文本直接打分示例📝
│
├── metrics/                # 评分指标模块📏
│   ├── cer.py              # 字符错误率（CER）计算
│   ├── levenshtein.py      # 编辑距离（Levenshtein Distance）算法🚚
│   └── wer.py              # 词错误率（WER）计算
│
├── preprocessing/          # 文本预处理模块📃
│   └── text_normalizer.py  # 文本标准化（繁简转换、去空格等）📑
│
├── tests/                  # 单元测试目录✅
│   └── test_levenshtein.py # 编辑距离算法测试🤌
│
├── data_loader.py          # 数据集加载工具🔗
├── scoring.py              # 核心打分逻辑封装🎯
├── pyproject.toml          # 项目配置文件（打包、依赖等）🔐
├── README.md               # 项目说明文档🧾
└── requirements.txt        # 项目依赖清单📜
```

## 三、环境准备 🛠️

### 1. 系统要求 🖥️

- 操作系统：Windows 10/11、macOS 12+、Linux（Ubuntu 20.04+）
- 硬件要求：
  - CPU：i5/R5 及以上（基础够用）
  - GPU（可选）：NVIDIA GPU（支持 CUDA 11.6+，加速 Whisper 等模型）
  - 内存：4GB 起步，批量评测建议 8GB+

### 2. 依赖安装 📥

```bash
pip install -r requirements.txt
```

## 四、数据集 📋

用于测试的数据集下载地址：

https://box.nju.edu.cn/d/7c46c2b693ec4c6abc71/🌐🌐🌐

## 五、快速使用 🚀

### 1.关键配置修改（2 处必改）🔑

在 `scoring.py` 中修改：

```python
# 1. 替换为你的数据集根目录
data_dir = r"D:\desktop\hw1_testdata"

# 2. 选择 ASR 模型（默认 Whisper，可替换为 Vosk 等）
asr = WhisperASR(model_name="base")  # Whisper 基础模型（轻量快）
# asr = VoskASR(model_dir=r"D:\models\vosk-model-en-us-0.22")  # Vosk 英文模型
```

### 2. 批量评测数据集（核心功能）📊

运行 `examples/scoring.py`，自动完成 “加载数据→ASR 识别→计算评分” 全流程：

```bash
# 在项目根目录中执行
python scoring.py
```

## 六、ASR 模型扩展指南📝

### 步骤 1：创建模型类 📝

在 `asr_scoring_tool/asr/` 目录下新建模型文件（如 `your_asr.py`），继承 `BaseASR` 并实现 `transcribe` 方法：

### 步骤 2：在评测脚本中使用新模型 🔄

修改 `scoring.py`，导入并初始化新模型：

```python
from asr.your_asr import YourAsr

# 初始化 Wav2Vec 2.0 模型
asr = YourAsr(model_name="...")
```

## 七、致谢 🙏

- 文本繁简转换使用 [opencc-python-reimplemented](https://pypi.org/project/opencc-python-reimplemented/) 🀄；
- 评分指标参考 [WER/CER 国际标准](https://en.wikipedia.org/wiki/Word_error_rate) 📏。