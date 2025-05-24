import textstat

def count_word_usage(tokens, words):
    """
    Count the number of times a word appears in a list of tokens.
    :param tokens: list of tokens
    :param words: list of words to count
    :return: number of times the word appears
    """

    count = 0
    for token in tokens:
        if token in words:
            count += 1

    return count

def compute_total_average_word_length(sentence_list):
    """
    Compute the average word length in a list of sentences.
    :param sentence_list: list of tokenized sentences
    :return: average word length
    """
    total_length = 0
    total_words = 0

    for tokens in sentence_list:
        for token in tokens:
            total_length += len(token)
            total_words += 1

    if total_words == 0:
        return 0
    
    return total_length / total_words

def compute_total_unique_words_fraction(sentence_list):
    """
    Compute the fraction of unique words in a list of sentences.
    :param sentence_list: list of tokenized sentences
    :return: fraction of unique words
    """

    unique_words = set()
    total_words = 0
    for tokens in sentence_list:
        for token in tokens:
            unique_words.add(token)
            total_words += 1

    if total_words == 0:
        return 0
    return len(unique_words) / total_words

def count_total_syllables(sentence_list):
    """
    Count the total number of syllables in a list of sentences.
    :param sentence_list: list of tokenized sentences
    :return: total number of syllables
    """
    total_syllables = 0
    for tokens in sentence_list:
        for token in tokens:
            total_syllables += textstat.syllable_count(token)

    return total_syllables

def count_total_words(sentence_list):
    """
    Count the total number of words in a list of sentences.
    :param sentence_list: list of tokenized sentences
    :return: total number of words
    """
    total_words = 0
    for tokens in sentence_list:
        total_words += len(tokens)

    return total_words

def compute_flesch_reading_ease(number_of_words, number_of_sentences, number_of_syllables):
    """
    Compute the Flesch reading ease score.
    :param number_of_words: total number of words
    :param number_of_sentences: total number of sentences
    :param number_of_syllables: total number of syllables
    :return: Flesch reading ease score
    """

    w_by_s = 1.015 * (number_of_words / number_of_sentences)
    sy_by_w = 84.6 * (number_of_syllables / number_of_words)
    flesch_score = 206.835 - w_by_s - sy_by_w

    return flesch_score

def get_reading_level_from_flesch(flesch_score):
    """
    Get the reading level from the Flesch reading ease score.
    :param flesch_score: Flesch reading ease score
    :return: reading level
    """

    if flesch_score >= 90:
        return "5th grade"
    elif flesch_score >= 80:
        return "6th grade"
    elif flesch_score >= 70:
        return "7th grade"
    elif flesch_score >= 60:
        return "8th-9th grade"
    elif flesch_score >= 50:
        return "10th-12th grade"
    elif flesch_score >= 30:
        return "College"
    else:
        return "College graduate"