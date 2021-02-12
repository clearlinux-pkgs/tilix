#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tilix
Version  : 1.9.4
Release  : 10
URL      : https://github.com/gnunn1/tilix/archive/1.9.4/tilix-1.9.4.tar.gz
Source0  : https://github.com/gnunn1/tilix/archive/1.9.4/tilix-1.9.4.tar.gz
Summary  : A tiling terminal emulator for Linux using GTK+ 3
Group    : Development/Tools
License  : CC-BY-SA-3.0 GPL-3.0 LGPL-3.0 MPL-2.0 MPL-2.0-no-copyleft-exception
Requires: tilix-bin = %{version}-%{release}
Requires: tilix-data = %{version}-%{release}
Requires: tilix-license = %{version}-%{release}
Requires: tilix-locales = %{version}-%{release}
Requires: tilix-man = %{version}-%{release}
Requires: gtk3
Requires: librsvg
Requires: libsecret
Requires: vte
BuildRequires : GtkD-dev
BuildRequires : appstream
BuildRequires : buildreq-meson
BuildRequires : desktop-file-utils
BuildRequires : gdk-pixbuf-dev
BuildRequires : glib-dev
BuildRequires : gtk3
BuildRequires : ldc
BuildRequires : ldc-dev
BuildRequires : librsvg
BuildRequires : libsecret
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(libunwind)
BuildRequires : pkgconfig(vte-2.91)
BuildRequires : vte

%description
Tilix is a tiling terminal emulator which uses the VTE GTK+ 3 widget. The
application was written using GTK 3 and an effort was made to conform to GNOME
Human Interface Guidelines (HIG). As a result, it does use CSD (i.e. the GTK
HeaderBar) though it can be disabled if necessary. Other than GNOME, only Unity
has been tested officially though users have had success with other desktop
environments.

%package bin
Summary: bin components for the tilix package.
Group: Binaries
Requires: tilix-data = %{version}-%{release}
Requires: tilix-license = %{version}-%{release}

%description bin
bin components for the tilix package.


%package data
Summary: data components for the tilix package.
Group: Data

%description data
data components for the tilix package.


%package license
Summary: license components for the tilix package.
Group: Default

%description license
license components for the tilix package.


%package locales
Summary: locales components for the tilix package.
Group: Default

%description locales
locales components for the tilix package.


%package man
Summary: man components for the tilix package.
Group: Default

%description man
man components for the tilix package.


%prep
%setup -q -n tilix-1.9.4
cd %{_builddir}/tilix-1.9.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1613090515
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/tilix
cp %{_builddir}/tilix-1.9.4/LICENSE %{buildroot}/usr/share/package-licenses/tilix/fa7c4d75bae3a641d1f9ab5df028175bfb8a69ca
cp %{_builddir}/tilix-1.9.4/data/icons/LICENSE %{buildroot}/usr/share/package-licenses/tilix/2093ad79c06332b64811fed22135d71855d2e2a2
cp %{_builddir}/tilix-1.9.4/source/x11/LICENSE %{buildroot}/usr/share/package-licenses/tilix/f98c7fffc3fe221e79fa19fe89c74e74c0da1266
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang tilix

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tilix

%files data
%defattr(-,root,root,-)
/usr/share/applications/com.gexperts.Tilix.desktop
/usr/share/dbus-1/services/com.gexperts.Tilix.service
/usr/share/glib-2.0/schemas/com.gexperts.Tilix.gschema.xml
/usr/share/icons/hicolor/scalable/apps/com.gexperts.Tilix.svg
/usr/share/icons/hicolor/symbolic/apps/com.gexperts.Tilix-symbolic.svg
/usr/share/metainfo/com.gexperts.Tilix.appdata.xml
/usr/share/nautilus-python/extensions/open-tilix.py
/usr/share/tilix/resources/tilix.gresource
/usr/share/tilix/schemes/base16-twilight-dark.json
/usr/share/tilix/schemes/linux.json
/usr/share/tilix/schemes/material.json
/usr/share/tilix/schemes/monokai.json
/usr/share/tilix/schemes/orchis.json
/usr/share/tilix/schemes/solarized-dark.json
/usr/share/tilix/schemes/solarized-light.json
/usr/share/tilix/schemes/tango.json
/usr/share/tilix/schemes/yaru.json
/usr/share/tilix/scripts/tilix_int.sh

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tilix/2093ad79c06332b64811fed22135d71855d2e2a2
/usr/share/package-licenses/tilix/f98c7fffc3fe221e79fa19fe89c74e74c0da1266
/usr/share/package-licenses/tilix/fa7c4d75bae3a641d1f9ab5df028175bfb8a69ca

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/tilix.1

%files locales -f tilix.lang
%defattr(-,root,root,-)

