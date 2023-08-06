# Portmod Migrate
![pipeline](https://gitlab.com/portmod/portmodmigrate/badges/master/pipeline.svg)
![coverage](https://gitlab.com/portmod/portmodmigrate/badges/master/coverage.svg)

A cli tool to help migrating from manually installed mods to the Portmod system.

### Importing Archives

```
usage: portmodmigrate import-archives [-h] [--pretend] [directory ...]

positional arguments:
  directory   Directories to search when importing archives

optional arguments:
  -h, --help  show this help message and exit
  --pretend   Instead of committing changes, just show what would have been done
```

Replacing dir with the directory containing the archives to import. By default this will move the archives to portmod's cache directory. If you want to just see which files would be moved, use the `--pretend` flag.

### Detecting Mods
```
usage: portmodmigrate scan-installed [-h] [--interactive] [--fuzzy] {openmw}

positional arguments:
  {openmw}       Name of the portmod prefix you want to use. You may need to create a prefix if you do not already have one. See the portmod installation guide for details.

optional arguments:
  -h, --help     show this help message and exit
  --interactive  Resolve ambiguity interactively
  --fuzzy        Does fuzzy matching when scanning mods (experimental)
```

This will detect packages in the repository that match mods you have installed.

This is done by matching plugin and archive file names. If you want to also try fuzzy searching on the file names pass the `--fuzzy` option as well, though note that this is experimental and produces a lot of false positives, largely due to mods that aren't in the repository reporting partial matches against similarly named mods. This will improve substantially as the mod repo grows in size.

You can also use the `--interactive` flag to have portmodmigrate prompt you when multiple mods match closely when fuzzy searching, as well as pass the mod list to portmod to merge when it's done.

You may want to backup your old `openmw.cfg` before setting up a portmod prefix to make sure you do not lose it, then restore the backup before running portmodmigrate
