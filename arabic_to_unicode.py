import json

def arabic_to_unicode(text):
    return ''.join(f'\\u{ord(c):04x}' for c in text)

def filter_long_examples(topic, max_total_length=250):
    new_paragraphs = []
    for paragraph in topic["paragraphs"]:
        new_qas = []
        for qa in paragraph["qas"]:
            question_length = len(qa["question"].split())
            context_length = len(paragraph["context"].split())
            if question_length + context_length <= max_total_length:
                new_qas.append(qa)
        if new_qas:
            new_paragraph = paragraph.copy()
            new_paragraph["qas"] = new_qas
            new_paragraphs.append(new_paragraph)
    return new_paragraphs

def process_squad_data(data):
    for topic in data["data"]:
        topic["paragraphs"] = filter_long_examples(topic)
        for paragraph in topic["paragraphs"]:
            paragraph["context"] = arabic_to_unicode(paragraph["context"])
            for qa in paragraph["qas"]:
                qa["question"] = arabic_to_unicode(qa["question"])
                for answer in qa["answers"]:
                    answer["text"] = arabic_to_unicode(answer["text"])
    return data

def convert_ids_to_string(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for article in data['data']:
        for paragraph in article['paragraphs']:
            for qa in paragraph['qas']:
                qa['id'] = str(qa['id'])

    with open(input_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def convert_arabic_squad_to_unicode(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)
    
    processed_data = process_squad_data(data)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(processed_data, outfile, ensure_ascii=False, indent=2)

input_file = "All Datasets/FINAL_AAQAD-v1.0.json"
output_file = "FINAL_AAQAD-v1.3.json"

convert_arabic_squad_to_unicode(input_file, output_file)
convert_ids_to_string(output_file)
