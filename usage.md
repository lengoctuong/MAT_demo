**Quick Test**
```bash
python generate_image.py --network pretrained/CelebA-HQ_512.pkl --dpath test_sets/CelebA-HQ/images --mpath test_sets/CelebA-HQ/masks --outdir test_sets/CelebA-HQ/samples > test_sets/CelebA-HQ/stdout.txt 2> test_sets/CelebA-HQ/stderr.txt
```
**Tran**
```bash
python train.py \
    --outdir=saved_model \
    --gpus=8 \
    --batch=32 \
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
    --lr=0.001
```
