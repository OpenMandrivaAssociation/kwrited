%define major %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Application for monitoring messages sent with write or wall
Name:		kwrited
Version:	5.5.4
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://kde.org/
Source0:	fhttp://download.kde.org/%{stable}/plasma/%{major}/%{name}-%{version}.tar.xz

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5)
BuildRequires:	cmake(KF5KDE4Support)
BuildRequires:	cmake(KF5Pty)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)

%description
Application for monitoring messages sent with write or wall.

%files

%{_libdir}/qt5/plugins/kded_kwrited.so
%{_datadir}/kservices5/kded/kwrited.desktop
%{_datadir}/knotifications5/kwrited.notifyrc

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{major}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

