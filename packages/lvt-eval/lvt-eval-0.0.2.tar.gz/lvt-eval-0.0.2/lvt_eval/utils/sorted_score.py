import json

import os
def save_json(jsondata, file):
    if not os.path.exists(file):
        os.makedirs(file.rsplit('/', 1)[0], exist_ok=True)
    with open(file, "w", encoding='utf-8') as f:
        json.dump(jsondata, f, ensure_ascii=False, indent=2)



data = json.load(open('/home/liaojiajia/download/0823/yh_pred_v2.json'))
results = []
new_results = {}

for k in range(1512):
    rr = []
    for d in data: 
        if d['image_id'] == k:
            rr.append(d)
    rn = sorted(rr, key=lambda k: k['score'], reverse = True)
    new_results[k] = rn[:100]
    results.extend(new_results[k])
save_json(results, '/home/liaojiajia/download/0823/yh_pred_100.json')  


    
