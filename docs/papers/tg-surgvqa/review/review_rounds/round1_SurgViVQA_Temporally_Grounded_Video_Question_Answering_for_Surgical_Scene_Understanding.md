---
tags:
  - papers/手术数据集
aliases:
  - "SurgViVQA"
  - "REAL-Colon-VQA"
  - "结肠镜视频问答数据集"
date: 2025-11-05
arxiv_id: 2511.03325
---

# SurgViVQA: Temporally-Grounded Video Question Answering for Surgical Scene Understanding

## 核心信息

- 标题: SurgViVQA: Temporally-Grounded Video Question Answering for Surgical Scene Understanding
- 标题翻译: SurgViVQA:面向手术场景理解的时间对齐视频问答
- 作者: Mauro Orazio Drago, Luca Carlini, Pelinsu Celebi Balyemez, Dennis Pierantozzi, Chiara Lena, Cesare Hassan, Danail Stoyanov, Elena De Momi, Sophia Bano, Mobarak I. Hoque
- 机构: 米兰理工大学 DEIB; IRCCS Humanitas 研究医院; 伦敦大学学院 UCL Hawkes 研究所与计算机系; 曼彻斯特大学
- 发表时间: 2025-11-05(arXiv v1);本笔记依据 v3(2026-04-23)
- 发表渠道: arXiv 预印本(cs.CV);代码仓库首页另给出 IJCARS 期刊版 DOI 10.1007/s11548-026-03695-z,论文正文未写
- arXiv: 2511.03325
- 论文链接: https://arxiv.org/abs/2511.03325
- 代码 / 项目: https://github.com/madratak/SurgViVQA(论文只写"Dataset and code are available in our GitHub",没有给出地址;此仓库描述与论文标题一致,作者列表相同)
- 数据 / 资源: https://github.com/madratak/SurgViVQA/tree/main/REAL-Colon-VQA_annotations(问答标注公开;视频帧需另从 REAL-Colon 数据集获取);模型权重 https://huggingface.co/maurodrago/SurgViVQA-weights(公开,未设门槛)
- 论文类型: 方法论文,附带新数据集(AI_method)

## 原文摘要翻译

目的:手术领域的视频问答(VideoQA)希望让 AI 模型在时间上连贯的事件上推理,而不是在孤立的帧上推理,从而增强术中理解。现有方法只用静态图像特征,已有数据集也常常缺少时间标注,忽略了准确理解手术过程所需的动态信息。

方法:我们提出 SurgViVQA,一个把视觉推理从静态图像扩展到动态手术场景的手术视频问答模型。它用一个掩码视频-文本编码器融合视频和问题特征,捕捉运动、器械与组织交互等时间线索,再由一个微调后的大语言模型(LLM)解码成连贯的回答。为评测其性能,我们构建了 REAL-Colon-VQA,一个结肠镜视频数据集,包含运动类问题和诊断属性,还包含经过改写或语义变化的模板外问题,用来评测模型的鲁棒性。

结果:在 REAL-Colon-VQA 和公开的 EndoVis18-VQA 数据集上的实验表明,SurgViVQA 优于现有基于图像的 VQA 基准模型,并与一个微调后的视频 VLM 基线保持竞争。

具体来说,SurgViVQA 的关键词准确率在 REAL-Colon-VQA 上比 PitVQA 高 9%,在 EndoVis18-VQA 上也高 9%,同时取得最强的整体词汇和语义生成性能。一项针对问题的扰动研究进一步证实了模型更好的泛化性,以及对问题措辞变化的鲁棒性。

结论:SurgViVQA 和 REAL-Colon-VQA 数据集为手术视频问答中的时间感知理解提供了一个框架,使 AI 模型能够理解动态的手术过程。

## 创新点

