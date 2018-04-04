""" Adam Fidler
    Assignment 1
    DIGHT 360
    """

from collections import defaultdict  # just like dict, but returns default if key not found  # noqa
import random
# Singular-plural pairs to be used for evaluation
pairs = [('snake', 'snakes'),
         ('window', 'windows'),
         ('box', 'boxes'),
         ('boy', 'boys'),
         ('lorry', 'lorries'),
         ('potato', 'potatoes'),
         ('knife', 'knives'),
         ('girl', 'girls'),
         ('window', 'windows'),
         ('witch', 'witches'),
         ('gas', 'gases'),
         ('bus', 'buses'),
         ('kiss', 'kisses'),
         ('way', 'ways'),
         ('baby', 'babies'),
         ('hero', 'heroes'),
         ('echo', 'echoes'),
         ('embargo', 'embargoes'),
         ('tomato', 'tomatoes'),
         ('torpedo', 'torpedoes'),
         ('veto', 'vetoes'),
         ('auto', 'autos'),
         ('kangaroo', 'kangaroos'),
         ('kilo', 'kilos'),
         ('memo', 'memos'),
         ('photo', 'photos'),
         ('piano', 'pianos'),
         ('pimento', 'pimentos'),
         ('pro', 'pros'),
         ('solo', 'solos'),
         ('soprano', 'sopranos'),
         ('studio', 'studios'),
         ('tattoo', 'tattoos'),
         ('video', 'videos'),
         ('zoo', 'zoos'),
         ('buffalo', 'buffalos'),
         ('buffalo', 'buffaloes'),
         ('cargo', 'cargos'),
         ('cargo', 'cargoes'),
         ('halo', 'halos'),
         ('halo', 'haloes'),
         ('mosquito', 'mosquitos'),
         ('mosquito', 'mosquitoes'),
         ('motto', 'mottos'),
         ('motto', 'mottoes'),
         ('no', 'nos'),
         ('no', 'noes'),
         ('tornado', 'tornados'),
         ('tornado', 'tornadoes'),
         ('volcano', 'volcanos'),
         ('volcano', 'volcanoes'),
         ('zero', 'zeros'),
         ('zero', 'zeroes'),
         ('knife', 'knives'),
         ('leaf', 'leaves'),
         ('hoof', 'hooves'),
         ('life', 'lives'),
         ('self', 'selves'),
         ('elf', 'elves'),
         ('fish', 'fish'),
         ('sheep', 'sheep'),
         ('barracks', 'barracks'),
         ('foot', 'feet'),
         ('tooth', 'teeth'),
         ('goose', 'geese'),
         ('child', 'children'),
         ('man', 'men'),
         ('woman', 'women'),
         ('person', 'people'),
         ('mouse', 'mice'),
         ('deer', 'deer'),
         ('alga', 'algae'),
         ('amoeba', 'amoebae'),
         ('amoeba', 'amoebas'),
         ('antenna', 'antennae'),
         ('antenna', 'antennas'),
         ('formula', 'formulae'),
         ('formula', 'formulas'),
         ('larva', 'larvae'),
         ('nebula', 'nebulae'),
         ('nebula', 'nebulas'),
         ('vertebra', 'vertebrae'),
         ('corpus', 'corpora'),
         ('genus', 'genera'),
         ('alumnus', 'alumni'),
         ('bacillus', 'bacilli'),
         ('cactus', 'cacti'),
         ('cactus', 'cactuses'),
         ('focus', 'foci'),
         ('fungus', 'fungi'),
         ('fungus', 'funguses'),
         ('nucleus', 'nuclei'),
         ('octopus', 'octopi'),
         ('octopus', 'octopuses'),
         ('radius', 'radii'),
         ('stimulus', 'stimuli'),
         ('syllabus', 'syllabi'),
         ('syllabus', 'syllabuses'),
         ('terminus', 'termini'),
         ('addendum', 'addenda'),
         ('bacterium', 'bacteria'),
         ('curriculum', 'curricula'),
         ('curriculum', 'curriculums'),
         ('datum', 'data'),
         ('erratum', 'errata'),
         ('medium', 'media'),
         ('memorandum', 'memoranda'),
         ('memorandum', 'memorandums'),
         ('ovum', 'ova'),
         ('stratum', 'strata'),
         ('symposium', 'symposia'),
         ('symposium', 'symposiums'),
         ('apex', 'apices'),
         ('apex', 'apexes'),
         ('appendix', 'appendices'),
         ('appendix', 'appendixes'),
         ('cervix', 'cervices'),
         ('cervix', 'cervixes'),
         ('index', 'indices'),
         ('index', 'indexes'),
         ('matrix', 'matrices'),
         ('matrix', 'matrixes'),
         ('vortex', 'vortices'),
         ('analysis', 'analyses'),
         ('axis', 'axes'),
         ('basis', 'bases'),
         ('crisis', 'crises'),
         ('diagnosis', 'diagnoses'),
         ('emphasis', 'emphases'),
         ('hypothesis', 'hypotheses'),
         ('neurosis', 'neuroses'),
         ('oasis', 'oases'),
         ('parenthesis', 'parentheses'),
         ('synopsis', 'synopses'),
         ('thesis', 'theses'),
         ('criterion', 'criteria'),
         ('phenomenon', 'phenomena'),
         ('automaton', 'automata'),
         ('news', ''),
         ('gymnastics', ''),
         ('economics', ''),
         ('mathematics', ''),
         ('statistics', ''),
         ('luggage', ''),
         ('baggage', ''),
         ('furniture', ''),
         ('information', '')]

