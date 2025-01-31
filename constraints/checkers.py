import time
import smact
from smact import neutral_ratios
import numpy as np
from pymatgen.core import Composition
import pymatgen as mg
from smact.screening import pauling_test
from tqdm import tqdm

def check_neutrality(formula):
    comp = Composition(formula)
    reduce_formula = comp.get_el_amt_dict()
    element_num = len(list(reduce_formula.keys()))

    if element_num == 1:
        return True
    elif element_num == 2:
        return check_neutrality_2(formula)
    elif element_num == 3:
        return check_neutrality_3(formula)
    elif element_num == 4:
        return check_neutrality_4(formula)
    elif element_num == 5:
        return check_neutrality_5(formula)
    elif element_num == 6:
        return check_neutrality_6(formula)
    elif element_num == 7:
        return check_neutrality_7(formula)
    elif element_num == 8:
        return check_neutrality_8(formula)
    else:
        print(formula)
        raise Exception('Not implemented: contact 897902311@qq.com')
        return False

def check_neutrality_2(formula):
    charge_neutral_count = 0
    comp = Composition(formula)
    reduce_formula = comp.get_el_amt_dict()
    list_of_elements = list(reduce_formula.keys())
    stoichs = list(
                np.array(list(reduce_formula.values())).astype(np.int32)[:,np.newaxis]
            )
    max_num = max(reduce_formula.values())
    for i, ele_a in enumerate(list_of_elements):
        for ox_a in smact.Element(ele_a).oxidation_states:
            for j, ele_b in enumerate(list_of_elements[i+1:]):
                for ox_b in smact.Element(ele_b).oxidation_states:                    
                            
                    # Checks if the combination is charge neutral before printing it out! #                        
                    # neutral_ratios(oxidations, stoichs=False, threshold=5) #speed up by providing stoichs 
                    # cn_e, cn_r = neutral_ratios([ox_a, ox_b], threshold = int(max_num))
                    cn_e, cn_r = neutral_ratios([ox_a, ox_b], stoichs = stoichs, threshold = int(max_num))
                    
                    if cn_e:
                        for num in cn_r:
                            if tuple(reduce_formula.values()) == num:
                                return True

                        # print(cn_e)
                        # print(cn_r)
                        # print(ox_a, ox_b, ox_c)
                        # charge_neutral_count = charge_neutral_count + 1
                        # print('{0:3s}  {1:3s}  {2:3s}'.format(ele_a, ele_b, ele_c))
    # print('Number of combinations = {0}'.format(charge_neutral_count))
    # print("--- {0} seconds to run ---".format(time.time() - start_time)) 
    return False

def check_neutrality_3(formula):
    charge_neutral_count = 0
    comp = Composition(formula)
    reduce_formula = comp.get_el_amt_dict()
    list_of_elements = list(reduce_formula.keys())
    stoichs = list(
                np.array(list(reduce_formula.values())).astype(np.int32)[:,np.newaxis]
            )
    max_num = max(reduce_formula.values())
    for i, ele_a in enumerate(list_of_elements):
        for ox_a in smact.Element(ele_a).oxidation_states:
            for j, ele_b in enumerate(list_of_elements[i+1:]):
                for ox_b in smact.Element(ele_b).oxidation_states:
                    for k, ele_c in enumerate(list_of_elements[i+j+2:]):
                        for ox_c in smact.Element(ele_c).oxidation_states:
                            
                            # Checks if the combination is charge neutral before printing it out! #                        
                            cn_e, cn_r = neutral_ratios([ox_a, ox_b, ox_c], stoichs = stoichs, threshold = int(max_num))
                            
                            if cn_e:
                                for num in cn_r:
                                    if tuple(reduce_formula.values()) == num:
                                        return True

                                                                # print(cn_e)
                                                                # print(cn_r)
                                                                # print(ox_a, ox_b, ox_c)
                                                                # charge_neutral_count = charge_neutral_count + 1
                                                                # print('{0:3s}  {1:3s}  {2:3s}'.format(ele_a, ele_b, ele_c))
    # print('Number of combinations = {0}'.format(charge_neutral_count))
    # print("--- {0} seconds to run ---".format(time.time() - start_time)) 
    return False

