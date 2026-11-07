---
tags:
  - papers/手术数据集
aliases:
  - "SurgMotion"
  - "SurgMotion-15M"
  - "SurgMotion 手术视频基础模型"
date: 2026-02-05
arxiv_id: 2602.05638
---

# SurgMotion: A Video-Native Foundation Model for Universal Understanding of Surgical Videos

## 核心信息

- 标题: SurgMotion: A Video-Native Foundation Model for Universal Understanding of Surgical Videos
- 标题翻译: SurgMotion：面向手术视频通用理解的视频原生基础模型
- 作者: Jinlin Wu, Felix Holm, Chuxi Chen, An Wang, Yaxin Hu, Xiaofan Ye, Zelin Zang, Miao Xu, Lihua Zhou, Huarui Wu, Huai Liao, Danny T. M. Chan, Ming Feng, Wai S. Poon, Hongliang Ren, Dong Yi, Nassir Navab, Gaofeng Meng, Jiebo Luo, Hongbin Liu, Zhen Lei
- 机构: 香港科学创新研究院人工智能与机器人中心; 慕尼黑工业大学 CAMP; 香港中文大学; 中国科学院大学; 中国科学院自动化研究所; 香港大学深圳医院; 中山大学附属第一医院; 北京协和医院; 联影手术（United Imaging Surgical） 等
- 发表时间: 2026-02-05（arXiv v1，本文据 v5 阅读）
- 发表渠道: arXiv 预印本（cs.CV）
- arXiv: 2602.05638
- 论文链接: https://arxiv.org/abs/2602.05638
- 代码 / 项目: https://github.com/CAIR-HKISI/SurgMotion ; https://surgmotion.cares-copilot.com/
- 数据 / 资源: 预训练权重 https://huggingface.co/CAIR-HKISI/SurgMotion ；SurgMotion-15M 语料本身未发布
- 论文类型: 方法论文（AI_method），附带预训练语料汇编

## 原文摘要翻译

基础模型推动了手术视频分析的发展，但现有方法主要依赖像素级重建目标，把模型容量浪费在烟雾、镜面反光和液体流动等低层视觉细节上，而不是手术理解所需的语义结构。我们提出 SurgMotion，一个视频原生的基础模型，把学习范式从像素级重建转向潜空间运动预测。

该模型基于视频联合嵌入预测架构（V-JEPA），针对手术视频提出三项关键技术：1）运动引导的潜空间掩码预测，优先关注语义上有意义的区域；2）时空亲和自蒸馏，强化关系一致性；3）时空特征多样性正则（SFDR），防止纹理稀疏的手术场景中出现表征坍塌。

为支持大规模预训练，我们汇编了 SurgMotion-15M，这是迄今最大的手术视频数据集，包含来自 50 个来源、覆盖 13 个器官的 3,658 小时视频。

在 17 个基准上的大量实验表明，SurgMotion 在手术工作流识别（EgoSurgery 上 F1 提升 14.6%，PitVis 上提升 10.3%）、动作三元组识别（CholecT50 上 mAP-IVT 达 39.54%）、技能评估、息肉分割和深度估计上显著优于最先进方法。这些结果使它成为通用、面向运动的手术视频理解的新标准。代码和项目资源已在代码托管平台和项目网站发布。

## 创新点

1. 运动引导的潜空间掩码预测。在 V-JEPA 的掩码潜空间回归上，按像素空间的时间差分与空间邻域差分给每个被掩码的管状词元 打运动分，只取 Top-K（K=3）个运动最强的词元 做加权 ℓ1 回归。作用是把监督集中到器械与组织交互区域，而不是平均分摊到大片静止背景上。
2. 掩码词元 之间的亲和自蒸馏。学生预测与 EMA 教师目标各自在掩码词元 内算 softmax 相似度分布，用 KL 对齐。只在掩码集合内算，是为了不让可见的背景词元 主导关系结构。
3. 时空特征多样性正则（SFDR）。对批内预测潜向量逐维标准差加铰链惩罚 $\max(0,\sigma_0-\sigma_d)$，针对脂肪、光滑脏器表面等低纹理画面里的维度坍塌。
4. SurgMotion-15M 预训练语料。汇编 12 个专科、表 1 列名的 15 个公开数据集加网络与机构视频，共 3,658 小时，并按专科与数据集双重反比采样平衡分布。
5. 统一评测 13 个基础模型。在冻结骨干、相同注意力探测头和相同超参搜索下，比较 17 个下游基准，覆盖工作流、动作、三元组、技能、分割与深度。

## 一句话总结

SurgMotion 在 V-JEPA 上加入运动加权、掩码亲和蒸馏和方差正则，用 3,658 小时多专科手术视频预训练，冻结骨干后在 8 个工作流识别集上全部第一（如 PitVis F1 75.53 对 GastroNet 65.22），但论文没有任何消融，收益无法拆分到损失设计、数据规模或 64 帧长输入。

