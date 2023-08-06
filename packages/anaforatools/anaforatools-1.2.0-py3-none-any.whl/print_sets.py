import os

import anafora

root = '/Users/bethard/Data/thymedata'
text_roots = ['/Users/bethard/Data/THYME-corpus/train', '/Users/bethard/Data/THYME-corpus/dev']

for input_dir, output_dir, text_name, xml_names in anafora.walk_anafora_to_anafora(root):
    for text_root in text_roots:
        text_path = os.path.join(text_root, text_name)
        if os.path.exists(text_path):
            text = open(text_path).read().decode('utf-8')
            for xml_name in xml_names:
                if 'Temporal' in xml_name:
                    data = anafora.AnaforaData.from_file(os.path.join(root, input_dir, xml_name))
                    for ann in data.annotations.select_type('TIMEX3'):
                        if ann.properties['Class'] == 'SET':
                            ann_text = '...'.join(text[begin:end] for begin, end in ann.spans)
                            print(ann_text)
