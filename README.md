# Must-read Papers on Textual Adversarial Attack and Defense

Contributed by Chenghao Yang, Fanchao Qi and Yuan Zang.



## Content

| Section | Description |
|-|-|
| [Survey](#survey) | Survey papers on Textual Attack and Defense |
| [Black-box Only](#black-box-only) | Attack generators only have access to confidence of victim models |
| [White-box Only](#white-box-only) | Attack generators have full access to victim models |
| [Both](#both) | Papers work on both black-box and white-box setting |
| [Defense Only](#defense-only) | Papers work on defense |
| [Evaluation](#evaluation) |  Papers propose new evaluations of textual attacks and defense |

## Survey Papers
1. **Analysis Methods in Neural Language Processing: A Survey.**
*Yonatan Belinkov, James Glass.* TACL 2019. [paper](https://www.aclweb.org/anthology/papers/Q/Q19/Q19-1004/)
1. **Towards a Robust Deep Neural Network in Text Domain A Survey.**
*Wenqi Wang, Lina Wang, Benxiao Tang, Run Wang, Aoshuang Ye.* 2019. [paper](https://arxiv.org/pdf/1902.07285.pdf)
1. **Adversarial Attacks on Deep Learning Models in Natural Language Processing: A Survey.**
*Wei Emma Zhang, Quan Z. Sheng, Ahoud Alhazmi, Chenliang Li.* 2019. [paper](https://arxiv.org/pdf/1901.06796.pdf)

## Black-box Only
1. **PAWS: Paraphrase Adversaries from Word Scrambling.**
*Yuan Zhang, Jason Baldridge, Luheng He.* NAACL-HLT 2019. [paper](https://www.aclweb.org/anthology/N19-1131).[dataset](https://g.co/dataset/paws)
1. **Text Processing Like Humans Do: Visually Attacking and Shielding NLP Systems.**
*Steffen Eger, Gözde Gül ¸Sahin, Andreas Rücklé, Ji-Ung Lee, Claudia Schulz, Mohsen Mesgar, Krishnkant Swarnkar, Edwin Simpson, Iryna Gurevych.* NAACL-HLT 2019. [paper](https://www.aclweb.org/anthology/N19-1165)
1. **Adversarial Over-Sensitivity and Over-Stability Strategies for Dialogue Models.**
*Tong Niu, Mohit Bansal.* CoNLL 2018. [paper](https://www.aclweb.org/anthology/K18-1047)
1. **Generating Natural Language Adversarial Examples.**
*Moustafa Alzantot, Yash Sharma, Ahmed Elgohary, Bo-Jhang Ho, Mani Srivastava, Kai-Wei Chang.* EMNLP 2018. [paper](https://www.aclweb.org/anthology/D18-1316)
1. **Breaking NLI Systems with Sentences that Require Simple Lexical Inferences.**
*Max Glockner, Vered Shwartz, Yoav Goldberg* ACL 2018. [paper](https://www.aclweb.org/anthology/P18-2103)
1. **AdvEntuRe: Adversarial Training for Textual Entailment with Knowledge-Guided Examples.**
*Dongyeop Kang, Tushar Khot, Ashish Sabharwal, Eduard Hovy.* ACL 2018. [paper](https://aclweb.org/anthology/P18-1079)
1. **Semantically Equivalent Adversarial Rules for Debugging NLP Models.**
*Marco Tulio Ribeiro, Sameer Singh, Carlos Guestrin* ACL 2018. [paper](https://aclweb.org/anthology/P18-1079)
1. **Robust Machine Comprehension Models via Adversarial Training.**
*Yicheng Wang, Mohit Bansal.* NAACL-HLT 2018. [paper](https://www.aclweb.org/anthology/N18-2091)
1. **Adversarial Example Generation with Syntactically Controlled Paraphrase Networks.**
*Mohit Iyyer, John Wieting, Kevin Gimpel, Luke Zettlemoyer.* NAACL-HLT 2018. [paper](https://www.aclweb.org/anthology/N18-1170)
1. **Black-box Generation of Adversarial Text Sequences to Evade Deep Learning Classifiers.**
*Ji Gao, Jack Lanchantin, Mary Lou Soffa, Yanjun Qi.* IEEE SPW 2018. [paper](https://ieeexplore.ieee.org/document/8424632)
1. **Synthetic and Natural Noise Both Break Neural Machine Translation.**
*Yonatan Belinkov, Yonatan Bisk.* ICLR 2018. [paper](https://arxiv.org/pdf/1711.02173.pdf)
1. **Generating Natural Adversarial Examples.**
*Zhengli Zhao, Dheeru Dua, Sameer Singh.* ICLR 2018. [paper](https://arxiv.org/pdf/1710.11342.pdf)
1. **Adversarial Examples for Evaluating Reading Comprehension Systems.**
*Robin Jia, and Percy Liang.* EMNLP 2017. [paper](https://www.aclweb.org/anthology/D17-1215)

## White-box Only
1. **On Adversarial Examples for Character-Level Neural Machine Translation.**
*Javid Ebrahimi, Daniel Lowd, Dejing Dou.* COLING 2018. [paper](https://www.aclweb.org/anthology/C18-1055)
1. **HotFlip: White-Box Adversarial Examples for Text Classification.**
*Javid Ebrahimi, Anyi Rao, Daniel Lowd, Dejing Dou.* ACL 2018. [paper](https://www.aclweb.org/anthology/P18-2006)
1. **Towards Crafting Text Adversarial Samples.**
*Suranjana Samanta, Sameep Mehta.* ECIR 2018. [paper](https://arxiv.org/pdf/1707.02812.pdf)

## Both
1. **TEXTBUGGER: Generating Adversarial Text Against Real-world Applications.**
*Jinfeng Li, Shouling Ji, Tianyu Du, Bo Li, Ting Wang.* NDSS 2019. [paper](https://arxiv.org/pdf/1812.05271.pdf)
1. **Comparing Attention-based Convolutional and Recurrent Neural Networks: Success and Limitations in Machine Reading Comprehension.**
*Matthias Blohm, Glorianna Jagfeld, Ekta Sood, Xiang Yu, Ngoc Thang Vu.* CoNLL 2018. [paper](https://www.aclweb.org/anthology/K18-1011)
1. **Deep Text Classification Can be Fooled.**
*Bin Liang, Hongcheng Li, Miaoqiang Su, Pan Bian, Xirong Li, Wenchang Shi.* IJCAI 2018. [paper](https://arxiv.org/ftp/arxiv/papers/1704/1704.08006.pdf)

## Defense Only
1. **Combating Adversarial Misspellings with Robust Word Recognition.**
*Danish Pruthi, Bhuwan Dhingra, Zachary C. Lipton.* ACL 2019. [paper](https://arxiv.org/pdf/1905.11268.pdf)

## Evaluation
1. **On Evaluation of Adversarial Perturbations for Sequence-to-Sequence Models.**
*Paul Michel, Xian Li, Graham Neubig, Juan Miguel Pino.* NAACL-HLT 2019. [paper](https://www.aclweb.org/anthology/N19-1314)

