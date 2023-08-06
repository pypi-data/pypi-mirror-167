# Changelog

## Unreleased

## [1.0.12]
### Fixed
 - Minor typos and clarification of README.md (#35, !39).
 - Fix author attribution (!40)

## [1.0.10] - [2022-08-19]
### Changed
 - first public release

## Added
 - now has a DOI and citation instructions in README.md (#31, !35).

## [1.0.9] - [2022-03-39]

### Added
 - Now has a extras option, so you can do `pip install fractionalcover3[rsc]` which will install the packages
   needed if you were to run the scripts on the RSC system (#28, !31).
 - Added information to metadata description (#29, !32)

## [1.0.8] - [2022-03-23]
### Changed
 - Tested on python 3.9 and seems ok.
 - Changed way requirements are managed to allow testing to work more generally, and to
   be compatible with the new python publishing approach (!21).

## [1.0.6] - [2021-08-19]

### Fixed
- A bug that could cause unintended SWIR sharpening in `qv_fractionalcver_sentinel2.py` was fixed (#18, !17)

## [1.0.5] - [2021-08-16]

### Added
 - Allow passing of `--allow-missing-metadata` to the scripts. This allows the use of development
   containers which may not have the correct metadata to be tested.

## [1.0.4] - [2021-02-18]
### Changed
- Default stage for the sentinel 2 single date fractional cover product changed from aja to aj0. (#13, !12)


## [1.0.3] - [2021-01-19]
### Changed
- Default stage for the landsat single date fractional cover product changed from dpa to dp0.

## [1.0.2] - [2020-12-23]

### Changed
- Landsat and Sentinel2 fractional cover images now scaled the same way. Output values are between 0 and 100
  with null values set to 255.

### Added
- Basic version of fractionalcover3 using tensorflow lite.

### Fixed
 - Bug in input null values fixed (#9, !10) and output null values fixed (#2, !7)

