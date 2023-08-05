# SPDX-License-Identifier: MIT
# Copyright (C) 2021 Max Bachmann

from rapidfuzz.utils import _fallback_import

_mod = "rapidfuzz.fuzz"
ratio = _fallback_import(_mod, "ratio")
partial_ratio = _fallback_import(_mod, "partial_ratio")
partial_ratio_alignment = _fallback_import(_mod, "partial_ratio_alignment")
token_sort_ratio = _fallback_import(_mod, "token_sort_ratio")
token_set_ratio = _fallback_import(_mod, "token_set_ratio")
token_ratio = _fallback_import(_mod, "token_ratio")
partial_token_sort_ratio = _fallback_import(_mod, "partial_token_sort_ratio")
partial_token_set_ratio = _fallback_import(_mod, "partial_token_set_ratio")
partial_token_ratio = _fallback_import(_mod, "partial_token_ratio")
WRatio = _fallback_import(_mod, "WRatio")
QRatio = _fallback_import(_mod, "QRatio")
