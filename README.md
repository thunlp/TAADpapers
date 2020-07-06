# Must-read Papers on Textual Adversarial Attack and Defense (TAAD)

![](https://img.shields.io/github/last-commit/thunlp/TAADpapers?color=blue) ![](https://img.shields.io/badge/PaperNumber-55-brightgreen) ![](https://img.shields.io/badge/PRs-Welcome-red) 

Contributed by Fanchao Qi, Chenghao Yang and Yuan Zang.

### Contents

* [1. Survey Papers](#1-survey-papers)
* [2. Attack Papers](#2-attack-papers) (classified according to perturbation level)
	* [2.1 Sentence-level Attack](#21-sentence-level-attack)
	* [2.2 Word-level Attack](#22-word-level-attack) 
	* [2.3 Char-level Attack](#23-char-level-attack)
	* [2.4 Multi-level Attack](#24-multi-level-attack)
* [3. Defense Papers](#3-defense-papers)
* [4. Certified Robustness Papers](#4-certified-robustness-papers)
* [5. Benchmark and Evaluation](#5-benchmark-and-evaluation)
* [6. Other Papers](#6-other-papers)



## 1. Survey Papers

1. **Towards a Robust Deep Neural Network in Texts: A Survey**.
*Wenqi Wang, Lina Wang, Benxiao Tang, Run Wang, Aoshuang Ye*. arXiv 2020. [[pdf](https://arxiv.org/pdf/1902.07285.pdf)]
1. **Adversarial Attacks on Deep Learning Models in Natural Language Processing: A Survey**.
*Wei Emma Zhang, Quan Z. Sheng, Ahoud Alhazmi, Chenliang Li*. ACM TIST 2020. [[pdf](https://dl.acm.org/doi/pdf/10.1145/3374217)]
1. **Adversarial Attacks and Defenses in Images, Graphs and Text: A Review**.
*Han Xu, Yao Ma, Haochen Liu, Debayan Deb, Hui Liu, Jiliang Tang, Anil K. Jain*. arXiv 2019. [[pdf](https://arxiv.org/pdf/1909.08072.pdf)]
1. **Analysis Methods in Neural Language Processing: A Survey**.
*Yonatan Belinkov, James Glass*. TACL 2019. [[pdf](https://www.aclweb.org/anthology/papers/Q/Q19/Q19-1004/)]

## 2. Attack Papers

Each paper is attached to one or more following labels indicating how much information the **attack model** knows about the **victim model**: `gradient` (=`white`, all information), `score` (output decision and scores), `decision` (only output decision) and `blind` (nothing)

### 2.1 Sentence-level Attack
1. **Probing Neural Network Understanding of Natural Language Arguments**.
*Timothy Niven, Hung-Yu Kao*. ACL 2019. `score` [[pdf](https://www.aclweb.org/anthology/P19-1459.pdf)] [[code&data](https://github.com/IKMLab/arct2)]
1. **Robust Neural Machine Translation with Doubly Adversarial Inputs**.
*Yong Cheng, Lu Jiang, Wolfgang Macherey*. ACL 2019. `gradient` [[pdf](https://www.aclweb.org/anthology/P19-1425)]
1. **Trick Me If You Can: Human-in-the-Loop Generation of Adversarial Examples for Question Answering**.
*Eric Wallace, Pedro Rodriguez, Shi Feng, Ikuya Yamada, Jordan Boyd-Graber*. TACL 2019. `score` [[pdf](https://www.aclweb.org/anthology/Q19-1029.pdf)]
1. **PAWS: Paraphrase Adversaries from Word Scrambling**.
*Yuan Zhang, Jason Baldridge, Luheng He*. NAACL-HLT 2019. `blind` [[pdf](https://www.aclweb.org/anthology/N19-1131)] [[dataset](https://g.co/dataset/paws)]
1. **Evaluating and Enhancing the Robustness of Dialogue Systems: A Case Study on a Negotiation Agent**.
*Minhao Cheng, Wei Wei, Cho-Jui Hsieh*. NAACL-HLT 2019. `gradient` `score` [[pdf](https://www.aclweb.org/anthology/N19-1336)] [[code](https://github.com/cmhcbb/Robustness-of-Dialogue-systems)]
1. **Semantically Equivalent Adversarial Rules for Debugging NLP Models**.
*Marco Tulio Ribeiro, Sameer Singh, Carlos Guestrin*. ACL 2018. `decision` [[pdf](https://aclweb.org/anthology/P18-1079)] [[code](https://github.com/marcotcr/sears)]
1. **Adversarial Over-Sensitivity and Over-Stability Strategies for Dialogue Models**.
*Tong Niu, Mohit Bansal*. CoNLL 2018. `score` [[pdf](https://www.aclweb.org/anthology/K18-1047)] [[code&data](https://github.com/WolfNiu/AdversarialDialogue)]
1. **Adversarially Regularising Neural NLI Models to Integrate Logical Background Knowledge**.
*Pasquale Minervini, Sebastian Riedel*. CoNLL 2018. `score` [[pdf](https://www.aclweb.org/anthology/K18-1007)] [[code&data](https://github.com/uclmr/adversarial-nli/)]
1. **Robust Machine Comprehension Models via Adversarial Training**.
*Yicheng Wang, Mohit Bansal*. NAACL-HLT 2018. `decision` [[pdf](https://www.aclweb.org/anthology/N18-2091)] [[dataset](https://drive.google.com/drive/folders/19Ye31SUpxdVyLzfaB2B7orbqSl9aOHfQ)]
1. **Adversarial Example Generation with Syntactically Controlled Paraphrase Networks**.
*Mohit Iyyer, John Wieting, Kevin Gimpel, Luke Zettlemoyer*. NAACL-HLT 2018. `blind` [[pdf](https://www.aclweb.org/anthology/N18-1170)] [[code&data](https://github.com/miyyer/scpn)]
1. **Generating Natural Adversarial Examples**.
*Zhengli Zhao, Dheeru Dua, Sameer Singh*. ICLR 2018. `decision` [[pdf](https://arxiv.org/pdf/1710.11342.pdf)] [[code](https://github.com/zhengliz/natural-adversary)]
1. **Adversarial Examples for Evaluating Reading Comprehension Systems**.
*Robin Jia, and Percy Liang*. EMNLP 2017. `score` `decision` `blind` [[pdf](https://www.aclweb.org/anthology/D17-1215)] [[code](https://github.com/robinjia/adversarial-squad)]
1. **Adversarial Sets for Regularising Neural Link Predictors**.
*Pasquale Minervini, Thomas Demeester, Tim Rocktäschel, Sebastian Riedel*. UAI 2017. `score` [[pdf](https://arxiv.org/pdf/1707.07596.pdf)] [[code](https://github.com/uclmr/inferbeddings)]

### 2.2 Word-level Attack
1. **Greedy Attack and Gumbel Attack: Generating Adversarial Examples for Discrete Data**. *Puyudi Yang, Jianbo Chen, Cho-Jui Hsieh, Jane-LingWang, Michael I. Jordan*. Journal of Machine Learning Research 21, no. 43 (2020): 1-36. `score` [[pdf](http://jmlr.org/papers/volume21/19-569/19-569.pdf)]
1. **Word-level Textual Adversarial Attacking as Combinatorial Optimization**. *Yuan Zang, Fanchao Qi, Chenghao Yang, Zhiyuan Liu, Meng Zhang, Qun Liu, Maosong Sun*. ACL 2020. `score` [[pdf](https://arxiv.org/pdf/1910.12196.pdf)] [[code](https://github.com/thunlp/SememePSO-Attack)]
1. **Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment**.
*Di Jin, Zhijing Jin, Joey Tianyi Zhou, Peter Szolovits*. AAAI 2020. `score` [[pdf](https://arxiv.org/pdf/1907.11932v4)] [[code](https://github.com/jind11/TextFooler)]
1. **Seq2Sick: Evaluating the Robustness of Sequence-to-Sequence Models with Adversarial Examples**.
*Minhao Cheng, Jinfeng Yi, Pin-Yu Chen, Huan Zhang, Cho-Jui Hsieh*. AAAI 2020. `score`  [[pdf](https://arxiv.org/pdf/1803.01128.pdf)][[code](https://github.com/cmhcbb/Seq2Sick)]
1. **Generating Natural Language Adversarial Examples through Probability Weighted Word Saliency**.
*Shuhuai Ren, Yihe Deng, Kun He, Wanxiang Che*. ACL 2019. `score` [[pdf](https://www.aclweb.org/anthology/P19-1103.pdf)] [[code](https://github.com/JHL-HUST/PWWS/)]
1. **Generating Fluent Adversarial Examples for Natural Languages**.
*Huangzhao Zhang, Hao Zhou, Ning Miao, Lei Li*. ACL 2019. `gradient` `score` [[pdf](https://www.aclweb.org/anthology/P19-1559)] [[code](https://github.com/LC-John/Metropolis-Hastings-Attacker)]
1. **Universal Adversarial Attacks on Text Classifiers**.
*Melika Behjati, Seyed-Mohsen Moosavi-Dezfooli, Mahdieh Soleymani Baghshah, Pascal Frossard*. ICASSP 2019. `gradient` [[pdf](https://ieeexplore.ieee.org/abstract/document/8682430)]
1. **Generating Natural Language Adversarial Examples**.
*Moustafa Alzantot, Yash Sharma, Ahmed Elgohary, Bo-Jhang Ho, Mani Srivastava, Kai-Wei Chang*. EMNLP 2018. `score` [[pdf](https://www.aclweb.org/anthology/D18-1316)] [[code](https://github.com/nesl/nlp_adversarial_examples)]
1. **Breaking NLI Systems with Sentences that Require Simple Lexical Inferences**.
*Max Glockner, Vered Shwartz, Yoav Goldberg*. ACL 2018. `blind` [[pdf](https://www.aclweb.org/anthology/P18-2103)] [[dataset](https://github.com/BIU-NLP/Breaking_NLI)]
1. **Deep Text Classification Can be Fooled**.
*Bin Liang, Hongcheng Li, Miaoqiang Su, Pan Bian, Xirong Li, Wenchang Shi*. IJCAI 2018. `gradient` `score` [[pdf](https://arxiv.org/ftp/arxiv/papers/1704/1704.08006.pdf)]
1. **Interpretable Adversarial Perturbation in Input Embedding Space for Text**.
*Sato, Motoki, Jun Suzuki, Hiroyuki Shindo, and Yuji Matsumoto*. IJCAI 2018. `gradient` [[pdf](https://arxiv.org/pdf/1805.02917.pdf)] [[code](https://github.com/aonotas/interpretable-adv)]
1. **Towards Crafting Text Adversarial Samples**.
*Suranjana Samanta, Sameep Mehta*. ECIR 2018. `gradient` [[pdf](https://arxiv.org/pdf/1707.02812.pdf)]
1. **Crafting Adversarial Input Sequences For Recurrent Neural Networks**.
*Nicolas Papernot, Patrick McDaniel, Ananthram Swami, Richard Harang*. MILCOM 2016. `gradient` [[pdf](https://arxiv.org/pdf/1604.08275.pdf)]

### 2.3 Char-level Attack

1. **Text Processing Like Humans Do: Visually Attacking and Shielding NLP Systems**.
*Steffen Eger, Gözde Gül ¸Sahin, Andreas Rücklé, Ji-Ung Lee, Claudia Schulz, Mohsen Mesgar, Krishnkant Swarnkar, Edwin Simpson, Iryna Gurevych*. NAACL-HLT 2019. `score` [[pdf](https://www.aclweb.org/anthology/N19-1165)] [[code&data](https://github.com/UKPLab/naacl2019-like-humans-visual-attacks)]
1. **TEXTBUGGER: Generating Adversarial Text Against Real-world Applications**.
*Jinfeng Li, Shouling Ji, Tianyu Du, Bo Li, Ting Wang*. NDSS 2019. `gradient` `score` [[pdf](https://arxiv.org/pdf/1812.05271.pdf)]
1. **Black-box Generation of Adversarial Text Sequences to Evade Deep Learning Classifiers**.
*Ji Gao, Jack Lanchantin, Mary Lou Soffa, Yanjun Qi*. IEEE SPW 2018. `score` `blind` [[pdf](https://ieeexplore.ieee.org/document/8424632)] [[code](https://github.com/QData/deepWordBug)]
1. **On Adversarial Examples for Character-Level Neural Machine Translation**.
*Javid Ebrahimi, Daniel Lowd, Dejing Dou*. COLING 2018. `gradient` [[pdf](https://www.aclweb.org/anthology/C18-1055)] [[code](https://github.com/jebivid/adversarial-nmt)]
1. **Synthetic and Natural Noise Both Break Neural Machine Translation**.
*Yonatan Belinkov, Yonatan Bisk*. ICLR 2018. `blind` [[pdf](https://arxiv.org/pdf/1711.02173.pdf)] [[code&data](https://github.com/ybisk/charNMT-noise)]

### 2.4 Multi-level Attack
1. **Universal Adversarial Triggers for Attacking and Analyzing NLP**.
*Eric Wallace, Shi Feng, Nikhil Kandpal, Matt Gardner, Sameer Singh*. EMNLP-IJCNLP 2019. `gradient` [[pdf](https://arxiv.org/pdf/1908.07125.pdf)] [[code](https://github.com/Eric-Wallace/universal-triggers)] [[website](http://www.ericswallace.com/triggers)]
1. **Generating Black-Box Adversarial Examples for Text Classifiers Using a Deep Reinforced Model**.
*Prashanth Vijayaraghavan, Deb Roy*. ECMLPKDD 2019. `score` [[pdf](https://ecmlpkdd2019.org/downloads/paper/852.pdf)]
1. **HotFlip: White-Box Adversarial Examples for Text Classification**.
*Javid Ebrahimi, Anyi Rao, Daniel Lowd, Dejing Dou*. ACL 2018. `gradient` [[pdf](https://www.aclweb.org/anthology/P18-2006)] [[code](https://github.com/AnyiRao/WordAdver)]
1. **Comparing Attention-based Convolutional and Recurrent Neural Networks: Success and Limitations in Machine Reading Comprehension**.
*Matthias Blohm, Glorianna Jagfeld, Ekta Sood, Xiang Yu, Ngoc Thang Vu*. CoNLL 2018. `gradient` [[pdf](https://www.aclweb.org/anthology/K18-1011)] [[code](https://github.com/DigitalPhonetics/reading-comprehension)]

## 3. Defense Papers

1. **Joint Character-level Word Embedding and Adversarial Stability Training to Defend Adversarial Text**.
*Hui Liu, Yongzheng Zhang, Yipeng Wang, Zheng Lin, Yige Chen*. AAAI 2020. [[pdf](https://www.aaai.org/Papers/AAAI/2020GB/AAAI-LiuH.1396.pdf)]
1. **A Robust Adversarial Training Approach to Machine Reading Comprehension**.
*Kai Liu, Xin Liu, An Yang, Jing Liu, Jinsong Su, Sujian Li, Qiaoqiao She*. AAAI 2020. [[pdf](https://www.aaai.org/Papers/AAAI/2020GB/AAAI-LiuK.6841.pdf)]
1. **Learning to Discriminate Perturbations for Blocking Adversarial Attacks in Text Classification**.
*Yichao Zhou, Jyun-Yu Jiang, Kai-Wei Chang, Wei Wang*. EMNLP-IJCNLP 2019. [[pdf](https://www.aclweb.org/anthology/D19-1496.pdf)] [[code](https://github.com/joey1993/bert-defender)]
1. **Build it Break it Fix it for Dialogue Safety: Robustness from Adversarial Human Attack**.
*Emily Dinan, Samuel Humeau, Bharath Chintagunta, Jason Weston*. EMNLP-IJCNLP 2019. [[pdf](https://www.aclweb.org/anthology/D19-1461.pdf)] [[data](https://parl.ai/projects/dialogue_safety/)]
1. **Combating Adversarial Misspellings with Robust Word Recognition**.
*Danish Pruthi, Bhuwan Dhingra, Zachary C. Lipton*. ACL 2019. [[pdf](https://www.aclweb.org/anthology/P19-1561.pdf)] [[code](https://github.com/danishpruthi/adversarial-misspellings)]
1. **Robust-to-Noise Models in Natural Language Processing Tasks**.
*Valentin Malykh*. ACL 2019. [[pdf](https://www.aclweb.org/anthology/P19-2002.pdf)][[code](https://gitlab.com/madrugado/robust-w2v)]
1. **Robust Encodings: A Framework for Combating Adversarial Typos**.
*Erik Jones, Robin Jia, Aditi Raghunathan, Percy Liang*. ACL 2020. [[pdf](https://arxiv.org/pdf/2005.01229.pdf)][[code](https://worksheets.codalab.org/worksheets/0x8fc01c7fc2b742fdb29c05669f0ad7d2)]


## 4. Certified Robustness Papers

1. **Robustness Verification for Transformers**.
*Zhouxing Shi, Huan Zhang, Kai-Wei Chang, Minlie Huang, Cho-Jui Hsieh*. ICLR 2020. [[pdf](https://arxiv.org/pdf/2002.06622.pdf)] [[code](https://github.com/shizhouxing/Robustness-Verification-for-Transformers)]
1. **Achieving Verified Robustness to Symbol Substitutions via Interval Bound Propagation**.
*Po-Sen Huang, Robert Stanforth, Johannes Welbl, Chris Dyer, Dani Yogatama, Sven Gowal, Krishnamurthy Dvijotham, Pushmeet Kohli*. EMNLP-IJCNLP 2019. [[pdf](https://www.aclweb.org/anthology/D19-1419.pdf)]
1. **Certified Robustness to Adversarial Word Substitutions**.
*Robin Jia, Aditi Raghunathan, Kerem Göksel, Percy Liang*. EMNLP-IJCNLP 2019. [[pdf](https://www.aclweb.org/anthology/D19-1423.pdf)] [[code](https://github.com/robinjia/certified-word-sub)]
1. **POPQORN: Quantifying Robustness of Recurrent Neural Networks**.
*Ching-Yun Ko, Zhaoyang Lyu, Lily Weng, Luca Daniel, Ngai Wong, Dahua Lin*. ICML 2019. [[pdf](http://proceedings.mlr.press/v97/ko19a/ko19a.pdf)] [[code](https://github.com/ZhaoyangLyu/POPQORN)]


## 5. Benchmark and Evaluation
1. **Adversarial NLI: A New Benchmark for Natural Language Understanding**. *Yixin Nie, Adina Williams, Emily Dinan, Mohit Bansal, Jason Weston, Douwe Kiela*. ACL 2020. [[pdf](https://arxiv.org/abs/1910.14599)] [[demo](https://www.adversarialnli.com/)] [[dataset&leaderboard](https://github.com/facebookresearch/anli/)]
1. **Evaluating NLP Models via Contrast Sets**.
*Matt Gardner, Yoav Artzi, Victoria Basmova, Jonathan Berant, Ben Bogin, Sihao Chen, Pradeep Dasigi, Dheeru Dua, Yanai Elazar, Ananth Gottumukkala, Nitish Gupta, Hanna Hajishirzi, Gabriel Ilharco, Daniel Khashabi, Kevin Lin, Jiangming Liu, Nelson F. Liu, Phoebe Mulcaire, Qiang Ning, Sameer Singh, Noah A. Smith, Sanjay Subramanian, Reut Tsarfaty, Eric Wallace, Ally Zhang, Ben Zhou*. arXiv 2020. [[pdf](https://arxiv.org/pdf/2004.02709.pdf)] [[website](https://allennlp.org/contrast-sets)]
1. **On Evaluation of Adversarial Perturbations for Sequence-to-Sequence Models**.
*Paul Michel, Xian Li, Graham Neubig, Juan Miguel Pino*. NAACL-HLT 2019. [[pdf](https://www.aclweb.org/anthology/N19-1314)] [[code](https://github.com/pmichel31415/teapot-nlp)]

## 6. Other Papers

1. **LexicalAT: Lexical-Based Adversarial Reinforcement Training for Robust Sentiment Classification**.
*Jingjing Xu, Liang Zhao, Hanqi Yan, Qi Zeng, Yun Liang, Xu Sun*. EMNLP-IJCNLP 2019. [[pdf](https://www.aclweb.org/anthology/D19-1554.pdf)] [[code](https://github.com/lancopku/LexicalAT)]
1. **Unified Visual-Semantic Embeddings: Bridging Vision and Language with Structured Meaning Representations**.
*Hao Wu, Jiayuan Mao, Yufeng Zhang, Yuning Jiang, Lei Li, Weiwei Sun, Wei-Ying Ma*. CVPR 2019. [[pdf](http://openaccess.thecvf.com/content_CVPR_2019/papers/Wu_Unified_Visual-Semantic_Embeddings_Bridging_Vision_and_Language_With_Structured_Meaning_CVPR_2019_paper.pdf)]
1. **AdvEntuRe: Adversarial Training for Textual Entailment with Knowledge-Guided Examples**.
*Dongyeop Kang, Tushar Khot, Ashish Sabharwal, Eduard Hovy*. ACL 2018. [[pdf](https://www.aclweb.org/anthology/P18-1225)] [[code](https://github.com/dykang/adventure)]
1. **Learning Visually-Grounded Semantics from Contrastive Adversarial Samples**.
*Haoyue Shi, Jiayuan Mao, Tete Xiao, Yuning Jiang, Jian Sun*. COLING 2018.
[[pdf](https://aclweb.org/anthology/C18-1315)] [[code](https://github.com/ExplorerFreda/VSE-C)]
