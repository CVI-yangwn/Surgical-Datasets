<div align="center">

# 🩺 Surgical-Datasets

**手术视频与内镜公开数据集整理 · 附中文论文精读**

[![Papers](https://img.shields.io/badge/精读论文-4-4f5bd5)](https://cvi-yangwn.github.io/Surgical-Datasets/)
[![Datasets](https://img.shields.io/badge/数据集-5-8b5cf6)](#-数据集总览)
[![Reading](https://img.shields.io/badge/在线阅读-GitHub%20Pages-b84fa3)](https://cvi-yangwn.github.io/Surgical-Datasets/)

[📚 在线阅读全部精读](https://cvi-yangwn.github.io/Surgical-Datasets/) · [📊 数据集总览](#-数据集总览) · [🔍 精读是怎么做的](#-精读是怎么做的)

</div>

---

## 📚 论文精读

每篇精读都包含：背景与动机、核心观点速览、数据与实验、深入分析，以及**论文没有说明或前后对不上的地方**。

| 数据集 | 领域 | 一句话 | 阅读 |
| :-- | :-- | :-- | :-- |
| **Cataract-1K** | 眼科 · 白内障 | 一个来自单一诊所的白内障手术视频数据集:1000 个视频,三类标注各自只覆盖其中一小部分 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cataract-1k.html) · [📝 笔记](DeepPaperNote_output/%E6%89%8B%E6%9C%AF%E6%95%B0%E6%8D%AE%E9%9B%86/Cataract_1K_Cataract_Surgery_Dataset_for_Scene_Segmentation_Phase_Recognition_and_Irregularity_Detection/Cataract_1K_Cataract_Surgery_Dataset_for_Scene_Segmentation_Phase_Recognition_and_Irregularity_Detection.md) |
| **OphNet** | 眼科 · 工作流 | 一个由 YouTube 眼科手术视频搭起来的三级标注基准，规模是真的，几个数字却对不上 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/ophnet.html) · [📝 笔记](DeepPaperNote_output/%E6%89%8B%E6%9C%AF%E6%95%B0%E6%8D%AE%E9%9B%86/OphNet_A_Large_Scale_Video_Benchmark_for_Ophthalmic_Surgical_Workflow_Understanding/OphNet_A_Large_Scale_Video_Benchmark_for_Ophthalmic_Surgical_Workflow_Understanding.md) |
| **OphCLIP** | 眼科 · 视频-语言 | 用眼科手术视频教会模型看懂手术：数据集 OphVL 与检索增强预训练 OphCLIP | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/ophclip.html) · [📝 笔记](DeepPaperNote_output/%E6%89%8B%E6%9C%AF%E6%95%B0%E6%8D%AE%E9%9B%86/OphCLIP_Hierarchical_Retrieval_Augmented_Learning_for_Ophthalmic_Surgical_Video_Language_Pretraining/OphCLIP_Hierarchical_Retrieval_Augmented_Learning_for_Ophthalmic_Surgical_Video_Language_Pretraining.md) |
| **EndoBench** | 内镜 · 多模态评测 | 用 6,832 道选择题量一量大模型离内镜医师有多远 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/endobench.html) · [📝 笔记](DeepPaperNote_output/%E6%89%8B%E6%9C%AF%E6%95%B0%E6%8D%AE%E9%9B%86/EndoBench_A_Comprehensive_Evaluation_of_Multi_Modal_Large_Language_Models_for_Endoscopy_Analysis/EndoBench_A_Comprehensive_Evaluation_of_Multi_Modal_Large_Language_Models_for_Endoscopy_Analysis.md) |

> 页面上的分数是模型自评，不是外部评审；文中的数字都用脚本与论文原文逐一核对过。

---

## 📊 数据集总览

### 👁️ 眼科 Ophthalmic

| 数据集 | 年份 | 论文 | 数据 | 任务 | 规模 | 来源 | 精读 |
| :-- | :--: | :--: | :--: | :-- | :-- | :-- | :--: |
| Cataract-1K | 2023 | [arXiv](https://arxiv.org/abs/2312.06295) | [<img src="https://github.githubassets.com/favicons/favicon.svg" width="16">](https://github.com/Negin-Ghamsarian/Cataract-1K) | 阶段识别 / 分割 / 异常检测 | 1000 个视频 | 医院 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cataract-1k.html) |
| OphNet | 2024 | [arXiv](https://arxiv.org/abs/2406.07471) | [<img src="https://github.githubassets.com/favicons/favicon.svg" width="16">](https://minghu0830.github.io/OphNet-benchmark) | 阶段、器械、操作识别 | 2278 个视频 | YouTube | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/ophnet.html) |

### 🔬 内镜 Endoscopic

| 数据集 | 年份 | 论文 | 数据 | 任务 | 规模 | 来源 | 精读 |
| :-- | :--: | :--: | :--: | :-- | :-- | :-- | :--: |
| EndoBench | 2025 | [arXiv](https://arxiv.org/abs/2505.23601) | [🤗](https://huggingface.co/datasets/Saint-lsy/EndoBench) | 视觉问答 | | | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/endobench.html) |

### 🩻 腹腔镜 Laparoscopic

| 数据集 | 年份 | 论文 | 数据 | 任务 | 规模 | 来源 | 精读 |
| :-- | :--: | :--: | :--: | :-- | :-- | :-- | :--: |
| SLAM | 2025 | Nature（链接待补） | [figshare](https://figshare.com/articles/dataset/SLAM_-_Surgical_LAparoscopic_Motions/28104782/3) | 分类 | ~3650 个视频 | | ⏳ |

### 🕒 尚未公开 Not yet

| 数据集 | 年份 | 论文 | 任务 | 规模 | 来源 | 精读 |
| :-- | :--: | :--: | :-- | :-- | :-- | :--: |
| OphCLIP（眼科） | 2025 | [arXiv](https://arxiv.org/abs/2411.15421) | 图文对齐 | 375K 图文对 | YouTube | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/ophclip.html) |

---

## 🔍 精读是怎么做的

精读由仓库内的 [DeepPaperNote](.claude/skills/deeppapernote) skill 生成（基于 [917Dhj/DeepPaperNote](https://github.com/917Dhj/DeepPaperNote) 修改），每篇走两轮：

1. **第 1 轮：原版精读**。取 PDF、按章节抽原文、逐张审图表，写出结构化笔记并通过引用与格式检查。
2. **第 2 轮：多轮追问与叙事修改**。先列出读者需要的知识点，再对着原文追问细节（答不上的写“论文未说明”），然后对每个核心结论找最强的另一种解释；最后按“背景 → 核心观点 → 实验 → 深入分析”重写，并核对每个数字。

两轮各自评分，评分前保存当时笔记的快照和哈希，记录在每篇目录的 `scorecard.json` 与 `review_rounds/` 中。

### 目录结构

```
docs/                     # GitHub Pages：精读网页
  index.html
  papers/*.html
DeepPaperNote_output/
  手术数据集/<论文>/
    <论文>.md             # Markdown 精读笔记
    <论文>.html           # 图文解读网页（单文件，图片内嵌）
    reading_report.md     # 网页文稿
    insight_pass.json     # 多轮追问记录
    scorecard.json        # 两轮自评记录
    review_rounds/        # 每轮评分时的快照
    images/
.claude/skills/deeppapernote/   # 生成精读的 skill
```

### 自己读一篇

在仓库根目录启动 Claude Code，说：

```
读这篇论文并生成深度笔记：arXiv:xxxx.xxxxx，输出中文，保存到工作区
```
