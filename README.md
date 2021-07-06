# Few_Shot_Learning_with_BAM

----------------------

** Contributor    
JongHwan Park : bomebug15@ds.seoultech.ac.kr    
HoHyeun Hwang : hhhwang94@naver.com       
JuHee Han : fgtr153@ds.seoultech.ac.kr    
Soonki Kwon : kwonrince@gmail.com

This repository is a follow-up study of the [A Closer Look at Few-shot Classification]https://arxiv.org/abs/1904.04232 (https://github.com/wyharveychen/CloserLookFewShot) and [BAM:Bottleneck Attention Module]https://arxiv.org/abs/1807.06514 (https://github.com/Jongchan/attention-module)

![image](https://user-images.githubusercontent.com/56014940/124572020-4387fe00-de83-11eb-8b6a-0d39258586a4.png)

We experimented Few Shot Classification with backbone network that combine with BAM(Bottleneck Attention Module). Experiment setting is same as paper 'A Closer Look At Few-shot Classification'. Difference is add another dataset 'PlantVillage' for extra experiment on cross domain and 5-shot, 1-shot. Accuracy between 'with BAM models' and 'without BAM models', it does not make dramatical difference. But mostly on 1-shot and cross domain, 'with BAM models' has little bit increase accuracy.


## Requirements    
------------------- 
```
* ubuntu 18.04
* CUDA 11.0
* python 3.6.9
* torch >= 1.7.1+cu101
* torchvision >= 0.8.2+cu101
```

## Dataset
* CUB
* miniImagenet
* PlantVillage
* omniglot
* emnist

---------------    
## How to Use    
-----------------    

You should make json file or csv file for each datasets. Use write filelist python file each dataset.

##### Example

```
cd ./filelists/CUB
python write_CUB_filelist.py
```

 Using argparse, you can your experiment control easily. Check the file io_utils.py
```
 # Training
python train.py --dataset [CUB|miniImagenet|plant|] --model [Conv4|Conv6|ResNet10|ResNet18|ResNet34] --method [baseline|baseline++|protonet|matchingnet|relationnet|maml] --bam [true|false] [--OPTIONARG]
```

``` 
 ## Extract Features with bam(maml doesn't supposed to save feature)
python save_features.py --dataset [CUB|miniImagenet|plant|] --model [Conv4|Conv6|ResNet10|ResNet18|ResNet34] --method [baseline|baseline++|protonet|matchingnet|relationnet] --bam [true|false] [--OPTIONARG]
```

```
 ### Testing
python test.py --dataset [CUB|miniImagenet|plant|] --model [Conv4|Conv6|ResNet10|ResNet18|ResNet34] --method [baseline|baseline++|protonet|matchingnet|relationnet|maml] --bam [true|false] [--OPTIONARG]
 ```
--------------    

## Results
------------

You can check training result file on the directory 
`./result/checkpoints/[Datasetname]/[BAM_true|BAM_false]`

Feature files directory is 
`./result/features/[Datasetname]/[BAM_true|BAM_false]`


-----------    



