#!/usr/bin/env python3

class fasta:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_fasta_file(self):
        with open (self.filepath,'r') as f :
            d={} # placeholder locally defined dictionary for the output
            for line in f :
                l=line.strip()
                if l=="":
                    continue
                if l[0]==">":
                    d[l[1:]]=""
                    tmp=l[1:]
                    continue
                d[tmp]+=l
        return d         

    # def fasta_length(self):
    # def gc_content(self):
    # def k-mer_composition(self): 
    
        

if __name__=="__main__":
    print("Script for handling fasta file functions")

    # Dev Tests
    f=fasta('../tests/fasta_test_files/grph.fa')
    print(f.fasta_length())
