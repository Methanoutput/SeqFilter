"""
Last modified on 21 Apr 2023
It filters any given Sequence file, based on a given list of sequence IDs. It can also order your Sequences in alphabetical order.
@author: J. Hille
"""
import argparse

#function to get the string of the current header.
def getheader(pos, database):
    header = ''
    x = pos
    while database[x] != ',':
        header = header + database[x]
        x = x + 1
    return header

#function to get the string of the current sequence.
def getsequence(spos, end, database):
    tmpdata = database[spos:end].replace(',', '')
    return tmpdata

#required parser and a program description.
parser = argparse.ArgumentParser(prog = 'SeqFilter', description = 'It filters any given Sequence file, based on a given list of sequence IDs. It can also order your Sequences in alphabetical order.', epilog = 'If you find a bug please report it via Github.')
parser.add_argument('-d', '--database', required = True, help = 'requires a file containing your sequences.')
parser.add_argument('-l', '--list', required = True, help = 'requires a txt. file containing the sequences you want to write in a new file')
parser.add_argument('-s', '--sort', required = True, help = 'your output file will be sorted alphabetically if you set the Value to "T".')
parser.add_argument('-n', '--name', required = True, help = 'requires a string that represents the output file name.')
args = parser.parse_args()


if str(args.sort) == 'T':
    sortbool = True

else:
    sortbool = False

#saving database as a string.
with open(args.database, 'r') as file:
    database: str = file.read().replace('\n', ',')
print('Database was read correctly.\n')

#saving idlist as a string.
with open(args.list, 'r') as idfile:
    id_list = idfile.read()
count = 0
arr = []
tmpid = ''

#filling an array with the wanted headers.
for i in range(len(id_list)):
    if id_list[i] == '\n':
        arr.append(tmpid)
        count = count + 1
        tmpid = ''
    else:
        tmpid = tmpid + id_list[i]

#create output file
wfile = open(args.name, 'a')
last_seq = database.rfind('>')

#sort if wanted
if sortbool:
    arr.sort(key=str.lower)

#write output file
while arr:
    seqname = arr.pop(0)
    pos = database.find(seqname)
    spos = pos + database[pos:len(database)].find(',')
    end = pos + database[pos:len(database)].find('>')
    if end == last_seq:
        wfile.write('>')
        wfile.write(getheader(pos, database))
        wfile.write('\n')
        wfile.write(getsequence(spos, len(database), database))
        wfile.write('\n')
    else:
        wfile.write('>')
        wfile.write(getheader(pos, database))
        wfile.write('\n')
        wfile.write(getsequence(spos, end, database))
        if len(arr) > 0:
            wfile.write('\n')
print('output file was written successfully.')
file.close()
wfile.close()
