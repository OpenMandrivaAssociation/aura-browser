%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Web browser optimized for full screen TV with remote control interface
Name:		aura-browser
Version:	5.25.90
Release:	1
License:	LGPL
Group:		System/Libraries
Url:		http://plasma-bigscreen.org/
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5WebEngineCore)
Suggests:	plasma-bigscreen
Suggests:	plasma-remotecontrollers
Supplements:	plasma-bigscreen

%description
Web browser optimized for full screen TV with remote control interface

%files -f %{name}.lang
%{_bindir}/aura-browser
%{_datadir}/applications/org.aura.browser.desktop
%{_datadir}/icons/hicolor/*/apps/aura-browser.png
%{_datadir}/metainfo/org.kde.invent.aura_browser.metainfo.xml

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name