1. 把视频编码器接到生成式问答上。作者把 VideoMAE 从片段级分类改为逐词元的时序编码,视频词元与问题词元通过 BLIP 的交叉注意力融合。
   融合结果交给 LoRA 微调的 GPT-2 或 Qwen 生成自由文本答案;此前的 SurgicalGPT、PitVQA 都只输入单帧。
2. 结肠镜视频问答数据集 REAL-Colon-VQA。在 REAL-Colon 的 6 段录像上逐帧标注内镜运动、器械、可见度、遮挡、冲洗和照明模式,再生成 5200 条与 8 帧片段绑定的问答。作者称这是第一个公开的结肠镜视频问答数据集。
3. 同一题给模板题和改写题两套。每条样本同时有模板内问法和模板外问法,答案相同,可以直接测题面换说法后模型会掉多少。每题还同时给短答案和长答案。
4. 系统比较五种时序编码器。在同一 GPT-2 解码器和训练协议下比较 X-CLIP、ViViT、TimeSformer、VideoMamba 和 VideoMAE,另外做了关键词加权损失的 λ 扫描。

## 一句话总结

SurgViVQA 用 8 帧视频输入替代单帧,在 REAL-Colon-VQA 上把关键词准确率从 PitVQA 的 54.13 提到 62.80,运动类问题上视频模型约 82 到 83、图像模型只有 42.00;但在 EndoVis18-VQA 上它的关键词准确率 48.27 明显低于 LoRA 微调的 InternVL3(70.31),模板外改写题上更降到 9.23。

## 研究问题

现有手术 VQA 模型和数据集都停在单帧上。SurgicalGPT 把视觉-文本嵌入接入 GPT-2 解码器,PitVQA 用 ViT 加交叉注意力文本编码器再接 GPT-2,两者都只看一帧,不能表达内镜前进还是后退、病灶往哪漂这类需要跨帧证据的问题。

数据集也有同样的问题。EndoVis18-VQA、PitVQA、Kvasir-VQA、SSG-VQA 多数缺少时间标注,而且测试题和训练题措辞几乎相同(模板内评测),模型可能靠题面文字就能答对,答案听起来通顺却没有给出关键临床信息。

论文还问了第三个问题:用 LoRA 微调一个通用视频 VLM 是否就够了,还是需要专门的时序手术问答架构。

## 数据与任务定义

### 数据来源

REAL-Colon-VQA 由 REAL-Colon 扩展而来。REAL-Colon 是公开的真实临床结肠镜视频数据集,病灶的部位、大小和组织病理来自其临床核实标签。论文正文没有写用了几段录像;GitHub 标注说明写明取自 6 段完整结肠镜操作,我检查的标注文件里视频编号为 002-001 到 002-006。

新增的帧级标注包括:内镜运动(前进、后退、退出)、器械(导管、圈套器、活检钳)、可见度、遮挡、冲洗和照明模式(白光或窄带成像 NBI)。标注由两名有内镜视频分析经验的非临床标注员完成,一名内镜专家监督,第三名标注员处理分歧。标注一致性指标,论文未说明。

### 片段构造

- 每条问答绑定一个 8 帧片段。原始视频 30 fps,每 4 帧取 1 帧(stride 4),片段跨度约 0.93 秒。
- 只有当对应条件在片段的多数帧中持续存在时,才把该问题分给这个片段。
- 作者有意只覆盖 1 秒内可观察的动态:内镜进退、病灶在屏幕上的短暂漂移、短时冲洗、照明切换和短暂遮挡。

![Fig 2](images/page_006_fig_fig_2_review.png)
*论文原图编号：Fig 2。两段 8 帧片段的样例:上面一题问内镜是否在后退(模板题与改写题各一),下面一题问画面中是哪种器械;每题都给长答案和短答案。放在这里是因为它直接展示了一条样本的完整字段。*

### 问题类别与规模

