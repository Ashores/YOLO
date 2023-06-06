## Build Documentation

1. Clone YOLO_person

   ```bash
   git clone [https://github.com/open-mmlab/mmyolo.git](https://github.com/Ashores/YOLO_person)
   cd YOLO_person
   ```

2. Install the building dependencies of documentation

   ```bash
   create an torch environment
   pip install torch==1.13.0+cu116 torchvision==0.14.0+cu116 torchaudio==0.13.0 --extra-index-url https://download.pytorch.org/whl/cu116
   pip install -r requirements/docs.txt
   cd mmyolo/models/ops_dcnv3/
   bash make.sh
   
   ```

3. You should change the dataset dir on the config. our CrowdHuman pth is available at https://pan.baidu.com/s/1kPkd0F0Afcd1bCS_BwVWPQ?pwd=YOLO code:YOLO.You can test the model with the following command

   ```bash
   python tools/test.py configs/yolov7/Crowdhuman/yolov7_w_p6_8xb16-300e_ignore_Crowdhuman.py best_crowd_human_mAP_epoch_159.pth
   ##you can got the result AP:93.51 mMr:37.04 JI:85.1
   python tools/test.py configs/yolov7/Crowdhuman/yolov7_w_p6_8xb16-300e_ignore_Crowdhuman.py best_crowd_human_mAP_epoch_159.pth --tta
   ##you can got the result AP:94.1 mMR:38.14 JI:84.56
   ```
