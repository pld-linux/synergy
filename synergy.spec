# TODO:
# - add xdg/autostart for -client and -server instead
#
Summary:	Mouse and keyboard sharing utility
Summary(pl.UTF-8):	Narzędzie do dzielenia myszy i klawiatury
Name:		synergy
Version:	1.4.8
Release:	1
License:	GPL v2
Group:		Daemons
Source0:	http://synergy.googlecode.com/files/%{name}-%{version}-Source.tar.gz
# Source0-md5:	0aa803b82b6d37c6c3542f8ed0656943
Source1:	%{name}-client.init
Source2:	%{name}-client.conf
Source3:	%{name}-server.init
Source4:	%{name}-server.conf
Source5:	%{name}-server-layout.conf
URL:		http://synergy-foss.org/
BuildRequires:	cmake
BuildRequires:	libstdc++-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Synergy lets you easily share a single mouse and keyboard between
multiple computers with different operating systems, each with its own
display, without special hardware. It's intended for users with
multiple computers on their desk since each system uses its own
display.

%description -l pl.UTF-8
Synergy pozwala łatwo i bez specjalnego sprzętu dzielić jedną mysz i
klawiaturę pomiędzy wiele komputerów z różnymi systemami operacyjnymi,
z których każdy ma własny monitor. Jest przeznaczony dla użytkowników
z wieloma komputerami na biurku, jako że każdy system używa własnego
monitora.

%package xinitrc-client
Summary:	xinitrc startup scripts for synergy client
Summary(pl.UTF-8):	Skrypty startowe xinitrc dla klienta synergy
Group:		Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	xinitrc

%description xinitrc-client
xinitrc startup scripts for synergy client.

%description xinitrc-client -l pl.UTF-8
Skrypty startowe xinitrc dla klienta synergy.

%package xinitrc-server
Summary:	xinitrc startup scripts for synergy server
Summary(pl.UTF-8):	Skrypty startowe xinitrc dla serwera synergy
Group:		Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	xinitrc

%description xinitrc-server
xinitrc startup scripts for synergy server.

%description xinitrc-server -l pl.UTF-8
Skrypty startowe xinitrc dla serwera synergy.

%prep
%setup -q -n %{name}-%{version}-Source

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/X11/xinit/xinitrc.d,%{_sysconfdir}/synergy,%{_bindir},%{_mandir}/man1}

install -p bin/* $RPM_BUILD_ROOT%{_bindir}
%{__rm} $RPM_BUILD_ROOT%{_bindir}/*tests

install -p %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/xinit/xinitrc.d/synergyc.sh
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/synergy/client.conf

install -p %{SOURCE3} $RPM_BUILD_ROOT/etc/X11/xinit/xinitrc.d/synergys.sh
cp -p %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/synergy/server.conf

cp -p %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/synergy/layout.conf

cp -p doc/synergyc.man $RPM_BUILD_ROOT%{_mandir}/man1/synergyc.1
cp -p doc/synergys.man $RPM_BUILD_ROOT%{_mandir}/man1/synergys.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog INSTALL README
%doc doc/synergy.conf*
%dir %{_sysconfdir}/synergy
%attr(755,root,root) %{_bindir}/synergyc
%attr(755,root,root) %{_bindir}/synergys
%{_mandir}/man1/synergyc.1*
%{_mandir}/man1/synergys.1*

%files xinitrc-client
%defattr(644,root,root,755)
%attr(755,root,root) %{_sysconfdir}/X11/xinit/xinitrc.d/synergyc.sh
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/synergy/client.conf

%files xinitrc-server
%defattr(644,root,root,755)
%attr(755,root,root) %{_sysconfdir}/X11/xinit/xinitrc.d/synergys.sh
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/synergy/server.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/synergy/layout.conf
