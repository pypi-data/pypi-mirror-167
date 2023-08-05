def word_tokenize(text, language="english", preserve_line=False):
    """
    Return a tokenized copy of *text*,
    :param text: text to split into words
    :type text: str
    :param language: the model name in the Punkt corpus
    :type language: str
    :param preserve_line: A flag to decide whether to sentence tokenize the text or not.
    :type preserve_line: bool
    """
    # return [
    #     token for sent in sentences for token in _treebank_word_tokenizer.tokenize(sent)
    #     ''.join(lst).split()
    # ]
    return ''.join(text).split()