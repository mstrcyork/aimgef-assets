# Introduction

This repository contains the stimuli used in the listening study and a sheet file showing the ratings for each stimulus.

## Stimuli 
The MIDI files can be found in the `stimuli` folder where each file is named with the index corresponding to its category:

| |CSQ|CPI|
|:-|:-|:-|
|Orig|1-25|151-175|
|MuTr|101-125|201-225|
|MVAE|76-100|176-200|
|MaMa|26-50|-|
|CoRe|51-75|-|
|BeAf|126-150|-|
|LiTr|-|226-250|

## Ratings
`ratings.csv` contains the ratings of stimuli which received from the listening study:

|Column name|Description|
|:-|:-|
|id|The name of index associated with the above table|
|ss|Stylistic success rating|
|ap|Aesthetic pleasure rating|
|re|Repetition rating|
|me|Melody rating|
|ha|Harmony rating|
|rh|Rhythm rating|
|highlight|The optionally selected highlight sections|
|comment|The optional comment|

## Classical string quartets
`CSQ` folder contains 71 string quartets collected from [KernScores](http://kern.ccarh.org/), metadata for each of them is listed in `index.json`.
