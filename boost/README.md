# Boost build
The current `boost/1.91.0` (`857a04e51881582791677311c881b00d`) does not work on Windows.

## Reproduce
Just install the dependencies:
```
conan install --profile:host .\profiles\VS --build=missing -c 'tools.build:verbosity=verbose'
```

See also:
- https://github.com/conan-io/conan-center-index/issues/30414
- https://github.com/conan-io/conan-center-index/issues/29193

## Output
The build fails with the following output:
```
boost/1.91.0: Created package revision 6128e29b21b95022a3a379f6ac858719
boost/1.91.0: Package 'cf78e35dfc9d9792e6bb4a1bb334c8419d5b96fd' created
boost/1.91.0: Full package reference: boost/1.91.0#857a04e51881582791677311c881b00d:cf78e35dfc9d9792e6bb4a1bb334c8419d5b96fd#6128e29b21b95022a3a379f6ac858719
boost/1.91.0: Package folder C:\co\p\b\boost283617303291b\p
boost/1.91.0: Disabled magic autolinking (smart and magic decisions)
boost/1.91.0: WARN: Boost component 'cobalt_io_ssl' is missing libraries. Try building boost with '-o boost:without_cobalt_io_ssl'. (Option is not guaranteed to exist)
Generated lockfile: C:\Projects\conan-issues\boost\conan.lock
ERROR: boost/1.91.0: Error in package_info() method, line 2044
        raise ConanException(f"These libraries were expected to be built, but were not built: {non_built}")
        ConanException: These libraries were expected to be built, but were not built: {'boost_cobalt_io_ssl'}
```