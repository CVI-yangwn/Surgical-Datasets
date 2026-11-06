---
tags:
  - papers/手术数据集
aliases:
  - "SurgBench"
  - "SurgBench-P"
  - "SurgBench-E"
date: 2025-06-09
arxiv_id: 2506.07603
---

# SurgBench: A Unified Large-Scale Benchmark for Surgical Video Analysis

## 核心信息

- 标题: SurgBench: A Unified Large-Scale Benchmark for Surgical Video Analysis
- 标题翻译: SurgBench：面向手术视频分析的统一大规模基准
- 作者: Jianhui Wei, Zikai Xiao, Danyu Sun, Luqi Gong, Zongxin Yang, Zuozhu Liu, Jian Wu
- 机构: 浙江大学; 之江实验室; 哈佛大学; 浙江省医学影像人工智能重点实验室
- 发表时间: 2025-06-09(arXiv v1),本笔记依据 v2(2025-06-16)
- 发表渠道: arXiv 预印本(cs.CV)
- arXiv: 2506.07603
- 论文链接: https://arxiv.org/abs/2506.07603
- 代码 / 项目: 论文称代码可申请获取,未给出公开链接
- 数据 / 资源: 论文称数据可申请获取,未给出公开链接
- 论文类型: 基准与数据集论文(benchmark_or_dataset)

## 原文摘要翻译

手术视频理解对于实现术中自动决策、技能评估和术后质量改进至关重要。然而,手术视频基础模型的发展仍受制于缺少可用于预训练和系统评测的大规模、多样化数据集。

本文提出 SurgBench,一个统一的手术视频基准框架,由预训练数据集 SurgBench-P 和评测基准 SurgBench-E 组成。

SurgBench 广泛覆盖多种手术场景:SurgBench-P 包含 22 种术式、11 个专科的 5300 万帧;SurgBench-E 在六个类别(阶段分类、摄像机运动、器械识别、疾病诊断、动作分类和器官检测)上提供稳健评测,共 72 个细粒度任务。

大量实验表明,现有视频基础模型难以泛化到多样的手术视频分析任务,而在 SurgBench-P 上预训练能带来显著的性能提升,并对未见过的术式和模态有更好的跨域泛化。我们的数据集和代码可申请获取。

## 创新点

1. 把 16 个来源(15 个公开数据集、1 个私有数据集)统一成一个预训练语料。所有视频统一为 H.264 编码、短边 320、帧率 20 到 30 FPS,再切成 10 秒片段。论文称它覆盖 11 个专科、22 种术式和腹腔镜、内镜、机器人、开放四种模态,比 Endo-FM、GSViT、Surg-3M 的 3 到 5 个专科更广。这一步的价值在于给手术视频自监督预训练提供了格式一致的输入。
2. 把带标签的 9 个来源重新切成 1 到 10 秒的标注片段,组织成 6 个类别、10 个子类、72 个标签的分类体系(论文称 6C-10S-72T),共 23,004 个片段。这样同一个模型可以在阶段、器械、病变、动作、摄像机运动和器官六类问题上一起评测,而不是各个数据集各用一套协议。
3. 用 VideoMAE 在 SurgBench-P 上继续预训练,得到 SurgMAE 的标准版与大模型版,并在冻结骨干只训分类头的设定下与 Kinetics 预训练的 VideoMAE、随机初始化对比,作为这个基准的首个参考结果。

## 一句话总结

SurgBench 把 16 个手术视频来源统一切片,组成约 5300 万帧的预训练集和 72 个标签、23,004 个片段的分类评测集;在它上面继续预训练的 VideoMAE 在线性探测下平均 Top-1 从 0.378 升到 0.448,但规模数字前后不一致,预训练与评测同源,数据也只能申请获取。

## 研究问题

手术视频分析可以支持术中决策、技能评估和术后质量改进。通用视频基础模型靠数百万片段、数 TB 的数据学到可迁移的表示,论文想把这条路线搬到手术视频上。

论文认为阻碍在数据。已有的手术预训练和评测数据有三个短板:

- 病种单一。多数数据集只针对一种疾病,例如结直肠癌。
- 术式和专科窄。主要是腹腔镜胆囊切除和机器人前列腺切除等微创手术,开放手术和非标准术式很少。
- 任务孤立。常见的是单一术式的阶段识别,或单独的器械识别,缺少覆盖多个时间和语义维度的统一评测。

论文要回答的问题是:能否用现有公开数据拼出一个覆盖面更广的预训练集和统一的多任务评测集,并证明在它上面预训练比用自然视频预训练更好。

## 数据与任务定义

### 数据来源

论文收集了 16 个来源,编号 S1 到 S16。表 2 把它们分成两组:S1 到 S7 没有可用标签,只进预训练集;S8 到 S16 既贡献预训练帧,也贡献评测帧。

![Table 2](images/page_004_fig_table_2_review.png)
*论文原图编号：Table 2。16 个来源的病种、术式、任务类型、预训练帧数和评测帧数。放在这里是因为虚线把只用于预训练的 S1 到 S7 与带评测帧的 S8 到 S16 分开,一眼能看出 AVOS 一个来源的帧数占比。*

几个关键事实:

- AVOS(S1)是从 YouTube 收集的开放手术视频,贡献 28,473,879 个预训练帧,占预训练帧合计 56,062,458 的一半以上。
- 私有数据(S16)是腹腔镜右半结肠切除,来自中国三家三甲医院,按 6 个阶段标注。原视频切成 30 秒再 3 倍加速压成 10 秒,分辨率 1920 × 1080、30 fps。
- 许可限制:AVOS、SimSurgSkill2021、AIxSuture 的许可禁止修改或再分发,只用于预训练,不随评测集发布。

### 规模统计

论文给出的规模数字:

| 口径 | 片段 | 帧 | 时长 |
|---|---|---|---|
| 全库 | 225,250 | 59,742,875 | 575 小时 |
| SurgBench-P | 202,246 | 摘要称 53M | 538 小时 |
| SurgBench-E | 23,004 | 表 2 合计 3,680,417 | 论文未说明 |

全库帧数恰好等于表 2 的预训练帧合计加评测帧合计。

### 分类体系

SurgBench-E 的 72 个标签按表 3 组织成 10 个子类,编码 T1 到 T10:

![Table 3](images/page_006_fig_table_3_review.png)
*论文原图编号：Table 3。6C-10S-72T 分类体系。放在这里是因为后面所有结果都按 T1 到 T10 报告,需要先知道每个编码对应哪个子类、几个标签、来自哪个来源。*

| 编码 | 子类 | 标签数 | 来源 |
|---|---|---|---|
| T1 | 子宫切除阶段 | 7 | AutoLaparo |
| T2 | 右半结肠切除阶段 | 6 | 私有数据 |
| T3 | 腹腔镜胆囊切除阶段 | 12 | CholecT50、EndoVis 2019 |
| T4 | 摄像机运动 | 7 | AutoLaparo |
| T5 | 器械识别 | 2 | CholecT50 |
| T6 | 消化道病变诊断 | 19 | Hyper-Kvasir、Colonoscopic-web、Kvasir-Capsule |
| T7 | 结肠息肉检测 | 2 | LDPolypVideo |
| T8 | 内镜手术动作 | 2 | CholecT50 |
| T9 | 机器人教学手术动作 | 13 | JIGSAWS |
| T10 | 器官检测 | 2 | CholecT50 |

所谓“72 个任务”实际是 72 个类别标签。T5、T8、T10 都只有两个标签:器械是抓钳与电钩,动作是牵拉与分离,器官是胆囊与肝脏。

> [!figure] Table 7 72 个标签的说明(第一部分)
> 建议位置：数据与任务定义
> 放置原因：列出每个标签的名字,可用来核对各子类的标签。
> 当前状态：保留占位；自动视觉质量检查已拒绝该裁图。

> [!figure] Table 8 72 个标签的说明(第二部分)
> 建议位置：数据与任务定义
> 放置原因：和第一部分一起构成完整的标签清单。
> 当前状态：保留占位；自动视觉质量检查已拒绝该裁图。

### 标签分布

![Figure 3](images/page_005_fig_figure_3_review.png)
*论文原图编号：Figure 3。SurgBench-E 训练与测试集每个标签的样本数,按频率排序。放在这里是因为它显示最多的标签有约 1300 个样本,尾部标签只有十几个,训练与测试分布接近。*