- 共 5200 条片段-问答,训练 4450 条,测试 750 条。
- 20 个问题类别,归入 6 个领域:器械存在与类型 10.58%,尺寸 2.88%,诊断(组织病理)2.88%,位置(解剖部位与屏幕位置)5.77%,操作记录(照明、可见度、冲洗、遮挡)46.15%,运动(内镜运动与病灶运动)31.73%。
- 问题由临床验证过的模板实例化,再改写成语义等价的变体。每题有短答案(如 yes、catheter、advancing)和长答案。

![Table 1](images/page_006_fig_table_1_review.png)
*论文原图编号：Table 1。五个手术 VQA 数据集在术式、是否视频、是否有模板外问题、是否有短答案,以及各类别题型数上的对比。放在这里是因为它是"唯一的视频、改写题、长短答案三者兼有"这一主张的依据。*

### EndoVis18-VQA 的使用方式

EndoVis18-VQA 来自 14 段肾切除视频的 2086 个场景,共 13790 条问答,答案属于 18 个离散类(1 个肾脏、13 个器械-组织交互、4 个器械位置)。官方划分训练 1560 帧 10574 条、验证 447 帧 3216 条。视频设置下,作者为每条问答构造 8 帧片段,只保留 8 个连续帧都存在、且与最后一帧标注对齐的样本。模板外评测使用文献 [14] 的扰动版本问题。

## 方法主线

### 机制流程

1. 输入 8 帧结肠镜片段,切成时空立方体词元,送入 VideoMAE 视频编码器;训练时按"管状"方式高比例掩码,同一空间位置在所有时刻一起被遮住。输出逐词元的视频嵌入,不再是片段级分类向量。
2. 输入问题文本,经 LLM 分词器后进入 BLIP 交叉注意力文本编码器;每个问题词元对全部时序视频特征做交叉注意力。输出融合后的视觉-文本嵌入。
3. 输入融合嵌入,送入冻结的因果 LLM(GPT-2 或 Qwen),只训练 LoRA 适配器。输出自回归生成的自由文本答案。
4. 训练时用 BCE 损失,可选对答案中的关键词词元加权 λ。

![Fig 1](images/page_004_fig_fig_1_review.png)
*论文原图编号：Fig 1。SurgViVQA 结构:8 帧输入经管状掩码视频编码器得到视频嵌入,问题经分词器与跨模态文本编码器融合,再由带 LoRA 层的冻结 LLM 生成答案;图例标出了冻结和微调部分。放在这里是因为它对应上面四步。*

### 管状掩码的作用

视频相邻帧高度冗余。若只随机遮住单个立方体,模型可以从相邻时刻同一位置抄回内容。管状掩码把同一位置的所有时刻一起遮掉,迫使模型从更远的语义上下文推断,作者认为这样学到的是器械交互和解剖变化,而不是低层的时间连续性。

### 关键词加权损失

$$\mathcal{L}_{WBCE}=\frac{1}{N}\sum_{i=1}^{N} w_i\,\mathrm{BCE}(y_i,\hat{y}_i),\qquad w_i=\begin{cases}\lambda & i\in K\\ 1 & i\notin K\end{cases}$$

$N$ 是答案的词元数,$K$ 是参考答案中的关键词集合,λ=1 即普通 BCE。动机是避免把 kidney 答成 lung 这类关键词错误。

### 关键实现细节

- VideoMAE 预训练用 16 帧,这里改为 8 帧,所以放开 patch embedding 层和最后的 LayerNorm,其余冻结。
- GPT-2 的 LoRA 加在 c_attn 和 c_proj 上;Qwen 的 LoRA 加在 q_proj、k_proj、v_proj、o_proj 上。
- 训练 60 轮,Adam,学习率 $2\times10^{-7}$,单卡 NVIDIA H100。
- 图像基线:SurgicalGPT、PitVQA 用官方代码重训。
- 零样本基线:InternVL3-1B、Qwen2.5-VL-3B、MedGemma、VideoLLaMA3,配一段描述手术环境的长提示。
- 微调视频基线:InternVL3 用 LoRA 在同一训练集上微调。
- Qwen 的具体型号和参数量、LoRA 的秩、批大小,论文未说明。

