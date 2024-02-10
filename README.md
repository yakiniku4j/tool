最近在学习英语，发现直接阅读原著还是有困难的。所以想着可不可以把书里的所有单词都统计出来 然后再看有多少词需要理解和背， 先熟悉单词再去看书。
然后就通过gpt 询问怎么用python做这样一件简单的事情（然后才发现其实背后也不简单）， 然后就知道了nltk这个工具（在这之前没有了解过自然语言处理相关的知识，也算是学到了一点东西。

跟着gpt的步骤，基本上没有改到什么代码，就完成了。
要完成这件事需要以下步骤：
1. 读取文件并提取文本 （文件可以是epub、txt等，因为我只需要统计词频，txt似乎更方便，所以用calibre把epub转换为了txt
要使用calibre提供的命令行工具，需要将其添加到PATH，
```
export PATH="/Applications/calibre.app/Contents/MacOS:$PATH"
```
then 使用ebook-convert命令就可以转换了， 这个用来管理电子书的软件还提供了许多的工具
```
ebook-convert /path/to/input/book.epub /path/to/output/book.txt
```
2. Tokenization 字符串分词
使用的是word_tokenize方法
3. 对单词进行标准化
似乎在自然语言处理里 把这个叫做词形归并 lemmatization
这个步骤主要是我需要统计的词频是单词的原形，而在文章中，可能同一个单词使用的时态不一样可能会被统计为不同的单词。
例如 running、和run，我都希望统计为run
4. 停用词过滤
在文章中，会出现许多人称代词、连词、介词、冠词这些在语法上是重要的，但是没有具体的重要信息。
所以就需要过滤掉

6. 统计词频
使用collections.Counter来进行统计

7. 输出结果
最后将统计结果输出到文件即可。

遇到的问题

我在使用WordNetLemmatizer进行词形归并的时候，发现有些单词是动名词，但是没有被归并到动词，
因为没有提供词性标签的话默认认为是名词。
但是NLTK提供了多个词性标注器(Part Of Speach taggers)
之后我就使用了pos_tag()方法，先标注词性，然后传入到标准化方法里。 
这样就可以将running标注为动词，然后就被归并为run了


以及还需要改进的
1. 很多高频单词都已经熟知，还需要进一步针对自身英语水平进行单词的过滤
   所以可以优化的点是将高频单词通过某种方式去除。或者将高频单词的这部分全部去除。
2. 获得了单词表后，还需要一个个查词， 如果可以再通过自动化查词翻译整理好就更好。（不过自己查词本身也是一种学习过程）