def check_neutrality_4(formula):
    charge_neutral_count = 0
    comp = Composition(formula)
    reduce_formula = comp.get_el_amt_dict()
    list_of_elements = list(reduce_formula.keys())
    stoichs = list(
                np.array(list(reduce_formula.values())).astype(np.int32)[:,np.newaxis]
            )
    max_num = max(reduce_formula.values())
    for i, ele_a in enumerate(list_of_elements):
        for ox_a in smact.Element(ele_a).oxidation_states:
            for j, ele_b in enumerate(list_of_elements[i+1:]):
                for ox_b in smact.Element(ele_b).oxidation_states:
                    for k, ele_c in enumerate(list_of_elements[i+j+2:]):
                        for ox_c in smact.Element(ele_c).oxidation_states:
                            for m, ele_d in enumerate(list_of_elements[i+j+k+3:]):
                                for ox_d in smact.Element(ele_d).oxidation_states:
                            
                                    # Checks if the combination is charge neutral before printing it out! #                        
                                    cn_e, cn_r = neutral_ratios([ox_a, ox_b, ox_c, ox_d], stoichs = stoichs, threshold = int(max_num))
                                    
                                    if cn_e:
                                        for num in cn_r:
                                            if tuple(reduce_formula.values()) == num:
                                                return True

                                                                # print(cn_e)
                                                                # print(cn_r)
                                                                # print(ox_a, ox_b, ox_c)
                                                                # charge_neutral_count = charge_neutral_count + 1
                                                                # print('{0:3s}  {1:3s}  {2:3s}'.format(ele_a, ele_b, ele_c))
    # print('Number of combinations = {0}'.format(charge_neutral_count))
    # print("--- {0} seconds to run ---".format(time.time() - start_time)) 
    return False

def check_neutrality_5(formula):
    charge_neutral_count = 0
    comp = Composition(formula)
    reduce_formula = comp.get_el_amt_dict()
    list_of_elements = list(reduce_formula.keys())
    stoichs = list(
                np.array(list(reduce_formula.values())).astype(np.int32)[:,np.newaxis]
            )
    max_num = max(reduce_formula.values())
    for i, ele_a in enumerate(list_of_elements):
        for ox_a in smact.Element(ele_a).oxidation_states:
            for j, ele_b in enumerate(list_of_elements[i+1:]):
                for ox_b in smact.Element(ele_b).oxidation_states:
                    for k, ele_c in enumerate(list_of_elements[i+j+2:]):
                        for ox_c in smact.Element(ele_c).oxidation_states:
                            for m, ele_d in enumerate(list_of_elements[i+j+k+3:]):
                                for ox_d in smact.Element(ele_d).oxidation_states:
                                    for n, ele_e in enumerate(list_of_elements[i+j+k+m+4:]):
                                        for ox_e in smact.Element(ele_e).oxidation_states:                             
                                            # Checks if the combination is charge neutral before printing it out! #                        
                                            cn_e, cn_r = neutral_ratios([ox_a, ox_b, ox_c, ox_d, ox_e], stoichs = stoichs, threshold = int(max_num))
                                            
                                            if cn_e:
                                                for num in cn_r:
                                                    if tuple(reduce_formula.values()) == num:
                                                        return True

                                                                # print(cn_e)
                                                                # print(cn_r)
                                                                # print(ox_a, ox_b, ox_c)
                                                                # charge_neutral_count = charge_neutral_count + 1
                                                                # print('{0:3s}  {1:3s}  {2:3s}'.format(ele_a, ele_b, ele_c))
    # print('Number of combinations = {0}'.format(charge_neutral_count))
    # print("--- {0} seconds to run ---".format(time.time() - start_time)) 
    return False

def check_neutrality_6(formula):
    charge_neutral_count = 0
    comp = Composition(formula)
    reduce_formula = comp.get_el_amt_dict()
    list_of_elements = list(reduce_formula.keys())
    stoichs = list(
                np.array(list(reduce_formula.values())).astype(np.int32)[:,np.newaxis]
            )
    max_num = max(reduce_formula.values())
    for i, ele_a in enumerate(list_of_elements):
        for ox_a in smact.Element(ele_a).oxidation_states:
            for j, ele_b in enumerate(list_of_elements[i+1:]):
                for ox_b in smact.Element(ele_b).oxidation_states:
                    for k, ele_c in enumerate(list_of_elements[i+j+2:]):
                        for ox_c in smact.Element(ele_c).oxidation_states:
                            for m, ele_d in enumerate(list_of_elements[i+j+k+3:]):
                                for ox_d in smact.Element(ele_d).oxidation_states:
                                    for n, ele_e in enumerate(list_of_elements[i+j+k+m+4:]):
                                        for ox_e in smact.Element(ele_e).oxidation_states:
                                            for p, ele_f in enumerate(list_of_elements[i+j+k+m+n+5:]):
                                                for ox_f in smact.Element(ele_f).oxidation_states:
                                                    # Checks if the combination is charge neutral before printing it out! #                        
                                                    cn_e, cn_r = neutral_ratios([ox_a, ox_b, ox_c, ox_d, ox_e, ox_f], stoichs = stoichs, threshold = int(max_num))
                                                    
                                                    if cn_e:
                                                        for num in cn_r:
                                                            if tuple(reduce_formula.values()) == num:
                                                                return True

                                                                # print(cn_e)
                                                                # print(cn_r)
                                                                # print(ox_a, ox_b, ox_c)
                                                                # charge_neutral_count = charge_neutral_count + 1
                                                                # print('{0:3s}  {1:3s}  {2:3s}'.format(ele_a, ele_b, ele_c))
    print('Number of combinations = {0}'.format(charge_neutral_count))
    print("--- {0} seconds to run ---".format(time.time() - start_time)) 
    return False