## 关键结果

指标:BLEU-4(BLE-4)、ROUGE-L(ROU-L)、METEOR(MET)衡量生成答案与参考答案的词汇和语义重合。

关键词准确率 K-ACC 衡量答案里是否出现正确的手术或解剖术语,作者把它作为最重要的临床指标。所有数字为百分比。

### 主结果与强基线

REAL-Colon-VQA(Table 2 上半):

| 模型 | 输入 | 模板内 BLE-4 | 模板内 MET | 模板内 K-ACC | 模板外 MET | 模板外 K-ACC |
|---|---|---|---|---|---|---|
| SurgicalGPT | 图像 | 14.93 | 52.36 | 33.33 | 50.49 | 46.67 |
| PitVQA | 图像 | 64.55 | 79.99 | 54.13 | 53.22 | 42.93 |
| InternVL3 零样本 | 视频 | 7.13 | 54.31 | 68.67 | 44.34 | 53.73 |
| InternVL3 + LoRA | 视频 | 64.88 | 76.42 | 59.07 | 54.37 | 51.77 |
| SurgViVQA(Qwen) | 视频 | 60.09 | 75.32 | 59.73 | 35.26 | 38.00 |
| SurgViVQA(GPT-2) | 视频 | 71.98 | 84.11 | 62.80 | 54.89 | 47.73 |

EndoVis18-VQA(Table 2 下半):

| 模型 | 输入 | 模板内 BLE-4 | 模板内 MET | 模板内 K-ACC | 模板外 BLE-4 | 模板外 K-ACC |
|---|---|---|---|---|---|---|
| PitVQA | 图像 | 81.73 | 83.28 | 40.35 | 17.57 | 9.73 |
| Qwen2.5-VL 零样本 | 图像 | 19.04 | 68.60 | 51.22 | 11.92 | 46.90 |
| InternVL3 + LoRA | 视频 | 33.99 | 83.67 | 70.31 | 6.27 | 56.42 |
| SurgViVQA(Qwen) | 视频 | 79.05 | 84.70 | 46.30 | 0.60 | 0.99 |
| SurgViVQA(GPT-2) | 视频 | 84.94 | 86.08 | 48.27 | 24.84 | 9.23 |

这两张表说明三件事:

- 对图像基线,SurgViVQA(GPT-2)在两个数据集模板内的四个指标都更高,K-ACC 比 PitVQA 高 8.67(REAL-Colon-VQA)和 7.92(EndoVis18-VQA),作者四舍五入写作"约 9%"。
- 对 LoRA 微调的 InternVL3,SurgViVQA 在语言重合指标上更高,但关键词准确率不总是更高:EndoVis18-VQA 模板内 70.31 对 48.27,模板外 56.42 对 9.23。作者把这解读为"专用架构在事实性与开放式生成之间更均衡",但若以 K-ACC 为主指标,这个结论在 EndoVis18-VQA 上不成立。
- 零样本 InternVL3 在 REAL-Colon-VQA 模板内 K-ACC 68.67,是所有模型中最高的,而它的 BLEU-4 只有 7.13。这说明通用视频模型能说出正确关键词,只是措辞与参考答案不同。

![Table 2](images/page_008_fig_table_2_review.png)
*论文原图编号：Table 2。两个数据集上基线、零样本、LoRA 微调视频模型与 SurgViVQA 在模板内和模板外的全部指标。放在这里是因为上面两张精简表都取自这里,完整列可在原表核对。*

### 模板外改写题

所有模型在模板外问题上都下降。结肠镜数据上,SurgViVQA(GPT-2)的 ROUGE-L 和 METEOR 仍是最高,K-ACC 从 62.80 降到 47.73。

肾切除数据上下降更剧烈:GPT-2 版本 K-ACC 9.23;Qwen 版本 BLEU-4 0.60、K-ACC 0.99,几乎完全失效。

