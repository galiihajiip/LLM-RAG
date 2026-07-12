import json, re

ansi = re.compile(r'\x1b\[[0-9;]*m')

with open('RAG_submission_PGABL_Galih_Aji_Pangestu_executed.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

errors_found = []
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        for output in cell.get('outputs', []):
            if output.get('output_type') == 'error':
                errors_found.append((i+1, output))

print(f'Total error cells: {len(errors_found)}')
for cell_num, out in errors_found:
    print(f'\n=== ERROR di Cell {cell_num} ===')
    print(f'Type: {out.get("ename")} - {out.get("evalue", "")[:300]}')
    tb = out.get('traceback', [])
    print('--- Last 8 lines of traceback ---')
    for line in tb[-8:]:
        print(ansi.sub('', line))