def check_neutrality_7(formula):
    charge_neutral_count = 0
    comp = Composition(formula)
    reduce_formula = comp.get_el_amt_dict()
    list_of_elements = list(reduce_formula.keys())
    stoichs = list(
                np.array(list(reduce_formula.values())).astype(np.int32)[:,np.newaxis]
            )
    max_num = max(reduce_formula.values())
    for element in reduce_formula.keys():
        print(len(smact.Element(element).oxidation_states), end = ",")
    for i, ele_a in enumerate(list_of_elements):
        for ox_a in smact.Element(ele_a).oxidation_states:
            for j, ele_b in enumerate(list_of_elements[i+1:]):
                for ox_b in smact.Element(ele_b).oxidation_states:
                    for k, ele_c in enumerate(list_of_elements[i+j+2:]):
                        for ox_c in smact.Element(ele_c).oxidation_states:
                            for m, ele_d in enumerate(list_of_elements[i+j+k+3:]):
                                for ox_d in smact.Element(ele_d).oxidation_states:
                                    for n, ele_e in enumerate(list_of_elements[i+j+k+m+4:]):
                                        for ox_e in smact.Element(ele_e).oxidation_states:
                                            for p, ele_f in enumerate(list_of_elements[i+j+k+m+n+5:]):
                                                for ox_f in smact.Element(ele_f).oxidation_states:
                                                    for q, ele_g in enumerate(list_of_elements[i+j+k+m+n+p+6:]):
                                                        for ox_g in smact.Element(ele_g).oxidation_states:
                                                            # Checks if the combination is charge neutral before printing it out! #                        
                                                            cn_e, cn_r = neutral_ratios([ox_a, ox_b, ox_c, ox_d, ox_e, ox_f, ox_g], stoichs = stoichs, threshold = int(max_num))
                                                            
                                                            if cn_e:
                                                                for num in cn_r:
                                                                    if tuple(reduce_formula.values()) == num:
                                                                        return True

                                                                # print(cn_e)
                                                                # print(cn_r)
                                                                # print(ox_a, ox_b, ox_c)
                                                                # charge_neutral_count = charge_neutral_count + 1
                                                                # print('{0:3s}  {1:3s}  {2:3s}'.format(ele_a, ele_b, ele_c))
    print('Number of combinations = {0}'.format(charge_neutral_count))
    print("--- {0} seconds to run ---".format(time.time() - start_time)) 
    return False

def check_neutrality_8(formula):
    charge_neutral_count = 0
    comp = Composition(formula)
    reduce_formula = comp.get_el_amt_dict()
    list_of_elements = list(reduce_formula.keys())
    stoichs = list(
                np.array(list(reduce_formula.values())).astype(np.int32)[:,np.newaxis]
            )
    max_num = max(reduce_formula.values())
    for element in reduce_formula.keys():
        print(len(smact.Element(element).oxidation_states), end = ",")

    for i, ele_a in enumerate(list_of_elements):
        for ox_a in smact.Element(ele_a).oxidation_states:
            for j, ele_b in enumerate(list_of_elements[i+1:]):
                for ox_b in smact.Element(ele_b).oxidation_states:
                    for k, ele_c in enumerate(list_of_elements[i+j+2:]):
                        for ox_c in smact.Element(ele_c).oxidation_states:
                            for m, ele_d in enumerate(list_of_elements[i+j+k+3:]):
                                for ox_d in smact.Element(ele_d).oxidation_states:
                                    for n, ele_e in enumerate(list_of_elements[i+j+k+m+4:]):
                                        for ox_e in smact.Element(ele_e).oxidation_states:
                                            for p, ele_f in enumerate(list_of_elements[i+j+k+m+n+5:]):
                                                for ox_f in smact.Element(ele_f).oxidation_states:
                                                    for q, ele_g in enumerate(list_of_elements[i+j+k+m+n+p+6:]):
                                                        for ox_g in smact.Element(ele_g).oxidation_states:
                                                            for s, ele_h in enumerate(list_of_elements[i+j+k+m+n+p+q+7:]):
                                                                for ox_h in smact.Element(ele_h).oxidation_states:
                                                                    # Checks if the combination is charge neutral before printing it out! #                        
                                                                    cn_e, cn_r = neutral_ratios([ox_a, ox_b, ox_c, ox_d, ox_e, ox_f, ox_g, ox_h], stoichs = stoichs, threshold = int(max_num))
                                                                    
                                                                    if cn_e:
                                                                        for num in cn_r:
                                                                            if tuple(reduce_formula.values()) == num:
                                                                                return True

                                                                            # print(cn_e)
                                                                            # print(cn_r)
                                                                            # print(ox_a, ox_b, ox_c)
                                                                            # charge_neutral_count = charge_neutral_count + 1
                                                                            # print('{0:3s}  {1:3s}  {2:3s}'.format(ele_a, ele_b, ele_c))
    print('Number of combinations = {0}'.format(charge_neutral_count))
    print("--- {0} seconds to run ---".format(time.time() - start_time)) 
    return False