## 研究问题

手术视频自监督预训练的主流做法沿用 MAE、VideoMAE 的像素重建。作者认为这在手术场景里目标错位：烟雾、镜面反光、液体流动带来大量不可预测的高频像素变化，模型容量被花在重建这些噪声上，而真正有用的语义（器械与组织的交互运动）在画面中稀疏。

第二个问题是数据面窄。Cholec80 只覆盖胆囊切除，PitVis 只覆盖垂体手术，已有手术基础模型的预训练语料多在几十到一千多小时，且偏向单一术式或内镜，难以跨专科、跨机构泛化。

![Figure 1](images/page_002_fig_figure_1_review.png)
*论文原图编号：Figure 1。五个子图依次为：语料按器官的视频数与时长；与已有手术预训练语料的时长对比；预训练时长与工作流平均 F1 的跨模型散点；预训练思路示意；各任务雷达图。放在这里是因为第二、第三个子图正是论文“数据越大越好”这一论点的依据。*

作者据此提出四条需求：关注运动语义而不是像素；在时间上保持关系稳定；在纹理稀疏场景中保持特征多样；扩大数据覆盖。SurgMotion 分别用三个损失项和一个汇编语料回应。

## 数据与任务定义

### 预训练语料 SurgMotion-15M

![Table 1](images/page_006_fig_table_1_review.png)
*论文原图编号：Table 1。SurgMotion-15M 的数据来源与规模，按专科列出来源、视频数、小时数与公开或私有属性。放在这里是因为它是判断语料构成与偏斜的唯一明细。*

- 神经外科（垂体、颅脑、脊柱）占 2,860.85 小时，来源为 PitVis 加网络与机构视频，属性为 Mixed，是语料的绝对主体。
- 其余专科多为一两个公开数据集。普外科 AVOS 125.16 小时；眼科 OphNet 加 CATARACTS 230.76 小时；胃部手术 MultiBypass140 加 CoPESD 252.10 小时。
- 胆囊切除 Cholec80 加 M2CAI-2016 共 77.51 小时；结肠镜来自 EndoFM 语料，30,000 段只有 45.00 小时。
- 唯一完全私有的是机构支气管镜 50.00 小时；EgoSurgery 乳腺手术 10.55 小时标为 Mixed。
- 所有视频统一 1 fps，短边缩放到 256，再随机裁成 224 × 224。

### 下游任务与指标

- 工作流识别 8 个集，报告准确率、F1 与 Jaccard 指数。腹腔镜三集为 Cholec80、M2CAI-2016、AutoLaparo。
- 其余五集为开放手术 EgoSurgery、经鼻垂体 PitVis、颅脑神经外科 Atlas-Neurosurgical。
- 再加眼科 OphNet 与肝切除 PMLR50。
- 动作识别 3 个集：SurgicalActions160、AVOS、PolypDiag，报告 Acc、F1。
- 三元组识别：CholecT50，分别报告器械、动词、目标三个分量的平均精度，以及它们两两和三者组合的平均精度（最难的是 AP-IVT）。
- 技能评估：JIGSAWS，预测全局技能分，报告 MAE 和 Spearman。
- 息肉分割 5 个集，报告 Dice 与平均绝对误差。分布内为 Kvasir 与 CVC-ClinicDB。
- 分布外为 CVC-300、CVC-ColonDB 与 ETIS。
- 深度估计：C3VD，报告 RMSE、AbsRel、SqRel、δ < 1.1。

## 方法主线

### 机制流程

![Figure 2](images/page_007_fig_figure_2_review.png)
*论文原图编号：Figure 2。左为预训练：掩码片段经在线编码器与预测器推断被掩码管状词元 的潜表示，EMA 编码器看完整片段给出停梯度目标，三个损失共同监督；右为冻结编码器加注意力探测头的下游评测。放在这里是因为它对应下面四步。*

1. 管状词元化与掩码。输入为 T 帧片段，每帧切成 16 × 16 块，同一空间位置跨全部帧构成一个管状词元，词元数等于两个方向块数之积。按在 0.75 到 0.95 之间均匀采样的掩码率，随机分成可见集与掩码集，送入两支编码器。
2. 在线支与 EMA 支编码。上下文编码器只编码可见词元，得到可见潜表示。每个掩码位置用共享查询加位置编码作为占位，与可见潜表示一起送入预测器，输出掩码位置的预测潜表示。
   EMA 编码器编码完整片段得到目标潜表示，动量 0.99925，全部停梯度。两者都送入损失。
