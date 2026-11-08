#!/usr/bin/env python3
"""Build docs/index.html and the dataset tables in README.md from one catalog.

Run from the repository root after tools/publish_paper.py. Each reading is read
from docs/papers/<slug>/ (report.md front matter and review/scorecard.json).
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "docs" / "papers"
PAGES = "https://cvi-yangwn.github.io/Surgical-Datasets/papers/"
GH = '<svg viewBox="0 0 16 16" width="14" height="14" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>'

# "slug" names docs/papers/<slug>/; "note" is the paper's directory prefix under
# DeepPaperNote_output/手术数据集/, used by tools/publish_paper.py. None = not read yet.
CATALOG = [
    ('ophthalmic', '👁️ 眼科', 'Ophthalmic', [
        {'name': 'Cataract-1K', 'year': 2023, 'paper': 'https://arxiv.org/abs/2312.06295', 'data': 'https://github.com/Negin-Ghamsarian/Cataract-1K', 'task': '阶段识别 / 分割 / 异常检测', 'size': '1000 个视频', 'source': '医院', 'slug': 'cataract-1k', 'note': 'Cataract_1K'},
        {'name': 'OphNet', 'year': 2024, 'paper': 'https://arxiv.org/abs/2406.07471', 'data': 'https://forms.gle/GhJyQDPUrE74jLy87', 'task': '阶段、器械、操作识别', 'size': '2278 个视频', 'source': 'YouTube', 'slug': 'ophnet', 'note': 'OphNet'},
        {'name': 'CaDIS', 'year': 2019, 'paper': 'https://arxiv.org/abs/1906.11586', 'data': 'https://cataracts-semantic-segmentation2020.grand-challenge.org/', 'task': '白内障手术图像语义分割', 'size': '', 'source': '', 'slug': 'cadis', 'note': 'CaDIS'},
        {'name': 'Cataract-LMM', 'year': 2025, 'paper': 'https://arxiv.org/abs/2510.16371', 'data': 'https://huggingface.co/datasets/mjahmadi/Cataract-LMM', 'task': '阶段识别 / 实例分割 / 器械-组织交互跟踪 / 技能评估', 'size': '3000 个视频', 'source': '两家眼科医院', 'slug': 'cataract-lmm', 'note': 'Cataract_LMM'},
        {'name': 'Cataract-101', 'year': 2018, 'paper': 'https://doi.org/10.1145/3204949.3208137', 'data': 'https://doi.org/10.5281/zenodo.1220951', 'task': '白内障手术阶段识别（十阶段）', 'size': '101 个视频（14 小时）', 'source': '奥地利克拉根福医院', 'slug': 'cataract-101', 'note': 'Cataract_101'},
        {'name': 'CATARACTS', 'year': 2019, 'paper': 'https://discovery.ucl.ac.uk/10068008/1/CATARACTS.pdf', 'data': 'https://cataracts.grand-challenge.org', 'task': '帧级器械使用识别（21 种器械）', 'size': '50 个视频', 'source': '布雷斯特大学医院', 'slug': 'cataracts', 'note': 'CATARACTS'},
    ]),
    ('endoscopic', '🔬 内镜', 'Endoscopic', [
        {'name': 'Colon-Bench', 'year': 2026, 'paper': 'https://arxiv.org/abs/2603.25645', 'data': 'https://huggingface.co/datasets/ajhamdi/colon-bench', 'task': '结肠镜病灶检测 / 开放词汇分割 / 视频问答', 'size': '528 个视频窗口（46 万帧，14 类病灶）', 'source': 'REAL-Colon 全程结肠镜录像', 'slug': 'colon-bench', 'note': 'Colon_Bench'},
        {'name': 'REAL-Colon-VQA（SurgViVQA）', 'year': 2025, 'paper': 'https://arxiv.org/abs/2511.03325', 'data': 'https://github.com/madratak/SurgViVQA/tree/main/REAL-Colon-VQA_annotations', 'task': '结肠镜短片段视频问答', 'size': '5,200 条 8 帧片段问答', 'source': 'REAL-Colon 6 段结肠镜录像', 'slug': 'tg-surgvqa', 'note': 'SurgViVQA'},
        {'name': 'EndoBench', 'year': 2025, 'paper': 'https://arxiv.org/abs/2505.23601', 'data': 'https://huggingface.co/datasets/Saint-lsy/EndoBench', 'task': '多模态大模型视觉问答评测', 'size': '', 'source': '', 'slug': 'endobench', 'note': 'EndoBench'},
        {'name': 'Kvasir-SEG', 'year': 2019, 'paper': 'https://arxiv.org/abs/1911.07069', 'data': 'https://datasets.simula.no/kvasir-seg/', 'task': '息肉分割', 'size': '', 'source': '', 'slug': 'kvasir-seg', 'note': 'Kvasir_SEG'},
        {'name': 'PolypGen', 'year': 2021, 'paper': 'https://arxiv.org/abs/2106.04463', 'data': 'https://doi.org/10.7303/syn26376615', 'task': '息肉检测与分割（跨中心泛化）', 'size': '超过 300 名患者', 'source': '六个中心', 'slug': 'polypgen', 'note': 'A_multi_centre'},
        {'name': 'PitVis', 'year': 2024, 'paper': 'https://arxiv.org/abs/2409.01184', 'data': 'https://doi.org/10.5522/04/26531686', 'task': '内镜垂体手术步骤 / 器械识别', 'size': '25 个公开视频 + 8 个私有测试视频', 'source': '英国国立神经病学与神经外科医院', 'slug': 'pitvis', 'note': 'PitVis'},
        {'name': 'EndoSLAM', 'year': 2020, 'paper': 'https://arxiv.org/abs/2006.16670', 'data': 'https://github.com/CapsuleEndoscope/EndoSLAM', 'task': '内镜视觉里程计与深度估计', 'size': '', 'source': '', 'slug': 'endoslam', 'note': 'EndoSLAM'},
    ]),
    ('laparoscopic', '🩻 腹腔镜', 'Laparoscopic', [
        {'name': 'SLAM', 'year': 2025, 'paper': 'https://www.nature.com/articles/s41597-025-05093-7', 'data': 'https://figshare.com/articles/dataset/SLAM_-_Surgical_LAparoscopic_Motions/28104782/3', 'task': '动作分类', 'size': '4,097 个视频片段', 'source': '瑞金医院卢湾分院', 'slug': 'slam', 'note': 'A_Comprehensive_Video'},
        {'name': 'Cholec80（EndoNet）', 'year': 2016, 'paper': 'https://arxiv.org/abs/1602.03012', 'data': 'https://camma.unistra.fr/datasets/', 'task': '阶段识别 / 器械识别', 'size': '', 'source': '', 'slug': 'cholec80', 'note': 'EndoNet'},
        {'name': 'CholecT50', 'year': 2021, 'paper': 'https://arxiv.org/abs/2109.03223', 'data': 'https://github.com/CAMMA-public/cholect50', 'task': '手术动作三元组识别', 'size': '50 个视频', 'source': '', 'slug': 'cholect50', 'note': 'Rendezvous'},
        {'name': 'CholecSeg8k', 'year': 2020, 'paper': 'https://arxiv.org/abs/2012.12453', 'data': 'https://www.kaggle.com/newslab/cholecseg8k', 'task': '胆囊切除语义分割', 'size': '8,080 帧（17 段视频）', 'source': 'Cholec80', 'slug': 'cholecseg8k', 'note': 'CholecSeg8k'},
        {'name': 'HeiChole', 'year': 2021, 'paper': 'https://arxiv.org/abs/2109.14956', 'data': 'https://www.synapse.org/#!Synapse:syn18824884', 'task': '工作流与技能评估', 'size': '33 个视频', 'source': '三个中心', 'slug': 'heichole', 'note': 'Comparative_Validation'},
        {'name': 'AutoLaparo', 'year': 2022, 'paper': 'https://arxiv.org/abs/2208.02049', 'data': 'https://autolaparo.github.io', 'task': '子宫切除多任务（工作流、运动预测、分割）', 'size': '', 'source': '', 'slug': 'autolaparo', 'note': 'AutoLaparo'},
        {'name': 'Endoscapes', 'year': 2023, 'paper': 'https://arxiv.org/abs/2312.12429', 'data': 'https://github.com/CAMMA-public/Endoscapes', 'task': '分割 / 检测 / 关键安全视野评估', 'size': '201 个视频', 'source': '', 'slug': 'endoscapes', 'note': 'The_Endoscapes'},
        {'name': 'CholecTrack20', 'year': 2023, 'paper': 'https://arxiv.org/abs/2312.07352', 'data': 'https://github.com/camma-public/cholectrack20', 'task': '多器械跟踪', 'size': '20 个视频', 'source': '', 'slug': 'cholectrack20', 'note': 'CholecTrack20'},
        {'name': 'CholecInstanceSeg', 'year': 2024, 'paper': 'https://arxiv.org/abs/2406.16039', 'data': 'https://doi.org/10.7303/syn64891826.1', 'task': '器械实例分割', 'size': '41.9k 帧（85 台手术）', 'source': 'Cholec80 与 CholecT50', 'slug': 'cholecinstanceseg', 'note': 'CholecInstanceSeg'},
        {'name': 'ROBUST-MIS', 'year': 2021, 'paper': 'https://arxiv.org/abs/2003.10299', 'data': 'https://www.synapse.org/#!Synapse:syn18779624/wiki/592660', 'task': '器械二值 / 多实例检测与分割', 'size': '30 台手术（10,040 帧）', 'source': '海德堡大学医院', 'slug': 'robust-mis', 'note': 'Comparative_validation_of_multi_instance'},
        {'name': 'DSAD', 'year': 2023, 'paper': 'https://www.nature.com/articles/s41597-022-01719-2', 'data': 'https://doi.org/10.6084/m9.figshare.21702600', 'task': '腹部解剖结构语义分割（11 类）', 'size': '13,195 张图像（32 台手术）', 'source': '德累斯顿大学医院机器人直肠手术', 'slug': 'dsad', 'note': 'The_Dresden_Surgical_Anatomy'},
        {'name': 'D4D', 'year': 2026, 'paper': 'https://arxiv.org/abs/2603.02985', 'data': 'https://doi.org/10.25532/OPARA-1033', 'task': '形变软组织 4D 重建 / 深度估计评测', 'size': '98 段序列（30 万+ 帧）', 'source': '猪尸体开腹，达芬奇立体内镜 + 结构光', 'slug': 'd4d', 'note': 'The_Dresden_Dataset_for_4D'},
        {'name': 'MultiBypass140', 'year': 2024, 'paper': 'https://arxiv.org/abs/2312.11250', 'data': 'https://github.com/CAMMA-public/MultiBypass140', 'task': '胃旁路阶段与步骤识别（跨中心泛化）', 'size': '140 个视频', 'source': '斯特拉斯堡与伯尔尼两家医院', 'slug': 'multibypass140', 'note': 'Challenges_in_Multi_centric'},
        {'name': 'GynSurg', 'year': 2025, 'paper': 'https://arxiv.org/abs/2506.11356', 'data': 'https://ftp.itec.aau.at/datasets/GynSurge/', 'task': '妇科动作识别 / 出血烟雾检测 / 语义分割', 'size': '152 个动作视频 + 12,362 帧掩码', 'source': '维也纳与多伦多两所医科大学', 'slug': 'gynsurg', 'note': 'GynSurg'},
        {'name': 'ATLAS-120k', 'year': 2026, 'paper': 'https://arxiv.org/abs/2606.22124', 'data': 'https://huggingface.co/datasets/TimJaspersTue/ATLAS-120k', 'task': '整场景解剖结构视频分割（42 类）', 'size': '100 个视频（121,018 帧）', 'source': 'YouTube 公开视频，14 种术式', 'slug': 'atlas-120k', 'note': 'Surgical_Anatomy_Recognition'},
        {'name': 'PhaKIR', 'year': 2025, 'paper': 'https://arxiv.org/abs/2511.06549', 'data': 'https://doi.org/10.5281/zenodo.15740619', 'task': '阶段识别 / 器械关键点 / 器械实例分割', 'size': '8 个视频（485,875 帧阶段标注）', 'source': '三家德国医院', 'slug': 'phakir', 'note': 'Video_Dataset_for_Surgical_Phase'},
    ]),
    ('robotic', '🤖 机器人手术', 'Robotic', [
        {'name': 'JIGSAWS', 'year': 2014, 'paper': 'https://cirl.lcsr.jhu.edu/wp-content/uploads/dlm_uploads/2014/09/JIGSAWS.pdf', 'data': 'https://cirl.lcsr.jhu.edu/research/hmm/datasets/jigsaws_release/', 'task': '手势识别 / 技能评估', 'size': '103 个试次（8 名医生）', 'source': '达芬奇台架任务', 'slug': 'jigsaws', 'note': 'JIGSAWS'},
        {'name': 'EndoVis 2017', 'year': 2019, 'paper': 'https://arxiv.org/abs/1902.06426', 'data': 'https://endovissub2017-roboticinstrumentsegmentation.grand-challenge.org', 'task': '器械分割', 'size': '', 'source': 'MICCAI 挑战赛', 'slug': 'endovis2017', 'note': '2017_Robotic'},
        {'name': 'EndoVis 2018', 'year': 2020, 'paper': 'https://arxiv.org/abs/2001.11190', 'data': 'https://endovissub2018-roboticscenesegmentation.grand-challenge.org', 'task': '手术场景分割', 'size': '', 'source': 'MICCAI 挑战赛', 'slug': 'endovis2018', 'note': '2018_Robotic'},
        {'name': 'SCARED', 'year': 2021, 'paper': 'https://arxiv.org/abs/2101.01133', 'data': 'https://endovissub2019-scared.grand-challenge.org/', 'task': '双目匹配与三维重建', 'size': '', 'source': 'MICCAI 挑战赛', 'slug': 'scared', 'note': 'Stereo_Correspondence'},
        {'name': 'PSI-AVA', 'year': 2022, 'paper': 'https://arxiv.org/abs/2212.04582', 'data': 'https://github.com/BCV-Uniandes/TAPIR', 'task': '阶段、步骤、器械与原子动作识别', 'size': '', 'source': '前列腺根治术', 'slug': 'psi-ava', 'note': 'Towards_Holistic'},
        {'name': 'SAR-RARP50', 'year': 2023, 'paper': 'https://arxiv.org/abs/2401.00496', 'data': 'https://rdr.ucl.ac.uk/projects/SARRARP50_Segmentation_of_surgical_instrumentation_and_Action_Recognition_on_Robot-Assisted_Radical_Prostatectomy_Challenge/191091', 'task': '动作识别 / 器械分割', 'size': '50 段缝合视频', 'source': '前列腺根治术', 'slug': 'sar-rarp50', 'note': 'SAR_RARP50'},
        {'name': 'GraSP', 'year': 2024, 'paper': 'https://arxiv.org/abs/2401.11174', 'data': 'https://github.com/BCV-Uniandes/GraSP', 'task': '整体场景理解（含分割）', 'size': '', 'source': '前列腺根治术', 'slug': 'grasp', 'note': 'Pixel_Wise'},
        {'name': 'SurgToolLoc / SurgVU', 'year': 2023, 'paper': 'https://arxiv.org/abs/2305.07152', 'data': 'https://console.cloud.google.com/storage/browser/isi-surgtoolloc-2022', 'task': '器械定位', 'size': '', 'source': 'MICCAI 挑战赛', 'slug': 'surgtoolloc', 'note': 'Intuitive'},
        {'name': 'SurgVU', 'year': 2025, 'paper': 'https://arxiv.org/abs/2501.09209', 'data': 'https://storage.googleapis.com/isi-surgvu/surgvu24_videos_only.zip', 'task': '器械识别与弱监督检测 / 步骤识别 / 视觉问答', 'size': '840+ 小时（280 个片段）', 'source': '达芬奇培训录像（猪模型）', 'slug': 'surgvu', 'note': 'Surgical_Visual_Understanding'},
    ]),
    ('multimodal', '💬 多模态与问答', 'Multimodal', [
        {'name': 'Surgical-VQA', 'year': 2022, 'paper': 'https://arxiv.org/abs/2206.11053', 'data': 'https://github.com/lalithjets/Surgical_VQA', 'task': '手术场景视觉问答', 'size': '', 'source': 'EndoVis 2018 与 Cholec80', 'slug': 'surgical-vqa', 'note': 'Surgical_VQA'},
        {'name': 'SurgMLLMBench', 'year': 2025, 'paper': 'https://arxiv.org/abs/2511.21339', 'data': 'https://huggingface.co/datasets/KIST-HARILAB/SurgMLLMBench', 'task': '多模态大模型问答 / 器械分割', 'size': '561,418 帧（112.8 小时）', 'source': '5 个公开数据集 + 新采集 MAVIS', 'slug': 'surgmllmbench', 'note': 'SurgMLLMBench'},
        {'name': 'SurgVLM', 'year': 2025, 'paper': 'https://arxiv.org/abs/2506.02555', 'data': 'https://huggingface.co/datasets/SurgSigma/SurgSigma-DB', 'task': '手术视觉语言指令微调与多任务评测', 'size': '181 万帧、779 万段对话（部分公开）', 'source': '23 个公开数据集改写', 'slug': 'surgvlm', 'note': 'SurgVLM'},
        {'name': 'SUREON', 'year': 2026, 'paper': 'https://arxiv.org/abs/2603.06570', 'data': 'https://huggingface.co/datasets/aleperez24/sureon', 'task': '手术视频推理问答', 'size': '76,061 条训练问答 + 340 题基准', 'source': 'YouTube 手术讲解视频', 'slug': 'sureon', 'note': 'SUREON'},
        {'name': 'SurgCoT', 'year': 2026, 'paper': 'https://arxiv.org/abs/2604.20319', 'data': 'https://huggingface.co/datasets/wanggui/SurgCoT', 'task': '链式时空推理问答', 'size': '2,841 个视频（19,345 个主问题）', 'source': '公开平台、10 个开源数据集与临床档案', 'slug': 'surgcot', 'note': 'SurgCoT'},
        {'name': 'SurgVidLM（SVU-31K）', 'year': 2025, 'paper': 'https://arxiv.org/abs/2506.17873', 'data': 'https://huggingface.co/datasets/gkw0010/SVU-31K', 'task': '多粒度手术视频指令问答', 'size': '1,882 个视频（约 3.1 万条问答）', 'source': 'YouTube 与 WebSurg 机器人手术讲解', 'slug': 'surgvidlm', 'note': 'SurgVidLM'},
        {'name': 'MIS-VQA', 'year': 2026, 'paper': 'https://arxiv.org/abs/2610.34210', 'data': 'https://huggingface.co/datasets/M-Hamdy/MIS-VQA', 'task': '手术视觉问答 / 场景描述 / 复杂推理', 'size': '84.9 万问答（3.3 万帧）', 'source': 'EndoVis18 与 CholecT50', 'slug': 'mis-vqa', 'note': 'MIS_VQA'},
        {'name': 'SAP-Bench（已撤稿）', 'year': 2025, 'paper': 'https://arxiv.org/abs/2506.07196v1', 'data': 'https://huggingface.co/datasets/SAPbench/SAPBench', 'task': '下一手术动作预测（多模态大模型评测）', 'size': '1,152 帧（74 台手术）', 'source': 'CholecT50 与 HeiChole 重标', 'slug': 'sap-bench', 'note': 'SAP_Bench'},
        {'name': 'SSG-VQA', 'year': 2024, 'paper': 'https://arxiv.org/abs/2312.10251', 'data': 'https://github.com/CAMMA-public/SSG-VQA', 'task': '基于场景图的手术视觉问答', 'size': '96 万问答（2.5 万场景）', 'source': 'CholecT45', 'slug': 'ssg-vqa', 'note': 'Advancing_Surgical_VQA'},
        {'name': 'SurgBench', 'year': 2025, 'paper': 'https://arxiv.org/abs/2506.07603', 'data': 'https://huggingface.co/datasets/JianhuiWei/SurgBench_NIPS25', 'task': '手术视频基础模型预训练与多任务评测', 'size': '5300 万帧（22 种术式）', 'source': '16 个来源整合', 'slug': 'surgbench', 'note': 'SurgBench'},
        {'name': 'SurgAtlas', 'year': 2026, 'paper': 'https://arxiv.org/abs/2606.25905', 'data': 'https://huggingface.co/datasets/filbel/SurgAtlas', 'task': '手术视频-语言预训练与推理问答', 'size': '15,291 个视频（2,391 小时）', 'source': 'YouTube', 'slug': 'surgatlas', 'note': 'SurgAtlas'},
        {'name': 'LEMON（Surg-3M）', 'year': 2025, 'paper': 'https://arxiv.org/abs/2503.19740', 'data': 'https://github.com/visurg-ai/LEMON', 'task': '手术视频自监督预训练 / 术式分类', 'size': '4K+ 视频（938 小时）', 'source': 'YouTube', 'slug': 'lemon', 'note': 'LEMON'},
    ]),
    ('or', '🏥 手术室', 'Operating room', [
        {'name': 'MVOR', 'year': 2018, 'paper': 'https://arxiv.org/abs/1808.08180', 'data': 'https://github.com/CAMMA-public/MVOR', 'task': '手术室人员检测与 2D/3D 姿态估计', 'size': '732 个多视角帧', 'source': '斯特拉斯堡大学附属医院介入手术室', 'slug': 'mvor', 'note': 'MVOR'},
        {'name': '4D-OR', 'year': 2022, 'paper': 'https://arxiv.org/abs/2203.11937', 'data': 'https://github.com/egeozsoy/4D-OR', 'task': '手术室语义场景图 / 3D 位姿 / 临床角色', 'size': '10 台手术（6734 帧）', 'source': '模拟全膝关节置换', 'slug': '4d-or', 'note': '4D_OR'},
        {'name': 'MM-OR', 'year': 2025, 'paper': 'https://arxiv.org/abs/2503.02579', 'data': 'https://forms.gle/kj47QXEcraQdGidg6', 'task': '手术室多模态场景图 / 全景分割 / 动作预测', 'size': '17 台完整录制（约 500GB）', 'source': '模拟机器人膝关节置换', 'slug': 'mm-or', 'note': 'MM_OR'},
        {'name': 'EgoExOR', 'year': 2025, 'paper': 'https://arxiv.org/abs/2505.24287', 'data': 'https://github.com/ardamamur/EgoExOR', 'task': '手术室场景图生成（第一人称 + 外部视角）', 'size': '94 分钟（84,553 帧）', 'source': '模拟脊柱手术', 'slug': 'egoexor', 'note': 'EgoExOR'},
    ]),
    ('notyet', '🕒 尚未公开', 'Not yet', [
        {'name': 'Colon-LQA（SurgLQA）', 'year': 2026, 'paper': 'https://arxiv.org/abs/2605.17915', 'data': '', 'task': '结肠镜长视频问答', 'size': '', 'source': 'REAL-Colon-VQA 片段拼接', 'slug': 'long-horizon-vqa', 'note': 'SurgLQA', 'tag': '内镜'},
        {'name': 'SurgXBench', 'year': 2025, 'paper': 'https://arxiv.org/abs/2505.10764', 'data': '', 'task': '手术视觉语言模型可解释性评测', 'size': '', 'source': 'Cholec80BBox 与 CholecT45', 'slug': 'surgxbench', 'note': 'SurgXBench', 'tag': '多模态'},
        {'name': 'SurgMotion-15M', 'year': 2026, 'paper': 'https://arxiv.org/abs/2602.05638', 'data': '', 'task': '手术视频基础模型预训练', 'size': '3,658 小时（50 个来源）', 'source': '公开数据集 + 网络与机构视频', 'slug': 'surgmotion', 'note': 'SurgMotion', 'tag': '预训练'},
        {'name': 'LD-RSVIS', 'year': 2026, 'paper': 'https://arxiv.org/abs/2609.23067', 'data': '', 'task': '指代式器械视频分割', 'size': '3,536 个视频（109 万帧）', 'source': '15 个公开数据集重标', 'slug': 'ld-rsvis', 'note': 'LD_RSVIS', 'tag': '器械分割'},
        {'name': 'SurgSkill-Bench', 'year': 2026, 'paper': 'https://arxiv.org/abs/2608.30872', 'data': '', 'task': '多模态技能评估（OSATS）', 'size': '214 段视频', 'source': '缝合打结模拟训练', 'slug': 'surgskill-bench', 'note': 'SurgSkill_Bench', 'tag': '技能评估'},
        {'name': 'SVL（SurgVLP）', 'year': 2023, 'paper': 'https://arxiv.org/abs/2307.15220', 'data': '', 'task': '手术视频-语言预训练', 'size': '', 'source': '手术讲解视频', 'slug': 'svl', 'note': 'Learning_Multi', 'tag': '多模态'},
        {'name': 'Sankara-MSICS', 'year': 2024, 'paper': 'https://arxiv.org/abs/2411.16794', 'data': '', 'task': '小切口白内障器械分割 / 阶段识别', 'size': '53 个视频（3527 帧像素标注）', 'source': 'Sankara 眼科医院', 'slug': 'sankara-msics', 'note': 'Phase_Informed', 'tag': '眼科'},
        {'name': 'OphCLIP', 'year': 2025, 'paper': 'https://arxiv.org/abs/2411.15421', 'data': '', 'task': '图文对齐', 'size': '375K 图文对', 'source': 'YouTube', 'slug': 'ophclip', 'note': 'OphCLIP', 'tag': '眼科'},
        {'name': 'SurgPub-Video', 'year': 2025, 'paper': 'https://arxiv.org/abs/2508.10054', 'data': '', 'task': '手术视频视觉问答', 'size': '3000 多个视频', 'source': '医学期刊附带视频', 'slug': 'surgpub-video', 'note': 'SurgPub_Video', 'tag': '多模态'},
        {'name': 'NeuroABench', 'year': 2025, 'paper': 'https://arxiv.org/abs/2512.06921', 'data': '', 'task': '神经外科解剖识别（多模态大模型评测）', 'size': '9 小时视频（1079 道题）', 'source': 'Neurosurgical Atlas', 'slug': 'neuroabench', 'note': 'NeuroABench', 'tag': '神经外科'},
        {'name': 'RoboSurg-VQA', 'year': 2026, 'paper': 'https://arxiv.org/abs/2605.23068', 'data': '', 'task': '分割感知的手术视觉问答', 'size': '11,480 帧', 'source': 'EndoVis 2017 与 2018', 'slug': 'robosurg-vqa', 'note': 'RoboSurg_VQA', 'tag': '机器人手术'},
    ]),
]


def front_matter(path: Path) -> dict:
    meta = {}
    for line in path.read_text(encoding="utf-8").split("---")[1].splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    return meta


def reading(slug: str) -> dict:
    d = PAPERS / slug
    meta = front_matter(d / "report.md")
    meta["score"] = json.loads((d / "review" / "scorecard.json").read_text(encoding="utf-8"))["rounds"][-1]["overall"]
    return meta


def esc(s) -> str:
    return html.escape(str(s))


def card(item: dict) -> str:
    links = []
    if item["paper"]:
        links.append(f'<a href="{esc(item["paper"])}" target="_blank" rel="noopener">论文</a>')
    if item["data"]:
        label = f"{GH} 数据" if "github" in item["data"] else "数据"
        links.append(f'<a href="{esc(item["data"])}" target="_blank" rel="noopener">{label}</a>')
    facts = " · ".join(esc(x) for x in (item["year"], item["task"], item["size"], item["source"]) if x)
    extra = f'<span class="chip ghost">{esc(item["tag"])}</span>' if item.get("tag") else ""
    if not item["note"]:
        return (f'<div class="card pending"><div class="top"><span class="name">{esc(item["name"])}</span>{extra}'
                f'<span class="state">精读待补</span></div><p class="facts">{facts}</p>'
                f'<p class="one">{"论文链接待补，" if not item["paper"] else ""}暂未精读。</p><div class="links">{"".join(links)}</div></div>')
    r = reading(item["slug"])
    tags = "".join(f'<span class="tag">{esc(t.strip())}</span>' for t in r["tags"].strip("[]").split(",") if t.strip())
    return (f'<div class="card"><div class="top"><span class="name">{esc(item["name"])}</span>{extra}'
            f'<span class="score">{r["score"]}<small> / 10 自评</small></span></div>'
            f'<p class="facts">{facts}</p><p class="sub">{esc(r["subtitle"])}</p><p class="one">{esc(r["one_sentence"])}</p>'
            f'<div class="tags">{tags}</div><div class="links"><a class="go" href="papers/{item["slug"]}/">阅读精读 →</a>'
            f'{"".join(links)}</div></div>')


def section(key: str, title: str, en: str, items: list) -> str:
    done = sum(1 for i in items if i["note"])
    cards = "".join(card(i) for i in items)
    return (f'<details class="group" id="{key}" open><summary><span class="t">{title}</span><span class="en">{en}</span>'
            f'<span class="cnt">{len(items)} 个数据集 · {done} 篇精读</span><span class="arr"></span></summary>'
            f'<div class="grid">{cards}</div></details>')


CSS = """
:root{--bg:#f6f7fb;--card:#fff;--bd:#e4e6f0;--tx:#1b1d2b;--tx2:#4b4f66;--mut:#7c8099;--ac:#4f5bd5;--ac2:#b84fa3;--sum:#fff}
@media(prefers-color-scheme:dark){:root{--bg:#12131c;--card:#1b1d2b;--bd:#2a2d42;--tx:#eef0fb;--tx2:#c3c6dc;--mut:#8a8ea8;--ac:#8b93ff;--ac2:#f07ad0;--sum:#171927}}
*{box-sizing:border-box}body{margin:0;font:16px/1.65 -apple-system,"PingFang SC","Microsoft YaHei",system-ui,sans-serif;background:var(--bg);color:var(--tx)}
header{padding:52px 20px 28px;text-align:center;background:linear-gradient(135deg,#4f5bd5,#8b5cf6 55%,#b84fa3);color:#fff}
header h1{margin:0 0 8px;font-size:2.05em}header p{margin:4px auto;max-width:720px;opacity:.92}header a{color:#fff}
.stats{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-top:16px}.stats span{background:rgba(255,255,255,.16);border-radius:999px;padding:3px 14px;font-size:.88em}
.wrap{max-width:1080px;margin:0 auto;padding:24px 18px 60px}
.tools{display:flex;justify-content:flex-end;gap:8px;margin-bottom:12px}.tools button{background:var(--card);color:var(--tx2);border:1px solid var(--bd);border-radius:8px;padding:4px 12px;font:inherit;font-size:.85em;cursor:pointer}
.tools button:hover{border-color:var(--ac);color:var(--ac)}
.group{background:var(--sum);border:1px solid var(--bd);border-radius:16px;margin-bottom:16px;overflow:hidden}
summary{list-style:none;cursor:pointer;display:flex;align-items:baseline;gap:10px;padding:16px 22px;user-select:none}
summary::-webkit-details-marker{display:none}summary:hover{background:rgba(79,91,213,.06)}
summary .t{font-size:1.18em;font-weight:700}summary .en{color:var(--mut);font-size:.9em}summary .cnt{margin-left:auto;color:var(--mut);font-size:.85em}
summary .arr{width:10px;height:10px;border-right:2px solid var(--mut);border-bottom:2px solid var(--mut);transform:rotate(-45deg);transition:.2s;align-self:center}
details[open] summary .arr{transform:rotate(45deg)}details[open] summary{border-bottom:1px solid var(--bd)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:16px;padding:18px 20px 20px}
.card{display:flex;flex-direction:column;background:var(--card);border:1px solid var(--bd);border-radius:14px;padding:18px 20px;transition:.18s}
.card:hover{box-shadow:0 10px 26px rgba(79,91,213,.14);border-color:var(--ac)}.card.pending{opacity:.75;border-style:dashed}
.top{display:flex;gap:8px;align-items:center}.name{font-weight:700;font-size:1.08em}
.chip{border-radius:999px;padding:0 9px;font-size:.75em}.chip.ghost{color:var(--ac);border:1px solid var(--ac)}
.score{margin-left:auto;font-weight:700;color:var(--ac2)}.score small{font-weight:400;color:var(--mut)}.state{margin-left:auto;color:var(--mut);font-size:.85em}
.facts{color:var(--mut);font-size:.84em;margin:4px 0 8px}.sub{color:var(--ac);margin:0 0 8px;font-size:.94em}.one{color:var(--tx2);font-size:.9em;margin:0 0 12px;flex:1}
.tags{margin-bottom:12px}.tag{display:inline-block;font-size:.74em;color:var(--mut);border:1px solid var(--bd);border-radius:6px;padding:0 6px;margin:2px 4px 2px 0}
.links{display:flex;gap:14px;align-items:center;flex-wrap:wrap;font-size:.88em}.links a{color:var(--tx2);text-decoration:none;display:inline-flex;gap:4px;align-items:center}
.links a:hover{color:var(--ac)}.links a.go{background:var(--ac);color:#fff;border-radius:8px;padding:4px 12px;font-weight:600}.links a.go:hover{opacity:.9;color:#fff}
.note{margin-top:28px;color:var(--mut);font-size:.86em;text-align:center}
"""

JS = """document.getElementById('ex').onclick=function(){document.querySelectorAll('details.group').forEach(function(d){d.open=true})};
document.getElementById('co').onclick=function(){document.querySelectorAll('details.group').forEach(function(d){d.open=false})};"""


def main() -> None:
    total = sum(len(i) for *_, i in CATALOG)
    done = sum(1 for *_, items in CATALOG for i in items if i["note"])
    body = "".join(section(*g) for g in CATALOG)
    page = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Surgical-Datasets · 论文精读</title><style>{CSS}</style></head><body>
<header><h1>🩺 Surgical-Datasets · 论文精读</h1>
<p>手术视频与内镜数据集论文的中文图文解读：背景与动机、核心观点、数据与实验、深入分析，以及论文没有说明的地方。</p>
<div class="stats"><span>{len(CATALOG)} 个类别</span><span>{total} 个数据集</span><span>{done} 篇精读</span></div>
<p style="margin-top:14px"><a href="https://github.com/CVI-yangwn/Surgical-Datasets">GitHub 仓库</a></p></header>
<div class="wrap"><div class="tools"><button id="ex" type="button">全部展开</button><button id="co" type="button">全部收起</button></div>{body}
<p class="note">每篇由 DeepPaperNote 两轮流程生成：第 1 轮为原版精读，第 2 轮为多轮追问与叙事修改。分数是模型自评，不是外部评审；数字经脚本与原文逐一核对。</p></div>
<script>{JS}</script></body></html>"""
    (ROOT / "docs" / "index.html").write_text(page, encoding="utf-8")
    write_readme(total, done)
    print(f"docs/index.html and README.md: {len(CATALOG)} groups, {total} datasets, {done} readings")


GH_ICON = '<img src="https://github.githubassets.com/favicons/favicon.svg" width="16">'


def md_data(url: str) -> str:
    if not url:
        return ""
    if "github" in url:
        return f"[{GH_ICON}]({url})"
    if "huggingface" in url:
        return f"[🤗]({url})"
    if "figshare" in url:
        return f"[figshare]({url})"
    return f"[链接]({url})"


def md_paper(url: str) -> str:
    if not url:
        return "链接待补"
    return f"[arXiv]({url})" if "arxiv" in url else f"[论文]({url})"


def readme_readings() -> str:
    out = ""
    for _, title, en, items in CATALOG:
        rows = [i for i in items if i["note"]]
        if not rows:
            continue
        out += (f"<details open>\n<summary><b>{title} {en}</b>（{len(rows)} 篇）</summary>\n\n"
                "| 数据集 | 一句话 | 阅读 |\n| :-- | :-- | :-- |\n")
        for i in rows:
            sub = reading(i["slug"])["subtitle"].replace("|", "｜")
            out += (f"| **{i['name']}** | {sub} | [🌐 网页]({PAGES}{i['slug']}/) · "
                    f"[📝 笔记](docs/papers/{i['slug']}/note.md) |\n")
        out += "\n</details>\n\n"
    return out


def readme_tables() -> str:
    out = ""
    for key, title, en, items in CATALOG:
        items = [i for i in items if i["data"]]
        if key == "notyet" or not items:
            continue
        out += f"### {title} {en}\n\n"
        if key == "notyet":
            out += "| 数据集 | 年份 | 论文 | 任务 | 规模 | 来源 | 精读 |\n| :-- | :--: | :--: | :-- | :-- | :-- | :--: |\n"
        else:
            out += "| 数据集 | 年份 | 论文 | 数据 | 任务 | 规模 | 来源 | 精读 |\n| :-- | :--: | :--: | :--: | :-- | :-- | :-- | :--: |\n"
        for i in items:
            done = f"[✅]({PAGES}{i['slug']}/)" if i["note"] else "⏳"
            name = i["name"] + (f"（{i['tag']}）" if i.get("tag") else "")
            data = "" if key == "notyet" else f" {md_data(i['data'])} |"
            out += (f"| {name} | {i['year']} | {md_paper(i['paper'])} |{data} {i['task']} | "
                    f"{i['size']} | {i['source']} | {done} |\n")
        out += "\n"
    return out


def write_readme(total: int, done: int) -> None:
    import re

    path = ROOT / "README.md"
    s = path.read_text(encoding="utf-8")
    a = s.index("## 📚 论文精读\n")
    b = s.index("> 页面上的分数是模型自评")
    intro = ("## 📚 论文精读\n\n每篇精读都包含：背景与动机、核心观点速览、数据与实验、深入分析，"
             "以及**论文没有说明或前后对不上的地方**。点开分组查看。\n\n")
    s = s[:a] + intro + readme_readings() + s[b:]
    a = s.index("### ", s.index("## 📊 数据集总览"))
    b = s.index("---\n\n## 🔍")
    s = s[:a] + readme_tables() + s[b:]
    s = re.sub(r"精读论文-\d+-", f"精读论文-{done}-", s)
    s = re.sub(r"数据集-\d+-", f"数据集-{total}-", s)
    path.write_text(s, encoding="utf-8")


if __name__ == "__main__":
    main()
