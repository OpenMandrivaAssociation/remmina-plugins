Summary:	A set of plugins for remmina
Name:		remmina-plugins
Version:	0.8.2
Release:	%mkrel 1
License:	GPLv2
Group:		Networking/Remote access
Url:		http://remmina.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/remmina/%{version}/%{name}-%{version}.tar.gz
Requires:	remmina
BuildRequires:	remmina-devel
BuildRequires:	gtk2-devel >= 2.16
BuildRequires:	zlib-devel
BuildRequires:	jpeg-devel
BuildRequires:	gnutls-devel
BuildRequires:	libssh-devel >= 0.4
BuildRequires:	libxkbfile-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtelepathy-glib-devel
BuildRequires:	freerdp-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A set of plugins for remote desktop client - remmina.

%prep
%setup -q

%build
#aclocal
#autoconf
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std
%__rm -f %{buildroot}%{_iconsdir}/hicolor/icon-theme.cache

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README*
%{_libdir}/remmina/plugins
%{_datadir}/locale/*/*/%{name}.mo
%{_datadir}/telepathy/clients/Remmina.client
%{_datadir}/dbus-1/services/*Remmina.service
%{_datadir}/remmina/icons/hicolor/*/*/*.png
