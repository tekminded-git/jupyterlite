import os
import re
import json
import textwrap

CURRICULUM = 'content/python_finance_tutorials.md'
OUTPUT_DIR = 'content/lessons'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# parse curriculum
lessons=[]
current=None
with open(CURRICULUM, 'r') as f:
    for line in f:
        m=re.match(r'^(\d{2})\s-\s(.+):', line.strip())
        if m:
            if current:
                lessons.append(current)
            current={'num':int(m.group(1)), 'title':m.group(2).strip(), 'lines':[]}
        elif current is not None:
            current['lines'].append(line.rstrip())
if current:
    lessons.append(current)

# helper to create markdown cell
def md(text):
    return {"cell_type":"markdown","metadata":{},"source":textwrap.dedent(text).strip().splitlines(True)}

# helper to create code cell
def code(text):
    return {"cell_type":"code","metadata":{},"execution_count":None,"outputs":[],"source":textwrap.dedent(text).strip().splitlines(True)}

def generic_examples():
    """Return a list of (title, code) tuples with progressively complex examples."""
    examples = [
        ("Preview Orders Data", "orders.head()"),
        ("Count Total Orders", "print('Total orders:', len(orders))"),
        ("Merge Orders with Items", "merged = order_items.merge(orders, on='OrderID')\nmerged.head()"),
        (
            "Revenue by Product Category",
            "temp = order_items.merge(orders, on='OrderID').merge(products, on='ProductID')\nrevenue = temp.groupby('ProductCategory')['PurchaseAmount'].sum()\nrevenue.head()",
        ),
        (
            "Plot Daily Order Counts",
            "orders['OrderDate'] = pd.to_datetime(orders['OrderDate'])\ndaily = orders.set_index('OrderDate').resample('D').size()\ndaily.plot(figsize=(8,4))",
        ),
    ]
    return examples

for lesson in lessons:
    num=lesson['num']
    title=lesson['title']
    slug=title.lower().replace(' ','_')
    cells=[]
    # introduction from first two lines
    desc=[]
    concepts=[]
    exercises=[]
    mode='desc'
    for l in lesson['lines']:
        if re.match(r'-?\s*concepts', l.strip().lower()):
            mode='concepts'
            if ':' in l:
                concepts.append(l.split(':',1)[1].strip())
        elif re.match(r'-?\s*exercises', l.strip().lower()):
            mode='ex'
        else:
            if mode=='desc':
                if l.strip().startswith('-'):
                    desc.append(l.strip('- ').strip())
            elif mode=='concepts':
                if l.strip().startswith('-'):
                    concepts.append(l.strip('- ').strip())
                else:
                    concepts.append(l.strip())
            elif mode=='ex':
                m=re.match(r'\s*\d+\.\s*(.*)', l)
                if m:
                    exercises.append(m.group(1).strip())
    intro=' '.join(desc)
    objective_items=[c for c in concepts if c]
    # Build cells
    cells.append(md(f"# Lesson {num:02d} – {title}\n\n{intro}"))
    if objective_items:
        obj_md='\n'.join([f"- {o}" for o in objective_items])
        cells.append(md(f"## Learning Objectives\n{obj_md}"))
    # Standard dataset load code
    cells.append(md("## Loading the E-commerce Dataset"))
    cells.append(code("""import pandas as pd
import sys
sys.path.append('python4finance')
from generate_ecommerce_dataset import generate_ecommerce_dataset

orders, order_items, products = generate_ecommerce_dataset()
"""))
    cells.append(md("The dataset provides Orders, Order Items, and Products tables for analysis."))

    # Add example code cells based on exercises or use generic examples
    example_count = 1
    for title_text, code_text in generic_examples():
        cells.append(md(f"### Example {example_count}: {title_text}"))
        cells.append(code(code_text))
        example_count += 1

    if exercises:
        ex_md='\n'.join([f"{i+1}. {e}" for i,e in enumerate(exercises)])
        cells.append(md(f"## Exercises\n{ex_md}"))

    notebook={"cells":cells,"metadata":{},"nbformat":4,"nbformat_minor":5}
    fname=f"lesson_{num:02d}_{slug}.ipynb"
    with open(os.path.join(OUTPUT_DIR,fname), 'w') as f:
        json.dump(notebook,f,indent=2)

print(f"Generated {len(lessons)} notebooks in {OUTPUT_DIR}")