论文称标签分布呈长尾,并认为这与真实临床一致。

## 方法主线

这是基准论文,方法主线是数据构建流程和评测协议;模型直接用 VideoMAE。

### 构建流程

1. 统一编码:所有视频转为 H.264,短边缩放到 320 并保持宽高比,帧率统一到 20 到 30 FPS;网络输入为 224 × 224。
2. 预训练切片:无标签视频直接切成 10 秒片段。
3. 评测切片:带标签视频切成 1 到 10 秒的片段,每个数据集的切法不同,附录逐一说明。例如 CholecT50 切成 5 秒、10 fps;Hyper-Kvasir 与 Kvasir-Capsule 切成 5 秒。
4. 划分:评测片段按 5:5 分成训练与测试,同一视频的片段只能出现在一侧。
5. 平衡:通过调整片段时长、下采样多数标签、删除稀少标签,把不平衡因子控制在 10 以内。一个片段对应多个标签时,拆成多个单标签样本,并用 top-k 准确率评测。

![Table 6](images/page_013_fig_table_6_review.png)
*论文原图编号：Table 6。11 个专科、22 种术式及其来源编号。放在这里是因为它是“覆盖面广”这一主张的唯一依据,可以逐行核对每个术式由哪些来源提供。*

### 机制流程

1. 输入 16 个来源的原始视频,统一编码、分辨率和帧率,输出格式一致的视频。
2. 输入无标签部分,切成 10 秒片段,经四阶段精炼(收集、过滤大来源、上采样少数来源、上下采样对齐评测分布)得到 39,807 个片段,送入 VideoMAE 继续预训练,输出 SurgMAE-CPT。
3. 输入带标签部分,切成 1 到 10 秒片段,按视频 5:5 划分并控制不平衡,输出 SurgBench-E 的 23,004 个片段与 72 个标签。
4. 冻结 SurgMAE-CPT 骨干,只训练分类头,在 T1 到 T10 上输出 Top-1 与 Top-3 准确率。

![Figure 1](images/page_003_fig_figure_1_review_repair1.png)
*论文原图编号：Figure 1。SurgBench 的数据构建流程。放在这里是因为它把数据来源、原始片段、SurgBench-P 与 SurgBench-E 的拆分以及 10 个子类的样本数画在一张图上。*

### 继续预训练

从 Kinetics-400 预训练的 VideoMAE 出发继续训练。

- 目标:按 VideoMAE 的做法遮盖时空“管”状图块并重建,遮盖比例 0.9。
- 标准版:ViT-Base 编码器加 4 层 Transformer 解码器,有效批大小 512(每卡 64)。
- 大模型版:ViT-Large 编码器加 12 层 Transformer 解码器,有效批大小 256(每卡 32)。
- 共同设置:每个片段 16 帧,时间采样率 4;AdamW,$\beta_1=0.9$,$\beta_2=0.95$。
- 算力:8 张 A100,标准版训 54 个 epoch,大模型版训 38 个 epoch,两者合计约一周。

### 评测协议

评测时冻结骨干,只训练分类头,也就是线性探测。

- 标准版:AdamW,$\beta_1=0.9$,$\beta_2=0.99$,学习率 $10^{-3}$,批大小 64。
- 大模型版:学习率 $2\times10^{-3}$,批大小 16。
- 都训 100 个 epoch,8 张 RTX3090,约 14 小时收敛。

指标是 top-k 准确率:

$$\mathrm{Acc@}k=\frac{1}{M}\sum_{m=1}^{M}\mathbb{1}\left[y_m\in\mathrm{Top}_k(\hat{p}_m)\right]$$

其中 $M$ 是测试样本数,$y_m$ 是真值标签,$\mathrm{Top}_k(\hat{p}_m)$ 是预测概率最高的 $k$ 个类别。

论文报告 $k=1$ 和 $k=3$ 两档。

## 关键结果

### 与已有预训练语料的比较

![Table 1](images/page_002_fig_table_1_review.png)
*论文原图编号：Table 1。已有手术视频预训练数据与 SurgBench 的比较。放在这里是因为论文的“覆盖更广”主张来自这张表。*

