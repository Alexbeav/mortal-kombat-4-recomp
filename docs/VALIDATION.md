# Mortal Kombat 4 validation receipt

Date: 2026-08-31

Status: The `v0.3.0` through `v0.3.3` package drafts are rejected. The
replacement `v0.3.4` Windows package passes the local archive audit and two
clean-room RetComM canaries. No repository, release, or catalog entry was
published.

Current graduation state: `bootstrap_verified`. The runtime evidence validates
the RetComM build flow. Public package qualification remains incomplete.

## Scope

- Game: Mortal Kombat 4, USA, `SLUS-00605`
- Disc layout: one CUE/BIN set with one data track
- Runtime BIOS: retail SCPH-1001
- Proposed release: `v0.3.4`
- Proposed RetComM catalog ID: `mortal-kombat-4-psx`

## Framework identity

- Studio intake: `249422969c1c59ac2a1f8aa2299e876a7133998e`
- Accepted psxrecomp base: `f23c5ba1a220fe1ca8818cc48c026d6c2f7f2c64`
- Setup-host integration: `Alexbeav/psxrecomp` tag
  `setup-host-retail-bios-v2`, commit
  `eecf3b2a4ee3148f01f8f92b512930fd6307d82e`
- recomp-ui: `87bbf43c419c16b97bf433a84d600969159e2e84`
- recomp-net: `268e74fe718b38fe38643c358588bbc1e0f0af70`
- RetComM rbengine: `ebd94a4729abe2c0615070cef3ffe05b3f9ebf28`
- RetComM package consumer: release `v0.6.33`
- RetComM inspected source: `4a30d0615ddbf71c9c62c3bce1e3b6163e42a1bd`

The setup host pins the exact public integration tag and commit in Alex's
framework fork. No upstream pull request was opened.

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

## Rejected package drafts

### `v0.3.0`

- File: `mortal-kombat-4-recomp-0.3.0-windows-x64.zip`
- Size: `47369495`
- SHA-256: `a1369cb36c778356aaefcbd57caa7a015cf6abd58b67c3de64baf942e6961a7f`
- Disposition: rejected before publication and preserved under ignored scratch storage

The archive contained a 131,072-byte memory-card backup. Its SHA-256 was
`7706c7d43edaf8cb7618e574f03457105153e3bdc196db803a600ad96a8f58e8`.
The extension-only audit did not match the backup suffix. The archive also used
a full generated-game executable instead of a setup-only host. These defects
invalidate the earlier private-payload pass claim.

### `v0.3.1`

- File: `mortal-kombat-4-recomp-0.3.1-windows-x64.zip`
- Size: `29550030`
- SHA-256: `f44d7e397c4b0c3f5c7fdd319bea7d55e676a8c148f7fe0aa6895e0863844bb5`
- ZIP entries: `2198`
- Extracted files: `1951`
- Extracted bytes: `75180405`
- Forbidden owned-input or player-state files: `0`
- Forbidden retail BIOS files: `0`
- Generated game or BIOS source files: `0`
- Unsafe ZIP paths: `0`
- Exact private local paths: `0`
- Mod manifests: `4`
- Setup-host executable size: `13884344`
- Setup-host executable SHA-256: `1df4a86afc87954835cc4ba204f90ba657eaf1d2aedf286cb776cab5f7d122f2`
- Disposition: rejected before publication because its packaged README retained an obsolete pass claim

The `v0.3.1` payload audit confirms the corrected package boundary. It does not
qualify `v0.3.2`.

## Rejected `v0.3.2` Windows package draft

- File: `mortal-kombat-4-recomp-0.3.2-windows-x64.zip`
- Size: `29549894`
- SHA-256: `6d41a4a7bb8287f373e0b4a8edd7071a323efa2b20b1da3f9cd70c81fde957da`
- ZIP entries: `2198`
- Extracted files: `1951`
- Extracted bytes: `75180127`
- Forbidden disc, memory-card, or player-state files: `0`
- Forbidden retail BIOS dumps: `0`
- Generated game or BIOS source files: `0`
- Unsafe ZIP paths: `0`
- Exact private local paths: `0`
- Root mod manifests: `4`
- Setup-host executable size: `13884344`
- Setup-host executable SHA-256: `b6ede3bc2625cea4c8c3b366a28bb07b98a41e3b7d55f4bc88e628169ebb5070`
- Clean setup-host executable match: yes
- Package version and build stamp: `0.3.2`