3. 三项损失监督掩码预测。运动加权 ℓ1 回归、掩码内亲和 KL 蒸馏、批内逐维方差铰链，加权求和后反传到在线编码器与预测器。
4. 冻结后探测。预训练结束后冻结编码器，接 4 层、16 头的注意力探测头，同时训练 16 组不同超参的探测头，报告最好一组。所有对比模型走同一流程。

### 训练目标

运动分数由时间差分与空间邻域差分组成：

$$g_i=\frac{1}{T-1}\sum_{t=1}^{T-1}\|x_{t+1,i}-x_{t,i}\|_1+\frac{1}{T}\sum_{t=1}^{T}\frac{1}{|\mathcal N(i)|}\sum_{j\in\mathcal N(i)}\|x_{t,i}-x_{t,j}\|_1$$

在掩码集中取 Top-K（K=3）得到 $I_h$，用 $\gamma=2$ 的 softmax 得权重 $w_i$，损失为

$$\mathcal L_{motion}=\sum_{i\in I_h}(1+w_i)\,\|\hat z_i-\mathrm{sg}(z^E_i)\|_1$$

亲和蒸馏在掩码词元之间用温度 0.1 分别计算学生与教师的相似度分布，再用 KL 散度对齐：

$$\mathcal L_{st}=\frac{1}{|I_m|}\sum_{i}\sum_{j}a^E_{i,j}\log\frac{a^E_{i,j}}{\hat a_{i,j}}$$

SFDR 对批内预测潜向量逐维标准差加铰链：

$$\mathcal L_{var}=\frac{1}{D}\sum_{d=1}^{D}\max(0,\sigma_0-\sigma_d)$$

总目标为：

$$\mathcal L=\mathcal L_{motion}+0.1\,\mathcal L_{st}+0.3\,\mathcal L_{var}$$

论文未说明阈值 $\sigma_0$ 的取值，复现时需要查代码。

### 关键实现细节

- 两阶段训练：第一阶段 T=16 帧、200 轮、学习率 5×10⁻⁴；第二阶段从第一阶段权重继续，T=64 帧、80 轮。
- 采样权重 $w(x)\propto 1/(N_d|D_s|)$，使每个专科、每个数据集的采样质量相等。
- AdamW，权重衰减 0.04，余弦学习率；4 张 H800，单卡批量 64 与 16，全局批量 256 与 64。
- 骨干规模正文未写；仓库给出 ViT-L 与 ViT-G 两个权重，图 1(c) 中 SurgMotion 标为约 1.01B 参数。

## 关键结果

### 工作流识别

![Table 2](images/page_010_fig_table_2_review_repair1.png)
*论文原图编号：Table 2。腹腔镜工作流识别，三个胆囊切除或子宫切除数据集上的准确率、F1 与 Jaccard。放在这里是因为它是与最强基线差距最小、最常用的一组数据集。*

![Table 3](images/page_011_fig_table_3_review.png)
*论文原图编号：Table 3。开放、经鼻与神经外科工作流识别：EgoSurgery、PitVis、Atlas-Neurosurgical。放在这里是因为论文的两个摘要级数字都出自这张表。*

![Table 4](images/page_011_fig_table_4_review.png)
*论文原图编号：Table 4。眼科与肝脏手术工作流识别：OphNet 与 PMLR50。放在这里是因为它补充了腹腔镜以外的两个专科。*

| 数据集 | SurgMotion F1 | 最强基线 F1 | 最强基线 |
|---|---|---|---|
| Cholec80 | 84.17 | 81.22 | GastroNet |
| AutoLaparo | 78.73 | 74.55 | DINOv3-L |
| M2CAI-2016 | 82.91 | 74.56 | DINOv3-L |
| EgoSurgery | 50.72 | 36.34 | DINOv3-H |
| PitVis | 75.53 | 65.22 | GastroNet |
| Atlas-Neurosurgical | 65.26 | 63.19 | DINOv3-L |
| OphNet | 51.22 | 39.99 | DINOv3-L |
| PMLR50 | 85.65 | 68.68 | VideoMAE-L |

8 个集上 SurgMotion 三项指标全部第一。腹腔镜三集与 Atlas 上的领先是几个点，EgoSurgery、PitVis、OphNet、PMLR50 上领先超过 10 个点。

![Figure 3](images/page_017_fig_figure_3_review.png)
*论文原图编号：Figure 3。12 个代表病例的逐帧阶段预测色带，与真值和五个基线对比，右侧为单病例准确率。放在这里是因为它显示 SurgMotion 的提升主要体现为更少的阶段碎片化。*

### 动作、三元组与技能

![Table 5](images/page_012_fig_table_5_review_repair1.png)
*论文原图编号：Table 5。腹腔镜动作、开放手术动作与结肠镜诊断三个集上的准确率与 F1。放在这里是因为它同时显示了 SurgMotion 优势最大和最小的情况。*

