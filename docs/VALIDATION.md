# Mortal Kombat 4 validation receipt

Date: 2026-08-31

Status: The local Windows build, setup-package audit, isolated RetComM build,
installed-binary boot gate, and operator acceptance pass. No repository,
release, or catalog entry was published.

Current graduation state: `bootstrap_verified`. This evidence validates the
packaging route. It does not establish full-game quality.

## Scope

- Game: Mortal Kombat 4, USA, `SLUS-00605`
- Disc layout: one CUE/BIN set with one data track
- Runtime BIOS: retail SCPH-1001
- Proposed release: `v0.3.0`
- Proposed RetComM catalog ID: `mortal-kombat-4-psx`

## Framework identity

- Studio intake: `249422969c1c59ac2a1f8aa2299e876a7133998e`
- Accepted psxrecomp base: `f23c5ba1a220fe1ca8818cc48c026d6c2f7f2c64`
- Local setup-host candidate: `84f70d670e3c458730f26fc8430e02f39b2f53a4`
- recomp-ui: `87bbf43c419c16b97bf433a84d600969159e2e84`
- recomp-net: `268e74fe718b38fe38643c358588bbc1e0f0af70`
- RetComM rbengine: `ebd94a4729abe2c0615070cef3ffe05b3f9ebf28`
- RetComM package consumer: release `v0.6.33`
- RetComM inspected source: `4a30d0615ddbf71c9c62c3bce1e3b6163e42a1bd`

The setup host uses a local framework candidate. Review and integration of that
candidate remain release gates.

## Owned-input identity

The repository and setup package do not include these files.

### Disc BIN

- Size: `718112640`
- CRC32: `8f6b19f1`
- MD5: `3c3ddcb5d2fe38070fc53f556769dd4a`
- SHA-1: `21515cdd9829521a2db76a83300b77e83855fa88`
- SHA-256: `c43311155c03f7f9c23e7228bbf8874a5fdaa0984dbbefa356e5899eb40038a3`
- Disc fingerprint: `859865f0500ef3678533867c900098be6500034e1608798a6c6b4eaeda79b6b9`
- Boot executable SHA-256: `61c94bfbe3edf1dd0d15c242320412ee11c11bc5eb3484fb117bc45fc5c7a41e`

### SCPH-1001 BIOS

- Size: `524288`
- CRC32: `37157331`
- MD5: `924e392ed05558ffdb115408c263dccf`
- SHA-1: `10155d8d6e6e832d6ea66db9bc098321fb5e8ebf`
- SHA-256: `71af94d1e47a68c11e8fdb9f8368040601514a42a5a399cda48c7d3bff1e99d3`

## Generation and local build

The generator emitted 4,729 static functions in 188 shards. The generated
game source contained 10,426,285 lines. CMake configured and built the
`psx-runtime` Release target with retail SCPH-1001 support and netplay disabled.

The local setup-host executable had these properties:

- File: `Mortal_Kombat_4.exe`
- Size: `63260754`
- SHA-256: `7160e9452cd69804ae041f0ccf9caf909f44667c682c8e2b350c9ce926916693`

## Setup package

- File: `mortal-kombat-4-recomp-0.3.0-windows-x64.zip`
- Size: `47369495`
- SHA-256: `a1369cb36c778356aaefcbd57caa7a015cf6abd58b67c3de64baf942e6961a7f`
- ZIP entries: `2186`
- Extracted files: `1949`
- Extracted bytes: `124755064`
- Forbidden disc, save, and memory-card files: `0`
- Forbidden retail BIOS files: `0`
- Unsafe ZIP paths: `0`
- Private absolute paths: `0`

The package includes the CLI and both emitters. It does not include retail disc
data, retail BIOS data, generated retail game code, or save data.

## RetComM installation evidence

RetComM release `v0.6.33` consumed the exact extracted archive in a fresh data
root. It matched the disc and SCPH-1001 BIOS identities from the local catalog
draft. It then generated, built, and installed source ref `v0.3.0`.

Installed executable:

- File: `Mortal_Kombat_4.exe`
- Size: `51767808`
- SHA-256: `89275554b48bfaa56a1979b2c7f277434c4d1dfb45fe07a6b0652bb5ee50daa5`

Hidden headless boot gate:

- BIOS backend: LLE, recompiled SCPH-1001
- BIOS boot: LLE, real intro
- Final frame: `5417`
- Required frame: `600`
- VBlank raises: `5417`
- Fatal state: none
- Automatic freeze dumps: `0`
- Failed freeze dumps: `0`
- Process state after 25 seconds: active; the bounded gate stopped it

## Operator acceptance

On 2026-08-31, the operator reported that Mortal Kombat 4 works after the
exact-package handoff. This closes the manual Windows package-acceptance gate.
The operator also ran the package from a writable directory whose path contains
spaces. This closes the spaced-path setup gate. The test route and duration
were not recorded. This result does not establish full-game quality or support
on another platform.

## Open release gates

1. Review and integrate the setup-host candidate through the framework process.
2. Pin the accepted framework commit in this repository.
3. Run setup-host release CI on Windows, Linux x64, macOS x64, and macOS ARM64.
4. Prepare the standalone public repository and immutable `v0.3.0` draft.
5. Show the exact release manifest and request publication approval.
6. Publish only after approval, then download and audit the public asset.
7. Show the final catalog manifest and request submission approval.