The audit matched backup suffixes such as `.mcd.bak`. It allowed the bundled
OpenBIOS image in the framework BIOS directory. Mortal Kombat 4 disables
OpenBIOS and requires a retail BIOS. The owned-input release boundary forbids
the unused OpenBIOS image. Therefore, this package is rejected before
publication and preserved under ignored scratch storage.

## Rejected `v0.3.2` clean-room canaries

RetComM v0.6.33 built the exact package twice with source ref `v0.3.2`.
Each run used a new RetComM data root and the verified disc and BIOS inputs.

Canary A:

- Installed executable size: `51767808`
- Installed executable SHA-256: `1bdc38e2ec7d6b44bc0c585666fa7b36aa425cad1b6d950d7cbfd15de29c1399`
- Final frame after the bounded 25-second gate: `3561`
- VBlank raises: `3561`
- Fatal state: none
- Automatic freeze dumps: `0`
- Failed freeze dumps: `0`

Canary B put the source, data root, install, and writable-state directory in
paths that contain spaces.

- Installed executable size: `51767808`
- Installed executable SHA-256: `9f3fb3e9abe06ceea1737c5c1c4e23a155818c8ae7c491ed23668d58cb6df1a7`
- Final frame after the bounded 25-second gate: `3680`
- VBlank raises: `3680`
- Fatal state: none
- Automatic freeze dumps: `0`
- Failed freeze dumps: `0`

Both processes remained active until the bounded gate stopped them. These
results prove the RetComM path and spaced-path handling. They do not qualify
`v0.3.4` because the tested package is rejected.

## Rejected `v0.3.3` Windows package draft

- File: `mortal-kombat-4-recomp-0.3.3-windows-x64.zip`
- Size: `29409479`
- SHA-256: `23f3ba10d206e50d07a2ef8d49e7c75bdb6c2fece0456f7fe1d70556fc2b0b83`
- ZIP entries: `2195`
- Extracted files: `1948`
- Forbidden owned-input, player-state, or BIOS image files: `0`
- OpenBIOS artifacts: `0`
- Generated game or BIOS source files: `0`
- Unsafe ZIP paths: `0`
- Root mod manifests: `4`
- Setup-host executable SHA-256: `32d22af46b95f803d024d7a23f705cfe3323f53aa9ebcdad4439eaca24d9cb0b`

The archive passed its payload audit. Its exact-package RetComM build generated
the retail SCPH-1001 backend and game source. CMake then stopped because the
runtime required `openbios.bin` from the requested stem list, although it did
not link the OpenBIOS backend. Framework commit `decc42d` makes OpenBIOS staging
follow the linked backend set. This archive is rejected and preserved.

## Local `v0.3.4` Windows package candidate

- File: `mortal-kombat-4-recomp-0.3.4-windows-x64.zip`
- Size: `29410101`
- SHA-256: `d79f082ba5bd3e71783213f0b052bd905c596f151253ec040d313795e7809029`
- ZIP entries: `2196`
- Extracted files: `1949`
- Extracted bytes: `74650179`
- Forbidden disc, memory-card, or player-state files: `0`
- BIOS images: `0`
- OpenBIOS artifacts: `0`
- Generated game or BIOS source files: `0`
- Mod state files: `0`
- Unsafe ZIP paths: `0`
- Exact private local paths: `0`
- Root mod manifests: `4`
- Setup-host executable size: `13884344`
- Setup-host executable SHA-256: `a0c40a712fac8eacd1a5b3d2e2ca1b3bc52bcfebb0fe17b6c500f0aa225c327`
- Clean setup-host executable match: yes
- Package version and build stamp: `0.3.4`

The clean setup build referenced no generated retail source in `build.ninja`.
The exact ZIP passed the owned-input and private-path audits.

RetComM v0.6.33 consumed the exact ZIP twice. Each run used a new data root,
the verified disc, and the verified SCPH-1001 BIOS.

Canary A:

- Installed executable size: `51767808`
- Installed executable SHA-256: `331d004fc08d516bf64bdf09daabba6b8c2c4d6d5e1c9e0ec80f172a870feec5`
- Final frame after the bounded 25-second gate: `3638`
- VBlank raises: `3638`
- Fatal state: none
- Automatic freeze dumps: `0`
- Failed freeze dumps: `0`

Canary B put the source, data root, install, and writable-state directory in
paths that contain spaces.

- Installed executable size: `51767808`
- Installed executable SHA-256: `64ca67160a9d6d37c70a427bad20c9bf559107cc205924144e6b58ff97667088`
- Final frame after the bounded 25-second gate: `3658`
- VBlank raises: `3658`
- Fatal state: none
- Automatic freeze dumps: `0`
- Failed freeze dumps: `0`

Both processes remained active until the bounded gate stopped them. These
results qualify the local Windows package for remote release-build validation.

## Remote release-build validation

GitHub Actions run `33374787051` used title commit `8ef9495` and framework
commit `decc42d`. Linux and both macOS jobs stopped at the framework's
test-registration guard. Four new Python tests existed on disk but had no
CTest registration. No package was produced by those jobs.

Framework commit `eecf3b2a` registers all four tests. A clean recompiler CMake
configuration reports 125 test files and no unregistered test. The four focused
tests pass locally.

Replacement run `33375274724` passed emitter and setup-host compilation on
macOS ARM64. Its archive step then stopped because the title wrapper required
`launcher_assets`, although that optional directory contained no tracked file
and was absent from the clean checkout. The wrapper now includes that directory
only when it contains a file.

Final run `33375675671` used title commit `98adbed` and framework commit
`eecf3b2a`. Windows x64, Linux x64, macOS x64, and macOS ARM64 all passed.
The exact CI archives have these identities:

- Windows x64: `2a02f1789ab6652ad2b80dbafd125bda27e432d274b7f79726ff85dee7fb9e9e`
  (`30098559` bytes)
- Linux x64: `d7cc6a88f8182fda1b6747f148e5e75020a2bc9d8da6db4bb5bd0f06fd7c7273`
  (`28063725` bytes)
- macOS x64: `f988420386dd3b0e2f4d154fda46517fae95554018234fe311ae221885f1ebdd`
  (`25852777` bytes)
- macOS ARM64: `3c0f06dc00ae295795ddc1e42c629a492a65602fe98794f23a651ba4717d9afc`
  (`25506416` bytes)

Each archive reports version `0.3.4`. Each archive contains four root mod
manifests and the expected platform executable. The repeated archive audit
found no disc, BIOS, save/state, generated retail source, unsafe ZIP path, or
exact private local path.

RetComM v0.6.33 consumed the exact CI Windows archive in a new data root. It
generated the game and retail SCPH-1001 BIOS backends, built the runtime, and
installed it. The installed executable is `51767808` bytes with SHA-256
`b6bf0e546eece5e2435ce6d36fca4d278080db0e3955cd30c7bd6676168d3138`.
The hidden 25-second gate reached frame and VBlank `3719`. The process remained
active until the gate stopped it. It reported no fatal state and zero automatic
or failed freeze dumps.

Tag `v0.3.4` points to exact CI source commit `98adbed`. The private draft
release is
`https://github.com/Alexbeav/mortal-kombat-4-recomp/releases/tag/untagged-c3adb2a9fba5d8daa998`.
All six draft assets were downloaded again. Their sizes and SHA-256 values
match the local candidate. The repeated content audit passed.

## RetComM installation evidence

RetComM release `v0.6.33` consumed the rejected `v0.3.0` archive in a fresh
data root. It matched the disc and SCPH-1001 BIOS identities from the local
catalog draft. It then generated, built, and installed source ref `v0.3.0`.

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

This evidence proves the RetComM generation and build flow. The exact CI
Windows canary above qualifies the replacement package for operator gameplay.

## Operator acceptance

On 2026-08-31, the operator reported that Mortal Kombat 4 works after the
`v0.3.0` package handoff. This is behavior evidence for the build flow.
The operator also ran the package from a writable directory whose path contains
spaces. The test route and duration were not recorded. Because the tested
archive is rejected, these results do not qualify the replacement package.

## Open release gates

1. Record operator gameplay acceptance for the exact CI `v0.3.4` package.
2. Show the final catalog manifest and request submission approval.
3. Publish the private draft only after explicit approval.
