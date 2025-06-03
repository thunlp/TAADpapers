# Must-read Papers on Textual Adversarial Attack and Defense (TAAD)


![](https://img.shields.io/github/last-commit/thunlp/TAADpapers?color=blue) ![](https://img.shields.io/badge/PaperNumber-154-brightgreen) ![](https://img.shields.io/badge/PRs-Welcome-red) 


This list is currently maintained by [Chenghao Yang](https://yangalan123.github.io/) at UChicago. 

Other previous main contributors including [Fanchao Qi](https://fanchao-qi.github.io/), and [Yuan Zang](https://zangy17.github.io/) when they were at [THUNLP](http://nlp.csai.tsinghua.edu.cn/). 

We thank all the great [contributors](#contributors) very much.

### Contents

* [0. Toolkits](#0-toolkits)
* [1. Survey Papers](#1-survey-papers)
* [2. Attack Papers](#2-attack-papers) (classified according to perturbation level)
	* [2.1 Sentence-level Attack](#21-sentence-level-attack)
	* [2.2 Word-level Attack](#22-word-level-attack) 
	* [2.3 Char-level Attack](#23-char-level-attack)
	* [2.4 Multi-level Attack](#24-multi-level-attack)
* [3. Defense Papers](#3-defense-papers)
* [4. Certified Robustness](#4-certified-robustness)
* [5. Benchmark and Evaluation](#5-benchmark-and-evaluation)
* [6. Other Papers](#6-other-papers)
* [Contributors](#contributors)


## 0. Toolkits
1. **RobustQA: A Framework for Adversarial Text Generation Analysis on Question Answering Systems**. *Yasaman Boreshban, Seyed Morteza Mirbostani, Seyedeh Fatemeh Ahmadi, Gita Shojaee, Fatemeh Kamani, Gholamreza Ghassem-Sani, Seyed Abolghasem Mirroshandel*. EMNLP 2022 Demo. [[codebase](https://github.com/mirbostani/RobustQA)] [[pdf](https://aclanthology.org/2023.emnlp-demo.24.pdf)]
1. **SeqAttack: On Adversarial Attacks for Named Entity Recognition**. *Walter Simoncini, Gerasimos Spanakis*. EMNLP 2021 Demo. [[website](https://github.com/WalterSimoncini/SeqAttack)] [[pdf](https://aclanthology.org/2021.emnlp-demo.35.pdf)]
1. **OpenAttack: An Open-source Textual Adversarial Attack Toolkit**. *Guoyang Zeng, Fanchao Qi, Qianrui Zhou, Tingji Zhang, Bairu Hou, Yuan Zang, Zhiyuan Liu, Maosong Sun*. ACL-IJCNLP 2021 Demo. [[website](https://github.com/thunlp/OpenAttack)] [[doc](https://openattack.readthedocs.io/)] [[pdf](https://aclanthology.org/2021.acl-demo.43.pdf)]
1. **TextAttack: A Framework for Adversarial Attacks, Data Augmentation, and Adversarial Training in NLP**. *John Morris, Eli Lifland, Jin Yong Yoo, Jake Grigsby, Di Jin, Yanjun Qi*. EMNLP 2020 Demo. [[website](https://github.com/QData/TextAttack)] [[doc](https://textattack.readthedocs.io/)] [[pdf](https://www.aclweb.org/anthology/2020.emnlp-demos.16.pdf)] 

## 1. Survey Papers
1. **Measure and Improve Robustness in NLP Models: A Survey**. *Xuezhi Wang, Haohan Wang, Diyi Yang*. NAACL 2022. [[pdf](https://arxiv.org/pdf/2112.08313.pdf)]
1. **Towards a Robust Deep Neural Network in Texts: A Survey**. *Wenqi Wang, Lina Wang, Benxiao Tang, Run Wang, Aoshuang Ye*. TKDE 2021. [[pdf](https://arxiv.org/pdf/1902.07285.pdf)]
1. **Adversarial Attacks on Deep Learning Models in Natural Language Processing: A Survey**. *Wei Emma Zhang, Quan Z. Sheng, Ahoud Alhazmi, Chenliang Li*. ACM TIST 2020. [[pdf](https://dl.acm.org/doi/pdf/10.1145/3374217)]
1. **Adversarial Attacks and Defenses in Images, Graphs and Text: A Review**. *Han Xu, Yao Ma, Hao-chen Liu, Debayan Deb, Hui Liu, Ji-liang Tang, Anil K. Jain*. International Journal of Automation and Computing 2020. [[pdf](https://link.springer.com/content/pdf/10.1007/s11633-019-1211-x.pdf)]
1. **Analysis Methods in Neural Language Processing: A Survey**. *Yonatan Belinkov, James Glass*. TACL 2019. [[pdf](https://www.aclweb.org/anthology/papers/Q/Q19/Q19-1004/)]

## 2. Attack Papers

Each paper is attached to one or more following labels indicating how much information the **attack model** knows about the **victim model**: `gradient` (=`white`, all information), `score` (output decision and scores), `decision` (only output decision) and `blind` (nothing)

### 2.1 Sentence-level Attack
1. **Using Adversarial Attacks to Reveal the Statistical Bias in Machine Reading Comprehension Models**. *Jieyu Lin, Jiajie Zou, Nai Ding*. ACL-IJCNLP 2021. `blind` [[pdf](https://aclanthology.org/2021.acl-short.43.pdf)]
1. **Grey-box Adversarial Attack And Defence For Sentiment Classiﬁcation**. *Ying Xu, Xu Zhong, Antonio Jimeno Yepes, Jey Han Lau*. NAACL-HLT 2021. `gradient` [[pdf](https://aclanthology.org/2021.naacl-main.321.pdf)] [[code](https://github.com/ibm-aur-nlp/adv-def-text-dist)]
1. **Generating Syntactically Controlled Paraphrases without Using Annotated Parallel Pairs**. *Kuan-Hao Huang and Kai-Wei Chang*. EACL 2021. [[pdf](https://aclanthology.org/2021.eacl-main.88.pdf)] [[code](https://github.com/uclanlp/synpg)]
1. **CAT-Gen: Improving Robustness in NLP Models via Controlled Adversarial Text Generation**. *Tianlu Wang, Xuezhi Wang, Yao Qin, Ben Packer, Kang Lee, Jilin Chen, Alex Beutel, Ed Chi*. EMNLP 2020. `score` [[pdf](https://www.aclweb.org/anthology/2020.emnlp-main.417.pdf)]
1. **T3: Tree-Autoencoder Constrained Adversarial Text Generation for Targeted Attack**. *Boxin Wang, Hengzhi Pei, Boyuan Pan, Qian Chen, Shuohang Wang, Bo Li*. EMNLP 2020. `gradient` [[pdf](https://arxiv.org/abs/1912.10375)] [[code](https://github.com/AI-secure/T3)]
1. **Adversarial Attack and Defense of Structured Prediction Models**. *Wenjuan Han, Liwen Zhang, Yong Jiang, Kewei Tu*. EMNLP 2020. `blind` [[pdf](https://www.aclweb.org/anthology/2020.emnlp-main.182.pdf)] [[code](https://github.com/WinnieHAN/structure_adv)]
1. **MALCOM: Generating Malicious Comments to Attack Neural Fake News Detection Models**. *Thai Le, Suhang Wang, Dongwon Lee*. ICDM 2020. `gradient` [[pdf](https://arxiv.org/pdf/2009.01048.pdf)] [[code](https://github.com/lethaiq/MALCOM)]
1. **Improving the Robustness of Question Answering Systems to Question Paraphrasing**. *Wee Chung Gan, Hwee Tou Ng*. ACL 2019. `blind` [[pdf](https://www.aclweb.org/anthology/P19-1610.pdf)] [[data](https://github.com/nusnlp/paraphrasing-squad)]
1. **Trick Me If You Can: Human-in-the-Loop Generation of Adversarial Examples for Question Answering**. *Eric Wallace, Pedro Rodriguez, Shi Feng, Ikuya Yamada, Jordan Boyd-Graber*. TACL 2019. `score` [[pdf](https://www.aclweb.org/anthology/Q19-1029.pdf)]
1. **PAWS: Paraphrase Adversaries from Word Scrambling**. *Yuan Zhang, Jason Baldridge, Luheng He*. NAACL-HLT 2019. `blind` [[pdf](https://www.aclweb.org/anthology/N19-1131.pdf)] [[dataset](https://g.co/dataset/paws)]
1. **Evaluating and Enhancing the Robustness of Dialogue Systems: A Case Study on a Negotiation Agent**. *Minhao Cheng, Wei Wei, Cho-Jui Hsieh*. NAACL-HLT 2019. `gradient` `score` [[pdf](https://www.aclweb.org/anthology/N19-1336)] [[code](https://github.com/cmhcbb/Robustness-of-Dialogue-systems)]
1. **Semantically Equivalent Adversarial Rules for Debugging NLP Models**. *Marco Tulio Ribeiro, Sameer Singh, Carlos Guestrin*. ACL 2018. `decision` [[pdf](https://aclweb.org/anthology/P18-1079)] [[code](https://github.com/marcotcr/sears)]
1. **Adversarially Regularising Neural NLI Models to Integrate Logical Background Knowledge**. *Pasquale Minervini, Sebastian Riedel*. CoNLL 2018. `score` [[pdf](https://www.aclweb.org/anthology/K18-1007)] [[code&data](https://github.com/uclmr/adversarial-nli/)]
1. **Robust Machine Comprehension Models via Adversarial Training**. *Yicheng Wang, Mohit Bansal*. NAACL-HLT 2018. `decision` [[pdf](https://www.aclweb.org/anthology/N18-2091.pdf)] [[dataset](https://drive.google.com/drive/folders/19Ye31SUpxdVyLzfaB2B7orbqSl9aOHfQ)]
1. **Adversarial Example Generation with Syntactically Controlled Paraphrase Networks**. *Mohit Iyyer, John Wieting, Kevin Gimpel, Luke Zettlemoyer*. NAACL-HLT 2018. `blind` [[pdf](https://www.aclweb.org/anthology/N18-1170)] [[code&data](https://github.com/miyyer/scpn)]
1. **Generating Natural Adversarial Examples**. *Zhengli Zhao, Dheeru Dua, Sameer Singh*. ICLR 2018. `decision` [[pdf](https://arxiv.org/pdf/1710.11342.pdf)] [[code](https://github.com/zhengliz/natural-adversary)]
1. **Adversarial Examples for Evaluating Reading Comprehension Systems**. *Robin Jia, Percy Liang*. EMNLP 2017. `score` `decision` `blind` [[pdf](https://www.aclweb.org/anthology/D17-1215)] [[code](https://github.com/robinjia/adversarial-squad)]
1. **Adversarial Sets for Regularising Neural Link Predictors**. *Pasquale Minervini, Thomas Demeester, Tim Rocktäschel, Sebastian Riedel*. UAI 2017. `score` [[pdf](https://arxiv.org/pdf/1707.07596.pdf)] [[code](https://github.com/uclmr/inferbeddings)]

### 2.2 Word-level Attack
1. **Confidence Elicitation: A New Attack Vector for Large Language Models**. *Brian Formento, Chuan-Sheng Foo, See-Kiong Ng*. ICLR 2025. `score`[[pdf](https://openreview.net/pdf?id=aTYexOYlLb)][[code](https://github.com/Aniloid2/Confidence_Elicitation_Attacks)]
1. **Expanding Scope: Adapting English Adversarial Attacks to Chinese**. *Hanyu Liu, Chengyuan Cai, Yanjun Qi*. Findings of ACL 2023.`decision`[[pdf](https://arxiv.org/abs/2306.04874)][[code](https://github.com/QData/TextAttack/blob/master/docs/2notebook/Example_6_Chinese_Attack.ipynb)]
1. **Adversarial Text Generation by Search and Learning**. *Guoyi Li, Bingkang Shi, Zongzhen Liu, Dehan Kong, Yulei Wu, Xiaodan Zhang, Longtao Huang, Honglei Lyu*. Findings of ACL 2023.`score`[[pdf](https://aclanthology.org/2023.findings-emnlp.1053.pdf)][[code](https://github.com/DABAI6666/ATGSL)]
1. **Bridge the Gap Between CV and NLP! A Gradient-based Textual Adversarial Attack Framework**. *Lifan Yuan, Yichi Zhang, Yangyi Chen, Wei Wei*. Findings of ACL 2023. `decision`[[pdf](https://arxiv.org/abs/2110.15317)][[code]([https://github.com/jhl-hust/texthacker](https://github.com/Phantivia/T-PGD))]
1. **TextHacker: Learning based Hybrid Local Search Algorithm for Text Hard-label Adversarial Attack**. *Zhen Yu, Xiaosen Wang, Wanxiang Che, Kun He*. Findings of EMNLP 2022. `decision`[[pdf](https://arxiv.org/abs/2201.08193)][[code](https://github.com/jhl-hust/texthacker)]
1. **TextHoaxer: Budgeted Hard-Label Adversarial Attacks on Text**. *Muchao Ye, Chenglin Miao, Ting Wang, Fenglong Ma*. AAAI 2022. `decision` [[pdf](https://ojs.aaai.org/index.php/AAAI/article/view/20303)] [[code](https://github.com/machinelearning4health/TextHoaxer)]
1. **Query-Efficient and Scalable Black-Box Adversarial Attacks on Discrete Sequential Data via Bayesian Optimization**. *Deokjae Lee, Seungyong Moon, Junhyeok Lee, Hyun Oh Song*. ICML 2022. `score` [[pdf](https://arxiv.org/abs/2206.08575)][[code](https://github.com/snu-mllab/DiscreteBlockBayesAttack)]
1. **SemAttack: Natural Textual Attacks on Different Semantic Spaces**. *Boxin Wang, Chejian Xu, Xiangyu Liu, Yu Cheng, Bo Li*. Findings of NAACL 2022. `gradient` [[pdf](https://arxiv.org/abs/2205.01287)] [[code](https://github.com/AI-secure/SemAttack)]
1. **Gradient-based Adversarial Attacks against Text Transformers**. *Chuan Guo, Alexandre Sablayrolles, Hervé Jégou, Douwe Kiela*. EMNLP 2021. `gradient` [[pdf](https://aclanthology.org/2021.emnlp-main.464.pdf)] [[code](https://github.com/facebookresearch/text-adversarial-attack)]
1. **A Strong Baseline for Query Efficient Attacks in a Black Box Setting**. *Rishabh Maheswary, Saket Maheshwary, Vikram Pudi*. EMNLP 2021. `score` [[pdf](https://arxiv.org/abs/2109.04775)] [[code](https://github.com/rishabhmaheshwary/query-attack)]
1. **On the Transferability of Adversarial Attacks against Neural Text Classifier**. *Liping Yuan, Xiaoqing Zheng, Yi Zhou, Cho-Jui Hsieh, Kai-Wei Chang*. EMNLP 2021. [[pdf](https://arxiv.org/pdf/2011.08558.pdf)]
1. **Crafting Adversarial Examples for Neural Machine Translation**. *Xinze Zhang, Junzhe Zhang, Zhenhua Chen, Kun He*. ACL-IJCNLP 2021. `score` [[pdf](https://aclanthology.org/2021.acl-long.153.pdf)] [[code](https://github.com/JHL-HUST/AdvNMT-WSLS/)]
1. **An Empirical Study on Adversarial Attack on NMT: Languages and Positions Matter**. *Zhiyuan Zeng, Deyi Xiong*. ACL-IJCNLP 2021. `score` [[pdf](https://aclanthology.org/2021.acl-short.58.pdf)]
1. **A Closer Look into the Robustness of Neural Dependency Parsers Using Better Adversarial Examples**. *Yuxuan Wang, Wanxiang Che, Ivan Titov, Shay B. Cohen, Zhilin Lei, Ting Liu*. Findings of ACL: ACL-IJCNLP 2021. `score` [[pdf](https://aclanthology.org/2021.findings-acl.207.pdf)] [[code](https://github.com/WangYuxuan93/DepAttacker.git)]
1. **Contextualized Perturbation for Textual Adversarial Attack**. *Dianqi Li, Yizhe Zhang, Hao Peng, Liqun Chen, Chris Brockett, Ming-Ting Sun, Bill Dolan*. NAACL-HLT 2021. `score` [[pdf](https://aclanthology.org/2021.naacl-main.400.pdf)] [[code](https://github.com/cookielee77/CLARE)]
1. **Adv-OLM: Generating Textual Adversaries via OLM**. *Vijit Malik, Ashwani Bhat, Ashutosh Modi*. EACL 2021. `score` [[pdf](https://aclanthology.org/2021.eacl-main.71.pdf)] [[code](https://github.com/vijit-m/Adv-OLM)]
1. **Adversarial Stylometry in the Wild: Transferable Lexical Substitution Attacks on Author Proﬁling**. *Chris Emmery, Ákos Kádár, Grzegorz Chrupała*. EACL 2021. `blind` [[pdf](https://aclanthology.org/2021.eacl-main.203.pdf)] [[code](https://github.com/cmry/reap)]
1. **Generating Natural Language Attacks in a Hard Label Black Box Setting**. *Rishabh Maheshwary, Saket Maheshwary, Vikram Pudi*. AAAI 2021. `decision` [[pdf](https://arxiv.org/pdf/2012.14956.pdf)] [[code](https://github.com/RishabhMaheshwary/hard-label-attack)]
1. **A Geometry-Inspired Attack for Generating Natural Language Adversarial Examples**. *Zhao Meng, Roger Wattenhofer*. COLING 2020. `gradient` [[pdf](https://www.aclweb.org/anthology/2020.coling-main.585.pdf)] [[code](https://github.com/zhaopku/nlp_geometry_attack)]
1. **BERT-ATTACK: Adversarial Attack Against BERT Using BERT**. *Linyang Li, Ruotian Ma, Qipeng Guo, Xiangyang Xue, Xipeng Qiu*. EMNLP 2020. `score` [[pdf](https://www.aclweb.org/anthology/2020.emnlp-main.500.pdf)] [[code](https://github.com/LinyangLee/BERT-Attack)]
1. **BAE: BERT-based Adversarial Examples for Text Classification**. *Siddhant Garg, Goutham Ramakrishnan*. EMNLP 2020. `score` [[pdf](https://www.aclweb.org/anthology/2020.emnlp-main.498.pdf)] [[code](https://github.com/QData/TextAttack/blob/master/textattack/attack_recipes/bae_garg_2019.py)]
1. **Detecting Word Sense Disambiguation Biases in Machine Translation for Model-Agnostic Adversarial Attacks**. *Denis Emelin, Ivan Titov, Rico Sennrich*. EMNLP 2020. `blind` [[pdf](https://aclanthology.org/2020.emnlp-main.616.pdf)] [[code](http://github.com/demelin/detecting_wsd_biases_for_nmt)]
1. **Imitation Attacks and Defenses for Black-box Machine Translation Systems**. *Eric Wallace, Mitchell Stern, Dawn Song*. EMNLP 2020. `decision` [[pdf](https://aclanthology.org/2020.emnlp-main.446.pdf)] [[code](https://github.com/Eric-Wallace/adversarial-mt)]
1. **Robustness to Modification with Shared Words in Paraphrase Identification**. *Zhouxing Shi, Minlie Huang*. Findings of ACL: EMNLP 2020. `score` [[pdf](https://www.aclweb.org/anthology/2020.findings-emnlp.16.pdf)] 
1. **Word-level Textual Adversarial Attacking as Combinatorial Optimization**. *Yuan Zang, Fanchao Qi, Chenghao Yang, Zhiyuan Liu, Meng Zhang, Qun Liu, Maosong Sun*. ACL 2020. `score` [[pdf](https://www.aclweb.org/anthology/2020.acl-main.540.pdf)] [[code](https://github.com/thunlp/SememePSO-Attack)]
1. **It's Morphin' Time! Combating Linguistic Discrimination with Inflectional Perturbations**. *Samson Tan, Shafiq Joty, Min-Yen Kan, Richard Socher*. ACL 2020. `score` [[pdf](https://www.aclweb.org/anthology/2020.acl-main.263.pdf)] [[code](https://github.com/salesforce/morpheus)]
1. **On the Robustness of Language Encoders against Grammatical Errors**. *Fan Yin, Quanyu Long, Tao Meng, Kai-Wei Chang*. ACL 2020. `score` [[pdf](https://www.aclweb.org/anthology/2020.acl-main.310.pdf)] [[code](https://github.com/uclanlp/ProbeGrammarRobustness)]
1. **Evaluating and Enhancing the Robustness of Neural Network-based Dependency Parsing Models with Adversarial Examples**. *Xiaoqing Zheng, Jiehang Zeng, Yi Zhou, Cho-Jui Hsieh, Minhao Cheng, Xuanjing Huang*. ACL 2020. `gradient` `score`  [[pdf](https://www.aclweb.org/anthology/2020.acl-main.590.pdf)] [[code](https://github.com/zjiehang/DPAttack)]
1. **A Reinforced Generation of Adversarial Examples for Neural Machine Translation**. *Wei Zou, Shujian Huang, Jun Xie, Xinyu Dai, Jiajun Chen*. ACL 2020. `decision` [[pdf](https://www.aclweb.org/anthology/2020.acl-main.319.pdf)]
1. **Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment**. *Di Jin, Zhijing Jin, Joey Tianyi Zhou, Peter Szolovits*. AAAI 2020. `score` [[pdf](https://arxiv.org/pdf/1907.11932v4)] [[code](https://github.com/jind11/TextFooler)]
1. **Seq2Sick: Evaluating the Robustness of Sequence-to-Sequence Models with Adversarial Examples**. *Minhao Cheng, Jinfeng Yi, Pin-Yu Chen, Huan Zhang, Cho-Jui Hsieh*. AAAI 2020. `score`  [[pdf](https://arxiv.org/pdf/1803.01128.pdf)] [[code](https://github.com/cmhcbb/Seq2Sick)]
1. **Greedy Attack and Gumbel Attack: Generating Adversarial Examples for Discrete Data**. *Puyudi Yang, Jianbo Chen, Cho-Jui Hsieh, Jane-LingWang, Michael I. Jordan*. JMLR 2020. `score` [[pdf](http://jmlr.org/papers/volume21/19-569/19-569.pdf)] [[code](https://github.com/Puyudi/Greedy-Attack-and-Gumbel-Attack)]
1. **On the Robustness of Self-Attentive Models**. *Yu-Lun Hsieh, Minhao Cheng, Da-Cheng Juan, Wei Wei, Wen-Lian Hsu, Cho-Jui Hsieh*. ACL 2019. `score` [[pdf](https://www.aclweb.org/anthology/P19-1147.pdf)]
1. **Generating Natural Language Adversarial Examples through Probability Weighted Word Saliency**. *Shuhuai Ren, Yihe Deng, Kun He, Wanxiang Che*. ACL 2019. `score` [[pdf](https://www.aclweb.org/anthology/P19-1103.pdf)] [[code](https://github.com/JHL-HUST/PWWS/)]
1. **Generating Fluent Adversarial Examples for Natural Languages**. *Huangzhao Zhang, Hao Zhou, Ning Miao, Lei Li*. ACL 2019. `gradient` `score` [[pdf](https://www.aclweb.org/anthology/P19-1559)] [[code](https://github.com/LC-John/Metropolis-Hastings-Attacker)]
1. **Robust Neural Machine Translation with Doubly Adversarial Inputs**. *Yong Cheng, Lu Jiang, Wolfgang Macherey*. ACL 2019. `gradient` [[pdf](https://www.aclweb.org/anthology/P19-1425)]
1. **Universal Adversarial Attacks on Text Classifiers**. *Melika Behjati, Seyed-Mohsen Moosavi-Dezfooli, Mahdieh Soleymani Baghshah, Pascal Frossard*. ICASSP 2019. `gradient` [[pdf](https://ieeexplore.ieee.org/abstract/document/8682430)]
1. **Generating Natural Language Adversarial Examples**. *Moustafa Alzantot, Yash Sharma, Ahmed Elgohary, Bo-Jhang Ho, Mani Srivastava, Kai-Wei Chang*. EMNLP 2018. `score` [[pdf](https://www.aclweb.org/anthology/D18-1316)] [[code](https://github.com/nesl/nlp_adversarial_examples)]
1. **Breaking NLI Systems with Sentences that Require Simple Lexical Inferences**.
*Max Glockner, Vered Shwartz, Yoav Goldberg*. ACL 2018. `blind` [[pdf](https://www.aclweb.org/anthology/P18-2103)] [[dataset](https://github.com/BIU-NLP/Breaking_NLI)]
1. **Deep Text Classification Can be Fooled**. *Bin Liang, Hongcheng Li, Miaoqiang Su, Pan Bian, Xirong Li, Wenchang Shi*. IJCAI 2018. `gradient` `score` [[pdf](https://arxiv.org/ftp/arxiv/papers/1704/1704.08006.pdf)]
1. **Interpretable Adversarial Perturbation in Input Embedding Space for Text**. *Sato, Motoki, Jun Suzuki, Hiroyuki Shindo, Yuji Matsumoto*. IJCAI 2018. `gradient` [[pdf](https://arxiv.org/pdf/1805.02917.pdf)] [[code](https://github.com/aonotas/interpretable-adv)]
1. **Towards Crafting Text Adversarial Samples**. *Suranjana Samanta, Sameep Mehta*. ECIR 2018. `gradient` [[pdf](https://arxiv.org/pdf/1707.02812.pdf)]
1. **Crafting Adversarial Input Sequences For Recurrent Neural Networks**. *Nicolas Papernot, Patrick McDaniel, Ananthram Swami, Richard Harang*. MILCOM 2016. `gradient` [[pdf](https://arxiv.org/pdf/1604.08275.pdf)]

### 2.3 Char-level Attack
1. **Revisiting Character-level Adversarial Attacks for Language Models**. *Elias Abad Rocamora*, Yongtao Wu, Fanghui Liu, Grigorios G. Chrysos, Volkan Cevher, ICML 2024. `score` `blind` `gradient` [[pdf](https://arxiv.org/abs/2405.04346)] [[code](https://github.com/LIONS-EPFL/Charmer)]
1. **VertAttack: Taking advantage of Text Classifiers' horizontal vision**. *Jonathan Rusert*, NAACL 2024. `score` `blind` [[pdf](https://aclanthology.org/2024.naacl-long.41.pdf)]
1. **Punctuation-level Attack: Single-shot and Single Punctuation Can Fool Text Models**. *Wenqiang Wang, Chongyang Du, Tao Wang, Kaihao Zhang, Wenhan Luo, Lin Ma, Wei Liu, Xiaochun Cao*. NeurIPS 2023. `score` `blind` [[pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/9a9f4e15ad0d680429a3e0570a96f763-Paper-Conference.pdf)]
1. **Using Punctuation as an Adversarial Attack on Deep Learning-Based NLP Systems: An Empirical Study**.
  *Brian Formento, Chuan Sheng Foo, Luu Anh Tuan, See Kiong Ng*. EACL (Findings) 2023. `score` `blind` [[pdf](https://aclanthology.org/2023.findings-eacl.1.pdf)] [[code](https://github.com/Aniloid2/EmpiricalPunctuationInsertionAttacks)]
1. **Model Extraction and Adversarial Transferability, Your BERT is Vulnerable!**.
  *Xuanli He, Lingjuan Lyu, Lichao Sun, Qiongkai Xu*. NAACL-HLT 2021. `blind` [[pdf](https://aclanthology.org/2021.naacl-main.161.pdf)] [[code](https://github.com/xlhex/extract_and_transfer)]
1. **Text Processing Like Humans Do: Visually Attacking and Shielding NLP Systems**.
*Steffen Eger, Gözde Gül ¸Sahin, Andreas Rücklé, Ji-Ung Lee, Claudia Schulz, Mohsen Mesgar, Krishnkant Swarnkar, Edwin Simpson, Iryna Gurevych*. NAACL-HLT 2019. `blind` [[pdf](https://www.aclweb.org/anthology/N19-1165)] [[code&data](https://github.com/UKPLab/naacl2019-like-humans-visual-attacks)]
1. **White-to-Black: Efficient Distillation of Black-Box Adversarial Attacks**.
*SYotam Gil, Yoav Chai, Or Gorodissky, Jonathan Berant*. NAACL-HLT 2019.  `blind` [[pdf](https://www.aclweb.org/anthology/N19-1139.pdf)] [[code](https://github.com/orgoro/white-2-black)]
1. **Black-box Generation of Adversarial Text Sequences to Evade Deep Learning Classifiers**.
*Ji Gao, Jack Lanchantin, Mary Lou Soffa, Yanjun Qi*. IEEE SPW 2018. `score`[[pdf](https://ieeexplore.ieee.org/document/8424632)] [[code](https://github.com/QData/deepWordBug)]
1. **On Adversarial Examples for Character-Level Neural Machine Translation**.
*Javid Ebrahimi, Daniel Lowd, Dejing Dou*. COLING 2018. `gradient` [[pdf](https://www.aclweb.org/anthology/C18-1055)] [[code](https://github.com/jebivid/adversarial-nmt)]
1. **Synthetic and Natural Noise Both Break Neural Machine Translation**.
*Yonatan Belinkov, Yonatan Bisk*. ICLR 2018. `blind` [[pdf](https://arxiv.org/pdf/1711.02173.pdf)] [[code&data](https://github.com/ybisk/charNMT-noise)]

### 2.4 Multi-level Attack
1. **An LLM can Fool Itself: A Prompt-Based Adversarial Attack**. *Xilie Xu, Keyi Kong, Ning Liu, Lizhen Cui, Di Wang, Jingfeng Zhang, Mohan Kankanhalli*. ICLR 2024. `blind` [[pdf](https://arxiv.org/pdf/2310.13345.pdf)] 
1. **Multi-granularity Textual Adversarial Attack with Behavior Cloning**. *Yangyi Chen, Jin Su, Wei Wei*. EMNLP 2021. `blind` [[pdf](https://aclanthology.org/2021.emnlp-main.371.pdf)] [[code](https://github.com/Yangyi-Chen/MAYA)]
1. **Synthesizing Adversarial Negative Responses for Robust Response Ranking and Evaluation**. *Prakhar Gupta, Yulia Tsvetkov, Jeffrey Bigham*. Findings of ACL: ACL-IJCNLP 2021. `blind` [[pdf](https://aclanthology.org/2021.findings-acl.338.pdf)] [[code](https://github.com/prakharguptaz/Adv_gen_dialogue)]
1. **Code-Mixing on Sesame Street: Dawn of the Adversarial Polyglots**. *Samson Tan, Shafiq Joty*. NAACL-HLT 2021. `score` [[pdf](https://aclanthology.org/2021.naacl-main.282.pdf)] [[code](https://github.com/salesforce/adversarial-polyglots)]
1. **Universal Adversarial Attacks with Natural Triggers for Text Classification**. *Liwei Song, Xinwei Yu, Hsuan-Tung Peng, Karthik Narasimhan*. NAACL-HLT 2021. `gradient` [[pdf](https://aclanthology.org/2021.naacl-main.291.pdf)] [[code](https://github.com/Hsuan-Tung/universal_attack_natural_trigger)]
1. **BBAEG: Towards BERT-based Biomedical Adversarial Example Generation for Text Classification**. *Ishani Mondal*. NAACL-HLT 2021. `score` [[pdf](https://aclanthology.org/2021.naacl-main.423.pdf)] [[code](https://github.com/Ishani-Mondal/BBAEG.git)]
1. **Don’t take “nswvtnvakgxpm” for an answer –The surprising vulnerability of automatic content scoring systems to adversarial input**. *Yuning Ding, Brian Riordan, Andrea Horbach, Aoife Cahill, Torsten Zesch*. COLING 2020. `blind` [[pdf](https://aclanthology.org/2020.coling-main.76.pdf)] [[code](https://github.com/ltl-ude/adversarials)]
1. **Universal Adversarial Triggers for Attacking and Analyzing NLP**. *Eric Wallace, Shi Feng, Nikhil Kandpal, Matt Gardner, Sameer Singh*. EMNLP-IJCNLP 2019. `gradient` [[pdf](https://aclanthology.org/D19-1221.pdf)] [[code](https://github.com/Eric-Wallace/universal-triggers)] [[website](http://www.ericswallace.com/triggers)]
1. **TEXTBUGGER: Generating Adversarial Text Against Real-world Applications**. *Jinfeng Li, Shouling Ji, Tianyu Du, Bo Li, Ting Wang*. NDSS 2019. `gradient` `score` [[pdf](https://arxiv.org/pdf/1812.05271.pdf)]
1. **Generating Black-Box Adversarial Examples for Text Classifiers Using a Deep Reinforced Model**.
*Prashanth Vijayaraghavan, Deb Roy*. ECMLPKDD 2019. `score` [[pdf](https://ecmlpkdd2019.org/downloads/paper/852.pdf)]
1. **HotFlip: White-Box Adversarial Examples for Text Classification**. *Javid Ebrahimi, Anyi Rao, Daniel Lowd, Dejing Dou*. ACL 2018. `gradient` [[pdf](https://www.aclweb.org/anthology/P18-2006)] [[code](https://github.com/AnyiRao/WordAdver)]
1. **Adversarial Over-Sensitivity and Over-Stability Strategies for Dialogue Models**. *Tong Niu, Mohit Bansal*. CoNLL 2018. `blind` [[pdf](https://www.aclweb.org/anthology/K18-1047.pdf)] [[code&data](https://github.com/WolfNiu/AdversarialDialogue)]
1. **Comparing Attention-based Convolutional and Recurrent Neural Networks: Success and Limitations in Machine Reading Comprehension**. *Matthias Blohm, Glorianna Jagfeld, Ekta Sood, Xiang Yu, Ngoc Thang Vu*. CoNLL 2018. `gradient` [[pdf](https://www.aclweb.org/anthology/K18-1011)] [[code](https://github.com/DigitalPhonetics/reading-comprehension)]

## 3. Defense Papers
1. **Are AI-Generated Text Detectors Robust to Adversarial Perturbations?** *Guanhua Huang, Yuchen Zhang, Zhe Li, Yongjian You, Mingze Wang, and Zhouwang Yang.* ACL 2024. [[pdf](http://arxiv.org/abs/2406.01179)] [[code](https://github.com/CarlanLark/Robust-AIGC-Detector)]
1. **SemRoDe: Macro Adversarial Training to Learn Representations that are Robust to Word-Level Attacks**. *Brian Formento, Wenjie Feng, Chuan-Sheng Foo, Anh Tuan Luu, See-Kiong Ng*. NAACL 2024. [[pdf](https://aclanthology.org/2024.naacl-long.443)] [[code](https://github.com/Aniloid2/SemRoDe-MacroAdversarialTraining)]  
1. **DSRM: Boost Textual Adversarial Training with Distribution Shift Risk Minimization**. *SongYang Gao, Shihan Dou, Yan Liu, Xiao Wang, Qi Zhang, Zhongyu Wei, Jin Ma, Ying Shan*. ACL 2023. [[pdf](https://aclanthology.org/2023.acl-long.680)] [[code](https://github.com/SleepThroughDifficulties/DSRM)]
1. **Generative Adversarial Training with Perturbed Token Detection for Model Robustness**. *Jiahao Zhao, Wenji Mao*. EMNLP 2023. [[pdf](https://aclanthology.org/2023.emnlp-main.804/)] [[code](https://github.com/Opdoop/GenerAT)]
1. **Textual Manifold-based Defense against Natural Language Adversarial Examples**. *Dang Minh Nguyen, Luu Anh Tuan*. EMNLP 2022. [[pdf](https://arxiv.org/abs/2211.02878)] [[code](https://github.com/dangne/tmd/)]
1. **Detecting Word-Level Adversarial Text Attacks via SHapley Additive exPlanations**. *Lukas Huber, Marc Alexander Kühn, Edoardo Mosca, Georg Groh*. Repl4NLP@ACL 2022. [[pdf](https://aclanthology.org/2022.repl4nlp-1.16.pdf)] [[code](https://github.com/huberl/adversarial_shap_detect_Repl4NLP)]
1. **Detection of Adversarial Examples in Text Classification: Benchmark and Baseline via Robust Density Estimation**. *KiYoon Yoo, Jangho Kim, Jiho Jang, Nojun Kwawk*. ACL 2022 (Findings). [[pdf](https://aclanthology.org/2022.findings-acl.289.pdf)] [[code](https://github.com/bangawayoo/adversarial-examples-in-text-classification)]
1. **“That Is a Suspicious Reaction!”: Interpreting Logits Variation to Detect NLP Adversarial Attacks**. *Edoardo Mosca, Shreyash Agarwal, Javier Rando Ramírez, Georg Groh*. ACL 2022. [[pdf](https://aclanthology.org/2022.acl-long.538.pdf)] [[code](https://github.com/javirandor/wdr)]
1. **SHIELD: Defending Textual Neural Networks against Multiple Black-Box Adversarial Attacks with Stochastic Multi-Expert Patcher**. *Thai Le, Noseong Park, Dongwon Lee*. ACL 2022. [[pdf](https://arxiv.org/pdf/2011.08908.pdf)]
1. **Perturbations in the Wild: Leveraging Human-Written Text Perturbations for Realistic Adversarial Attack and Defense**. *Thai Le, Jooyoung Lee, Kevin Yen, Yifan Hu, Dongwon Lee*. ACL 2022 (Findings). [[pdf](https://arxiv.org/pdf/2203.10346.pdf)]
1. **Achieving Model Robustness through Discrete Adversarial Training**. *Maor Ivgi, Jonathan Berant*. EMNLP 2021. [[pdf](https://aclanthology.org/2021.emnlp-main.115.pdf)] [[code](https://github.com/Mivg/robust_transformers)]
1. **Defense against Synonym Substitution-based Adversarial Attacks via Dirichlet Neighborhood Ensemble**. *Yi Zhou, Xiaoqing Zheng, Cho-Jui Hsieh, Kai-Wei Chang, Xuanjing Huang*. ACL-IJCNLP 2021. [[pdf](https://aclanthology.org/2021.acl-long.426.pdf)]
1. **A Sweet Rabbit Hole by DARCY: Using Honeypots to Detect Universal Trigger’s Adversarial Attacks**. *Thai Le, Noseong Park, Dongwon Lee*. ACL-IJCNLP 2021. [[pdf](https://aclanthology.org/2021.acl-long.296.pdf)] [[code](https://github.com/lethaiq/ACL2021-DARCY-HoneypotDefenseNLP)]
1. **Better Robustness by More Coverage: Adversarial and Mixup Data Augmentation for Robust Finetuning**. *Chenglei Si, Zhengyan Zhang, Fanchao Qi, Zhiyuan Liu, Yasheng Wang, Qun Liu, Maosong Sun*. Findings of ACL: ACL-IJCNLP 2021. [[pdf](https://aclanthology.org/2021.findings-acl.137.pdf)] [[code](https://github.com/thunlp/MixADA)]
1. **BERT-Defense: A Probabilistic Model Based on BERT to Combat Cognitively Inspired Orthographic Adversarial Attacks**. *Yannik Keller, Jan Mackensen, Steffen Eger*. Findings of ACL: ACL-IJCNLP 2021. [[pdf](https://aclanthology.org/2021.findings-acl.141.pdf)] [[code](https://github.com/yannikkellerde/BERT-Defense)]
1. **Defending Pre-trained Language Models from Adversarial Word Substitution Without Performance Sacrifice**. *Rongzhou Bao, Jiayi Wang, Hai Zhao*. Findings of ACL: ACL-IJCNLP 2021. [[pdf](https://aclanthology.org/2021.findings-acl.287.pdf)] [[code](https://github.com/LilyNLP/ADFAR)]
1. **Manifold Adversarial Augmentation for Neural Machine Translation**. *Guandan Chen, Kai Fan, Kaibo Zhang, Boxing Chen, Zhongqiang Huang*. Findings of ACL: ACL-IJCNLP 2021. [[pdf](https://aclanthology.org/2021.findings-acl.281.pdf)]
1. **Natural Language Adversarial Defense through Synonym Encoding**. *Xiaosen Wang, Hao Jin, Kun He*. UAI 2021. [[pdf](https://arxiv.org/pdf/1909.06723)] [[code](https://github.com/JHL-HUST/SEM)]
1. **Adversarial Training with Fast Gradient Projection Method against Synonym Substitution based Text Attacks**. *Xiaosen Wang, Yichen Yang, Yihe Deng, Kun He*. AAAI 2021. [[pdf](https://ojs.aaai.org/index.php/AAAI/article/view/17648/17455)] [[code](https://github.com/JHL-HUST/FGPM)]
1. **Frequency-Guided Word Substitutions for Detecting Textual Adversarial Examples**. *Maximilian Mozes, Pontus Stenetorp, Bennett Kleinberg, Lewis D. Griffin*. EACL 2021. [[pdf](https://aclanthology.org/2021.eacl-main.13.pdf)] [[code](https://github.com/maximilianmozes/fgws)]
1. **Towards Robustness Against Natural Language Word Substitutions.**  *Xinshuai Dong, Anh Tuan Luu, Rongrong Ji, Hong Liu.* ICLR 2021. [[pdf](https://openreview.net/pdf?id=ks5nebunVn_)] [[code](https://github.com/dongxinshuai/ASCC)]
1. **InfoBERT: Improving Robustness of Language Models from An Information Theoretic Perspective**. *Boxin Wang, Shuohang Wang, Yu Cheng, Zhe Gan, Ruoxi Jia, Bo Li, Jingjing Liu*. ICLR 2021. [[pdf](https://openreview.net/pdf?id=hpH98mK5Puk)] [[code](https://github.com/AI-secure/InfoBERT)]
1. **Enhancing Neural Models with Vulnerability via Adversarial Attack**. *Rong Zhang, Qifei Zhou, Bo An, Weiping Li, Tong Mo, Bo Wu*. COLING 2020. [[pdf](https://aclanthology.org/2020.coling-main.98.pdf)] [[code](https://github.com/rzhangpku/VAA)]
1. **Contrastive Zero-Shot Learning for Cross-Domain Slot Filling withAdversarial Attack**. *Keqing He, Jinchao Zhang, Yuanmeng Yan, Weiran Xu, Cheng Niu, Jie Zhou*. COLING 2020. [[pdf](https://aclanthology.org/2020.coling-main.126.pdf)]
1. **Mind Your Inflections! Improving NLP for Non-Standard Englishes with Base-Inflection Encoding**. *Samson Tan, Shafiq Joty, Lav R. Varshney, Min-Yen Kan*. EMNLP 2020. [[pdf](https://www.aclweb.org/anthology/2020.emnlp-main.455v2.pdf)] [[code](https://github.com/salesforce/bite)]
1. **Robust Encodings: A Framework for Combating Adversarial Typos**. *Erik Jones, Robin Jia, Aditi Raghunathan, Percy Liang*. ACL 2020. [[pdf](https://www.aclweb.org/anthology/2020.acl-main.245.pdf)] [[code](https://worksheets.codalab.org/worksheets/0x8fc01c7fc2b742fdb29c05669f0ad7d2)]
1. **Joint Character-level Word Embedding and Adversarial Stability Training to Defend Adversarial Text**. *Hui Liu, Yongzheng Zhang, Yipeng Wang, Zheng Lin, Yige Chen*. AAAI 2020. [[pdf](https://www.aaai.org/Papers/AAAI/2020GB/AAAI-LiuH.1396.pdf)]
1. **A Robust Adversarial Training Approach to Machine Reading Comprehension**. *Kai Liu, Xin Liu, An Yang, Jing Liu, Jinsong Su, Sujian Li, Qiaoqiao She*. AAAI 2020. [[pdf](https://www.aaai.org/Papers/AAAI/2020GB/AAAI-LiuK.6841.pdf)]
1. **FreeLB: Enhanced Adversarial Training for Language Understanding**. *Chen Zhu, Yu Cheng, Zhe Gan, Siqi Sun, Tom Goldstein, Jingjing Liu*. CoRR 2019. [[pdf](https://arxiv.org/pdf/1909.11764.pdf)] [[code](https://github.com/zhuchen03/FreeLB)]
1. **Learning to Discriminate Perturbations for Blocking Adversarial Attacks in Text Classification**. *Yichao Zhou, Jyun-Yu Jiang, Kai-Wei Chang, Wei Wang*. EMNLP-IJCNLP 2019. [[pdf](https://www.aclweb.org/anthology/D19-1496.pdf)] [[code](https://github.com/joey1993/bert-defender)]
1. **Build it Break it Fix it for Dialogue Safety: Robustness from Adversarial Human Attack**. *Emily Dinan, Samuel Humeau, Bharath Chintagunta, Jason Weston*. EMNLP-IJCNLP 2019. [[pdf](https://www.aclweb.org/anthology/D19-1461.pdf)] [[data](https://parl.ai/projects/dialogue_safety/)]
1. **Combating Adversarial Misspellings with Robust Word Recognition**. *Danish Pruthi, Bhuwan Dhingra, Zachary C. Lipton*. ACL 2019. [[pdf](https://www.aclweb.org/anthology/P19-1561.pdf)] [[code](https://github.com/danishpruthi/adversarial-misspellings)]
1. **Robust-to-Noise Models in Natural Language Processing Tasks**. *Valentin Malykh*. ACL 2019. [[pdf](https://www.aclweb.org/anthology/P19-2002.pdf)] [[code](https://gitlab.com/madrugado/robust-w2v)]


## 4. Certified Robustness
1. **CERT-ED: Certifiably Robust Text Classification for Edit Distance**
*Zhuoqun Huang, Neil G. Marchant, Olga Ohrimenko, Benjamin I. P. Rubinstein*. Findings of ACL: EMNLP 2024. [[pdf](https://aclanthology.org/2024.findings-emnlp.635.pdf)]
1. **Certified Robustness to Word Substitution Attack with Differential Privacy**.
*Wenjie Wang, Pengfei Tang, Jian Lou, Li Xiong*. NAACL-HLT 2021. [[pdf](https://aclanthology.org/2021.naacl-main.87.pdf)]
1. **Automatic Perturbation Analysis for Scalable Certified Robustness and Beyond**.
*Kaidi Xu, Zhouxing Shi, Huan Zhang, Yihan Wang, Kai-Wei Chang, Minlie Huang, Bhavya Kailkhura, Xue Lin, Cho-Jui Hsieh*. NeurIPS 2020. [[pdf](https://proceedings.neurips.cc/paper/2020/file/0cbc5671ae26f67871cb914d81ef8fc1-Paper.pdf)] [[code](https://github.com/kaidixu/auto_LiRPA)]
1. **SAFER: A Structure-free Approach for Certified Robustness to Adversarial Word Substitutions**.
*Mao Ye, Chengyue Gong, Qiang Liu*. ACL 2020. [[pdf](https://www.aclweb.org/anthology/2020.acl-main.317.pdf)] [[code](https://github.com/lushleaf/Structure-free-certified-NLP)]
1. **Robustness Verification for Transformers**. *Zhouxing Shi, Huan Zhang, Kai-Wei Chang, Minlie Huang, Cho-Jui Hsieh*. ICLR 2020. [[pdf](https://arxiv.org/pdf/2002.06622.pdf)] [[code](https://github.com/shizhouxing/Robustness-Verification-for-Transformers)]
1. **Achieving Verified Robustness to Symbol Substitutions via Interval Bound Propagation**.
*Po-Sen Huang, Robert Stanforth, Johannes Welbl, Chris Dyer, Dani Yogatama, Sven Gowal, Krishnamurthy Dvijotham, Pushmeet Kohli*. EMNLP-IJCNLP 2019. [[pdf](https://www.aclweb.org/anthology/D19-1419.pdf)]
1. **Certified Robustness to Adversarial Word Substitutions**. *Robin Jia, Aditi Raghunathan, Kerem Göksel, Percy Liang*. EMNLP-IJCNLP 2019. [[pdf](https://www.aclweb.org/anthology/D19-1423.pdf)] [[code](https://github.com/robinjia/certified-word-sub)]
1. **POPQORN: Quantifying Robustness of Recurrent Neural Networks**.
*Ching-Yun Ko, Zhaoyang Lyu, Lily Weng, Luca Daniel, Ngai Wong, Dahua Lin*. ICML 2019. [[pdf](http://proceedings.mlr.press/v97/ko19a/ko19a.pdf)] [[code](https://github.com/ZhaoyangLyu/POPQORN)]


## 5. Benchmark and Evaluation
1. **DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models**. *Boxin Wang, Weixin Chen, Hengzhi Pei, Chulin Xie, Mintong Kang, Chenhui Zhang, Chejian Xu, Zidi Xiong, Ritik Dutta, Rylan Schaeffer, Sang T. Truong, Simran Arora, Mantas Mazeika, Dan Hendrycks, Zinan Lin, Yu Cheng, Sanmi Koyejo, Dawn Song, Bo Li*. NeurIPS 2023 (Datasets and Benchmarks Track). [[pdf](https://arxiv.org/pdf/2306.11698.pdf)] [[website](https://decodingtrust.github.io/)]
1. **Preserving Semantics in Textual Adversarial Attacks**. *David Herel, Hugo Cisneros, Tomas Mikolov*. ECAI 2023. [[pdf](https://arxiv.org/abs/2211.04205)] [[code](https://github.com/DavidHerel/semantics-preserving-encoder)]
1. **Prompting GPT-3 To Be Reliable**. *Chenglei Si, Zhe Gan, Zhengyuan Yang, Shuohang Wang, Jianfeng Wang, Jordan Boyd-Graber, Lijuan Wang*. ICLR 2023. [[pdf](https://arxiv.org/abs/2210.09150)] [[code](https://github.com/NoviScl/GPT3-Reliability)]
1. **Why Should Adversarial Perturbations be Imperceptible? Rethink the Research Paradigm in Adversarial NLP**. *Yangyi Chen, Hongcheng Gao, Ganqu Cui, Fanchao Qi, Longtao Huang, Zhiyuan Liu, Maosong Sun*. EMNLP 2022. [[pdf](https://arxiv.org/abs/2210.10683)] [[code&data](https://github.com/thunlp/Advbench)]
1. **Interpreting the Robustness of Neural NLP Models to Textual Perturbations.** *Yunxiang Zhang, Liangming Pan, Samson Tan, Min-Yen Kan*. Findings of ACL, 2022. [[pdf](https://arxiv.org/pdf/2110.07159.pdf)]
1. **Contrasting Human- and Machine-Generated Word-Level Adversarial Examples for Text Classification**. *Maximilian Mozes, Max Bartolo, Pontus Stenetorp, Bennett Kleinberg, Lewis D. Griffin*. EMNLP 2021. [[pdf](https://aclanthology.org/2021.emnlp-main.651.pdf)] [[code](https://github.com/maximilianmozes/human_adversaries)]
1. **Dynabench: Rethinking Benchmarking in NLP.** *Douwe Kiela, Max Bartolo, Yixin Nie, Divyansh Kaushik, Atticus Geiger, Zhengxuan Wu, Bertie Vidgen, Grusha Prasad, Amanpreet Singh, Pratik Ringshia, Zhiyi Ma, Tristan Thrush, Sebastian Riedel, Zeerak Waseem, Pontus Stenetorp, Robin Jia, Mohit Bansal, Christopher Potts, Adina Williams*. NAACL 2021. [[pdf](https://aclanthology.org/2021.naacl-main.324.pdf)] [[website](https://dynabench.org/)]
1. **Adversarial GLUE: A Multi-Task Benchmark for Robustness Evaluation of Language Models.** *Boxin Wang, Chejian Xu, Shuohang Wang, Zhe Gan, Yu Cheng, Jianfeng Gao, Ahmed Hassan Awadallah, Bo Li*. NeurIPS 2021 (Datasets and Benchmarks Track). [[pdf](https://arxiv.org/pdf/2111.02840.pdf)] [[website](https://adversarialglue.github.io/)]
1. **Searching for an Effiective Defender: Benchmarking Defense against Adversarial Word Substitution.** *Zongyi Li, Jianhan Xu, Jiehang Zeng, Linyang Li, Xiaoqing Zheng, Qi Zhang, Kai-Wei Chang, and Cho-Jui Hsieh*. EMNLP 2021. [[pdf](https://arxiv.org/pdf/2108.12777.pdf)]
1. **Double Perturbation: On the Robustness of Robustness and Counterfactual Bias Evaluation**. *Chong Zhang, Jieyu Zhao, Huan Zhang, Kai-Wei Chang, and Cho-Jui Hsieh* NAACL 2021. [[pdf](https://aclanthology.org/2021.naacl-main.305.pdf)] [[code](https://github.com/chong-z/nlp-second-order-attack)]
1. **Reevaluating Adversarial Examples in Natural Language**. *John Morris, Eli Lifland, Jack Lanchantin, Yangfeng Ji, Yanjun Qi*. Findings of ACL: EMNLP 2020. [[pdf](https://aclanthology.org/2020.findings-emnlp.341.pdf)] [[code&data](https://github.com/QData/Reevaluating-NLP-Adversarial-Examples)]
1. **From Hero to Zéroe: A Benchmark of Low-Level Adversarial Attacks**. *Steffen Eger, Yannik Benz*. AACL-IJCNLP 2020. [[pdf](https://www.aclweb.org/anthology/2020.aacl-main.79.pdf)] [[code&data](https://github.com/yannikbenz/zeroe)]
1. **Adversarial NLI: A New Benchmark for Natural Language Understanding**. *Yixin Nie, Adina Williams, Emily Dinan, Mohit Bansal, Jason Weston, Douwe Kiela*. ACL 2020. [[pdf](https://www.aclweb.org/anthology/2020.acl-main.441.pdf)] [[demo](https://www.adversarialnli.com/)] [[dataset & leaderboard](https://github.com/facebookresearch/anli/)]
1. **Evaluating NLP Models via Contrast Sets**. *Matt Gardner, Yoav Artzi, Victoria Basmova, Jonathan Berant, Ben Bogin, Sihao Chen, Pradeep Dasigi, Dheeru Dua, Yanai Elazar, Ananth Gottumukkala, Nitish Gupta, Hanna Hajishirzi, Gabriel Ilharco, Daniel Khashabi, Kevin Lin, Jiangming Liu, Nelson F. Liu, Phoebe Mulcaire, Qiang Ning, Sameer Singh, Noah A. Smith, Sanjay Subramanian, Reut Tsarfaty, Eric Wallace, Ally Zhang, Ben Zhou*. Findings of ACL: EMNLP 2020. [[pdf](https://www.aclweb.org/anthology/2020.findings-emnlp.117.pdf)] [[website](https://allennlp.org/contrast-sets)]
1. **On Evaluation of Adversarial Perturbations for Sequence-to-Sequence Models**. *Paul Michel, Xian Li, Graham Neubig, Juan Miguel Pino*. NAACL-HLT 2019. [[pdf](https://www.aclweb.org/anthology/N19-1314)] [[code](https://github.com/pmichel31415/teapot-nlp)]

## 6. Other Papers

1. **Identifying Human Strategies for Generating Word-Level Adversarial Examples**. *Maximilian Mozes, Bennett Kleinberg, Lewis D. Griffin*. Findings of ACL: EMNLP 2022. [[pdf](https://arxiv.org/abs/2210.11598)]
1. **LexicalAT: Lexical-Based Adversarial Reinforcement Training for Robust Sentiment Classification**. *Jingjing Xu, Liang Zhao, Hanqi Yan, Qi Zeng, Yun Liang, Xu Sun*. EMNLP-IJCNLP 2019. [[pdf](https://www.aclweb.org/anthology/D19-1554.pdf)] [[code](https://github.com/lancopku/LexicalAT)]
1. **Unified Visual-Semantic Embeddings: Bridging Vision and Language with Structured Meaning Representations**. *Hao Wu, Jiayuan Mao, Yufeng Zhang, Yuning Jiang, Lei Li, Weiwei Sun, Wei-Ying Ma*. CVPR 2019. [[pdf](http://openaccess.thecvf.com/content_CVPR_2019/papers/Wu_Unified_Visual-Semantic_Embeddings_Bridging_Vision_and_Language_With_Structured_Meaning_CVPR_2019_paper.pdf)]
1. **AdvEntuRe: Adversarial Training for Textual Entailment with Knowledge-Guided Examples**. *Dongyeop Kang, Tushar Khot, Ashish Sabharwal, Eduard Hovy*. ACL 2018. [[pdf](https://www.aclweb.org/anthology/P18-1225)] [[code](https://github.com/dykang/adventure)]
1. **Learning Visually-Grounded Semantics from Contrastive Adversarial Samples**. *Haoyue Shi, Jiayuan Mao, Tete Xiao, Yuning Jiang, Jian Sun*. COLING 2018.
[[pdf](https://aclweb.org/anthology/C18-1315)] [[code](https://github.com/ExplorerFreda/VSE-C)]

## Contributors

We thank all the contributors to this list. And more contributions are very welcome.

<a href="https://github.com/thunlp/TAADpapers/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=thunlp/TAADpapers" />
</a>

