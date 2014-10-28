%define major %(echo %{version} |cut -d. -f1-3)

Summary:	Application for monitoring messages sent with write or wall
Name:		kwrited
Version:	5.1.0.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/stable/plasma/%{major}/%{name}-%{version}.tar.xz

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake
BuildRequires:	cmake(KF5)
BuildRequires:	cmake(KF5KDE4Support)
BuildRequires:	cmake(KF5Pty)

%description
Application for monitoring messages sent with write or wall

%files
%{_sysconfdir}/xdg/autostart/kwrited-autostart.desktop
%{_bindir}/*
%{_datadir}/knotifications5/kwrited.notifyrc

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{major}

%build
%cmake
%make

%install
%makeinstall_std -C build

