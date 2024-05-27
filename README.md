# FPS Experiments
The experiments related to different Python version with different OpenCV backend frameworks.

#### The experiment shows the the different python version with different opencv versions the FPS on the same video is different.

I extended this experiment using the different video codecs also please check the `utils` for that.

Conda treat the Python as packages: to search the available python version you use the conda search:
```bash
(base) usman@saikhu:~ conda search python
```


To regenerate `conda env` for the experiment 0 and experiment 1 conda env file `exp0.yml` and `exp1.yml`.

```bash
conda env create -f exp0.yml
conda env create -f exp1.yml
```

# 
### Results

#### 1. Video 
Experiment 0:
    
```bash
Python Version: 3.5.4 |Anaconda, Inc.| (default, Feb 19 2018, 10:59:04) 
[GCC 7.2.0]
OpenCV Version: 3.4.11.41

FPS Results:
Backend: CAP_ANY, Frame Size: 640x480, Average FPS: 506.8247207168017
Backend: CAP_ANY, Frame Size: 1280x720, Average FPS: 559.6322759264818
Backend: CAP_ANY, Frame Size: 1920x1080, Average FPS: 601.2227129319452
```

Experiment 1:

```bash
Python Version: 3.12.3 | packaged by Anaconda, Inc. | (main, May  6 2024, 19:46:43) [GCC 11.2.0]
OpenCV Version: 4.9.0.80

FPS Results:
Backend: CAP_ANY, Frame Size: 640x480, Average FPS: 492.0691568676449
Backend: CAP_ANY, Frame Size: 1280x720, Average FPS: 584.7814478496131
Backend: CAP_ANY, Frame Size: 1920x1080, Average FPS: 584.6665105438649
```

#### 2. Camera

Logi camera is used for this experment.

```bash
Python Version: 3.10.0 (default, Mar  3 2022, 09:58:08) [GCC 7.5.0]
OpenCV Version: 4.8.1

FPS Results:
Backend: CAP_ANY, Frame Size: 640x480, Average FPS: 30.131996452814445
Backend: CAP_V4L2, Frame Size: 640x480, Average FPS: 28.14882036200088
Backend: CAP_GSTREAMER, Frame Size: 640x480, Average FPS: 30.09294415372491
Backend: CAP_ANY, Frame Size: 1280x720, Average FPS: 10.042207975430026
Backend: CAP_V4L2, Frame Size: 1280x720, Average FPS: 9.614235776145652
Backend: CAP_GSTREAMER, Frame Size: 1280x720, Average FPS: 10.042566717950917
Backend: CAP_ANY, Frame Size: 1920x1080, Average FPS: 5.040105165936439
Backend: CAP_V4L2, Frame Size: 1920x1080, Average FPS: 4.889260049903907
Backend: CAP_GSTREAMER, Frame Size: 1920x1080, Average FPS: 5.0417093074327015
```

```bash
Python Version: 3.6.13 |Anaconda, Inc.| (default, Jun  4 2021, 14:25:59) 
[GCC 7.5.0]
OpenCV Version: 3.4.18

FPS Results:
Backend: CAP_ANY, Frame Size: 640x480, Average FPS: 28.15196610518058
Backend: CAP_V4L2, Frame Size: 640x480, Average FPS: 28.15489709674507
Backend: CAP_ANY, Frame Size: 1280x720, Average FPS: 9.675097824088883
Backend: CAP_V4L2, Frame Size: 1280x720, Average FPS: 9.644858762614758
Backend: CAP_ANY, Frame Size: 1920x1080, Average FPS: 4.857731930680163
Backend: CAP_V4L2, Frame Size: 1920x1080, Average FPS: 4.857714714885553
```


# 
Note: these experiments still need more work and will update new experiment results in more structure format.