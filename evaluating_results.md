**MAT_LargeMask** 
- cfg:
    - val_img: follow paper
    - val_mask: follow paper
    - sample: follow paper
- metrics:
    - fid: 5.421466551712873
    - pids: 0.05412629468760441
    - uids: 0.16204477113264282
    - lpips: 0.1381715325877628
    - psnr: 23.222390064422967
    - ssim: 0.8006738261205346
    - l1: 0.03778517672420537

**Re-test-MAT_LargeMask** 
- cfg:
    - val_img: follow paper
    - val_mask: follow paper
    - sample: re-test
- metrics:
    - fid: 4.814876454773943
    - pids: 0.1259605746742399
    - uids: 0.23788840628132313
    - lpips: 0.1273492338861261
    - psnr: 23.458060170657706
    - ssim: 0.8232231067536491
    - l1: 0.033179636126687645

**00033-1024_LargeMask**
- cfg:
    - val_img: arange(0.jpg, 2993.jpg)
    - val_mask: random
- metrics:
    - fid: 16.88116169385414
    - pids: 0.007350484463748747
    - uids: 0.016204477113264337
    - lpips: 0.1990834317102395
    - psnr: 21.09112209990769
    - ssim: 0.802085329727634
    - l1: 0.04689736753496708

**00033-1024_SmallMask**
- cfg:
    - val_img: arange(0.jpg, 2993.jpg)
    - val_mask: random
- metrics:
    - fid: 7.204614476512072
    - pids: 0.056130972268626796
    - uids: 0.15536251252923483
    - lpips: 0.10412300956668186
    - psnr: 26.10195887965294
    - ssim: 0.8962156532374149
    - l1: 0.02368633730325002

**00013-512_LargeMask**
- cfg:
    - val_img: follow paper
    - val_mask: follow paper
- metrics:
    - fid: 5.181554809430678
    - pids: 0.1249582358837287
    - uids: 0.22736384898095552
    - lpips: 0.13526443669098268
    - psnr: 22.86274139897492
    - ssim: 0.8186109856256698
    - l1: 0.03535870744283149

**00014-512_LargeMask**
- cfg:
    - val_img: follow paper
    - val_mask: random
- metrics:
    - fid: 4.942399784805572
    - pids: 0.13197460741730704
    - uids: 0.24223187437353821
    - psnr: 22.882111395244323
    - ssim: 0.8200233077692402
    - l1: 0.034865919698751864

**00015-512_SmallMask**
- cfg:
    - val_img: follow paper
    - val_mask: follow paper
- metrics stg1:
    - fid: 3.468947926619543
    - pids: 0.14934847978616772
    - uids: 0.27965252255262274
- metrics:
    - fid: 2.9774290105929793
    - pids: 0.21583695289007684
    - uids: 0.32225192114934853