def check_electronegativity(formula):
    comp = Composition(formula)
    reduce_formula = comp.get_el_amt_dict()
    element_num = len(list(reduce_formula.keys()))

    if element_num == 1:
        return True
    elif element_num == 2:
        return check_electronegativity_2(formula)
    elif element_num == 3:
        return check_electronegativity_3(formula)
    elif element_num == 4:
        return check_electronegativity_4(formula)
    elif element_num == 5:
        return check_electronegativity_5(formula)
    elif element_num == 6:
        return check_electronegativity_6(formula)
    elif element_num == 7:
        return check_electronegativity_7(formula)
    elif element_num == 8:
        return check_electronegativity_8(formula)
    else:
        print(formula)
        raise Exception('Not implemented: contact 897902311@qq.com')
        # return False

def check_electronegativity_2(formula):
    pauling_count = 0
    comp = Composition(formula)
    reduce_formula = comp.get_el_amt_dict()
    list_of_elements = list(reduce_formula.keys())
    stoichs = list(
                np.array(list(reduce_formula.values())).astype(np.int32)[:,np.newaxis]
            )
    max_num = max(reduce_formula.values())
    for i, ele_a in enumerate(list_of_elements):
        paul_a = smact.Element(ele_a).pauling_eneg
        for ox_a in smact.Element(ele_a).oxidation_states:
            for j, ele_b in enumerate(list_of_elements[i+1:]):
                paul_b = smact.Element(ele_b).pauling_eneg
                for ox_b in smact.Element(ele_b).oxidation_states:                    
                    # Puts elements, oxidation states and electronegativites into lists for convenience #
                    elements = [ele_a, ele_b]
                    oxidation_states = [ox_a, ox_b]
                    pauling_electro = [paul_a, paul_b]
                    if None in pauling_electro:
                        raise Exception("No pauling electronegativity data")
#                         return False
                    # Checks if the electronegativity makes sense and if the combination is charge neutral #
                    electroneg_makes_sense = pauling_test(oxidation_states, pauling_electro, elements)
                    cn_e, cn_r = neutral_ratios([ox_a, ox_b], stoichs = stoichs, threshold = int(max_num))
                    
                    if cn_e:
                        if electroneg_makes_sense:
                            pauling_count = pauling_count + 1

                            for num in cn_r:
                                if tuple(reduce_formula.values()) == num:
                                    # print('{0:2s}{1:3d}   {2:2s}{3:3d}   {4:2s}{5:3d}'.format(ele_a, ox_a, ele_b,
                                    #                                               ox_b, ele_c, ox_c))
                                    return True
                                                              
    # print('Number of combinations = {0}'.format(pauling_count))
    # print("--- {0} seconds to run ---".format(time.time() - start_time)) 
    return False

