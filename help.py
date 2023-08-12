






def stp_word():
    auditor_open=open('StopWords_Auditor.txt','r')
    auditor=auditor_open.read()
    auditor_open.close()
    curriency_open=open('StopWords_Currencies.txt','r')
    curriency=curriency_open.read()
    curriency_open.close()
    dateandnum_open=open('StopWords_DatesandNumbers.txt','r')
    dateandnum=dateandnum_open.read()
    dateandnum_open.close()
    Generic_open=open('StopWords_Generic.txt','r')
    Generic=Generic_open.read()
    Generic_open.close()
    Genericlong_open=open('StopWords_GenericLong.txt','r')
    Genericlong=Genericlong_open.read()
    Genericlong_open.close()
    Geographic_open=open('StopWords_Geographic.txt','r')
    Geographic=Geographic_open.read()
    Geographic_open.close()
    Names_open=open('StopWords_Names.txt','r')
    Names=Names_open.read()
    Names_open.close()
    extra_open=open('extra.txt','r')
    extra=extra_open.read()
    extra_open.close()


    all=auditor+"\n"+curriency+"\n"+dateandnum+"\n"+Generic+"\n"+Genericlong+"\n"+Geographic+"\n"+Names+"\n"+extra
    all=all.replace("|","")
    all=all.replace("Surnames from 1990 census > .002%.  www.census.gov.genealogy/names/dist.all.last","")
    all=all.lower()
    all=all.split()
    return all
def pos():
    
    pos_open=open('positive-words.txt','r')
    pos=pos_open.read()
    pos_open.close()
    pos=pos.lower()
    pos=pos.split()
    return pos
def neg():    
    neg_open=open('negative-words.txt','r')
    neg=neg_open.read()
    neg_open.close()
    neg=neg.lower()
    neg=neg.split()
    return neg
