import itertools
import random

ngrams_list = ['essential ocean variable', 'essential climate variable',
               'essential biodiversity variable', 'advice',
'requirements',
'error', 'sources of error', 'error sources',
'data processing', 'data management',
'management plan',
'quality control',
'recommendation',
'community standard',
'common system', 'common standard', 'common practice', 'common protocol',
'manual',
'standard',
'expert report',
'expert review',
'guidelines', 'guide', 'guidance',
'calibration',
'validation',
'inter-comparability',
'best-practice', 'best practice',
'uncertainty',
'confidence',
'maintain',
'coordinate', 'coordination',
'review',
'definitions', 'definitions', 'descriptions',
'format', 'formatting',
'indicator',
'accuracy',
'frequency',
'capacity building',
'knowledge exchange', 'transfer',
'framework',
'working group',
'workshop',
'gap', 'fill gaps', 'fill a gap', 'gap filling',
'synthesis', 'synthesise', 'synthesize',
'compendium',
'feasible', 'feasibility',
'cost-effective',
'reproducibility', 'repeatability', 'repeatable', 'reproducible',
'monitoring',
'practice',
'procedure',
'protocol development', 'developing protocols', 'standard protocol',
'endorse', 'endorsement',
'observing', 'observational', 'observing systems', 'observatory',
'sustained', 'sustainable',
'timescales', 'temporal scale',
'spatial scale',
'models', 'model', 'modelling',
'operational',
'practicable', 'practical']



p1 = ['standard', 'endorsed', 'official', 'recommended', 'authoritative']
p2=['measurement', 'observation', 'collection', 'calibration']
p3 = ['marine', 'ocean', 'coastal', 'neritic', 'pelagic']
p4 = ['sensor', 'instrument', '']
prefix = p1+p2+p3+p4

s1 = ['protocol', 'procedure', 'method', 'recommendation', 'manual', 'guide']
s2 = ['measurement', 'observation', 'collection', 'calibration', '']
suffix = s1+s2

print(len(ngrams_list))
print (len(prefix))
print(len(suffix))
keywords = list(itertools.product(ngrams_list, prefix ,suffix))
random.shuffle(keywords)
keywordFile = open('keywords.txt', 'w')

for keyword in keywords:
    keywordFile.write('"'+keyword[0] + '", "'+keyword[1] + '", "' + keyword[2]+ '"')
    keywordFile.write('\n')

keywordFile.close()
