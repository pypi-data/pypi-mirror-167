
from IPython.core.display import display, HTML
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.physics import Physics
from pyvis.network import Network
import time
from basemodes.text_edges import text2edges

def avnn(comments_en,by_review = False,other_edges = True,verbose_text = False,only_otherNouns = False, only_opiAV = True, nncompound = True):

    time_start = time.time()
    all_adjV2N_edges = []
    allNNedges = [] # noun to noun is the noun in adjV2N 
    all_new_nodes= []
    all_old_nodes= []
    new_node_nouns= []
    new_node_verbs= []
    new_node_adjs= []

    """    by_review = False # by review or by sentence in review
        #opinion_verbs = False
        other_edges = True # not match verb, adj, noun
        verbose_text = False
        only_opiAV = True
        only_otherNouns =only_otherNouns
        nncompound = True"""
        
    for ia,line_ori in enumerate(comments_en):
        print(ia)
        try:
            line = line_ori.replace('\n','') # remove new line in the paragraph
            line = line.replace('\t','')
            line1 = re.sub('[:@#$+=%*`)(><]', ' , ', line)
            #line1 = re.sub(r'\b\d+\b', ' ', line1)
            line1 = re.sub(" \d+", "  ", line1)
            time.sleep(.5)
            line1 = re.sub(r'\b' + "th" + r'\b', ' ', line1) 
            line1 = line1.replace("."," . ") # in case: it is great.the food become a word of great.the
            line1 = line1.replace("!"," . ") # in case: it is great.the food become a word of great.the
            line1 = line1.replace("?"," . ") # ?,!, . for the sentence dependency 
            line1 = re.sub(' +', ' ', line1).strip() #remove extra space whitespace 
            print('line1:', line1)
            if by_review:
                all_adjV2N_edges0, allNNedges0, all_new_nodes0, all_old_nodes0,new_node_nouns0,new_node_verbs0,new_node_adjs0 = text2edges(line1,verbose= False, verbose_text = verbose_text,include_otherEdge = other_edges,only_otherNouns =only_otherNouns,only_opiAV = only_opiAV,nncompound= nncompound)
                #all_adjV2N_edges, allNNedges, all_adjV2N_edges_drop, all_new_nodes, all_old_nodes,new_node_nouns,new_node_verbs,new_node_adjs
                allNNedges.extend(allNNedges0)
                all_adjV2N_edges.extend(all_adjV2N_edges0)
                all_new_nodes.extend(all_new_nodes0)
                all_old_nodes.extend(all_old_nodes0)
                new_node_nouns.extend(new_node_nouns0)
                new_node_verbs.extend(new_node_verbs0)
                new_node_adjs.extend(new_node_adjs0)
            else:
                for ib,sent in enumerate(nlp(line1).sents):   # dependency parse https://spacy.io/usage/linguistic-features#sbd sentence
                    #print(sent)
                    if len(sent.text.split())>2: # minimal 2 words
                        print('sentence' + str(ib),sent.text)
                        all_adjV2N_edges0, allNNedges0, all_new_nodes0, all_old_nodes0,new_node_nouns0,new_node_verbs0,new_node_adjs0 = text2edges(sent.text,verbose_text = verbose_text,include_otherEdge = other_edges,only_otherNouns =only_otherNouns,only_opiAV = only_opiAV,nncompound= nncompound)
                        
                        allNNedges.extend(allNNedges0)
                        all_adjV2N_edges.extend(all_adjV2N_edges0)
                        all_new_nodes.extend(all_new_nodes0)
                        all_old_nodes.extend(all_old_nodes0)
                        new_node_nouns.extend(new_node_nouns0)
                        new_node_verbs.extend(new_node_verbs0)
                        new_node_adjs.extend(new_node_adjs0)
        except:
            print('---sth wrong ---')
        
    print('processing time1:', time.time()-time_start)
    return all_adjV2N_edges,allNNedges,all_new_nodes,all_old_nodes,new_node_nouns,new_node_verbs,new_node_adjs