| 数据 | 专科 | 术式 | 帧 | 评测集 |
|---|---|---|---|---|
| Endo-FM | 3 | 3 | 5M | 无 |
| GSViT | 3 | 28 | 70M | 无 |
| Surg-3M | 5 | 35 | 3M | 无 |
| SurgBench | 11 | 22 | 53M | 有,72 个标签 |

SurgBench 在专科数和是否配评测集上领先;术式数少于 Surg-3M 和 GSViT,帧数少于 GSViT。

### 主结果

![Table 4](images/page_007_fig_table_4_review.png)
*论文原图编号：Table 4。四个模型在 T1 到 T10 上的 Top-1 与 Top-3 准确率。放在这里是因为它是全文唯一的数值主结果表。*

| 子类 | 随机初始化 | VideoMAE | SurgMAE | SurgMAE(L) |
|---|---|---|---|---|
| T1 子宫切除阶段 | 0.000 | 0.125 | 0.185 | 0.182 |
| T2 右半结肠切除阶段 | 0.364 | 0.423 | 0.440 | 0.493 |
| T3 胆囊切除阶段 | 0.126 | 0.379 | 0.399 | 0.422 |
| T4 摄像机运动 | 0.000 | 0.298 | 0.293 | 0.306 |
| T5 器械识别 | 0.395 | 0.287 | 0.319 | 0.324 |
| T6 消化道病变 | 0.413 | 0.569 | 0.645 | 0.666 |
| T7 结肠息肉 | 0.003 | 0.374 | 0.561 | 0.739 |
| T8 内镜手术动作 | 0.000 | 0.005 | 0.015 | 0.020 |
| T9 机器人教学动作 | 0.003 | 0.102 | 0.475 | 0.627 |
| T10 器官检测 | 0.000 | 0.122 | 0.200 | 0.279 |
| 平均 Top-1 | 0.229 | 0.378 | 0.448 | 0.487 |
| 平均 Top-3 | 0.478 | 0.652 | 0.731 | 0.788 |

上表各子类为 Top-1,最后一行是 Top-3 平均值。

继续预训练后,标准版平均 Top-1 比 VideoMAE 高 7 个点,Top-3 高 7.9 个点。

提升主要来自 T9 和 T7;T4、T8 几乎不变,论文也承认这两项没有改善。大模型版再高 3.9 和 5.7 个点。

### 训练过程与数据质量

![Figure 2](images/page_005_fig_figure_2_review_repair1.png)
*论文原图编号：Figure 2。在各来源数据上微调 VideoMAE 标准版的准确率曲线。放在这里是因为论文用这些上升的曲线论证评测集质量,而图中 Endovis2019、CholecT50、AutoLaparo 三条曲线停在很低的水平。*

论文用训练曲线平稳上升来说明数据质量可靠。预训练四个阶段之间损失曲线不连续,最后一个阶段损失几乎不降,但下游准确率仍在上升。

### 分布外与混合预训练

![Figure 7](images/page_008_fig_figure_7_review_repair1.png)
*论文原图编号：Figure 7。LapGyn 事件识别任务上的微调曲线。放在这里是因为它是论文唯一的分布外实验。*

LapGyn 来自妇科腹腔镜手术,不在 SurgBench-P 中。SurgMAE 最终准确率 84.23%,VideoMAE 81.54%,高 2.69 个点,收敛也更快。

![Figure 8](images/page_009_fig_figure_8_review_repair1.png)
*论文原图编号：Figure 8。先用 JIGSAWS 与 CholecT50 混合数据继续预训练,再分别在两者上微调的曲线。放在这里是因为它是论文“末阶段分布对齐下游任务”这一假设的唯一对照。*

两个数据集上,两种继续预训练模型都高于 VideoMAE。混合预训练版前期收敛更快,最终准确率与标准版接近。

## 深度分析

### 这个基准真正测到什么

SurgBench-E 测的是冻结特征上的片段级分类。它不评测分割、检测或时序定位;“器官检测”与“息肉检测”在这里都是片段级二分类。72 这个数是标签数,真正独立的分类问题只有 10 个。

### 二分类子任务的数字说明分类头不是逐子任务的