零样本 Qwen2.5-VL 在同一组改写题上反而有 46.90。所以摘要中"对问题措辞变化更鲁棒"的说法,只在 REAL-Colon-VQA 的语言重合指标上成立。

![Fig 3](images/page_007_fig_fig_3_review.png)
*论文原图编号：Fig 3。一个"内镜是否在后退"的样例,各模型在模板题和改写题上的回答与正误。放在这里是因为它展示了图像模型在改写题上答偏、两个 SurgViVQA 版本都答对的典型情况;它只是单个样例。*

### 运动类与静态类问题

作者把 REAL-Colon-VQA 的模板内测试题分成需要跨帧证据的运动类和单帧可答的静态类(Table 3):

| 模型 | 总体 K-ACC | 运动类 K-ACC | 静态类 K-ACC |
|---|---|---|---|
| PitVQA(图像) | 54.13 | 42.00 | 58.55 |
| InternVL3(视频,零样本) | 68.67 | 82.00 | 63.82 |
| SurgViVQA(Qwen) | 59.73 | 83.00 | 51.27 |
| SurgViVQA(GPT-2) | 62.80 | 62.50 | 62.91 |

![Table 3](images/page_009_fig_table_3_review.png)
*论文原图编号：Table 3。REAL-Colon-VQA 模板内 K-ACC 按运动类与静态类分层。放在这里是因为它是"视频输入帮助运动类问题"最直接的证据。*

运动类题上,两个视频模型约 82 到 83,图像模型 42.00,差距约 40 个点,这是全文最清楚的时序证据。但 SurgViVQA 的 GPT-2 版本运动类只有 62.50,与静态类几乎一样;Qwen 版本运动类最好、静态类最差。同一架构换了解码器,运动类表现相差约 20 个点,说明"运动类题目受益"并不完全由视频编码器决定。运动类和静态类各有多少道测试题,论文未说明。

### 时序编码器消融

在 EndoVis18-VQA 模板内、相同 GPT-2 解码器和训练协议下(Table 4):

| 时序编码器 | BLEU-4 | ROUGE-L | METEOR |
|---|---|---|---|
| X-CLIP | 78.81 | 88.80 | 86.79 |
| ViViT | 78.27 | 86.89 | 84.02 |
| TimeSformer | 81.02 | 86.31 | 83.02 |
| VideoMamba | 84.47 | 89.06 | 85.64 |
| VideoMAE | 84.94 | 89.66 | 86.08 |

![Table 4](images/page_010_fig_table_4_review.png)
*论文原图编号：Table 4。五种时序编码器接 GPT-2 在 EndoVis18-VQA 模板内的五项语言指标。放在这里是因为它是"选 VideoMAE"这一设计的唯一依据。*

VideoMAE 在 BLEU-4 和 ROUGE-L 上最好,但 METEOR 低于 X-CLIP。

它与 VideoMamba 的 BLEU-4 只差 0.47。这张表没有 K-ACC,也没有在 REAL-Colon-VQA 上做,而后者才是有真正运动问题的数据集。

### 关键词加权的 λ 扫描

| λ | 模板内 BLE-4 | 模板内 K-ACC | 模板外 BLE-4 | 模板外 K-ACC |
|---|---|---|---|---|
| 1 | 84.94 | 48.27 | 24.85 | 9.23 |
| 10 | 83.92 | 49.03 | 27.91 | 11.47 |
| 50 | 80.16 | 46.83 | 12.38 | 12.08 |

![Table 5](images/page_010_fig_table_5_review.png)
*论文原图编号：Table 5。SurgViVQA(GPT-2)在 EndoVis18-VQA 上取 λ 为 1、2、5、10、25、50 时的全部指标。放在这里是因为它给出了关键词加权的实际增益。*

