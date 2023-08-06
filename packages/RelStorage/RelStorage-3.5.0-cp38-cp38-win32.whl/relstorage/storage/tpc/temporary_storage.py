# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2019 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

"""
Temporary local storage for pickles that
will be uploaded to the database and the local
and memcache.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tempfile import SpooledTemporaryFile

from relstorage._compat import OID_OBJECT_MAP_TYPE as OidObjectMap
from relstorage._compat import OidObjectMap_max_key
from relstorage._compat import iteroiditems
from relstorage._compat import NStringIO

class TPCTemporaryStorage(object):
    __slots__ = (
        '_queue',
        '_queue_contents',
    )

    def __init__(self):
        # start with a fresh in-memory buffer instead of reusing one that might
        # already be spooled to disk.
        # TODO: An alternate idea would be a temporary sqlite database.
        self._queue = SpooledTemporaryFile(max_size=10 * 1024 * 1024)
        # {oid: (startpos, endpos, prev_tid_int)}
        self._queue_contents = OidObjectMap()

    def reset(self):
        self._queue_contents.clear()
        self._queue.seek(0)

    def store_temp(self, oid_int, state, prev_tid_int=0):
        """
        Queue an object for caching.

        Typically, we can't actually cache the object yet, because its
        transaction ID is not yet chosen.
        """
        queue = self._queue
        queue.seek(0, 2)  # seek to end
        startpos = queue.tell()
        queue.write(state)
        endpos = queue.tell()
        self._queue_contents[oid_int] = (startpos, endpos, prev_tid_int)

    def __len__(self):
        # How many distinct OIDs have been stored?
        # This also lets us be used in a boolean context to see
        # if we've actually stored anything or are closed.
        return len(self._queue_contents)

    @property
    def stored_oids(self):
        return self._queue_contents

    @property
    def max_stored_oid(self):
        return OidObjectMap_max_key(self._queue_contents)

    def _read_temp_state(self, startpos, endpos):
        self._queue.seek(startpos)
        length = endpos - startpos
        state = self._queue.read(length)
        if len(state) != length:
            raise AssertionError("Queued cache data is truncated")
        return state

    def read_temp(self, oid_int):
        """
        Return the bytes for a previously stored temporary item.
        """
        startpos, endpos, _ = self._queue_contents[oid_int]
        return self._read_temp_state(startpos, endpos)

    def __iter__(self):
        return self.iter_for_oids(None)

    def iter_for_oids(self, oids):
        read_temp_state = self._read_temp_state
        for startpos, endpos, oid_int, prev_tid_int in self.items(oids):
            state = read_temp_state(startpos, endpos)
            yield state, oid_int, prev_tid_int

    def items(self, oids=None):
        # Order the queue by file position, which should help
        # if the file is large and needs to be read
        # sequentially from disk.
        items = [
            (startpos, endpos, oid_int, prev_tid_int)
            for (oid_int, (startpos, endpos, prev_tid_int)) in iteroiditems(self._queue_contents)
            if oids is None or oid_int in oids
        ]
        items.sort()
        return items

    def close(self):
        if self._queue is not None:
            self._queue.close()
            self._queue = None
            self._queue_contents = () # Not None so len() keeps working

    def __repr__(self):
        approx_size = 0
        if self._queue is not None:
            self._queue.seek(0, 2)  # seek to end
            # The number of bytes we stored isn't necessarily the
            # number of bytes we send to the server, if there are duplicates
            approx_size = self._queue.tell()
        return "<%s at 0x%x count=%d bytes=%d>" % (
            type(self).__name__,
            id(self),
            len(self),
            approx_size
        )

    def __str__(self):
        base = repr(self)
        if not self:
            return base

        out = NStringIO()

        div = '=' * len(base)
        headings = ['OID', 'Length', 'Previous TID']
        col_width = (len(base) - 5) // len(headings)

        print(base, file=out)
        print(div, file=out)
        print('| ', file=out, end='')
        for heading in headings:
            print('%-*s' % (col_width, heading), end='', file=out)
            print('| ', end='', file=out)
        out.seek(out.tell() - 3)
        print('|', file=out)
        print(div, file=out)

        items = sorted(
            (oid_int, endpos - startpos, prev_tid_int)
            for (startpos, endpos, oid_int, prev_tid_int)
            in self.items()
        )

        for oid_int, length, prev_tid_int in items:
            print('%*d  |%*d |%*d' % (
                col_width, oid_int,
                col_width, length,
                col_width, prev_tid_int
            ), file=out)


        return out.getvalue()

TemporaryStorage = TPCTemporaryStorage # BWC
