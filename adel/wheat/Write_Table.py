def Write_Table(Table,filename):
    '''
    returns a string representation of the content of the table
    '''
    
    header = [' '.join(Table.keys())]
    rows = zip(*[Table[k] for k in Table.keys()])
    lines = [' '.join(map(str,r)) for r in rows]
    fout = open(filename,"w")
    fout.write('\n'.join(header + lines))
    fout.close()
    
    return filename,
