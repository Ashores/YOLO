_base_ = '../yolov7_w-p6_syncbn_fast_8x16b-300e_coco.py'

# Use the model trained on the COCO as the pretrained model
# load_from = 'https://download.openmmlab.com/mmyolo/v0/yolov7/yolov7_w-p6_syncbn_fast_8x16b-300e_coco/yolov7_w-p6_syncbn_fast_8x16b-300e_coco_20221123_053031-a68ef9d2.pth'  # noqa
# load_from = '/hy-tmp/mmyolo/work_dirs/yolov7_w_p6_8xb16-300e_ignore_Crowdhuman/best_crowd_human_mAP_epoch_159.pth'
# dataset settings
data_root = '/hy-tmp/CrowdHuman/'
dataset_type = 'YOLOv5CrowdHumanDataset'

# parameters that often need to be modified
num_classes = 1

anchors = [
    [(10, 19), (15, 36), (35, 35)],
    [(23, 57), (32, 81), (44, 116)], 
    [(72, 72), (62, 162), (86, 232)],
    [(121, 332), (178, 475), (295, 732)] # P6/64
]
model = dict(
    bbox_head=dict(
        head_module=dict(num_classes=num_classes),
        prior_generator=dict(base_sizes=anchors)))

train_dataloader = dict(
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        ann_file='train.odgt',
        data_prefix=dict(img='images/')))

val_dataloader = dict(
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        ann_file='val.odgt',
        data_prefix=dict(img='images/'),
        # CrowdHumanMetric does not support out-of-order output images
        # for the time being. batch_shapes_cfg does not support.
        batch_shapes_cfg=None))
test_dataloader = val_dataloader

val_evaluator = dict(
    _delete_=True,
    type='mmdet.CrowdHumanMetric',
    ann_file=data_root + 'val.odgt',
    metric=['AP', 'MR', 'JI'])
test_evaluator = val_evaluator
