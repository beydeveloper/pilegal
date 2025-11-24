from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import json
import os
import random
from collections import defaultdict

app = Flask(__name__)
CORS(app)

data_cache = []
category_index = defaultdict(list)
search_index = {}
DATA_FILE = 'pilegal_data_v1.jsonl'

def normalize_category(category):
    if not category or category == 'general':
        return 'general'
    category = str(category).lower().strip()
    
    category_mapping = {
        'programming': ['code', 'coding', 'program', 'programming', 'python', 'javascript', 'java', 'c++', 'csharp'],
        'security': ['security', 'cyber', 'cybersecurity', 'exploit', 'vulnerability', 'hacking', 'pentest'],
        'data_science': ['data', 'ml', 'machine learning', 'ai', 'artificial intelligence', 'analytics'],
        'web': ['web', 'html', 'css', 'frontend', 'backend', 'fullstack', 'http'],
        'database': ['database', 'sql', 'mysql', 'postgresql', 'mongodb', 'db'],
        'network': ['network', 'networking', 'tcp', 'ip', 'routing'],
        'system': ['system', 'linux', 'windows', 'os', 'operating system']
    }
    
    for main_cat, keywords in category_mapping.items():
        if any(keyword in category for keyword in keywords):
            return main_cat
    
    return category

def load_data():
    global data_cache, category_index, search_index
    print(f"Loading data: {DATA_FILE}")
    
    if not os.path.exists(DATA_FILE):
        print(f"ERROR: {DATA_FILE} not found!")
        return
    
    data_cache = []
    category_index.clear()
    search_index.clear()
    
    try:
        with open(DATA_FILE, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if line:
                    try:
                        data = json.loads(line)
                        
                        original_category = data.get('category', 'general')
                        normalized_category = normalize_category(original_category)
                        data['category'] = normalized_category
                        
                        idx = len(data_cache)
                        data_cache.append(data)
                        
                        category_index[normalized_category].append(idx)
                        
                        instruction = data.get('instruction', '').lower()
                        output = data.get('output', '').lower()
                        search_text = f"{instruction} {output}"
                        search_index[idx] = search_text
                        
                    except (json.JSONDecodeError, KeyError, ValueError):
                        if line_num % 100000 == 0:
                            print(f"Processing line {line_num}...")
                        continue
                
                if line_num % 500000 == 0:
                    print(f"✅ Loaded {len(data_cache)} records so far...")
        
        print(f"✅ {len(data_cache)} records loaded successfully")
        print(f"📊 Categories: {len(category_index)} unique categories")
        
    except Exception as e:
        print(f"Data loading error: {e}")

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/api/stats', methods=['GET'])
def get_stats():
    categories = {cat: len(indices) for cat, indices in category_index.items()}
    
    return jsonify({
        'total_records': len(data_cache),
        'categories': categories,
        'top_categories': sorted(categories.items(), key=lambda x: x[1], reverse=True)[:10]
    })

@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('q', '').lower().strip()
    category = request.args.get('category', 'all')
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 20))
    
    if category != 'all' and category in category_index:
        candidate_indices = category_index[category]
    else:
        candidate_indices = range(len(data_cache))
    
    if query:
        matching_indices = []
        query_terms = query.split()
        
        for idx in candidate_indices:
            if idx >= len(data_cache):
                continue
            
            search_text = search_index.get(idx, '')
            if all(term in search_text for term in query_terms):
                matching_indices.append(idx)
                
                if len(matching_indices) >= 1000:
                    break
        
        results = [data_cache[idx] for idx in matching_indices]
    else:
        results = [data_cache[idx] for idx in candidate_indices]
    
    total = len(results)
    start = (page - 1) * limit
    end = start + limit
    paginated_results = results[start:end]
    
    return jsonify({
        'results': paginated_results,
        'total': total,
        'page': page,
        'limit': limit,
        'total_pages': (total + limit - 1) // limit if total > 0 else 0
    })

@app.route('/api/categories', methods=['GET'])
def get_categories():
    category_list = [
        {'name': 'programming', 'label': 'Programlama', 'count': len(category_index.get('programming', []))},
        {'name': 'security', 'label': 'Güvenlik', 'count': len(category_index.get('security', []))},
        {'name': 'data_science', 'label': 'Veri Bilimi', 'count': len(category_index.get('data_science', []))},
        {'name': 'web', 'label': 'Web Geliştirme', 'count': len(category_index.get('web', []))},
        {'name': 'database', 'label': 'Veritabanı', 'count': len(category_index.get('database', []))},
        {'name': 'network', 'label': 'Ağ', 'count': len(category_index.get('network', []))},
        {'name': 'system', 'label': 'Sistem', 'count': len(category_index.get('system', []))},
        {'name': 'general', 'label': 'Genel', 'count': len(category_index.get('general', []))}
    ]
    
    return jsonify({
        'categories': category_list,
        'total': len(category_index)
    })

@app.route('/api/random', methods=['GET'])
def get_random():
    if len(data_cache) == 0:
        return jsonify({
            'instruction': 'Veri yok',
            'output': 'Henüz veri yüklenmedi.',
            'category': 'system'
        })
    
    item = random.choice(data_cache)
    return jsonify(item)

if __name__ == '__main__':
    print("=" * 50)
    print("📚 PiLegal Knowledge Base")
    print("=" * 50)
    
    load_data()
    
    if len(data_cache) == 0:
        print("⚠️  WARNING: No data loaded!")
        print("Please ensure pilegal_data_v1.jsonl exists.")
    else:
        print(f"\n✅ Ready to serve {len(data_cache):,} articles")
    
    print("\n🚀 Server starting...")
    print("📍 URL: http://localhost:5000")
    print("🔍 API: http://localhost:5000/api/search?q=python")
    print("\nPress Ctrl+C to stop\n")
    
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
