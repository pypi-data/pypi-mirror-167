
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderD(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        if ftc == 'd_':
            from reversestem.dto.d import d_stem_d_
            return d_stem_d_

        if ftc == 'da':
            from reversestem.dto.d import d_stem_da
            return d_stem_da

        if ftc == 'db':
            from reversestem.dto.d import d_stem_db
            return d_stem_db

        if ftc == 'dc':
            from reversestem.dto.d import d_stem_dc
            return d_stem_dc

        if ftc == 'dd':
            from reversestem.dto.d import d_stem_dd
            return d_stem_dd

        if ftc == 'de':
            from reversestem.dto.d import d_stem_de
            return d_stem_de

        if ftc == 'df':
            from reversestem.dto.d import d_stem_df
            return d_stem_df

        if ftc == 'dg':
            from reversestem.dto.d import d_stem_dg
            return d_stem_dg

        if ftc == 'dh':
            from reversestem.dto.d import d_stem_dh
            return d_stem_dh

        if ftc == 'di':
            from reversestem.dto.d import d_stem_di
            return d_stem_di

        if ftc == 'dj':
            from reversestem.dto.d import d_stem_dj
            return d_stem_dj

        if ftc == 'dk':
            from reversestem.dto.d import d_stem_dk
            return d_stem_dk

        if ftc == 'dl':
            from reversestem.dto.d import d_stem_dl
            return d_stem_dl

        if ftc == 'dm':
            from reversestem.dto.d import d_stem_dm
            return d_stem_dm

        if ftc == 'dn':
            from reversestem.dto.d import d_stem_dn
            return d_stem_dn

        if ftc == 'do':
            from reversestem.dto.d import d_stem_do
            return d_stem_do

        if ftc == 'dp':
            from reversestem.dto.d import d_stem_dp
            return d_stem_dp

        if ftc == 'dq':
            from reversestem.dto.d import d_stem_dq
            return d_stem_dq

        if ftc == 'dr':
            from reversestem.dto.d import d_stem_dr
            return d_stem_dr

        if ftc == 'ds':
            from reversestem.dto.d import d_stem_ds
            return d_stem_ds

        if ftc == 'dt':
            from reversestem.dto.d import d_stem_dt
            return d_stem_dt

        if ftc == 'du':
            from reversestem.dto.d import d_stem_du
            return d_stem_du

        if ftc == 'dv':
            from reversestem.dto.d import d_stem_dv
            return d_stem_dv

        if ftc == 'dw':
            from reversestem.dto.d import d_stem_dw
            return d_stem_dw

        if ftc == 'dy':
            from reversestem.dto.d import d_stem_dy
            return d_stem_dy

        if ftc == 'dz':
            from reversestem.dto.d import d_stem_dz
            return d_stem_dz

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
