import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter

# 下载NLTK的停用词和WordNet词形还原器的资源
# 先执行 下载好后第二次可以不需要了
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')

# 读取文件地址
input_file_path = "a.txt"

# 将词频统计结果输出到txt文件
output_file_path = "b.txt"


# 将NLTK中的词性标签映射到WordNet中的词性标签
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return 'a'  # 形容词
    elif tag.startswith('V'):
        return 'v'  # 动词
    elif tag.startswith('N'):
        return 'n'  # 名词
    elif tag.startswith('R'):
        return 'r'  # 副词
    else:
        return 'n' # 默认为名词




# 读取txt文件并提取文本
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# 标准化单词
def normalize_word(word):
    # 传入的word是已经分词了的单词
    lemmatizer = WordNetLemmatizer()
    tagged_tokens = nltk.pos_tag([word])
    pos = get_wordnet_pos(tagged_tokens[0][1])
    return lemmatizer.lemmatize(word.lower(),pos)

# 主要处理函数：统计词频、标准化单词、过滤停用词
def process_text(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)  
    # word_tokenize 结果是一个字符串列表

    normalized_words = [normalize_word(word) for word in word_tokens if word.isalpha()]
    filtered_words = [word for word in normalized_words if word not in stop_words]
    word_freq = Counter(filtered_words)
    return word_freq


def write_counter_to_txt(counter, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for word, freq in counter.most_common():
            file.write(f"{word}: {freq}\n")





text = read_text_file(input_file_path)





# 处理文本并获取词频
word_freq = process_text(text)

# 输出前N个出现频率最高的单词及其频率
# N = 10
# print(len(word_freq))
# print(word_freq.most_common(N))


# 输出到txt
write_counter_to_txt(word_freq,output_file_path)


