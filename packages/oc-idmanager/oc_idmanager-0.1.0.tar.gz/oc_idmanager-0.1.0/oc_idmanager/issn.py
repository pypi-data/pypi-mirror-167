#!python
# Copyright 2019, Silvio Peroni <essepuntato@gmail.com>
# Copyright 2022, Giuseppe Grieco <giuseppe.grieco3@unibo.it>, Arianna Moretti <arianna.moretti4@unibo.it>, Elia Rizzetto <elia.rizzetto@studio.unibo.it>, Arcangelo Massari <arcangelo.massari@unibo.it>
#
# Permission to use, copy, modify, and/or distribute this software for any purpose
# with or without fee is hereby granted, provided that the above copyright notice
# and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
# DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
# SOFTWARE.


from re import sub, match
from oc_idmanager.base import IdentifierManager


class ISSNManager(IdentifierManager):
    """This class implements an identifier manager for issn identifier"""

    def __init__(self):
        """ISSN manager constructor."""
        self._p = "issn:"
        super(ISSNManager, self).__init__()

    def is_valid(self, id_string):
        """It returns the validity of an issn.

        Args:
            id_string (str): the issn to validate

        Returns:
            bool: true if the issn is valid, false otherwise.
        """
        issn = self.normalise(id_string)
        return (
            issn is not None
            and self.check_digit(issn)
        )

    def normalise(self, id_string, include_prefix=False):
        """It normalizes the ISSN.

        Args:
            id_string (str): the issn to normalize.
            include_prefix (bool, optional): indicates if include the prefix. Defaults to False.

        Returns:
            str: the normalized issn
        """
        try:
            issn_string = sub("[^X0-9]", "", id_string.upper())
            return "%s%s-%s" % (
                self._p if include_prefix else "",
                issn_string[:4],
                issn_string[4:8],
            )
        except:  # Any error in processing the ISSN will return None
            return None

    def check_digit(self,issn):
        """Returns True, if ISSN (of length 8 or 9) is valid according to issn syntax (this does not mean registered).

        Args:
            issn (str): the issn to check

        Returns:
            bool: true if issn is valid, false otherwise
        """
        if match("^[0-9]{4}-[0-9]{3}[0-9X]$", issn):
            issn = issn.replace("-", "")
            if len(issn) != 8:
                return False
            ss = sum([int(digit) * f for digit, f in zip(issn, range(8, 1, -1))])
            _, mod = divmod(ss, 11)
            checkdigit = 0 if mod == 0 else 11 - mod
            if checkdigit == 10:
                checkdigit = "X"
            return "{}".format(checkdigit) == issn[7]
        else:
            return False