def check_electronegativity_3(formula):
    pauling_count = 0
    comp = Composition(formula)
    reduce_formula = comp.get_el_amt_dict()
    list_of_elements = list(reduce_formula.keys())
    stoichs = list(
                np.array(list(reduce_formula.values())).astype(np.int32)[:,np.newaxis]
            )
    max_num = max(reduce_formula.values())
    for i, ele_a in enumerate(list_of_elements):
        paul_a = smact.Element(ele_a).pauling_eneg
        for ox_a in smact.Element(ele_a).oxidation_states:
            for j, ele_b in enumerate(list_of_elements[i+1:]):
                paul_b = smact.Element(ele_b).pauling_eneg
                for ox_b in smact.Element(ele_b).oxidation_states:
                    for k, ele_c in enumerate(list_of_elements[i+j+2:]):
                        paul_c = smact.Element(ele_c).pauling_eneg
                        for ox_c in smact.Element(ele_c).oxidation_states:
                            # Puts elements, oxidation states and electronegativites into lists for convenience #
                            elements = [ele_a, ele_b, ele_c]
                            oxidation_states = [ox_a, ox_b, ox_c]
                            pauling_electro = [paul_a, paul_b, paul_c]
                            if None in pauling_electro:
                                raise Exception("No pauling electronegativity data")
                                # return False
                            # print(pauling_electro)
                            # Checks if the electronegativity makes sense and if the combination is charge neutral #
                            electroneg_makes_sense = pauling_test(oxidation_states, pauling_electro, elements)
                            cn_e, cn_r = neutral_ratios([ox_a, ox_b, ox_c], stoichs = stoichs, threshold = int(max_num))
                            
                            if cn_e:
                                if electroneg_makes_sense:
                                    pauling_count = pauling_count + 1

                                    for num in cn_r:
                                        if tuple(reduce_formula.values()) == num:
                                            # print('{0:2s}{1:3d}   {2:2s}{3:3d}   {4:2s}{5:3d}'.format(ele_a, ox_a, ele_b,
                                            #                                               ox_b, ele_c, ox_c))
                                            return True
                                                              
    # print('Number of combinations = {0}'.format(pauling_count))
    # print("--- {0} seconds to run ---".format(time.time() - start_time)) 
    return False

def check_electronegativity_4(formula):
    pauling_count = 0
    comp = Composition(formula)
    reduce_formula = comp.get_el_amt_dict()
    list_of_elements = list(reduce_formula.keys())
    stoichs = list(
                np.array(list(reduce_formula.values())).astype(np.int32)[:,np.newaxis]
            )
    max_num = max(reduce_formula.values())
    for i, ele_a in enumerate(list_of_elements):
        paul_a = smact.Element(ele_a).pauling_eneg
        for ox_a in smact.Element(ele_a).oxidation_states:
            for j, ele_b in enumerate(list_of_elements[i+1:]):
                paul_b = smact.Element(ele_b).pauling_eneg
                for ox_b in smact.Element(ele_b).oxidation_states:
                    for k, ele_c in enumerate(list_of_elements[i+j+2:]):
                        paul_c = smact.Element(ele_c).pauling_eneg
                        for ox_c in smact.Element(ele_c).oxidation_states:
                            for m, ele_d in enumerate(list_of_elements[i+j+k+3:]):
                                paul_d = smact.Element(ele_d).pauling_eneg
                                for ox_d in smact.Element(ele_d).oxidation_states:
                                    # Puts elements, oxidation states and electronegativites into lists for convenience #
                                    elements = [ele_a, ele_b, ele_c, ele_d]
                                    oxidation_states = [ox_a, ox_b, ox_c, ox_d]
                                    pauling_electro = [paul_a, paul_b, paul_c, paul_d]
                                    if None in pauling_electro:
                                        raise Exception("No pauling electronegativity data")
                                        # return False
                                    # Checks if the electronegativity makes sense and if the combination is charge neutral #
                                    electroneg_makes_sense = pauling_test(oxidation_states, pauling_electro, elements)
                                    cn_e, cn_r = neutral_ratios([ox_a, ox_b, ox_c, ox_d], stoichs = stoichs, threshold = int(max_num))
                                    
                                    if cn_e:
                                        if electroneg_makes_sense:
                                            pauling_count = pauling_count + 1

                                            for num in cn_r:
                                                if tuple(reduce_formula.values()) == num:
                                                    # print('{0:2s}{1:3d}   {2:2s}{3:3d}   {4:2s}{5:3d}'.format(ele_a, ox_a, ele_b,
                                                    #                                               ox_b, ele_c, ox_c))
                                                    return True
                                                              
    # print('Number of combinations = {0}'.format(pauling_count))
    # print("--- {0} seconds to run ---".format(time.time() - start_time)) 
    return False

