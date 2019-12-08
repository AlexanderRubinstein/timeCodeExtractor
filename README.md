**Problem**: extraction of slides timecodes from video lectures.
Presentations are often used as supplementary materials in video lectures.
Our goal is to extract timecodes of each slide and provide those slides.

The expected value of CV in our project is the following:
* presentation slide detection on the video frame;
* extraction and projective transformation of the slide;
* matching of slides keypoints for two consequetive frames.

Dataset consists of video lecture with supplementary presentation slides (e.g. [How to Land the Space Shuttle... from Space](https://www.youtube.com/watch?v=Jb4prVsXkZU&feature=emb_logo)).

We plan to use the following CV methods:
* [Canny edge detection algorithm](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.420.3300&rep=rep1&type=pdf);
* [Harris-Laplacian keypoints detection algorithm](https://hal.inria.fr/inria-00548276/document).
