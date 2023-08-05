# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.4.0] - 2022-09-11

### Added
- Add support for [TBlock filter format v2](https://codeberg.org/tblock/tblock/src/branch/main/docs/specs/tblock-syntax.md#version-2-0-supported-since-tblock-2-4-0)
- Add warning when the user is running `tblock -S` but that the repository index hasn't been synced once (closes #49).
- New API function to get all active filter lists
- New API function go get all active rules
- New API function to get the total count of active rules
### Changed
- Update all tests
### Deprecated
- Deprecated [TBlock filter format v1](https://codeberg.org/tblock/tblock/src/branch/main/docs/specs/tblock-syntax.md#version-1-0-deprecated-since-tblock-2-4-0)
### Fixed
- Only append valid rules to hosts file after inserting them into database
- Fix `quiet` variable not being used everywhere in API
- Handle `OSError` when hosts file is read-only
- Fixed the program not letting user set rules that already exist with the same policy but a different priority
### Security
- Prevent custom filter lists from defining rules that have user priority

## [2.3.0] - 2022-07-27

### Added
- New operation allowing to enable protection without to rebuild the full hosts file (will be useful [for the upcoming GUI](https://codeberg.org/tblock/tblock-gui))
### Changed
- Sort domains alphabetically in hosts file, as well as rules and filter lists when listing
### Fixed
- Operation `--restore` has been renamed to `--disable` to avoid confusion

## [2.2.0] - 2022-07-22

### Added
- New converter option to prevent blank lines from being converted
- New option to rebuild the full hosts file when adding or deleting a rule
- New operation to check which filter list has set a rule for specified domains
- Add runit support (thanks [@rokosun](https://codeberg.org/rokosun))
- Use `pyproject.toml` for modern Python module
### Changed
- The converter now also converts blank lines by default
- Apply rules directly to hosts file without requiring full rebuild each time
- The `fetchall()` method is no longer used when performing SQLite queries, since [it can slow down the program and take more memory than iterating through the cursor](https://stackoverflow.com/questions/21334767/is-sqlite3-fetchall-necessary)
- Insert all rules without checking and run a SQL query afterwards to remove wildcard matches, instead of checking it when inserting rules
- Use directly sqlite to match wildcards instead of re.match()
- Alternate disk and RAM storage when updating hosts file
- Improve speed when updating hosts file
- Use multiprocessing for fast allowing rules checking (thanks [@schrmh](https://codeberg.org/schrmh))
- Don't check allowing rules that do not contain wildcards
- Upgrade the argumentor module to v1.0.0
- `0.0.0.0` is now the default blocking address
### Fixed
- Handle `sqlite3.OperationalError` when database is locked
- General speed improvements (see #39)
- Fixed "Cleaning rules cache" message showing `1` instead of `0` when no rules are set
### Removed
- Removed `pandoc` from build dependencies

## [2.2.0-rc.1] - 2022-07-17

### Added
- New option to rebuild the full hosts file when adding or deleting a rule
### Changed
- Apply rules directly to hosts file without requiring full rebuild each time
- The `fetchall()` method is no longer used when performing SQLite queries, since [it can slow down the program and take more memory than iterating through the cursor](https://stackoverflow.com/questions/21334767/is-sqlite3-fetchall-necessary)
- Upgrade the argumentor module to v1.0.0
- `0.0.0.0` is now the default blocking address
### Fixed
- Fixed "Cleaning rules cache" message showing `1` instead of `0` when no rules are set

## [2.2.0-rc] - 2022-07-13

### Added
- Use `pyproject.toml` for modern Python module
### Changed
- Use multiprocessing for fast allowing rules checking (thanks [@schrmh](https://codeberg.org/schrmh))
- Don't check allowing rules that do not contain wildcards
### Removed
- Removed `pandoc` from build dependencies

## [2.2.0-beta] - 2022-06-26

### Added
- Add runit support (thanks [@rokosun](https://codeberg.org/rokosun))
### Changed
- Improve speed when updating hosts file

## [2.2.0-alpha] - 2022-06-21

### Added
- New operation to check which filter list has set a rule for specified domains
### Changed
- Insert all rules without checking and run a SQL query afterwards to remove wildcard matches, instead of checking it when inserting rules
- Use directly sqlite to match wildcards instead of re.match()
- Alternate disk and RAM storage when updating hosts file
### Fixed
- General speed improvements (see #39)

## [2.1.0] - 2022-05-04

### Added
- Introduce filter lists tags and warnings
### Changed
- Use JSON index in remote repository
- Support older versions of the requests module (2.23.0)
- Set `sync_repo` to `true` by default in daemon configuration
### Deprecated
- Deprecated XML format in filter list repository
### Fixed
- Fix colors not showing properly on Windows by using `colorama.init()`
- Fix an issue with the daemon trying to use the database when it is locked
### Removed
- Remove defusedxml from dependencies
- Remove prefer_onion option from config
### Security
- Verify checksum of cached filter lists before using them

## [2.0.0] - 2022-04-20

### Added
- Added a daemon that regularly updates online blocklists
- Daemon can prevent the hosts file from being edited by another program
- Store retrieved blocklists in cache, in case the network is not available at next update
- Checks for new releases when fetching blocklist repository index
- Added an operation to clean cached filter lists
- Added an option to specify the syntax of a custom filter list
- Onion mirror can be selected by default in configuration
- Add script to generate a blocklist that blocks all sites protected by Cloudflare
- New terminal output
- Brand new status interface
### Changed
- Use the argumentor module to parse command-line arguments
- Code has been completely re-written
- Improved converter regex rules for detecting filter list syntax
- Improved configuration support
- New database structure
### Fixed
- Fixed memory issue with converter
### Removed
- Removed support for Opera filter list syntax
- Replaced the `--update-all` operation by `--update`, updating a single filter list is now not possible anymore

## [2.0.0-beta.1] - 2022-02-20

### Added
- Add option to specify the syntax of custom filter lists
### Fixed
- Fixed two issues with wildcard allowing rules

## [2.0.0-beta] - 2022-02-08

### Added
- Add script to generate a blocklist that blocks all sites protected by Cloudflare
### Fixed
- Fix cache directory not being present on Windows
- Fixed several bugs with database unlocking (including #37)
- Fixed error when converting a blocklist into tblock syntax
- Fixed status interface showing "mac" on Windows

## [2.0.0-alpha.1] - 2022-01-17

### Added
- Onion mirror can be selected by default in configuration
### Changed
- Allow to run with `python -m tblock`
### Fixed
- Sync operation is now quiet for other operations
- Fixed converter detection and convertion for list, dnsmasq, tblock and adblockplus syntax
- Fixed repository version in status interface
### Removed
- Replaced the `--update-all` operation by `--update`, updating a single filter list is now not possible anymore

## [2.0.0-alpha] - 2021-12-25

### Added
- Added a daemon that regularly updates online blocklists
- Daemon can prevent the hosts file from being edited by another program
- Store retrieved blocklists in cache, in case the network is not available at next update
- Checks for new releases when fetching blocklist repository index
- New terminal output
- Brand new status interface
### Changed
- Use the argumentor module to parse command-line arguments
- Code has been completely re-written
- New database structure
### Fixed
- Fixed memory issue with converter
- Improved converter speed
- Improved configuration support
### Removed
- Removed support for Opera filter list syntax

## [1.3.2] - 2021-08-09

### Security
- Security fixes (use defusedxml instead of xml)

## [1.3.1] - 2021-08-05

### Added
- New icon for the converter's Windows executable
### Fixed
- Fixed IPv6-related config
- Fixed animation while retrieving filter

## [1.3.0] - 2021-08-02

### Added
- Added support for IPv6 rules
- Added an unofficial mirror for Energized Protection Filters (see #29)
- Added custom configuration
- Added support for filter mirrors
### Changed
- Prompt now only reacts to 'y' and 'n'
- Updated database structure
### Fixed
- Fixed a critical issue (#27)

## [1.2.1] - 2021-08-01

### Added
- Added support for IPv6 rules
- Added custom configuration
### Fixed
- Fixed confirmation prompt

## [1.2.0] - 2021-07-12

### Added
- Added wildcards support for allowing rules
- Added option to generate hosts file

## [1.1.4] - 2021-06-23

### Changed
- Changed remote repository locations
### Fixed
- Fixed search operation

## [1.1.3] - 2021-06-22

### Fixed
Fixed critical issue #25

## [1.1.2] - 2021-06-22

### Changed
- TBlock now tries to get filters before marking them as `subscribed`
### Fixed
- Added a clean error message when local filter is a directory (#22)
- Fixed conflict between operation `--sync` and option `--sync` (#21)

## [1.1.1] - 2021-06-21

### Changed
- Now update remote repository before any other operation when '-y' option is specified
### Fixed
- Fixed developer scripts

## [1.1.0] - 2021-06-17

### Added
- Added new information on status page
### Changed
- Changed installation method in Makefile
### Fixed
- Fixed filter info display
- Fixed real path for local filters

## [1.0.1] - 2021-06-07

### Changed
- Improved examples in man page
### Fixed
- Fixed help page

## [1.0.0] - 2021-06-04

### Added
- Published package to Fedora Copr and Ubuntu PPA
- Added support for Windows
- Added a security feature to detect hosts hijack
- Locks the database while editing it
- It is now possible to change the ID of a custom filter
- Brand new CLI animation
### Changed
- Improved status overview
- Code has been completely re-written
- Lots of improvements in the converter
### Fixed
- Fixed redirecting rules in hosts file format (issue #15)
- New argument parsing (closes #10, #11)

## [0.0.6] - 2021-04-27

### Fixed
- Fixed a critical issue for new users

## [0.0.5] - 2021-04-27

### Added
- Added info about converter in converted filters
### Changed
- Changed the default Makefile installation method
- The database is now using primary keys in tables
- Improved argument parsing
### Fixed
- Fixed compatibility, now exits if unsupported OS

## [0.0.4] - 2021-04-23

### Changed
- Change arrows when executing a task
### Fixed
- Fixed release script
- Fixed Termux compatibility (thanks to Anter Amo, pull request #6)
### Removed
- Removed prompt before updating hosts file after another action

## [0.0.3] - 2021-04-22

### Added
- Added a new mirror on git.disroot.org
- Added support for Opera filter syntax
- Added an exception if downloaded repository index is not an XML file
### Changed
- Changed how TBlock retrieves mirrors
- Improved speed when fetching ad-blocker status
- Improved Opera filter convertion
### Fixed
- Fixed Termux support (issue #1)

## [0.0.2] - 2021-04-21

### Added
- Added support for Termux (issue #1)
- Added new converter option to detect filter syntax
### Changed
- Changed Makefile installation method
### Fixed
- Fixed script to generate man pages (issue #5)
- Fixed gpg-signing in when compiling into a binary
- Fixed filter rule priority (issue #4)

## [0.0.1] - 2021-04-20

### Added
- Initial release


[Unreleased]: https://codeberg.org/tblock/tblock/src/branch/main
[2.4.0]: https://codeberg.org/tblock/tblock/releases/tag/2.4.0
[2.3.0]: https://codeberg.org/tblock/tblock/releases/tag/2.3.0
[2.2.0]: https://codeberg.org/tblock/tblock/releases/tag/2.2.0
[2.2.0-rc.1]: https://codeberg.org/tblock/tblock/releases/tag/2.2.0-rc.1
[2.2.0-rc]: https://codeberg.org/tblock/tblock/releases/tag/2.2.0-rc
[2.2.0-beta]: https://codeberg.org/tblock/tblock/releases/tag/2.2.0-beta
[2.2.0-alpha]: https://codeberg.org/tblock/tblock/releases/tag/2.2.0-alpha
[2.1.0]: https://codeberg.org/tblock/tblock/releases/tag/2.1.0
[2.0.0]: https://codeberg.org/tblock/tblock/releases/tag/2.0.0
[2.0.0-beta.1]: https://codeberg.org/tblock/tblock/releases/tag/2.0.0-beta.1
[2.0.0-beta]: https://codeberg.org/tblock/tblock/releases/tag/2.0.0-beta
[2.0.0-alpha.1]: https://codeberg.org/tblock/tblock/releases/tag/2.0.0-alpha.1
[2.0.0-alpha]: https://codeberg.org/tblock/tblock/releases/tag/2.0.0-alpha
[1.3.2]: https://codeberg.org/tblock/tblock/releases/tag/1.3.2
[1.3.1]: https://codeberg.org/tblock/tblock/releases/tag/1.3.1
[1.3.0]: https://codeberg.org/tblock/tblock/releases/tag/1.3.0
[1.2.1]: https://codeberg.org/tblock/tblock/releases/tag/1.2.1
[1.2.0]: https://codeberg.org/tblock/tblock/releases/tag/1.2.0
[1.1.4]: https://codeberg.org/tblock/tblock/releases/tag/1.1.4
[1.1.3]: https://codeberg.org/tblock/tblock/releases/tag/1.1.3
[1.1.2]: https://codeberg.org/tblock/tblock/releases/tag/1.1.2
[1.1.1]: https://codeberg.org/tblock/tblock/releases/tag/1.1.1
[1.1.0]: https://codeberg.org/tblock/tblock/releases/tag/1.1.0
[1.0.1]: https://codeberg.org/tblock/tblock/releases/tag/1.0.1
[1.0.0]: https://codeberg.org/tblock/tblock/releases/tag/1.0.0
[0.0.6]: https://codeberg.org/tblock/tblock/releases/tag/0.0.6
[0.0.5]: https://codeberg.org/tblock/tblock/releases/tag/0.0.5
[0.0.4]: https://codeberg.org/tblock/tblock/releases/tag/0.0.4
[0.0.3]: https://codeberg.org/tblock/tblock/releases/tag/0.0.3
[0.0.2]: https://codeberg.org/tblock/tblock/releases/tag/0.0.2
[0.0.1]: https://codeberg.org/tblock/tblock/releases/tag/0.0.1
