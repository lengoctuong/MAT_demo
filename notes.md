**Env torch+cuda**

```bash
conda install pytorch torchvision cudatoolkit -c pytorch
``````

**Changed Code**

- ```generate_image.py```
    - Save mask (without mpath).
    - Add agrs: large-mask, hole-lrange, hole-rrange, seed. And codes based those.
- ```evaluation/cal_fid_pids_uids.py```, ```evaluation/cal_lpips.py```, ```evaluation/cal_psnr_ssim_l1.py```
    - Add case: convert 4 channels to RGB.
- ```networks/mat.py```
    - Add abs path for the torch_utils library.

**Quick Test**

```bash
CUDA_VISIBLE_DEVICES=2 python generate_image_having_stg1.py \
    --network pretrained/CelebA-HQ_512.pkl \
    --dpath test_sets/CelebA-HQ/images \
    --mpath test_sets/CelebA-HQ/masks \
    --maskdir test_sets/CelebA-HQ/masks \
    --outdir test_sets/CelebA-HQ/samples \
    --out1dir test_sets/CelebA-HQ/samples_stg1 \
    --large-mask True \
    --hole-lrange 0 \
    --hole-rrange 1 \
    --seed 99 \
    > test_sets/CelebA-HQ/stdout.txt \
    2> test_sets/CelebA-HQ/stderr.txt
```

```bash
CUDA_VISIBLE_DEVICES=2 python generate_image.py \
    --network pretrained/CelebA-HQ_512.pkl \
    --dpath test_sets/CelebA-HQ/images \
    --mpath test_sets/CelebA-HQ/masks \
    --outdir test_sets/CelebA-HQ/samples \
    --large-mask True \
    --hole-lrange 0 \
    --hole-rrange 1 \
    --seed 99 \
    > test_sets/CelebA-HQ/stdout.txt \
    2> test_sets/CelebA-HQ/stderr.txt
```

**Train**
```bash
python -W ignore
CUDA_VISIBLE_DEVICES=0,1 nohup python train.py \
    --outdir=saved_model \
    --gpus=2 \
    --snap=10 \
    --batch=8 \
    --metrics=fid2993_full \
    --data=/root/MAT/Data/CelebA-HQ/CelebA-HQ-img \
    --data_val=/root/MAT/Data/CelebA-HQ/CelebA-HQ-val_img \
    --dataloader=datasets.dataset_512.ImageFolderMaskDataset \
    --mirror=True \
    --cond=False \
    --cfg=celeba512 \
    --aug=noaug \
    --generator=networks.mat.Generator \
    --discriminator=networks.mat.Discriminator \
    --loss=losses.loss.TwoStageLoss \
    --pr=0.1 \
    --pl=False \
    --truncation=0.5 \
    --style_mix=0.5 \
    --ema=10 \
    --lr=0.001 \
    > stdout_bash/train_stdout.txt \
    2> stdout_bash/train_stderr.txt &
```

**Final models**

Ours
- saved_model/00033-CelebA-HQ-img-mirror-celeba512-mat-lr0.001-TwoStageLoss-pr0.1-nopl-kimg200-batch12-tc0.5-sm0.5-ema10-noaug-resumecustom/network-snapshot-000200.pkl

Paper:
- pretrained/CelebA-HQ_512.pkl
- pretrained/00032-CelebA-HQ-img-mirror-celeba512-mat-lr0.001-TwoStageLoss-pr0.1-nopl-kimg4-batch12-tc0.5-sm0.5-ema10-noaug-resumecustom/network-snapshot-000004.pkl

**Merits/demerits**
- Demerits: mask là random vì vậy model có thể ko học được cách mask xác định (ví dụ như những mask che các bộ phận mắt, mũi, miệng,..) khi đó model sẽ không nhận thức được bộ phận đó để phục hồi.

**Some problem**
- Chạy thử Evaluating metrics... (metrics/metric_main/fid2993_full)
- metrics/metric_main/fid2993_full (Evaluating metrics...) vs evaluation/cal_fid_pids_uids
- metrics/metric_main/fid2993_full (Evaluating metrics...) của re-train trên 1024 > re-train trên paper