import nltk
import argparse
from utils import (
    count_word_usage,
    compute_total_average_word_length,
    compute_total_unique_words_fraction,
    count_total_syllables,
    count_total_words,
)


def parse_arguments():
    """
    :return: the text to be edited
    """

    parser = argparse.ArgumentParser(
        description="Receive text to be edited"
    )
    parser.add_argument(
        'text',
        metavar='input_text',
        type=str,
    )

    args = parser.parse_args()
    return args.text

def clean_input(input_text):
    """
    :params text: text too be edited
    :return: cleaned text
    """

    return str(input_text.encode().decode('ascii', errors='ignore'))

def preprocess_input(text):
    """
    :param text: text to be preprocessed
    :return: tokenized sentences
    """

    sentences = nltk.sent_tokenize(text)
    tokens = [nltk.word_tokenize(sentence) for sentence in sentences]
    return tokens

def get_suggestions(sentence_list):
    """
    :param sentence_list: list of tokenized sentences
    :return: list of suggestions
    """

    told_said_usage = sum(
        (count_word_usage(tokens, ['told', 'said']) for tokens in sentence_list)
    )

    but_and_usage = sum(
        (count_word_usage(tokens, ['but', 'and']) for tokens in sentence_list)
    )

    wh_adverb_usage = sum(
        (
            count_word_usage(
                tokens,
                [
                    'when',
                    'where',
                    'why',
                    'whence',
                    'whereby',
                    'wherein',
                    'whereupon',
                ],
            )
            for tokens in sentence_list
        )
    )

    result_str = ""
    adverb_usage = "Adverb usage: %s told/said, %s but/and, %s wh-adverb\n" % (
        told_said_usage, but_and_usage, wh_adverb_usage
    )
    result_str += adverb_usage
    average_word_length = compute_total_average_word_length(sentence_list)
    unique_words_fraction = compute_total_unique_words_fraction(sentence_list)

    word_stats = "Average word length: %s, Unique words fraction: %s\n" % (
        average_word_length, unique_words_fraction
    )

    result_str = "<br/>"
    result_str += word_stats

    number_of_syllables = count_total_syllables(sentence_list)
    number_of_words = count_total_words(sentence_list)
    number_of_sentences = len(sentence_list)

    syllable_counts = "%d syllables, %d words, %d sentences\n" % (
        number_of_syllables, number_of_words, number_of_sentences
    )

    result_str += "<br/>"
    result_str += syllable_counts

    flesh_score = compute_flesch_reading_ease(
        number_of_words, number_of_sentences, number_of_syllables
    )

    flesh = "%d syllabes, %.2f Flesch reading ease\n %s" % (
        number_of_syllables,
        flesh_score,
        get_reading_level_from_flesch(flesh_score), 
    )

    result_str += "<br/>"
    result_str += flesh

    return result_str



input_text = parse_arguments()
processed = clean_input(input_text)
tokenized_sentences = preprocess_input(processed)
print(tokenized_sentences)
# suggestions = get_suggestions(tokenized_sentences)