def check_electronegativity_5(formula):
    pauling_count = 0
    comp = Composition(formula)
    reduce_formula = comp.get_el_amt_dict()
    list_of_elements = list(reduce_formula.keys())
    stoichs = list(
                np.array(list(reduce_formula.values())).astype(np.int32)[:,np.newaxis]
            )
    max_num = max(reduce_formula.values())
    for i, ele_a in enumerate(list_of_elements):
        paul_a = smact.Element(ele_a).pauling_eneg
        for ox_a in smact.Element(ele_a).oxidation_states:
            for j, ele_b in enumerate(list_of_elements[i+1:]):
                paul_b = smact.Element(ele_b).pauling_eneg
                for ox_b in smact.Element(ele_b).oxidation_states:
                    for k, ele_c in enumerate(list_of_elements[i+j+2:]):
                        paul_c = smact.Element(ele_c).pauling_eneg
                        for ox_c in smact.Element(ele_c).oxidation_states:
                            for m, ele_d in enumerate(list_of_elements[i+j+k+3:]):
                                paul_d = smact.Element(ele_d).pauling_eneg
                                for ox_d in smact.Element(ele_d).oxidation_states:
                                    for n, ele_e in enumerate(list_of_elements[i+j+k+m+4:]):
                                        paul_e = smact.Element(ele_e).pauling_eneg
                                        for ox_e in smact.Element(ele_e).oxidation_states:                             
                                            # Puts elements, oxidation states and electronegativites into lists for convenience #
                                            elements = [ele_a, ele_b, ele_c, ele_d, ele_e]
                                            oxidation_states = [ox_a, ox_b, ox_c, ox_d, ox_e]
                                            pauling_electro = [paul_a, paul_b, paul_c, paul_d, paul_e]
                                            if None in pauling_electro:
                                                raise Exception("No pauling electronegativity data")
                                                # return False
                                            # Checks if the electronegativity makes sense and if the combination is charge neutral #
                                            electroneg_makes_sense = pauling_test(oxidation_states, pauling_electro, elements)
                                            cn_e, cn_r = neutral_ratios([ox_a, ox_b, ox_c, ox_d, ox_e], stoichs = stoichs, threshold = int(max_num))
                                            
                                            if cn_e:
                                                if electroneg_makes_sense:
                                                    pauling_count = pauling_count + 1

                                                    for num in cn_r:
                                                        if tuple(reduce_formula.values()) == num:
                                                            # print('{0:2s}{1:3d}   {2:2s}{3:3d}   {4:2s}{5:3d}'.format(ele_a, ox_a, ele_b,
                                                            #                                               ox_b, ele_c, ox_c))
                                                            return True
                                                              
    # print('Number of combinations = {0}'.format(pauling_count))
    # print("--- {0} seconds to run ---".format(time.time() - start_time)) 
    return False

def check_electronegativity_6(formula):
    pauling_count = 0
    comp = Composition(formula)
    reduce_formula = comp.get_el_amt_dict()
    list_of_elements = list(reduce_formula.keys())
    stoichs = list(
                np.array(list(reduce_formula.values())).astype(np.int32)[:,np.newaxis]
            )
    max_num = max(reduce_formula.values())
    for i, ele_a in enumerate(list_of_elements):
        paul_a = smact.Element(ele_a).pauling_eneg
        for ox_a in smact.Element(ele_a).oxidation_states:
            for j, ele_b in enumerate(list_of_elements[i+1:]):
                paul_b = smact.Element(ele_b).pauling_eneg
                for ox_b in smact.Element(ele_b).oxidation_states:
                    for k, ele_c in enumerate(list_of_elements[i+j+2:]):
                        paul_c = smact.Element(ele_c).pauling_eneg
                        for ox_c in smact.Element(ele_c).oxidation_states:
                            for m, ele_d in enumerate(list_of_elements[i+j+k+3:]):
                                paul_d = smact.Element(ele_d).pauling_eneg
                                for ox_d in smact.Element(ele_d).oxidation_states:
                                    for n, ele_e in enumerate(list_of_elements[i+j+k+m+4:]):
                                        paul_e = smact.Element(ele_e).pauling_eneg
                                        for ox_e in smact.Element(ele_e).oxidation_states:
                                            for p, ele_f in enumerate(list_of_elements[i+j+k+m+n+5:]):
                                                paul_f = smact.Element(ele_f).pauling_eneg
                                                for ox_f in smact.Element(ele_f).oxidation_states:
                                                    # Puts elements, oxidation states and electronegativites into lists for convenience #
                                                    elements = [ele_a, ele_b, ele_c, ele_d, ele_e, ele_f]
                                                    oxidation_states = [ox_a, ox_b, ox_c, ox_d, ox_e, ox_f]
                                                    pauling_electro = [paul_a, paul_b, paul_c, paul_d, paul_e, paul_f]
                                                    if None in pauling_electro:
                                                        raise Exception("No pauling electronegativity data")
                                                        # return False
                                                    # Checks if the electronegativity makes sense and if the combination is charge neutral #
                                                    electroneg_makes_sense = pauling_test(oxidation_states, pauling_electro, elements)
                                                    cn_e, cn_r = neutral_ratios([ox_a, ox_b, ox_c, ox_d, ox_e, ox_f], stoichs = stoichs, threshold = int(max_num))
                                                    
                                                    if cn_e:
                                                        if electroneg_makes_sense:
                                                            pauling_count = pauling_count + 1

                                                            for num in cn_r:
                                                                if tuple(reduce_formula.values()) == num:
                                                                    # print('{0:2s}{1:3d}   {2:2s}{3:3d}   {4:2s}{5:3d}'.format(ele_a, ox_a, ele_b,
                                                                    #                                               ox_b, ele_c, ox_c))
                                                                    return True
                                                              
    # print('Number of combinations = {0}'.format(pauling_count))
    # print("--- {0} seconds to run ---".format(time.time() - start_time)) 
    return False

