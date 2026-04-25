---
--- 
layout: post
title: An open source song comparison tool
description: "OpenShazam is an open-source audio fingerprinting tool for comparing song similarities, inspired by Shazam's algorithm with modifications for parallel processing, applied to cases like the Led Zeppelin plagiarism lawsuit."
git: https://github.com/kirtivr/osshazam
--- 

Audio fingerprinting to find how similar two songs are. An interesting use case was the Led Zeppelin v/s Taurus plagiarism <a href="http://www.rollingstone.com/music/news/led-zeppelin-prevail-in-stairway-to-heaven-lawsuit-20160623">lawsuit</a>.
I used a parallelizable FFT based fingerprinting algorithm based on Shazam's <a href="http://www.ee.columbia.edu/~dpwe/papers/Wang03-shazam.pdf">paper</a>, with some significant modifications.
The fun part was running the FFT based algorithm on our CS cluster at Dartmouth.
The results have been encouraging.
