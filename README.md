# Arabic-QA-Datasets

data format (SQuAD format):

```
file.json
├── "data"
│   └── [i]
│       ├── "paragraphs"
│       │   └── [j]
│       │       ├── "context": "paragraph text"
│       │       └── "qas"
│       │           └── [k]
│       │               ├── "answers"
│       │               │   └── [l]
│       │               │       ├── "answer_start": N
│       │               │       └── "text": "answer"
│       │               ├── "id": "<uuid>"
│       │               └── "question": "paragraph question?"
│       └── "title": "document id"
└── "version": XXX
```

## Datasets:
- [ARCD and Arabic-SQuAD](https://github.com/husseinmozannar/SOQAL)
- [AAQAD](https://github.com/EmanElrefai/AAQAD)
- [TyDi QA: A Benchmark for Information-Seeking Question Answering in Typologically Diverse Languages](https://github.com/google-research-datasets/tydiqa)
- [MLQA](https://github.com/facebookresearch/MLQA)


| Dataset       | Q/A Pairs | Paragraphs | Articles |
|---------------|-----------|------------|----------|
| Arabic-SQuAD  | 48,344    | 10,364     | -       |
| AAQAD         | 17,911    | 3,381      | 299     |
| TyDiQA        | 16,425    | 15,726     | -       |
| MLQA          | 5,852     | 5,085      | 2,627   |
| ARCD          | 1,395     | 465        | 155     |
| **Total**     | **89,927**| **35,021** | **19,038** |





<!-- https://github.com/WissamAntoun/Arabic_QA_Datasets -->
