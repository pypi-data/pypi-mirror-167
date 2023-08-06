import os, re, sys
import logging
import time
import typer
import pandas as pd
from pathlib import Path
import subprocess
from rich.progress import track
from typing import List, Union, Optional, NamedTuple
from openpyxl import load_workbook
from openpyxl.workbook.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from collections import defaultdict
from collections import OrderedDict
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

'''
requerstment.txt
pandas
typer
pathlib
rich
openpyxl
biopython
'''


# start=time.perf_counter()
app=typer.Typer(help="Xingze Li's bioinformatics analysis scripts. \n\n\n emali: lixingzee@gmail.com")

@app.command("trans")
def to_one_line_fasta(infile, outfile):
    'Convert multi-line fasta to one-line fasta'
    inf = open(infile, 'r')
    outf = open(outfile, 'w')
    db = {}
    for line in inf.readlines():
        if line.startswith('>'):
            keys = line.strip()
            db[keys] = []
        else:
            db[keys].append(line.strip())
    for name, seq in db.items():
        outf.write(name + '\n')
        outf.write(''.join(seq) + '\n')
    inf.close()
    outf.close()

@app.command("seq")
def extract_target_seq(input_fasta_file: Path, 
                       output_file: Path, 
                       extract_seq_name_file: Path):
    'Extract sequences by sequence name or keyword'
    outf = open(output_file,'w')
    dict = {}
    with open(input_fasta_file, 'r') as fastaf:
        for line in fastaf:
            if line.startswith('>'):
                name = line
                dict[name] = ''
            else:
                dict[name] += line.replace('\n','') #读取整个fasta文件构成字典
         
    with open(extract_seq_name_file,'r') as listf:
        for row in listf:
            row = row.strip()
            for key in dict.keys(): #选取包含所需名称的基因名和序列
                if row in key:
                    outf.write(key)
                    outf.write(dict[key] + '\n')
    outf.close()

@app.command()
def fq2fa(fq: Path,
          fa: Path):
    'Convert a fastq file to a fasta file'
    out=[]
    with open(fq,'r') as fin:
        c=0
        for line in fin:
            c+=1
            if (c%4) == 1:
                out.append('>' + line[1:])
            elif (c%4) == 2:
                out.append(line)
    with open(fa,'w') as fo:
        fo.write(''.join(out))
    return

@app.command()
def fa2fq(fa: Path,
          fq: Path):
    'Convert a fasta file to a fastq file'
    seq=''
    out=[]
    n_reads=0
    with open(fa,'r') as fin:
        for line in fin:
            if line.startswith('>'):
                n_reads+=1
                if seq:
                    score='I'*len(seq)
                    out.append(seq+'\n+\n'+score+'\n')
                    seq=''
                out.append('@'+line[1:])
            else:
                seq+=line.strip()
    #the last one
    score='I'*len(seq)
    out.append(seq+'\n+\n'+score+'\n')
    with open(fq,'w') as fo:
        fo.write(''.join(out))
    return n_reads


codon_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 'CGT':'R', 'CGC':'R',   
    'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R', 'TCT':'S', 'TCC':'S',
    'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S', 'ATT':'I', 'ATC':'I',
    'ATA':'I', 'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L',
    'CTG':'L', 'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G', 'GTT':'V',
    'GTC':'V', 'GTA':'V', 'GTG':'V', 'ACT':'T', 'ACC':'T', 'ACA':'T',
    'ACG':'T', 'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'AAT':'N',
    'AAC':'N', 'GAT':'D', 'GAC':'D', 'TGT':'C', 'TGC':'C', 'CAA':'Q',
    'CAG':'Q', 'GAA':'E', 'GAG':'E', 'CAT':'H', 'CAC':'H', 'AAA':'K',
    'AAG':'K', 'TTT':'F', 'TTC':'F', 'TAT':'Y', 'TAC':'Y', 'ATG':'M',
    'TGG':'W',
    'TAG':'STOP', 'TGA':'STOP', 'TAA':'STOP'
    }


@app.command()
def cds2pep(cds_input: Path,
            cds_output: Path,
            pep_output: Path):
    'Convert cds file to pep file'
    inf = open(cds_input, 'r')
    cds_outf = open(cds_output, 'w')        
    pep_outf = open(pep_output, 'w')
    db = {}
    pep = {}
    for line in track(inf.readlines()):
        if line.startswith('>'):
            keys = line.strip()
            db[keys] = []
        else:
            db[keys].append(line.strip())

    for name, seq in track(db.items()):
        cds_outf.write(name + '\n')
        cds_outf.write(''.join(seq) + '\n')
    cds_outf.close()

    with open(cds_output, "r") as co:
        for line in co.readlines():
            if line.startswith('>'):
                key = line.strip()
                pep[key] = []
            else:
                seq = line.strip()
                # translate one frame at a time
                prot = '' 
                for i in range(0, len(seq), 3):
                    codon = seq[i:i + 3]
                    if codon in codon_table:
                        if codon_table[codon] == 'STOP':
                            prot = prot + '*'
                        else: 
                            prot = prot + codon_table[codon]
                pep[key].append(prot)
        for name, seq in track(pep.items()):
            pep_outf.write(name + '\n')
            pep_outf.write(''.join(seq) + '\n')
    inf.close()
    pep_outf.close()