- SurgicalActions160 准确率 75.63，DINOv3-H 为 75.00，几乎持平。
- AVOS 的 F1 为 66.32，DINOv3-H 为 45.12，这是动作识别中差距最大的一项。
- PolypDiag 准确率 98.81，GastroNet 为 98.75，已接近饱和。
- 多个基线在 AVOS 上给出完全相同的 48.34 / 8.15，像是退化为单一类别预测。

![Table 6](images/page_013_fig_table_6_review.png)
*论文原图编号：Table 6。CholecT50 三元组识别的分量 AP 与组合 AP。放在这里是因为论文用 AP-V 的提升支撑运动建模的论点。*

- AP-I 91.55、AP-V 57.72、AP-T 48.18、AP-IVT 39.54；DINOv3-L 分别为 87.16、53.90、43.44、36.85。

> [!figure] Table 7 JIGSAWS 技能评估
> 建议位置：关键结果
> 放置原因：它是技能评估的唯一数字来源。
> 当前状态：保留占位；自动裁切与表 6 是同一张图，身份不符，属于视觉缺陷，关键数字转写如下。

- SurgMotion 的平均绝对误差 2.649、Spearman 相关 0.770。
- 最强基线 GastroNet 为 3.5962 与 0.5002，误差降低约 26%。
- 表中 GSViT 与 Selfsupsurg 的相关系数记为 NaN，论文未说明原因。

### 稠密预测

> [!figure] Figure 4 息肉分割与结肠镜深度定性结果
> 建议位置：关键结果
> 放置原因：它是分割与深度两项稠密任务的定性证据。
> 当前状态：保留占位；子图 (a) 的说明文字夹在两块之间，底部 (b) 的说明被截断，属于视觉缺陷，无法在不破坏图体的情况下分离。

- 息肉分割（表 8）分布内两集：CVC-ClinicDB 的 Dice 为 0.8694，Kvasir 为 0.8919。Kvasir 上 DINOv3-H 为 0.9019，高于 SurgMotion。
- 分布外三集：CVC-300 为 0.9112，CVC-ColonDB 为 0.7985，ETIS 为 0.7798，三项都是最高。

![Table 9](images/page_015_fig_table_9_review.png)
*论文原图编号：Table 9。C3VD 结肠镜深度估计的 RMSE、AbsRel、SqRel 与 δ < 1.1。放在这里是因为它是唯一的几何任务。*

- RMSE 1.88，GastroNet 1.91、DINOv3-L 1.92；AbsRel 0.051；δ < 1.1 为 0.86。

## 深度分析

### 为什么有效

论文给出的解释是：潜空间回归不要求重建烟雾和反光，运动加权把梯度集中在器械附近，所以动词 AP-V 和工作流时序指标受益。这一解释与结果方向一致，但没有实验把它和另两个因素分开：语料从基线的几十到一千多小时扩到 3,658 小时，以及第二阶段 64 帧长输入。

### 收益分布说明了什么

差距最大的五个集是开放手术、垂体、眼科、肝切除和开放手术动作，这些都是图像级基线训练时少见的专科或视角。差距最小的胆囊切除、息肉诊断和 Kvasir，恰是已有模型反复训练过的腹腔镜和结肠镜。这更像数据覆盖的效应，而不只是目标函数的效应。

### 复现注意点

- 探测协议是 16 组超参同时训练、报告最好一组；在哪个划分上选最好论文未说明，若在测试集上选，分数会偏乐观。
- 下游数据集与预训练来源大量重叠。
- 只报单次结果，无方差。

## 局限

- 没有消融：三个损失、Top-K、两阶段训练各自的贡献都未知。
- 没有数据规模对照：图 1(c) 是不同模型之间的散点，不是同一模型的规模扫描。
- SurgMotion-15M 没有发布，神经外科部分包含网络与机构视频。
- 只评测冻结探测，没有全量微调。
- 作者承认部分术式和机构仍然覆盖不足。

## 我的笔记

- 想用手术视频冻结特征时，SurgMotion 的 ViT-L、ViT-G 权重是目前覆盖专科最广的选择。
- 汇编多源医疗视频时，专科与数据集双重反比采样值得照搬。
- 用它的分数做对照前，要先确认测试视频是否在预训练来源里。

## 引用

- Wu, J., Holm, F., Chen, C., et al. SurgMotion: A Video-Native Foundation Model for Universal Understanding of Surgical Videos. arXiv:2602.05638, 2026.
- arXiv: https://arxiv.org/abs/2602.05638
- 代码: https://github.com/CAIR-HKISI/SurgMotion
- 项目页: https://surgmotion.cares-copilot.com/
- 权重: https://huggingface.co/CAIR-HKISI/SurgMotion