def check_electronegativity_7(formula):
    pauling_count = 0
    comp = Composition(formula)
    reduce_formula = comp.get_el_amt_dict()
    list_of_elements = list(reduce_formula.keys())
    stoichs = list(
                np.array(list(reduce_formula.values())).astype(np.int32)[:,np.newaxis]
            )
    max_num = max(reduce_formula.values())
    # for element in reduce_formula.keys():
    #     print(len(smact.Element(element).oxidation_states), end = ",")
    for i, ele_a in enumerate(list_of_elements):
        paul_a = smact.Element(ele_a).pauling_eneg
        for ox_a in smact.Element(ele_a).oxidation_states:
            for j, ele_b in enumerate(list_of_elements[i+1:]):
                paul_b = smact.Element(ele_b).pauling_eneg
                for ox_b in smact.Element(ele_b).oxidation_states:
                    for k, ele_c in enumerate(list_of_elements[i+j+2:]):
                        paul_c = smact.Element(ele_c).pauling_eneg
                        for ox_c in smact.Element(ele_c).oxidation_states:
                            for m, ele_d in enumerate(list_of_elements[i+j+k+3:]):
                                paul_d = smact.Element(ele_d).pauling_eneg
                                for ox_d in smact.Element(ele_d).oxidation_states:
                                    for n, ele_e in enumerate(list_of_elements[i+j+k+m+4:]):
                                        paul_e = smact.Element(ele_e).pauling_eneg
                                        for ox_e in smact.Element(ele_e).oxidation_states:
                                            for p, ele_f in enumerate(list_of_elements[i+j+k+m+n+5:]):
                                                paul_f = smact.Element(ele_f).pauling_eneg
                                                for ox_f in smact.Element(ele_f).oxidation_states:
                                                    for q, ele_g in enumerate(list_of_elements[i+j+k+m+n+p+6:]):
                                                        paul_g = smact.Element(ele_g).pauling_eneg
                                                        for ox_g in smact.Element(ele_g).oxidation_states:
                                                            # Puts elements, oxidation states and electronegativites into lists for convenience #
                                                            elements = [ele_a, ele_b, ele_c, ele_d, ele_e, ele_f, ele_g]
                                                            oxidation_states = [ox_a, ox_b, ox_c, ox_d, ox_e, ox_f, ox_g]
                                                            pauling_electro = [paul_a, paul_b, paul_c, paul_d, paul_e, paul_f, paul_g]
                                                            if None in pauling_electro:
                                                                raise Exception("No pauling electronegativity data")
                                                                # return False
                                                            # Checks if the electronegativity makes sense and if the combination is charge neutral #
                                                            electroneg_makes_sense = pauling_test(oxidation_states, pauling_electro, elements)
                                                            cn_e, cn_r = neutral_ratios([ox_a, ox_b, ox_c, ox_d, ox_e, ox_f, ox_g], stoichs = stoichs, threshold = int(max_num))
                                                            
                                                            if cn_e:
                                                                if electroneg_makes_sense:
                                                                    pauling_count = pauling_count + 1

                                                                    for num in cn_r:
                                                                        if tuple(reduce_formula.values()) == num:
                                                                            # print('{0:2s}{1:3d}   {2:2s}{3:3d}   {4:2s}{5:3d}'.format(ele_a, ox_a, ele_b,
                                                                            #                                               ox_b, ele_c, ox_c))
                                                                            return True
                                                              
    # print('Number of combinations = {0}'.format(pauling_count))
    # print("--- {0} seconds to run ---".format(time.time() - start_time)) 
    return False

