#!/usr/bin/python
from __future__ import division
from Bio import SeqIO
import math
import sys
import re


#Read the query file, PSSM file and the background file
#All

def main():
	query_file= sys.argv[1]
	background_file= sys.argv[2]
	pssm_file= sys.argv[3]
	starting_point= int (sys.argv[4])
	end= sys.argv[5]

	read_files(query_file,background_file,pssm_file,end,starting_point)

#pval = -[sum(max_score >= observedscore)/Number of sequences];
#I am to count the number of max score that are greater or equal to the observed score and then divide by number of total sequences
# Then take -log(pvalue), which is what will be graphed
def pvalue(observed,background,end,starting_point):
	f = open('uploads/logp.txt','w+')
	N=len(background)
	for pos in range (0,len(observed)):
		sum_over=sum(i >= observed[pos] for i in background) #makes a list of how many max scores are greater than the observed
		p=sum_over/N
	#	print sum_over
		confidence=0
		if(p!=0):
			confidence= -math.log(p)
		f.write("%.5f\n" % confidence)
	f.write(end+"\n")
	f.write('%d' % starting_point)
	f.close()

#Function that calculates the score a given location
#Score(P,S,i)=sum j...k (P(s(i+j-1),j)). It will then  either return the max score for that sequence or an array of scores for that position depending on input

def get_score(sequence,pssm,length,i):
	nucleotides={'A':0,'C':1,'G':2,'T':3}
	score=0
#	making sure not to go beyond sequence length fo 1...k
	j=0
#	length=int(math.fabs(length-i))
	if length+i>len(sequence):
		length=len(sequence)-i

	for x in range(0,length-1): #goes over positions 1....k where k is how many positions in the motif query
		s=nucleotides[sequence[i+j]]
		score+=math.log(pssm[s][j])
		j+=1
	return score

#Takes a string, converts and returns it to a 2D array matrix
def format_matrix(matrix):
   	array2d=[]
	with open(matrix) as file:
	   	array2d = [[float(digit) for digit in line.split()] for line in file]
   	return array2d

#Reads in the query sequence, background sequences, and pssm file
def read_files(query_file,background_file,pssm_file,end,starting_point):
	instances=[];
	background=[]
	observed=[]
	query=""
	back_handle = open(background_file, "rU")
	query_handle = open(query_file, "rU")
	
	for record in SeqIO.parse(back_handle, "fasta"):
		instances.append(record.seq)
	back_handle.close()


	#Reading query file and extracting sequence
	for seq in SeqIO.parse(query_handle, "fasta") :
		query=seq.seq
	query_handle.close()

	#Sending PSSM file to be stored as a 2d matrix
	pssmf="";
	for line in open(pssm_file):
	    li=line.strip()
	    if not li.startswith("#"):
	        line = re.sub(r'^\s+$|\n', '', line)
	       	if line !="":
	       		pssmf+=line+"\n"
	f = open('uploads/PSSM2.txt','w+')
	f.write(pssmf)
	f.close()
	pssm = format_matrix('uploads/PSSM2.txt')

	#Getting max scores for each sequences
	f = open('uploads/Max_scores.txt','w+')
	for x in range(len(instances)):
		sequence=instances[x]
		max_score=0
		for pos in range(0,len(sequence)): #Iterating over each position as a starting point
			score=get_score(sequence,pssm,len(pssm[0]),pos)
			if max_score==0:
				max_score=score
			elif score<max_score:
				max_score=score
		f.write("%s\n" % max_score)
		background.append(max_score)
	f.close()	

	#Getting scores for each position in the oberved/query
	print "observed"
	for pos in range(0,len(query)): #Iterating over each position as a starting point
		observed.append(get_score(query,pssm,len(pssm[0]),pos))
	print observed
	pvalue(observed,background,end,starting_point)

main();