T5、T7、T8、T10 各只有 2 个标签。如果每个子类有自己的二分类头,Top-3 应恒为 1,Top-1 随机水平是 0.5。

但表 4 中这些子类的 Top-3 都低于 1,T8 的 Top-1 只有 0.000 到 0.020。

我的推断是分类头建在更大的标签空间上,可能是全部 72 个标签共用一个头,或者沿用 CholecT50 处理时 0 到 31 的统一映射。论文没有说明分类头的结构,这会直接影响如何读这些数字。

### 预训练与评测同源

S8 到 S16 同时贡献预训练帧和评测帧。论文没有说明预训练时是否排除了评测测试集所在的视频。如果没有排除,继续预训练的提升里有一部分来自模型在自监督阶段见过测试画面。

T7 和 T9 提升最大,它们的来源 LDPolypVideo 和 JIGSAWS 都在预训练集中。

### 规模数字前后不一致

- 摘要和结论称 SurgBench-P 有 53M 帧。
- 表 2 的预训练帧合计是 56,062,458。
- 第 4 节称预训练数据共 74.4M 帧。
- 全库 59,742,875 帧又被同时写成“共 60 million 帧”和 SurgBench-P 加 SurgBench-E 的总和。

53M、56,062,458 和 74.4M 三个预训练帧数无法互相换算,论文没有解释。

### 覆盖面主要来自一个来源

表 6 的 22 行里有 9 行只由 AVOS 一个来源覆盖,包括泌尿、神经、眼科、口腔颌面、骨科、耳鼻喉和小儿外科这 7 个专科的全部术式。AVOS 是 YouTube 开放手术视频,只有动作标签,只用于预训练,且有 330 个链接已失效。评测集只覆盖胆囊切除、子宫切除、右半结肠切除、消化道内镜和机器人缝合训练。

## 局限

- 论文自述:长尾分布使少数类难学;没有探索语言监督;手术视频基础模型的最优架构仍待研究。
- 所有结果只训练一次,没有随机种子、方差或显著性检验。
- 只评测线性探测,全参数微调下的差距论文未说明。
- 预训练是否排除评测测试视频,论文未说明。
- 分类头结构和 Top-3 在二类子任务上的算法,论文未说明。
- 规模数字在摘要、表 2、第 4 节之间不一致。
- 正文提到的逐类结果表显示为“Table ??”,没有给出。
- 数据和代码只能申请获取,没有公开链接;三个来源受许可限制不再分发。

## 我的笔记

- 用 SurgBench-E 报结果时,先确认分类头的标签空间,二类子任务的数字不能按二分类理解。
- 做手术视频预训练时,先从预训练语料里剔除评测测试视频,再比较线性探测结果。
- 引用规模数字时注明出处:53M、56,062,458、74.4M、59,742,875 来自不同位置。

后续问题:

- SurgBench-P 是否剔除了 SurgBench-E 测试集所在的视频?
- 全参数微调下 SurgMAE 与 VideoMAE 的差距还剩多少?
- 39,807 个精炼片段里各来源占多少?

## 引用

- Tong et al. (2022). VideoMAE: Masked autoencoders are data-efficient learners for self-supervised video pre-training. NeurIPS.
- Wang et al. (2023). Foundation model for endoscopy video analysis via large-scale self-supervised pre-train. MICCAI.
- Schmidgall et al. (2024). General surgery vision transformer: A video pre-trained foundation model for general surgery. arXiv.
- Che et al. (2025). Surg-3M: A dataset and foundation model for perception in surgical settings. arXiv:2503.19740.
- Goodman et al. (2024). Analyzing surgical technique in diverse open surgical videos with multitask machine learning. JAMA Surgery.
- Nwoye et al. (2022). Rendezvous: Attention mechanisms for the recognition of surgical action triplets in endoscopic videos. Medical Image Analysis.
- Wang et al. (2022). AutoLaparo: A new dataset of integrated multi-tasks for image-guided surgical automation in laparoscopic hysterectomy. MICCAI.
- Leibetseder et al. (2018). LapGyn4: A dataset for 4 automatic content analysis problems in the domain of laparoscopic gynecology. MMSys.
- Ahmidi et al. (2017). A dataset and benchmarks for segmentation and recognition of gestures in robotic surgery. IEEE TBME.
