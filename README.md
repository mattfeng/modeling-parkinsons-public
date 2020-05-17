# Disease Progression Modeling of Parkinsons


## DTI
* Because the file sizes were large, we focused our efforts on control vs. PD, for those between ages 25 and 50.

### Dataset Statistics
* Total original images
    * 321 Control
    * 1109 PD
* Unique patients
    * PPMI
        * 78 Control
        * 171 PD
    * IXI
        * 400 Control

### Train Stats, V1
* All CONTROL images
* Only PD_1, PD_2, and PD_3 for PD images

* Train/Valid/Test (70/15/15) Split
    * Control: 334/71/73 patients
    * Control: (19031+14619)/(4074+3250)/(4339+3508) images (control+pd)
    * PD: 105/22/23 patients
    * 

* Models:
    * **vgg16-2020-05-10T19:36:15.071174-epoch-0.pth**
    * validation: epoch=0 loss=0.036620, acc=0.6980, auc=0.7453
    * testing: loss=0.035914, acc=0.6662, auc=0.7672


### Train Stats, V2
* All CONTROL images



### Notes
* PPMI_3767_MR_DTI_gated__br_raw_20130204180706387_50_S181438_I357746 was deleted because it was corrupt.
* /home/eager/modeling-parkinsons/data/raw/ppmi_dti_control/PPMI_3816_MR_DTI_gated__br_raw_20121017103610217_40_S171107_I340642.nii
* /home/eager/modeling-parkinsons/data/raw/ppmi_dti_pd/PPMI_4038_MR_DTI_gated__br_raw_20150612104957703_14_S263108_I497249.nii