def check_electronegativity_8(formula):
    pauling_count = 0
    comp = Composition(formula)
    reduce_formula = comp.get_el_amt_dict()
    list_of_elements = list(reduce_formula.keys())
    stoichs = list(
                np.array(list(reduce_formula.values())).astype(np.int32)[:,np.newaxis]
            )
    max_num = max(reduce_formula.values())
    # for element in reduce_formula.keys():
    #     print(len(smact.Element(element).oxidation_states), end = ",")

    for i, ele_a in enumerate(list_of_elements):
        paul_a = smact.Element(ele_a).pauling_eneg
        for ox_a in smact.Element(ele_a).oxidation_states:
            for j, ele_b in enumerate(list_of_elements[i+1:]):
                paul_b = smact.Element(ele_b).pauling_eneg
                for ox_b in smact.Element(ele_b).oxidation_states:
                    for k, ele_c in enumerate(list_of_elements[i+j+2:]):
                        paul_c = smact.Element(ele_c).pauling_eneg
                        for ox_c in smact.Element(ele_c).oxidation_states:
                            for m, ele_d in enumerate(list_of_elements[i+j+k+3:]):
                                paul_d = smact.Element(ele_d).pauling_eneg
                                for ox_d in smact.Element(ele_d).oxidation_states:
                                    for n, ele_e in enumerate(list_of_elements[i+j+k+m+4:]):
                                        paul_e = smact.Element(ele_e).pauling_eneg
                                        for ox_e in smact.Element(ele_e).oxidation_states:
                                            for p, ele_f in enumerate(list_of_elements[i+j+k+m+n+5:]):
                                                paul_f = smact.Element(ele_f).pauling_eneg
                                                for ox_f in smact.Element(ele_f).oxidation_states:
                                                    for q, ele_g in enumerate(list_of_elements[i+j+k+m+n+p+6:]):
                                                        paul_g = smact.Element(ele_g).pauling_eneg
                                                        for ox_g in smact.Element(ele_g).oxidation_states:
                                                            for s, ele_h in enumerate(list_of_elements[i+j+k+m+n+p+q+7:]):
                                                                paul_h = smact.Element(ele_h).pauling_eneg
                                                                for ox_h in smact.Element(ele_h).oxidation_states:
                                                                    # Puts elements, oxidation states and electronegativites into lists for convenience #
                                                                    elements = [ele_a, ele_b, ele_c, ele_d, ele_e, ele_f, ele_g, ele_h]
                                                                    oxidation_states = [ox_a, ox_b, ox_c, ox_d, ox_e, ox_f, ox_g, ox_h]
                                                                    pauling_electro = [paul_a, paul_b, paul_c, paul_d, paul_e, paul_f, paul_g, paul_h]
                                                                    if None in pauling_electro:
                                                                        raise Exception("No pauling electronegativity data")
                                                                        # return False
                                                                    # Checks if the electronegativity makes sense and if the combination is charge neutral #
                                                                    electroneg_makes_sense = pauling_test(oxidation_states, pauling_electro, elements)
                                                                    cn_e, cn_r = neutral_ratios([ox_a, ox_b, ox_c, ox_d, ox_e, ox_f, ox_g, ox_h], stoichs = stoichs, threshold = int(max_num))
                                                                    
                                                                    if cn_e:
                                                                        if electroneg_makes_sense:
                                                                            pauling_count = pauling_count + 1

                                                                            for num in cn_r:
                                                                                if tuple(reduce_formula.values()) == num:
                                                                                    # print('{0:2s}{1:3d}   {2:2s}{3:3d}   {4:2s}{5:3d}'.format(ele_a, ox_a, ele_b,
                                                                                    #                                               ox_b, ele_c, ox_c))
                                                                                    return True
                                                              
    # print('Number of combinations = {0}'.format(pauling_count))
    # print("--- {0} seconds to run ---".format(time.time() - start_time)) 
    return False


def check_neutrality_multiple(compounds):
    '''
    Args: 
    compounds: List (of str) of compounds
    
    Returns:
    good: List of compounds that can be charge neutral
    bad: List of compounds that cannot be charge neutral
    '''
    good = []
    bad  = [] 
    for compound in tqdm(compounds):
        try:
            if check_neutrality(Composition(compound)): # If neutral
                good.append(compound)
            else:
                bad.append(compound)
        except Exception:
            print('Compound not valid')
    return good, bad

def check_electronegativity_multiple(compounds):
    '''
    Args: 
    compounds: List (of str) of compounds
    
    Returns:
    good: List of compounds that have acceptable electronegativity
    bad: List of compounds that do not have acceptable electronegativity
    '''
    good = []
    bad  = [] 
    for compound in tqdm(compounds):
        try:
            if check_electronegativity(compound): # If neutral
                good.append(compound)
            else:
                bad.append(compound)
        except Exception:
            print('Compound not valid')
    return good, bad

def check_both_multiple(compounds):
    '''
    Args: 
    compounds: List (of str) of compounds
    
    Returns:
    good: List of compounds that can be both charge neutral and have acceptable electronegativity
    bad: List of compounds that fails either one of the checks
    '''
    good = []
    bad  = [] 
    for compound in compounds:
        try:
            if check_electronegativity(compound) and check_neutrality(Composition(compound)): # If both
                good.append(compound)
            else:
                bad.append(compound)
        except Exception:
            print('Compound not valid')
    return good, bad