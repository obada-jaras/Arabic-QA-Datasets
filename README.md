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

Datasets:
- [ARCD and Arabic-SQuAD](https://github.com/husseinmozannar/SOQAL/tree/master)
- [TyDi QA: A Benchmark for Information-Seeking Question Answering in Typologically Diverse Languages](https://github.com/google-research-datasets/tydiqa)
- [MLQA](https://github.com/facebookresearch/MLQA)
- [FINAL_AAQAD](https://github.com/EmanElrefai/AAQAD)

<!-- https://github.com/WissamAntoun/Arabic_QA_Datasets -->
