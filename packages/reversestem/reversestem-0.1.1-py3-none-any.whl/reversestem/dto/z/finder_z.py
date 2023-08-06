
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderZ(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        if ftc == 'z_':
            from reversestem.dto.z import d_stem_z_
            return d_stem_z_

        if ftc == 'za':
            from reversestem.dto.z import d_stem_za
            return d_stem_za

        if ftc == 'zb':
            from reversestem.dto.z import d_stem_zb
            return d_stem_zb

        if ftc == 'zc':
            from reversestem.dto.z import d_stem_zc
            return d_stem_zc

        if ftc == 'zd':
            from reversestem.dto.z import d_stem_zd
            return d_stem_zd

        if ftc == 'ze':
            from reversestem.dto.z import d_stem_ze
            return d_stem_ze

        if ftc == 'zf':
            from reversestem.dto.z import d_stem_zf
            return d_stem_zf

        if ftc == 'zg':
            from reversestem.dto.z import d_stem_zg
            return d_stem_zg

        if ftc == 'zh':
            from reversestem.dto.z import d_stem_zh
            return d_stem_zh

        if ftc == 'zi':
            from reversestem.dto.z import d_stem_zi
            return d_stem_zi

        if ftc == 'zj':
            from reversestem.dto.z import d_stem_zj
            return d_stem_zj

        if ftc == 'zk':
            from reversestem.dto.z import d_stem_zk
            return d_stem_zk

        if ftc == 'zl':
            from reversestem.dto.z import d_stem_zl
            return d_stem_zl

        if ftc == 'zm':
            from reversestem.dto.z import d_stem_zm
            return d_stem_zm

        if ftc == 'zn':
            from reversestem.dto.z import d_stem_zn
            return d_stem_zn

        if ftc == 'zo':
            from reversestem.dto.z import d_stem_zo
            return d_stem_zo

        if ftc == 'zp':
            from reversestem.dto.z import d_stem_zp
            return d_stem_zp

        if ftc == 'zr':
            from reversestem.dto.z import d_stem_zr
            return d_stem_zr

        if ftc == 'zs':
            from reversestem.dto.z import d_stem_zs
            return d_stem_zs

        if ftc == 'zt':
            from reversestem.dto.z import d_stem_zt
            return d_stem_zt

        if ftc == 'zu':
            from reversestem.dto.z import d_stem_zu
            return d_stem_zu

        if ftc == 'zv':
            from reversestem.dto.z import d_stem_zv
            return d_stem_zv

        if ftc == 'zw':
            from reversestem.dto.z import d_stem_zw
            return d_stem_zw

        if ftc == 'zy':
            from reversestem.dto.z import d_stem_zy
            return d_stem_zy

        if ftc == 'zz':
            from reversestem.dto.z import d_stem_zz
            return d_stem_zz

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