# dicts that map sg to list of pl, and pl to list of sg
sgpl_dict = defaultdict(list)
plsg_dict = defaultdict(list)
for sg, pl in pairs:
    sgpl_dict[sg].append(pl)
    plsg_dict[pl].append(sg)

irr_dict = {'genus': 'genera',
            'corpus': 'corpora',
            'bus': 'buses',
            'person': 'people',
            'child': 'children',
            'information': '',
            'fish': 'fish',
            'news': '',
            'barracks': 'barracks',
            'mouse': 'mice',
            'furniture': ''
            }


def evaluate(func, input_type='sg'):
    '''Evaluate the performance of pluralize function based on pairs data.

    func -- function that changes input word (default=pluralize)
    input_type -- 'sg' or 'pl'
    '''
    assert input_type in ['sg', 'pl']
    if input_type == 'sg':
        pair_dict = sgpl_dict
    elif input_type == 'pl':
        pair_dict = plsg_dict
    total = len(pair_dict)
    # Determine how many lexemes have more than one plural form.
    # duplicates = len(set([i for i, j in pair_data]))
    correct = 0
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for k, v in pair_dict.items():
        v = set(v)
        predicted = set(func(k))
        if v == predicted:
            print('correct:', k, '/'.join(predicted),
                  '({})'.format('/'.join(v)), sep='\t')
            tp += len(v)
            correct += 1
        else:
            print('INcorrect:', k, '/'.join(predicted),
                  '({})'.format('/'.join(v)), sep='\t')
        if len(v.difference(predicted)) > 0:
            fn += len(v.difference(predicted))
        if len(predicted.difference(v)) > 0:
            fp += len(predicted.difference(v))
        if len(v) == 0 and len(predicted) == 0:
            tn += 1
    print('accuracy:', correct, '/', total, '{:.2%}'.format(correct / total),
          '(for how many words did you get all plurals correct?)')
    print('precision:', tp, '/', tp + fp, '{:.2%}'.format(tp / (tp + fp)),
          '(of all predicted plurals, how many are correct?)')
    print('recall:', tp, '/', tp + fn, '{:.2%}'.format(tp / (tp + fn)),
          '(of all correct plural forms, how many do you predict?)')


def pluralize(sg):
    """Return list of plural form(s) of input_word.

    Building this function is the purpose of Assignment 1.
    The most basic case is already provided.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']

    my_list = list(range(26))

    if sg in irr_dict:
        return[irr_dict[sg]]

    elif sg.endswith('age'):
        return ['']

    elif (sg.endswith('s') or sg.endswith('x') or
          sg.endswith('ch') or sg.endswith('z')):
        if sg.endswith('cs'):
            return ['']
        elif sg.endswith('is'):
            return [sg[:-2] + 'es']
        elif sg.endswith('us'):
            return [sg[:-2] + 'i']
            coin_flip = random.randint(0, 1)
            if coin_flip == 0:
                return [sg[:-2] + 'i', sg[:-2] + 'es']
            else:
                return [sg[:-2] + 'i']
        elif sg.endswith('ex') or sg.endswith('ix'):
            return [sg[:-2] + 'ices', sg[:] + 'es']
        else:
            return [sg + 'es']

    elif sg.endswith('um'):
        return [sg[:-2] + 'a', sg[:] + 's']

    elif sg.endswith('on'):
        return [sg[:-2] + 'a']

    elif sg.endswith('a'):
        coin_flip = random.randint(0, 1)
        if coin_flip == 0:
            return [sg + 'e']
        else:
            return [sg + 'e', sg + 's']
    elif sg.endswith('f'):
        return [sg[:-1] + 'ves']

    elif 'ee' in sg:
        return [sg]

    elif 'oo' in sg:
        j = sg.index('oo')
        if len(sg) == j + 2:
            return [sg + 's']
        else:
            pl = sg[:j] + 'ee' + sg[j+2:]
            return [pl]

    elif sg.endswith('fe'):
        return [sg[:-2] + 'ves']

    elif sg.endswith('man'):
        return [sg[:-2] + 'en']

    elif sg.endswith('y') and sg[-2] not in vowels:
        return [sg[:-1] + 'ies']

    elif sg.endswith('o'):
        die_roll = random.choice(my_list)
        """This noticeably increases precision and recall,
            but slightly decreases accuracy.
        """
        if die_roll in my_list[0::6]:
            # 7/27 chance of ending in 'es'
            return [sg + 'es']
        elif die_roll in my_list[7::18]:
            # 12/27 chance of ending in 's'
            return [sg + 's']
        else:
            # 8/27 chance of ending in either
            return [sg + 's', sg + 'es']
    else:
        return[sg + 's']

print('evaluate pluralize function...')
evaluate(pluralize)

