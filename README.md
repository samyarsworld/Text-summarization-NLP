# Text-summarization-NLP

### Project plan

1 - Build project initialization setup using setuptools, os, and pathlib.

1.1 - Include logging feature.

2 - Build configuration class tools for different stages deep learning design to have one source of truth.

3 - Build model by importing data, building dataset, network, training, evaluation, and prediction pipelines.

4 - Keep track of the project on github and use github action for CD/CI and deployment.

5 - Containerize project using Docker.

6 - Deploy the model on AWS using S3, EC2, and possibly EKS service.

# Model

Pegasus transformer model from hugging face project is used.
https://huggingface.co/docs/transformers/model_doc/pegasus

# SentencePiece

SentencePiece from the Hugging Face Transformers library, is an unsupervised text tokenizer and detokenizer mainly used for neural network-based text generation tasks. [sentencepiece] is an optional extra that can be added to the Transformers library for installation.

# rouge_score

The ROUGE (Recall-Oriented Understudy for Gisting Evaluation) metric is a set of metrics used for the automatic evaluation of machine-generated text, especially in the context of text summarization and machine translation. The ROUGE metrics focus on comparing the overlap between the generated text and reference (human-written) text in terms of n-grams, word sequences, and other linguistic units.

Here are some key ROUGE metrics:

1. **ROUGE-N (unigram, bigram, trigram, etc.):**

Measures the overlap of n-grams (contiguous sequences of n words) between the generated text and the reference text.
ROUGE-1 considers unigrams, ROUGE-2 considers bigrams, and so on.

2. **ROUGE-L (Longest Common Subsequence):**

Measures the overlap in terms of the longest common subsequence (LCS) between the generated and reference texts. It considers word sequences that are common to both.

3. **ROUGE-W (Weighted Overlap):**

Similar to ROUGE-N but assigns different weights to different n-grams based on their lengths.

4. **ROUGE-S (Skip-bigram):**

Measures the overlap of skip-bigrams, which are pairs of words that are separated by a certain number of words in between.

5. **ROUGE-SU (Skip-bigram plus Unigram):**

Combines skip-bigram and unigram measures.

# BLEU score from sacrebleu library:

The BLEU (Bilingual Evaluation Understudy) score is a metric used to evaluate the quality of machine-generated translations by comparing them to one or more human-generated reference translations. It was proposed as a metric for automatic evaluation of machine translation output.

The BLEU score is based on the precision of the n-grams (contiguous sequences of n items, usually words) produced by the machine translation system. Here are the key components and concepts associated with the BLEU score:

1. **Precision of N-grams:**

   - BLEU measures the precision of the n-grams (typically unigrams, bigrams, trigrams, etc.) in the machine-generated translation compared to the reference translations.
   - Precision is calculated as the number of overlapping n-grams in the candidate translation that match the n-grams in the reference translations.

2. **Brevity Penalty:**

   - BLEU includes a brevity penalty to account for the fact that shorter translations tend to receive higher precision scores. Without this penalty, a very short translation could artificially inflate the BLEU score.
   - The brevity penalty penalizes translations that are shorter than the average length of the reference translations.

3. **Cumulative BLEU:**

   - BLEU is often calculated for different values of n (e.g., BLEU-1, BLEU-2, BLEU-3, BLEU-4), representing the precision of different orders of n-grams.
   - Cumulative BLEU scores consider the precision of n-grams up to a certain order, incorporating information from lower-order n-grams.

4. **Formula:**

   - The BLEU score is typically computed using the formula:

     ![BLEU Formula](<https://latex.codecogs.com/svg.latex?BLEU%20=%20BP%20\cdot%20\exp(\sum_{n=1}^N%20w_n%20\log(p_n))>)

     - \(BP\) is the brevity penalty.
     - \(N\) is the maximum order of n-grams considered.
     - \(w_n\) is the weight assigned to the precision of n-grams (commonly set to \(\frac{1}{N}\)).
     - \(p_n\) is the precision of n-grams.

5. **Interpretation:**
   - BLEU scores range from 0 to 1, with 1 indicating a perfect match between the machine-generated translation and the reference translations.
   - Higher BLEU scores generally indicate better translation quality, but the interpretation depends on the specific use case and language pair.

It's important to note that BLEU is just one of many metrics used to evaluate machine translation, and it has its limitations, such as sensitivity to word order and inability to capture semantic meaning comprehensively. Researchers often use a combination of metrics and conduct human evaluations for a more comprehensive assessment of translation quality.

# Workflow:

In order, each of these files need to update when we add a new pipeline (stage):

1- Update config.yaml
2- Update params.yaml
3- Update src/config
4- update the component
5- update the pipeline
6- update main.py
7- update app.py
