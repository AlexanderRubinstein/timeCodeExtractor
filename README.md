**Problem**: extraction of slides timecodes from video lectures.

Presentations are often used as supplementary materials in video lectures.
Our goal is to extract timecodes of each slide and provide those slides.

The expected application of CV in our project is the following:
* presentation slide detection on the video frame;
* extraction and projective transformation of the slide;
* matching of slides keypoints for two consequetive frames.

Dataset consists of educational video lecture with supplementary presentation slides (e.g. [Generalized nonparametric method. An appendix to stock market analysis.](https://www.youtube.com/watch?v=u77WVB7mJMw&index=38&list=PLIvQImOQgbGbD1KLR4Pg_vipxuW5WeOx1)).

We plan to use the following CV methods:
* [Canny edge detection algorithm](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.420.3300&rep=rep1&type=pdf);
* [Harris-Laplacian keypoints detection algorithm](https://hal.inria.fr/inria-00548276/document).
