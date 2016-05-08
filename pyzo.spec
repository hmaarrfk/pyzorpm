Name:		pyzo-desktop
Version:	0.1.0
Release:	3%{?dist}
Summary:	A launcher for Pyzo

Group:		Development
License:	BSD
URL:		https://github.com/hmaarrfk/pyzorpm
Source0:    https://raw.githubusercontent.com/pyzo/pyzo/master/pyzo/resources/pyzo.desktop
Source1:    https://raw.githubusercontent.com/pyzo/pyzo/master/README.md
Source2:    https://raw.githubusercontent.com/pyzo/pyzo/master/pyzo/license.txt
Source3:    https://raw.githubusercontent.com/pyzo/pyzo/master/pyzo.appdata.xml
Source4:	https://raw.githubusercontent.com/pyzo/pyzo/master/pyzo/resources/appicons/pyzologo256.png
Source5:	https://raw.githubusercontent.com/pyzo/pyzo/master/pyzo/resources/appicons/pyzologo128.png
Source6:	https://raw.githubusercontent.com/pyzo/pyzo/master/pyzo/resources/appicons/pyzologo64.png
Source7:	https://raw.githubusercontent.com/pyzo/pyzo/master/pyzo/resources/appicons/pyzologo48.png
Source8:	https://raw.githubusercontent.com/pyzo/pyzo/master/pyzo/resources/appicons/pyzologo32.png
Source9:	https://raw.githubusercontent.com/pyzo/pyzo/master/pyzo/resources/appicons/pyzologo16.png

BuildArch:      noarch

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%description
A desktop launcher for Pyzo. This package does not contain an actual Pyzo
installation.  It is probably best left to install it from pip. This just
provides integration with the desktop environment.


%prep


%build
# Nothing to build
cp %{_sourcedir}/README.md %{_builddir}/.
cp %{_sourcedir}/license.txt %{_builddir}/LICENSE
cp %{_sourcedir}/pyzo.appdata.xml %{_builddir}/.


%install
rm -rf ${RPM_BUILD_ROOT}
install -d ${RPM_BUILD_ROOT}%{_datadir}/
desktop-file-install --delete-original --dir=${RPM_BUILD_ROOT}%{_datadir}/applications/ %{_sourcedir}/pyzo.desktop
install -d ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/{256x256,128x128,64x64,48x48,32x32,16x16}/apps/
install %{_sourcedir}/pyzologo256.png ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/256x256/apps/pyzologo.png
install %{_sourcedir}/pyzologo128.png ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/128x128/apps/pyzologo.png
install %{_sourcedir}/pyzologo64.png  ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/64x64/apps/pyzologo.png
install %{_sourcedir}/pyzologo48.png  ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/48x48/apps/pyzologo.png
install %{_sourcedir}/pyzologo32.png  ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/32x32/apps/pyzologo.png
install %{_sourcedir}/pyzologo16.png  ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/16x16/apps/pyzologo.png

install -d %{buildroot}/%{_datadir}/appdata/
install %{_builddir}/pyzo.appdata.xml %{buildroot}/%{_datadir}/appdata/.

%check
desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/pyzo.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%post
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc README.md LICENSE
%{_datadir}/applications/*
%{_datadir}/appdata/*
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Sun May 08 2016 Mark Harfouche <mark.harfouche@gmail.com> - 0.1.0-3
- With appdata

* Sun May 08 2016 Mark Harfouche <mark.harfouche@gmail.com> - 0.1.1-2
- With the provided desktop launcher


