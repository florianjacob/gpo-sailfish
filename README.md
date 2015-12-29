# gpo-sailfish #
This packages the [gpo command line client](https://github.com/gpodder/gpodder-core/blob/master/bin/gpo) from
[gpodder-core](https://github.com/gpodder/gpodder-core) for SailfishOS.

gpo can't be included to the gpodder harbour package, as we can't add multiple binaries or .desktop files (see
[harbour faq](https://harbour.jolla.com/faq)).

For starters, we use the gpodder-core lib packaged in the gui. It might be nicer to package that separately,
though, so that both frontends could depend on gpodder-core.

# TODO list #
 * correct pcast:// podcast:// gpodder:// handling
    * need to add some code in podcastparser
    * replace with http/https?
    * download format? mp3? opus?
 * Can GUI and CLI be run in parallel?
    * yes, but the GUI podcast list won't be refreshed when a new podcast was subscribed
    * => gpodder bug report? investigate in qml?
 * We need to set “progname“ kwarg of gpodder Core through the cli
    * needed to access the same data as the GUI, as progname is set to harbour-org.gpodder.sailfish in sailfish qml
    * how to do that? Maybe some kind of config?
    * https://github.com/gpodder/gpodder-core/blob/master/src/gpodder/config.py
 * webcat and default browser don't seem to support custom url schemes
    * default browser: about:config -> network.protocol-handler.all
       * can't be accessed through the gui, as search is impossible and only the first viewport is rendered, so no
         scrolling
    * webcat? => ask leszek / llelectronics
 * maybe the url handler .desktop file would make more sense to bundle with gpo and therefore in gpodder-core
    * or, actually, in a separate CLI repo only for gpo
 * how to build proper rpm files to transfer to phone?
    * fix spec file
    * replace cp with install?
    * what about the sailfish-typical yaml file to generate spec file?
        * https://wiki.merproject.org/wiki/Spectacle
 * icon for starting gpo in fingerterm? somehow modify gpodder icon, maybe black with green lines?
 * submission to warehouse
 * submission to harbour

# Resources #
 * Subscribe button for testing: http://podlove.org/podlove-subscribe-button/
 * The small testfeed that's behind it, to reduce parsing times: http://v4-feed-test.podlove.org/feed/
 * gpodder url: gpodder://v4-feed-test.podlove.org/feed/
 * .desktop file standard: http://standards.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html#extra-actions
 * .desktop file of gpodder3: https://github.com/gpodder/gpodder/blob/master/share/applications/gpodder-url-handler.desktop.in
