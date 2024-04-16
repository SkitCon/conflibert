# ConfliBERT
Repository for compilation and documentation of the multilingual ConfliBERT project

## Get Started:
* [Overview](#overview)
* [ConfliBERT Models](#conflibert-models)
* [Applications](#applications)
    * [Multi-class PLOVER Event Classifier](#multi-class-plover-event-classifier)
* Building your own domain-specific BERT
    * [Data Extraction Guide](#data-extraction)
    * [Filtering and Pre-Processing](#filtering-and-pre-processing)
    * [Pre-training](#pre-training)
* [Additional Data Sources](#additional-data-sources)
    * [UN Parallel Corpus](#un-corpus-pre-processing)

## Overview

This repository hosts relevant scripts and information related to the multilingual ConfliBERT project. This project has the goal of compiling all related code and documentation in one repository to allow for quick familiarization with our code and methodology.

ConfliBERT is a domain-specific language model based on BERT that is pre-trained on text relating to political conflict and violence. Results show that ConfliBERT consistently outperforms BERT when analyzing political conflict and violence[^1].

ConfliBERT is available in English, Spanish, and Arabic versions, with additional versions in French, Russian, and Hindi currently being developed.

Example applications using ConfliBERT are also documented in this repository. 

In this repository, we also supply information necessary to develop your own domain-specific models, including data extraction steps, pre-processing, and how to pre-train using BERT.

[^1]: https://aclanthology.org/2022.naacl-main.400.pdf

## ConfliBERT Models

### English

We provide four models in English:
1. ConfliBERT-scr-uncased:      Pretraining from scratch with our own uncased vocabulary (preferred)
2. ConfliBERT-scr-cased:      Pretraining from scratch with our own cased vocabulary
3. ConfliBERT-cont-uncased:      Continual pretraining with original BERT's uncased vocabulary
4. ConfliBERT-cont-cased:      Continual pretraining with original BERT's cased vocabulary

You can import the above four models directly via Huggingface API:

```
from transformers import AutoTokenizer, AutoModelForMaskedLM
tokenizer = AutoTokenizer.from_pretrained("snowood1/ConfliBERT-scr-uncased", use_auth_token=True)
model = AutoModelForMaskedLM.from_pretrained("snowood1/ConfliBERT-scr-uncased", use_auth_token=True)
```

### Spanish

Not yet uploaded

### Arabic

Not yet uploaded

### French

In development

### Russian

In development

### Hindi

In development

## Applications

### Multi-class PLOVER Event Classifier

Not yet completed

## Data Extraction

Data extraction (web scraping) is performed on websites with text in your target language and domain. In data extraction, there are two scripts available which can be configured to work with most online newspaper-style websites. One script extracts article text from HTML. The other is available for PDFs. These scripts are available in /data_extraction. Within data_extraction there are directories for each language with their respective scraping procedures.

## Filtering and Pre-Processing

To be uploaded

## Pre-training

Provided 

## Additional Data Sources

### UN Corpus Pre-Processing