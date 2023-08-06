v2.1.2 (2022-09-14)
===================

Bugfix
---------------------------

- Fix the type of some reprocessing keywords.


v2.1.1 (2022-09-12)
===================

Bugfix
------

- Relaxing requiredness of headers added in v2.1.0


v2.1.0 (2022-09-12)
===================

Features
--------

- Adding new keywords to support the addition of reprocessing metadata to the FITS headers.


v2.0.0 (2022-04-26)
===================

Backwards Compatible Changes to the Specification
-------------------------------------------------

- Updated Spec122 and Spec214 schemas to be consistent with SPEC-122 Rev F. (`#21 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/21>`__)


New Feature in the Python API
-----------------------------

- Change the return values of all specification loading functions to be
  ``frozendict``.
  This means that the specifications once constructed are (largely) immutable and
  therefore can be cached. Caching the specfications massively speeds up
  subsequent calls to the specification construction functions. (`#22 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/22>`__)


v1.5.0 (2022-02-10)
===================

Documentation
-------------

- Add a documenation build for the yaml files containing the specifications and other information about the data products. (`#18 <https://bitbucket.org/dkistdc/dkist-fits-specifications/pull-requests/18>`__)
