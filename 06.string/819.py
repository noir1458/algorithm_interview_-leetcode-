import re, collections
def extract_words(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
    counts = collections.defaultdict(int)
    counts = collections.Counter(words)
    
    return counts.most_common(1)[0][0]


if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(extract_words(paragraph, banned))  # Output: ['bob', 'a', 'ball', 'the', 'ball', 'flew', 'far', 'after', 'it', 'was']