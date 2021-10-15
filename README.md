# BBQ
Repository for the Bias Benchmark for QA dataset.

Authors: Alicia Parrish, Angelica Chen, Nikita Nangia, Vishakh Padmakumar, Jason Phang, Jana Thompson, Phu Mon Htut, and Samuel R. Bowman.

## About BBQ
It is well documented that NLP models learnsocial biases present in the world, but littlework has been done to show how these biasesmanifest in actual model outputs for appliedtasks like question answering (QA). We introduce the Bias Benchmark for QA (BBQ), adataset consisting of question-sets constructedby the authors that highlightattestedsocialbiases against people belonging to protectedclasses along nine different social dimensionsrelevant for U.S. English-speaking contexts.Our task evaluates model responses at two distinct levels: (i) given an under-informative context, test how strongly model answers reflectsocial biases, and (ii) given an adequately informative context, test whether the model’s biases still override a correct answer choice. Wefind that models strongly rely on stereotypeswhen the context is ambiguous, meaning thatthe model’s outputs consistently reproduceharmful biases in this setting. Though modelsare much more accurate when the context provides an unambiguous answer, they still relyon stereotyped information and achieve an accuracy 2.5 percentage points higher on examples where the correct answer aligns with a social bias, with this accuracy difference widening to over 5 points for examples targeting gender.

## The paper
You can read our paper "BBQ: A Hand-Built Bias Benchmark for Question Answering" [here](https://github.com/nyu-mll/BBQ/blob/main/QA_bias_benchmark.pdf).

## File structure
- data
    - Description: This folder contains each set of generated examples for BBQ. This is the folder you would use to test BBQ.
    - Contents: 11 jsonl files, each containing all templated examples. Each category is a separate file.
- results
    - Description: This folder contains our results after running BBQ on UnifiedQA
    - Contents: 11 jsonl files, each containing all templated examples and three sets of results for each example line:
        - Predictions using ARC-format
        - Predictions using RACE-format
        - Predictions using a question-only baseline
- supplemental
    - Description: Additional files used in validation and selecting names for the vocabulary
    - Contents: 
        - MTurk_validation contains the HIT templates, scripts, input data, and results from our MTurk validations
        - name_job_data contains files downloaded that contain name & demographic information or occupation prestige scores for developing these portions of the vocabulary
- templates
    - Description: This folder contains all the templates and vocabulary used to create BBQ
    - Contents: 11 csv files that contain the templates used in BBQ, 1 csv file listing all filler items used in the validation, 2 csv files for the BBQ vocabulary.

