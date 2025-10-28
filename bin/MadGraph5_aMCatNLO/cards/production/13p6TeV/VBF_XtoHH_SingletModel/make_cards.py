import numpy as np
from numpy import arange
import argparse
import os
import math

parser = argparse.ArgumentParser()
parser.add_argument('--masses', '-m', help= 'Masses to use for the heavy Higgs', default='600')
parser.add_argument('--widths', '-w', help= 'Relative Widths to use for the heavy Higgs', default='0.001')
args = parser.parse_args()

def WriteExtraModelsCard(out_name):
    with open(out_name+'_extramodels.dat', "w") as extramodels_file:
        extramodels_file.write('loop_sm_twoscalar.tar.gz')

def WriteRunCard(out_name):
    os.system('cp run_card_template.dat %s_run_card.dat' % out_name)

def WriteProcCard(out_name):
    proccard_out = 'import model loop_sm_twoscalar\n'
    proccard_out += 'define p = g u c d s u~ c~ d~ s~ b b~\n'
    proccard_out += 'define j = g u c d s u~ c~ d~ s~ b b~\n'
    proccard_out += 'generate p p > eta0 j j $$ w+ w- z eta0 / a j iota0 h QED=3 LAM112=0 LAM111=0 QCD=0, (eta0 > h h)\n' 
    proccard_out += 'output %s -nojpeg' % out_name.split('/')[0]
    with open(out_name+'_proc_card.dat', "w") as proccard_file:
        proccard_file.write(proccard_out)

def WriteCustomizeCard(out_name, out_str):
    with open(out_name+'_customizecards.dat', "w") as customizecard_file:
        customizecard_file.write(out_str)

def WriteReweightCard(out_name, mass, widths=[0.001,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.20,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.30]):
    reweight_out_string='\
change rwgt_dir ./rwgt\n\
\n'

    width_dep_string = '\
launch --rwgt_name=$postfix\n\
  set decay 99925 $W\n\
\n'

    for w in widths:
        postfix = ('RelWidth_%g' % (w)).replace('.','p')
        reweight_out_string += width_dep_string.replace('$W', '%g' % (float(mass)*w)).replace('$postfix', postfix)

    with open(out_name+'_reweight_card.dat', "w") as reweightcard_file:
        reweightcard_file.write(reweight_out_string)

if len(args.masses) == 0 or len(args.widths) == 0:
    print('At least one mass point and one width must be specified! Exiting.')
    exit()


masses = args.masses.split(',')
widths = args.widths.split(',')

masses = [float(x) for x in masses]
widths = [float(x) for x in widths]

for m in masses:
    for w in widths:
        ca = 1./math.sqrt(2)
        customizecards_base_file = open("customizecards_template.dat","r")
        res_customizecards = customizecards_base_file.read().replace('$Weta0','%g' % (w*m)).replace('$Meta0','%g' % m)
        out_name = ('VBF_XtoHH_SingletModel_M_%g_RelWidth_%g' % (m,w)).replace('.','p')

        res_customizecards_out = res_customizecards.replace('$Weta0','%g' % (w*m))
        os.system('mkdir -p %s' % out_name)

        card_name = "%(out_name)s/%(out_name)s" % vars()

        WriteProcCard(card_name)
        WriteExtraModelsCard(card_name)
        WriteRunCard(card_name)
        WriteCustomizeCard(card_name, res_customizecards_out)
        WriteReweightCard(card_name, m)
