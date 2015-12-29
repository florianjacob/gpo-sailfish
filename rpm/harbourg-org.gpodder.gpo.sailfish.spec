# Prevent brp-python-bytecompile from running
%define __os_install_post %{___build_post}

Summary: Media and podcast aggregator
Name: harbour-org.gpodder.sailfish
Version: 4.6.0
Release: 1
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: http://gpodder.org/
License: ISC / GPLv3
Group: System/GUI/Other
Requires: pyotherside-qml-plugin-python3-qt5 >= 1.3.0
Requires: sailfishsilica-qt5
Requires: libsailfishapp-launcher
Requires: harbour-org.gpodder.sailfish

%description
gpo is a command line version of gpodder

%prep
%setup -q

%build
# Nothing to do

%install

TARGET=%{buildroot}/%{_datadir}/%{name}
mkdir -p $TARGET
cp -rpv gpodder-core/bin/gpo $TARGET/

TARGET=%{buildroot}/%{_datadir}/applications
mkdir -p $TARGET
cp -rpv %{name}.desktop $TARGET/

TARGET=%{buildroot}/%{_datadir}/icons/hicolor/86x86/apps/
mkdir -p $TARGET
cp -rpv %{name}.png $TARGET/

%files
%defattr(-,root,root,-)
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
