## Build Documentation

1. Clone YOLO_person


   ```bash
   git clone (https://github.com/Ashores/YOLO)
   cd YOLO
   ```
2. dataset prepare can follow mmyolo.
3. Install the building dependencies of documentation

   ```bash
   ##create an torch environment
   pip install torch==1.13.0+cu116 torchvision==0.14.0+cu116 torchaudio==0.13.0 --extra-index-url https://download.pytorch.org/whl/cu116
   mim install "mmengine>=0.6.0"
   mim install "mmcv>=2.0.0rc4,<2.1.0"
   mim install "mmdet>=3.0.0rc6,<3.1.0"
   pip install -r requirements/docs.txt
   mim install -v -e .
   cd mmyolo/models/ops_dcnv3/
   bash make.sh
   
   ```

4. You should change the dataset dir on the config. our CrowdHuman pth is available at https://pan.baidu.com/s/1kPkd0F0Afcd1bCS_BwVWPQ?pwd=YOLO or https://drive.google.com/file/d/1L2uFE8puwYjC2PU_3Y3idquayWJTwHze/view?usp=sharing.You can test the model with the following command

   ```bash
   python tools/test.py configs/yolov7/Crowdhuman/yolov7_w_p6_8xb16-300e_ignore_Crowdhuman.py best_crowd_human_mAP_epoch_159.pth
   ##you can got the result AP:93.51 mMR:37.04 JI:85.1
   python tools/test.py configs/yolov7/Crowdhuman/yolov7_w_p6_8xb16-300e_ignore_Crowdhuman.py best_crowd_human_mAP_epoch_159.pth --tta
   ##you can got the result AP:94.1 mMR:38.14 JI:84.56
   ```