# @app.command()
# def rename_fasta(fasta_file: Path, output: Path):
#     with open (fasta_file, 'w+') as fin:
#         for line in fin:
            


@app.command()
def excel2txt(input: Path,
              output: Path):
    'Convert excel file to txt file'
    df = pd.read_excel(input, header=None)		# 使用pandas模块读取数据
    df.to_csv(output, header=None, sep='\t', index=False)		# 写入，分号分隔

@app.command('len')
def get_fasta_len(fasta: Path,
                  lenf: Path):
    fasta_dict = OrderedDict()
    gene_count = {}
    handle = open(fasta, "r")
    len_file = open(lenf, "w")
    active_sequence_name = ""
    for line in handle:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"): 
            active_sequence_name = line[1:]
            active_sequence_name = active_sequence_name.split(" ")[0]
        if active_sequence_name not in fasta_dict:
            fasta_dict[active_sequence_name] = 0
            continue
        sequence = line
        fasta_dict[active_sequence_name] += len(sequence)
    for chrom,lens in fasta_dict.items():
        print("{chrom}\t{lens}\t{count}".format(\
                chrom=chrom,lens=lens,count=gene_count.get(chrom,0)), file=len_file)
    len_file.close()    
    handle.close()
    return fasta_dict


@app.command('gff')
def parse_gff(gff: Path,
              sample_gff_file: Path):
    gene_count = {}
    gene_dict = OrderedDict()
    tx_pos_dict = defaultdict(list)
    CDS_dict = defaultdict(list)
    handle = open(gff, "r")
    gff_file = open(sample_gff_file, "w")    
    for line in handle:
        if line.startswith("#"):
            continue
        content = line.split("\t")
        if len(content) <= 8:
            continue
        #print(content)
        if content[2] == "transcript" or content[2] == "mRNA":

            # use regual expression to extract the gene ID
            # match the pattern ID=xxxxx; or ID=xxxxx
            
            tx_id = re.search(r'ID=(.*?)[;\n]',content[8]).group(1)
            tx_parent = re.search(r'Parent=(.*?)[;\n]',content[8]).group(1)
            tx_parent = tx_parent.strip() # remove the 'r' and '\n'

            # if the parent of transcript is not in the gene_dict, create it rather than append
            if tx_parent in gene_dict:
                gene_dict[tx_parent].append(tx_id)
            else:
                gene_dict[tx_parent] = [tx_id]
            tx_pos_dict[tx_id] = [content[0],content[3], content[4], content[6] ]
        # GFF must have CDS feature
        if content[2] == 'CDS':
            width = int(content[4]) - int(content[3])
            CDS_parent = re.search(r'Parent=(.*?)[;\n]',content[8]).group(1)
            CDS_parent = CDS_parent.strip() # strip the '\r' and '\n'
            CDS_dict[CDS_parent].append(width)
    
    for gene, txs in gene_dict.items():
        tmp = 0
        for tx in txs:
            tx_len = sum(CDS_dict[tx])
            if tx_len > tmp:
                lst_tx = tx
                tmp = tx_len
        tx_chrom = tx_pos_dict[lst_tx][0]
        if tx_chrom not in gene_count:
            gene_count[tx_chrom] = 1
        else:
            gene_count[tx_chrom] += 1
        tx_start = tx_pos_dict[lst_tx][1]
        tx_end   = tx_pos_dict[lst_tx][2]
        tx_strand = tx_pos_dict[lst_tx][3]

        print(f"{tx_chrom}\t{gene}\t{tx_start}\t{tx_end}\t{tx_strand}\t{gene_count[tx_chrom]}\t{lst_tx}", file=gff_file )
    gff_file.close()
    handle.close()
    # return [gene_dict, tx_pos_dict, CDS_dict]




@app.command('run')
def parallel_run(cmd_path, 
                 thread, 
                 stdout=None, 
                 stderr=None, 
                 parallel="parallel", 
                 fg=False):
    'Parallelized running tasks'
    thread=int(thread)
    if stdout == None:
        stdout = "%s.log" % cmd_path
    if stderr == None:
        stderr = "%s.err" % cmd_path
    if thread >1:
        cmd = "nohup %s -j %s ::: < %s > %s 2> %s " % (parallel, thread, cmd_path, stdout, stderr)
    else:
        cmd = "nohup bash %s > %s 2> %s " %(cmd_path, stdout, stderr)
    if fg==False:
        cmd +=" &"
    sys.stdout.write("CMD: %s \n" % cmd)
    subprocess.check_call(cmd, shell=True, executable='/bin/bash')



@app.command()
def gfa2fa(gfa_file, fa_file):
    'Convert gfa file to fasta file'
    input = open(gfa_file, 'r').readlines()
    output = open(fa_file, 'w')
    print(f"Converting GFA {input} --> FASTA {output}...")
    num_seqs = 0
    for i in trange(len(input)):
        line = input[i].strip('\n').split()
        if line[0] == 'S':
            num_seqs += 1
            simple_seq = Seq(line[2])
            simple_seq_r = SeqRecord(simple_seq, id=line[1])
            SeqIO.write(simple_seq_r, output, "fasta")
    output.close()
    print(f"FASTA of {num_seqs} sequences created at {output}.")

# end=time.perf_counter()
# print('Running time: %s Seconds'%(end-start)) #运行时间    

if __name__ == "__main__":
    app()


