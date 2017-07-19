import io
from nbformat import read

def execute_notebook(nbfile):
    
    with io.open(nbfile, 'r', encoding=('utf-8')) as f:
        nb = read(f, 4)
    
    ip = get_ipython()
    
    for cell in nb.cells:
        if cell.cell_type != 'code':
            continue
        ip.run_cell(cell.source)
