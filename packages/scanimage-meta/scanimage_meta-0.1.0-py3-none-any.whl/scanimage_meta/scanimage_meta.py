#  Copyright (c) 2022. Joseph Donovan <joe311@gmail.com>

import pprint
from collections import OrderedDict
from collections.abc import MutableMapping
from itertools import chain, zip_longest
# import ast
import re
import json

import numpy as np
import ScanImageTiffReader  # docs at https://vidriotech.gitlab.io/scanimagetiffreader-python/


def coerce_num(s):
    """Tries to coerce string into a usable value, e.g. ints"""
    s = s.strip()
    if s.startswith("'") and s.endswith("'"):
        s = s[1:-1]  # remove redundant '
    # if s == '':
    #     return None
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            if s == 'true':
                return True
            elif s == 'false':
                return False
            elif s.startswith('[') and s.endswith(']'):  # Lists and matrices
                if len(s) == 2:
                    return []
                elif s.count(';') > 0:  # Matrices
                    return np.asarray([[coerce_num(i) for i in sublist.split(' ')] for sublist in s[1:-1].split(';')]).T
                else:  # Lists
                    return [coerce_num(i) for i in s[1:-1].split(' ')]
            elif s.startswith('{') and s.endswith('}'):  # Cell array
                if s == '{}' or s == '{[]}':  # empty
                    pass
                elif s.count('[') == 0:  # 1d cell array
                    return [coerce_num(i) for i in s[1:-1].split(' ')]
                else:  # nested cell array
                    return [[coerce_num(sub) for sub in match.split(' ')] for match in re.findall('(?<=\[)[^]]+(?=\])', s)]
    # print(f'Unable to coerce: {s}')
    return s.strip()


def flatten_dummy(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        # if isinstance(v, MutableMapping):
        if isinstance(v, Dummy):
            items.extend(flatten_dummy(v.__dict__, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


class Dummy:
    """Dummy class used for exposing metadata params with dot notation, e.g. ScanimageMeta.SI.VERSION_MAJOR"""

    def __init__(self):
        pass

    def __repr__(self):
        return pprint.pformat(flatten_dummy(self.__dict__, sep='.'), compact=True, width=100)


class ScanimageMeta:
    def __init__(self, metadata, checktypecoersion=False):
        lines = metadata.split('\n')
        roiindex = lines.index('')
        header, rois = lines[:roiindex], lines[roiindex:]

        frags = [s.split('=') for s in header]
        assert set([len(l) for l in frags]) == {2}, 'Splitting metadata lines failed'

        if checktypecoersion:
            [print(l[1].strip(), coerce_num(l[1].strip()), l[0].strip()) for l in frags]
        d = {l[0].strip(): coerce_num(l[1].strip()) for l in frags}

        for k, v in d.items():
            current = self
            levels = k.split('.')
            lastlevel = levels.pop(-1)
            for level in levels:
                if hasattr(current, level):
                    current = current.__getattribute__(level)
                else:
                    current.__setattr__(level, Dummy())
                    current = current.__getattribute__(level)
            current.__setattr__(lastlevel, v)

        self.rois = json.loads(''.join(rois), object_pairs_hook=OrderedDict)['RoiGroups']['imagingRoiGroup']['rois']

    def __repr__(self):
        return pprint.pformat(flatten_dummy(self.__dict__, sep='.'), compact=True, width=100)

    @staticmethod
    def fromfilepath(tifpath):
        reader = ScanImageTiffReader.ScanImageTiffReader(tifpath)
        # desc = reader.description(0)
        metadata = reader.metadata()
        reader.close()

        return ScanimageMeta(metadata)

    def roi_indicies(self, tifdata):
        """Splits tifdata by scanimage roi, assumes single channel tifdata"""
        all_zs = sorted(list(set(chain.from_iterable([roi['zs'] for roi in self.rois]))))
        # could also use 'hStackManager.zs' - or is it actually hFastZ.userZs??
        # TODO check/ignore disabled ROIs?

        roi_zs, roi_xys = zip(*[(roi['zs'], [sf['pixelResolutionXY'] for sf in roi['scanfields']]) for roi in self.rois])

        z_rois = OrderedDict()
        for z in all_zs:
            rois_at_this_z = []
            for roinum, roi in enumerate(self.rois):
                if z in roi_zs[roinum]:
                    rois_at_this_z += (roi_xys[roinum][roi_zs[roinum].index(z)],)
            z_rois[z] = rois_at_this_z

        # zrois is dict keyed by Z, values list of roi XY sizes

        # tifdata[znum::len(zs), ...]
        # TODO is data actually saved properly according to roi format?

        raise NotImplementedError  # ROI format is a bit of a mess internally it seems...

        # return  #list of roi views into tifdata?
        # TODO scanfield object?

    # TODO could provide convenient CXYZT accessing of data, based on metadata (since tif is stored flat)
    # maybe ussing xarray?