λ=10 相对 λ=1 的模板内 K-ACC 只多 0.76 个点,模板外多 2.24 个点。λ=50 时模板外 BLEU-4 掉到 12.38。Table 2 中报告的 SurgViVQA 数字与 λ=1 一行一致(仅模板外 BLEU-4 写作 24.84 与 24.85 之差),说明主结果没有使用关键词加权。结论部分说"关键词加权进一步提升,共同造就了 SurgViVQA 的性能",与这一点不完全对得上。

## 深度分析

### 增益到底来自哪里

论文的核心主张是"时序建模带来提升",但主表里两者的区别不止输入帧数。

相对 PitVQA,SurgViVQA 的视觉编码器从 ViT 换成 VideoMAE,文本编码器换成 BLIP,解码器加了 LoRA。

论文没有"同一模型只输入 1 帧"的对照,所以 8.67 个点的 K-ACC 增益里有多少来自时序信息,无法从论文里分出来。

Table 3 是更直接的证据,但也只在一个维度上。运动类题上视频模型领先约 40 个点,静态类上 Qwen 版本反而落后 PitVQA 7 个点左右。可能的解释是 Qwen 版本更依赖片段整体的运动信号,对单帧里的细节(器械是否可见、照明模式)不敏感;论文给出了这个现象,没有给出原因。

### 语言指标与关键词指标为什么分歧

结肠镜数据的长答案几乎都是模板化句子,例如 Fig 3 中"内镜在前进"那句参考答案。

在这种数据上,BLEU-4、METEOR 主要奖励"学会了答案句式",小模型在训练集上反复见过这些句式,自然得分高;零样本大模型措辞自由,BLEU-4 只有个位数,但关键词常常是对的。所以本文的 BLEU-4、ROUGE-L 优势主要反映对答案模板的拟合,判断事实正确性应以 K-ACC 为准。

按 K-ACC 看,SurgViVQA 在 REAL-Colon-VQA 模板内领先 InternVL3 + LoRA 3.73 个点,在 EndoVis18-VQA 上落后 22.04 个点。

### EndoVis18-VQA 上为什么特别差

作者的解释是:EndoVis18-VQA 的问题是静态的、只在单帧标注,改成 8 帧片段后时序建模没有用武之地。这能解释为什么相对 PitVQA 的领先变小,但解释不了模板外 K-ACC 降到 9.23 甚至 0.99。更可能的原因是 EndoVis18-VQA 的答案只有 18 个类,训练出的小解码器高度依赖题面关键词,题面一改就输出错误类别;零样本 Qwen2.5-VL 有 46.90,说明这些改写题本身并不难。这一点论文没有分析。

### 复现注意点

- 学习率 $2\times10^{-7}$ 非常小,却训练 60 轮,LoRA 秩未给出,复现时要以 GitHub 代码为准。
- 训练测试按视频划分:代码中 REAL-Colon-VQA 用 002-001 到 002-005 训练、002-006 测试,与 4450/750 的条数吻合。测试集只有 1 段录像。
- K-ACC 依赖关键词表。仓库说明 EndoVis18-VQA 没有关键词字段,需要先运行 keywords_extraction.py 生成;关键词怎样定义直接影响 K-ACC,论文正文没有交代。

## 局限

- 数据规模小:只用 6 段结肠镜录像,测试集来自其中 1 段。不同病人、不同设备之间的差异没有被测到,也缺少多次划分的方差。
- 题面高度重复:我统计 GitHub 上的标注文件,模板内文件只有 20 种不同的问句,每类对应一句固定问法;模板外文件也只有 20 种。模板内测试题与训练题面完全相同,改写题测的只是 20 种固定改写。
- 没有简单基线:yes/no 题占大多数(模板内文件中短答案为 no 的 2004 条、yes 的 1296 条),论文缺少多数类或纯文本基线,无法判断模型比"只看题面猜答案"好多少。
- 片段只有约 0.93 秒,只能测短时动态;作者自己也把扩展到 8 帧以上列为未来工作。
- 关键词加权的增益很小,且主表没有使用;Table 4 的编码器比较只在 EndoVis18-VQA 上做,没有 K-ACC。
- EndoVis18-VQA 模板外 K-ACC 降到 9.23(GPT-2)和 0.99(Qwen),论文对这一失效没有给出分析。
- 没有临床评估,作者把与内镜医生的可用性研究列为未来工作。
- 标注员间一致性、各问题类别的测试题数、Qwen 的具体型号,论文未说明。

