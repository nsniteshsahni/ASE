# ASE
ASE is an abbr. for Auto Suggestion Engine written in python.No more incorrect spellings/words, just import AutoSuggest.py file to your project to get started

# Description
As the name suggests,it automatically suggests you the correct spelling for given word.It uses "RockYou.txt" as training dictionary in order to crawl correct spelling and suggest it to user.

It carries out the following processes:

- scans the text and extracts the words contained in it
- then compares each word with a known list of correctly spelled words (i.e. a dictionary). This might contain just a list of words, or it might also contain additional information, such as hyphenation points or lexical and grammatical attributes.
An additional step is a language-dependent algorithm for handling morphology. Even for a lightly inflected language like English, the spell-checker will need to consider different forms of the same word, such as plurals, verbal forms, contractions, and possessives. For many other languages, such as those featuring agglutination and more complex declension and conjugation, this part of the process is more complicated.

#Requirements & Usage
Nothing special,just need python 2.7.x+ to compile the AutoSuggest.py file.

In order to use this,follow these steps:

1. Download or clone the repository.
2. Place AutoSuggest.py and RockYou.txt in the same directory(in case you just extract the python file).
3. Now type
```
import AutoSuggest
```
in your python code file to use this and call
```
autosug('<Your input word>')
```
function from it.

The returned result would be corrected spelling(Gramatically),However,Just to test the Engine,Run AutoSuggest.py file and in python interperator type 
```
autosug('<Your input parameter>')
```

#License
The MIT License (MIT)

Copyright (c) 2016 Nitesh Sahni

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
