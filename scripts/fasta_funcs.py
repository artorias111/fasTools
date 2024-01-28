#!/usr/bin/env python3

class fasta:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_fasta_file(self):
        with open (self.filepath,'r') as f :
            d={} # output dictionary
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

    def fasta_length(self):
        d=self.read_fasta_file() # Read the fasta file
        l={} # dictionary that stores "scaffold_name:size"
        for i in d:
            l[i]=len(d[i])        
        return l

    def get_gc_count(s): # s is a string
        for i in s:
            gc_count=0
            if i=='G' or i=='C' or i=='g' or i=='c':
                gc_count+=1
        return gc_count

    def gc_content(self):
        d=self.read_fasta_file()
        l=self.fasta_length()
        gc={} # A dictionary that stores "scaffold_name:gc_fraction"
        for i in d:
            gc[i]=fasta.get_gc_count(d[i])/len(d[i])

        return gc

    # def k-mer_composition(self): 
    
    

if __name__=="__main__":
    print("Script for handling fasta file functions")

    # Dev Tests
    f=fasta('../tests/fasta_test_files/grph.fa')
    # print(f.read_fasta_file)
    # print(f.fasta_length())
    print(f.gc_content())