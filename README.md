# gpo-sailfish #
This packages the [gpo command line client](https://github.com/gpodder/gpodder-core/blob/master/bin/gpo) from
[gpodder-core](https://github.com/gpodder/gpodder-core) for SailfishOS.

gpo can't be included to the gpodder harbour package, as we can't add multiple binaries or .desktop files (see
[harbour faq](https://harbour.jolla.com/faq)).

For start, we decided to use the gpodder-core lib packaged in the gui. It would nicer to package that separately,
though, so that both frontends can depend on gpodder-core.