## 我的笔记

数据可获取性(我于 2026-11-08 检查):

- GitHub 仓库 madratak/SurgViVQA 公开,REAL-Colon-VQA_annotations 目录下有 in_template.jsonl 和 out_template.jsonl,各 5200 行,字段包括视频编号、8 个帧编号、问题、问题类别、支持帧比例、长答案和短答案。问题类别为 20 个,与论文一致;仓库说明写的是 18 个,与文件不符。
- 标注只给帧编号,不含图像。训练代码从本地 videos/<视频编号>_frames 目录读取帧,帧需从 REAL-Colon 原始数据集自行抽取。REAL-Colon 在 figshare 上发布,我访问时被 403 拒绝,未能确认其当前下载条件。
- id 字段在 5200 行中只有 3750 个不同值,同一 id 会对应不同视频的样本,使用时应以视频编号加帧编号作为主键。
- 模型权重在 Hugging Face 公开(maurodrago/SurgViVQA-weights,未设门槛)。

可以照搬的做法:

- 帧级状态标注再聚合成片段题目时,用"条件在多数帧持续"作为分配规则,能避免单帧偶然状态进入片段标签。
- 每条样本同时保留模板题和改写题,答案不变,单独报告两套结果,能直接看出模型对题面的依赖。
- 按运动类和静态类分层报告,能看出视频输入到底帮了哪类问题。

使用前要检查的:

- 先跑多数类和纯文本基线。20 种固定问句、yes/no 占大头的数据上,这两个基线可能已经很高。
- 测试集只有 1 段录像,建议改做 6 折留一视频交叉验证。
- K-ACC 的关键词表要和对比方法统一,否则数字不可比。

不要做的:

- 不要用 BLEU-4、METEOR 的领先来证明事实正确性,它们在模板化答案上主要反映句式拟合。
- 不要把"SurgViVQA 优于 LoRA 微调的通用视频 VLM"当作结论,EndoVis18-VQA 上的 K-ACC 恰好相反。

后续问题:

- SurgViVQA 只输入 1 帧时,运动类和静态类 K-ACC 各掉多少?
- 同一架构下 GPT-2 与 Qwen 在运动类题上相差约 20 个点,原因是解码器容量、LoRA 位置还是训练不稳定?
- 在结肠镜数据上重做表 4 并报告 K-ACC,VideoMAE 是否仍然最好?

## 引用

- Seenivasan et al. (2023). SurgicalGPT: End-to-end language-vision GPT for visual question answering in surgery. MICCAI.
- He et al. (2025). PitVQA++: Vector matrix-low-rank adaptation for open-ended visual question answering in pituitary surgery. arXiv:2502.14149.
- Seenivasan et al. (2022). Surgical-VQA: Visual question answering in surgical scenes using transformer. MICCAI.
- Biffi et al. (2024). REAL-Colon: A dataset for developing real-world AI applications in colonoscopy. Scientific Data 11, 539.
- Tong et al. (2022). VideoMAE: Masked autoencoders are data-efficient learners for self-supervised video pre-training. NeurIPS.
- Li et al. (2022). BLIP: Bootstrapping language-image pre-training for unified vision-language understanding and generation. ICML.
- Hu et al. (2022). LoRA: Low-rank adaptation of large language models. ICLR.
- Pierantozzi et al. (2025). When to trust the answer: Question-aligned semantic neighbour entropy for safer surgical VQA. arXiv:2511.01458.
