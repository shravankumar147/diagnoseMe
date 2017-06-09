# diagnoseMe

## Overview

This is a simple basic experiment to diagnose given symptoms of a patient. 
The program will take inputs as patient information, such as name, age, sex, etc., and the symptoms. After diagnosing using machine intelligence it provides the higest probable codition for the given symptoms as diagnosis results. 

## Dependencies

```sudo pip install -r requirements.txt```

## Usage

Once dependencies are installed, just run this to see it in your terminal. 

```
cd myexperiments
python test2.py -s "male" -a 25
```

That's it! If you performed everything correctly you will see the following.

```
==========
Your Personal Doctor
==========
--------
How would you describe intensity of your abdominal pain?
--------
--------
Yes
--------


Diagnosis Results:
********
It is possibly the following condition according to the mentioned symptoms
Cystitis with probability being 0.0772
******** 
```
